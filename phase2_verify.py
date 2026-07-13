#!/usr/bin/env python3
"""
Phase 2 content verification.
Compare each restored coffee page against the ORIGINAL snapshot on:
  1. <title>, meta description, <h1>
  2. All alt attributes on <img>
  3. All external and internal hrefs (link targets)
  4. All visible text content (all natural-language text nodes)
Reports every missing / added / changed text passage.
Only compares content — not layout, not chrome (site-header/breadcrumb/site-footer).
"""
import re
from pathlib import Path
from html.parser import HTMLParser

ORIG = Path("/app/_original_snapshot/KOFFYKRAFT-main")
CUR = Path("/app/KOFFYKRAFT-main")

PAGES = [
    "coffee/index.html",
    "coffee/roastery/index.html",
    "coffee/roastery/buy/index.html",
    "coffee/roastery/browse/index.html",
    "coffee/roastery/roast-days/index.html",
]

# Extract text nodes and structured fields from an HTML document.
class Collect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texts = []
        self.title = ""
        self.meta_desc = ""
        self.hrefs = []
        self.srcs = []
        self.alts = []
        self._in_title = False
        self._in_script = False
        self._in_style = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title": self._in_title = True
        if tag == "script": self._in_script = True
        if tag == "style": self._in_style = True
        if tag == "meta" and a.get("name","").lower() == "description":
            self.meta_desc = a.get("content", "").strip()
        if tag == "a" and "href" in a: self.hrefs.append(a["href"])
        if tag == "img":
            if "src" in a: self.srcs.append(a["src"])
            if "alt" in a: self.alts.append(a["alt"])
        if tag == "link" and a.get("rel","").lower() == "stylesheet" and "href" in a:
            self.hrefs.append(a["href"])
    def handle_endtag(self, tag):
        if tag == "title": self._in_title = False
        if tag == "script": self._in_script = False
        if tag == "style": self._in_style = False
    def handle_data(self, data):
        if self._in_script or self._in_style:
            return
        text = data.strip()
        if not text:
            return
        if self._in_title:
            self.title = text
            return
        # Normalize whitespace
        text = re.sub(r"\s+", " ", text)
        self.texts.append(text)

def collect(path):
    p = Collect()
    p.feed(path.read_text(encoding="utf-8", errors="replace"))
    return p

print("=" * 70)
print("PHASE 2 CONTENT VERIFICATION — coffee section vs. original snapshot")
print("=" * 70)

overall_issues = 0

for rel in PAGES:
    print(f"\n─── {rel} ───")
    o = collect(ORIG / rel)
    c = collect(CUR / rel)

    def check(label, o_val, c_val, allow_missing=False):
        global overall_issues
        if o_val == c_val:
            print(f"  ✓ {label}: identical")
        else:
            print(f"  ✗ {label}")
            print(f"      orig    = {o_val!r}")
            print(f"      current = {c_val!r}")
            overall_issues += 1

    check("Title", o.title, c.title)
    check("Meta description", o.meta_desc, c.meta_desc)
    check("Image alts", o.alts, c.alts)
    check("Image srcs", o.srcs, c.srcs)

    # Compare hrefs as multisets (order of doors/nav may differ across chrome).
    # But we must ensure every original href is preserved.
    o_hrefs = [h for h in o.hrefs if not h.startswith("#")]
    c_hrefs = [h for h in c.hrefs if not h.startswith("#")]
    missing_hrefs = [h for h in o_hrefs if c_hrefs.count(h) < o_hrefs.count(h) and h not in c_hrefs]
    # simpler: check every original href appears at least once in current
    truly_missing = [h for h in set(o_hrefs) if h not in c_hrefs]
    if truly_missing:
        print(f"  ✗ hrefs missing from current: {truly_missing}")
        overall_issues += 1
    else:
        print(f"  ✓ All {len(set(o_hrefs))} original hrefs are present in current")

    # Compare natural language text passages.
    # Normalise both lists into sets (visible-text bag).
    o_text = [t for t in o.texts if t and t not in ("/", "|")]
    c_text = [t for t in c.texts if t and t not in ("/", "|")]

    o_bag = {}
    for t in o_text:
        o_bag[t] = o_bag.get(t, 0) + 1
    c_bag = {}
    for t in c_text:
        c_bag[t] = c_bag.get(t, 0) + 1

    missing_passages = []
    for t, n in o_bag.items():
        if c_bag.get(t, 0) < n:
            missing_passages.append((t, n, c_bag.get(t, 0)))

    added_passages = []
    for t, n in c_bag.items():
        if o_bag.get(t, 0) < n:
            added_passages.append((t, n, o_bag.get(t, 0)))

    # Filter out chrome-only text that the ORIGINAL did not have and that we
    # explicitly kept in the current design (breadcrumb, aria labels, etc.).
    # These are legitimate presentational additions; not "invented copy".
    KNOWN_CHROME_ADDITIONS = {
        "☰", "Home",
    }
    added_passages_filtered = [
        (t,n,o) for (t,n,o) in added_passages if t not in KNOWN_CHROME_ADDITIONS
    ]

    if missing_passages:
        print(f"  ✗ Original passages missing from current ({len(missing_passages)}):")
        for t, n, cn in missing_passages:
            print(f"      - {t!r}   (orig x{n}, cur x{cn})")
        overall_issues += 1
    else:
        print(f"  ✓ No original text is missing")

    if added_passages_filtered:
        print(f"  ⚠ Passages present in current but NOT in original ({len(added_passages_filtered)}):")
        for t, n, on in added_passages_filtered:
            marker = "     "
            # any passage longer than a short breadcrumb hint deserves a look
            print(f"      + {t!r}   (cur x{n}, orig x{on})")
    else:
        print(f"  ✓ No extra text passages beyond known chrome additions")

print("\n" + "=" * 70)
print(f"Total structural issues: {overall_issues}")
print("=" * 70)
