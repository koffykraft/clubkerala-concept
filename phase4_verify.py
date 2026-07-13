#!/usr/bin/env python3
"""Phase 4 verifier — links/index.html vs original snapshot."""
import re
from pathlib import Path
from html.parser import HTMLParser

ORIG = Path("/app/_original_snapshot/KOFFYKRAFT-main/links/index.html")
CUR  = Path("/app/KOFFYKRAFT-main/links/index.html")

class Collect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texts=[]; self.title=""; self.meta_desc=""
        self.hrefs=[]; self.srcs=[]; self.alts=[]
        self._t=False; self._s=False; self._y=False
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=="title": self._t=True
        if tag=="script": self._s=True
        if tag=="style": self._y=True
        if tag=="meta" and a.get("name","").lower()=="description":
            self.meta_desc=a.get("content","").strip()
        if tag=="a" and "href" in a: self.hrefs.append(a["href"])
        if tag=="img":
            if "src" in a: self.srcs.append(a["src"])
            if "alt" in a: self.alts.append(a["alt"])
        if tag=="link" and a.get("rel","").lower()=="stylesheet" and "href" in a:
            self.hrefs.append(a["href"])
    def handle_endtag(self, tag):
        if tag=="title": self._t=False
        if tag=="script": self._s=False
        if tag=="style": self._y=False
    def handle_data(self, data):
        if self._s or self._y: return
        t=data.strip()
        if not t: return
        if self._t: self.title=t; return
        self.texts.append(re.sub(r"\s+"," ",t))

def collect(p): x=Collect(); x.feed(p.read_text(encoding="utf-8",errors="replace")); return x

KNOWN_CHROME={"☰","Home","Buy","Coffees"}

print("="*72)
print("PHASE 4 CONTENT VERIFICATION — links/index.html vs original snapshot")
print("="*72)

o=collect(ORIG); c=collect(CUR)
issues=0

def check(label, ov, cv):
    global issues
    if ov==cv: print(f"  ✓ {label}: identical")
    else:
        print(f"  ✗ {label}"); print(f"      orig    = {ov!r}"); print(f"      current = {cv!r}")
        issues+=1

check("Title", o.title, c.title)
check("Meta description", o.meta_desc, c.meta_desc)
check("Image alts", o.alts, c.alts)
check("Image srcs", o.srcs, c.srcs)

# Compare hrefs as ordered lists (order of doors matters here)
o_hrefs=[h for h in o.hrefs if not h.startswith("#") and not h.endswith(".css")]
c_hrefs=[h for h in c.hrefs if not h.startswith("#") and not h.endswith(".css")]
print(f"\n  Original non-CSS hrefs (in order): {o_hrefs}")
print(f"  Current  non-CSS hrefs (in order): {c_hrefs}")

# check every original href present in current
for h in o_hrefs:
    if o_hrefs.count(h) > c_hrefs.count(h):
        print(f"  ✗ href {h!r} present {o_hrefs.count(h)}x in original but only {c_hrefs.count(h)}x in current")
        issues+=1

# Verify order of the 4 door hrefs is exactly preserved
door_hrefs_orig = ["../training/deeper-dive/", "../training/lrn/references.html",
                   "../training/deeper-dive/", "../estate/"]
door_hrefs_cur = [h for h in c_hrefs if h in ("../training/deeper-dive/", "../training/lrn/references.html", "../estate/")]
if door_hrefs_cur == door_hrefs_orig:
    print("  ✓ 4 door hrefs are in the exact original order")
else:
    print(f"  ✗ Door order mismatch\n     orig={door_hrefs_orig}\n     cur ={door_hrefs_cur}")
    issues+=1

# Compare visible text passages
o_bag={}; c_bag={}
for t in o.texts: o_bag[t]=o_bag.get(t,0)+1
for t in c.texts: c_bag[t]=c_bag.get(t,0)+1
missing=[(t,n,c_bag.get(t,0)) for t,n in o_bag.items() if c_bag.get(t,0)<n]
added=[(t,n,o_bag.get(t,0)) for t,n in c_bag.items() if o_bag.get(t,0)<n and t not in KNOWN_CHROME]

print()
if missing:
    print(f"  ✗ Missing text passages ({len(missing)}):")
    for t,n,cn in missing: print(f"      - {t!r}  orig x{n}, cur x{cn}")
    issues+=1
else:
    print("  ✓ No original text is missing")

if added:
    print(f"  ⚠ Extra passages beyond approved chrome ({len(added)}):")
    for t,n,on in added: print(f"      + {t!r}  cur x{n}, orig x{on}")
else:
    print("  ✓ No extra text beyond approved chrome")

print("\n" + "="*72)
print(f"Total structural issues: {issues}")
print("="*72)
