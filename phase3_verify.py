#!/usr/bin/env python3
"""Phase 3 verifier — Buna section content vs. original snapshot."""
import re
from pathlib import Path
from html.parser import HTMLParser

ORIG = Path("/app/_original_snapshot/KOFFYKRAFT-main")
CUR  = Path("/app/KOFFYKRAFT-main")

PAGES = [
    "buna/index.html",
    "buna/traditions/index.html",
    "buna/brewing/index.html",
    "buna/learn/index.html",
    "buna/library/index.html",
]

class Collect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texts = []
        self.title = ""
        self.meta_desc = ""
        self.hrefs = []
        self.srcs = []
        self.alts = []
        self._in_title = False; self._in_script = False; self._in_style = False
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
        if self._in_script or self._in_style: return
        t = data.strip()
        if not t: return
        if self._in_title: self.title = t; return
        self.texts.append(re.sub(r"\s+", " ", t))

def collect(p):
    x = Collect(); x.feed(p.read_text(encoding="utf-8", errors="replace")); return x

KNOWN_CHROME = {"☰", "Home", "Buy", "Coffees", "Buna"}

print("="*72)
print("PHASE 3 CONTENT VERIFICATION — Buna section vs. original snapshot")
print("="*72)

total_issues = 0
for rel in PAGES:
    print(f"\n─── {rel} ───")
    o = collect(ORIG/rel); c = collect(CUR/rel)

    def check(label, ov, cv):
        global total_issues
        if ov == cv:
            print(f"  ✓ {label}: identical")
        else:
            print(f"  ✗ {label}")
            print(f"      orig    = {ov!r}")
            print(f"      current = {cv!r}")
            total_issues += 1

    check("Title", o.title, c.title)
    check("Meta description", o.meta_desc, c.meta_desc)
    check("Image alts", o.alts, c.alts)
    check("Image srcs", o.srcs, c.srcs)

    o_hrefs = [h for h in o.hrefs if not h.startswith("#")]
    c_hrefs = [h for h in c.hrefs if not h.startswith("#")]
    missing = [h for h in set(o_hrefs) if h not in c_hrefs]
    non_css_missing = [h for h in missing if not h.endswith(".css")]
    if non_css_missing:
        print(f"  ✗ Non-CSS hrefs missing from current: {non_css_missing}")
        total_issues += 1
    else:
        css_swap = [h for h in missing if h.endswith(".css")]
        print(f"  ✓ All non-CSS original hrefs present. CSS swap: {css_swap or 'none'}")

    o_bag, c_bag = {}, {}
    for t in o.texts:
        o_bag[t] = o_bag.get(t,0)+1
    for t in c.texts:
        c_bag[t] = c_bag.get(t,0)+1

    missing_txt = [(t,n,c_bag.get(t,0)) for t,n in o_bag.items() if c_bag.get(t,0) < n]
    added_txt   = [(t,n,o_bag.get(t,0)) for t,n in c_bag.items() if o_bag.get(t,0) < n and t not in KNOWN_CHROME]

    if missing_txt:
        print(f"  ✗ Missing text passages ({len(missing_txt)}):")
        for t,n,cn in missing_txt: print(f"      - {t!r}   orig x{n}, cur x{cn}")
        total_issues += 1
    else:
        print("  ✓ No original text is missing")

    if added_txt:
        print(f"  ⚠ Passages present in current but NOT in original ({len(added_txt)}) (excluding known chrome):")
        for t,n,on in added_txt: print(f"      + {t!r}   cur x{n}, orig x{on}")
    else:
        print("  ✓ No extra text passages beyond approved chrome")

print("\n" + "="*72)
print(f"Total structural issues: {total_issues}")
print("="*72)
