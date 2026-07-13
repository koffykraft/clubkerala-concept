#!/usr/bin/env python3
"""Phase 1 post-flight verification."""
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT_CUR = Path("/app/KOFFYKRAFT-main")
ROOT_ORIG = Path("/app/_original_snapshot/KOFFYKRAFT-main")

# Skip the 15 pages I rewrote — they were intentionally not touched in Phase 1.
REWRITTEN = {
    "index.html","coffee/index.html","coffee/roastery/index.html",
    "coffee/roastery/buy/index.html","coffee/roastery/browse/index.html",
    "coffee/roastery/roast-days/index.html","buna/index.html",
    "buna/traditions/index.html","buna/brewing/index.html",
    "buna/learn/index.html","buna/library/index.html","estate/index.html",
    "links/index.html","training/brewing/index.html","training/cupping/index.html",
}

# 1. Every Category-B file should now be byte-identical to its original.
not_identical = []
for cur in sorted(ROOT_CUR.rglob("*.html")):
    rel = cur.relative_to(ROOT_CUR).as_posix()
    if rel in REWRITTEN:
        continue
    orig = ROOT_ORIG / rel
    if not orig.exists():
        continue
    if cur.read_bytes() != orig.read_bytes():
        not_identical.append(rel)

print(f"[1] Category-B files not byte-identical to original: {len(not_identical)}")
for r in not_identical[:10]:
    print(f"    - {r}")

# 2. All referenced stylesheet/script/image/href paths resolve on disk.
ATTR_RE = re.compile(r'\b(?:href|src)=["\']([^"\']+)["\']', re.IGNORECASE)

def is_external_or_anchor(u):
    if not u: return True
    if u.startswith(("http://","https://","mailto:","tel:","#","data:","javascript:")):
        return True
    return False

broken = []
total_local = 0
for cur in sorted(ROOT_CUR.rglob("*.html")):
    html = cur.read_text(encoding="utf-8", errors="replace")
    for m in ATTR_RE.finditer(html):
        u = m.group(1).split("#", 1)[0]
        if is_external_or_anchor(u):
            continue
        total_local += 1
        target = (cur.parent / u).resolve()
        if target.exists():
            continue
        if u.endswith("/"):
            if (target / "index.html").exists():
                continue
        broken.append((cur.relative_to(ROOT_CUR).as_posix(), m.group(1)))

print(f"\n[2] Local link/asset paths checked: {total_local}")
print(f"    Broken: {len(broken)}")
for b in broken[:20]:
    print(f"    - {b[0]}  ->  {b[1]}")

# 3. Every stylesheet reference points to a CSS file that exists.
LINK_RE = re.compile(r'<link\s+rel=["\']stylesheet["\']\s+href=["\']([^"\']+)["\']', re.IGNORECASE)
missing_css = []
for cur in sorted(ROOT_CUR.rglob("*.html")):
    html = cur.read_text(encoding="utf-8", errors="replace")
    for m in LINK_RE.finditer(html):
        href = m.group(1)
        if href.startswith(("http://","https://")):
            continue
        target = (cur.parent / href).resolve()
        if not target.exists():
            missing_css.append((cur.relative_to(ROOT_CUR).as_posix(), href))

print(f"\n[3] Missing CSS targets: {len(missing_css)}")
for m in missing_css[:10]:
    print(f"    - {m[0]}  ->  {m[1]}")

# 4. No stray "toggleMenu" scripts left in pages that shouldn't have them.
strays = []
for cur in sorted(ROOT_CUR.rglob("*.html")):
    rel = cur.relative_to(ROOT_CUR).as_posix()
    if rel in REWRITTEN or rel == "index.html":
        continue  # index.html correctly has its own toggle
    html = cur.read_text(encoding="utf-8", errors="replace")
    if "function toggleMenu()" in html:
        strays.append(rel)
print(f"\n[4] Stray toggleMenu scripts on non-rewritten pages: {len(strays)}")
for s in strays[:10]:
    print(f"    - {s}")

print("\nSummary:")
print(f"  Byte-identical Category-B pages restored: {(155 - len(REWRITTEN) - len(not_identical))} / {155 - len(REWRITTEN)}")
