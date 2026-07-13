#!/usr/bin/env python3
"""
Phase 1 repair — minimal, targeted edits ONLY:
  1. If current stylesheet link href differs from original, replace exactly that <link ...> tag with the original one.
  2. Remove the appended <script>function toggleMenu()...</script> block I added before </body>.

Does NOT modify body content, headings, wording, images, structure, navigation, links, or filenames.
"""
import re
import json
from pathlib import Path

ROOT_CUR = Path("/app/KOFFYKRAFT-main")
ROOT_ORIG = Path("/app/_original_snapshot/KOFFYKRAFT-main")

# 15 pages rewritten in the previous pass — do NOT touch in Phase 1.
REWRITTEN = {
    "index.html",
    "coffee/index.html",
    "coffee/roastery/index.html",
    "coffee/roastery/buy/index.html",
    "coffee/roastery/browse/index.html",
    "coffee/roastery/roast-days/index.html",
    "buna/index.html",
    "buna/traditions/index.html",
    "buna/brewing/index.html",
    "buna/learn/index.html",
    "buna/library/index.html",
    "estate/index.html",
    "links/index.html",
    "training/brewing/index.html",
    "training/cupping/index.html",
}

LINK_RE = re.compile(
    r'<link\s+rel=["\']stylesheet["\']\s+href=["\']([^"\']+)["\']\s*/?>',
    re.IGNORECASE,
)

# The exact appended script block we introduced. Match tolerantly across whitespace.
SCRIPT_RE = re.compile(
    r'\n?\s*<script>\s*function toggleMenu\(\s*\)\s*\{[^<]*document\.getElementById\(\s*[\'"]mainNav[\'"]\s*\)\.classList\.toggle\(\s*[\'"]active[\'"]\s*\);?\s*\}\s*</script>\s*',
    re.IGNORECASE,
)

changes = []
warnings = []

for cur in sorted(ROOT_CUR.rglob("*.html")):
    rel = cur.relative_to(ROOT_CUR).as_posix()
    if rel in REWRITTEN:
        continue
    orig = ROOT_ORIG / rel
    if not orig.exists():
        continue

    cur_text = cur.read_text(encoding="utf-8", errors="replace")
    orig_text = orig.read_text(encoding="utf-8", errors="replace")

    if cur_text == orig_text:
        continue  # already identical

    new_text = cur_text
    ops = []

    # --- Operation A: restore original CSS link tag verbatim if it differs ---
    cur_link_m = LINK_RE.search(new_text)
    orig_link_m = LINK_RE.search(orig_text)
    if cur_link_m and orig_link_m:
        cur_tag = cur_link_m.group(0)
        orig_tag = orig_link_m.group(0)
        if cur_tag != orig_tag:
            # Replace only the first occurrence, exactly.
            new_text = new_text.replace(cur_tag, orig_tag, 1)
            ops.append(f"link: {cur_link_m.group(1)}  ->  {orig_link_m.group(1)}")

    # --- Operation B: remove appended toggleMenu script block ---
    if "function toggleMenu()" in new_text and "function toggleMenu()" not in orig_text:
        new_text2, n = SCRIPT_RE.subn("\n", new_text, count=1)
        if n == 1:
            new_text = new_text2
            ops.append("script: removed appended toggleMenu block")
        else:
            warnings.append((rel, "toggleMenu present but regex did not match — skipped script removal"))

    if new_text != cur_text:
        cur.write_text(new_text, encoding="utf-8")
        changes.append({"file": rel, "ops": ops, "now_identical_to_original": (new_text == orig_text)})

# Summary
identical = sum(1 for c in changes if c["now_identical_to_original"])
print(f"Files modified: {len(changes)}")
print(f"  of which now byte-identical to original: {identical}")
print(f"  of which still differ (should investigate): {len(changes) - identical}")
if warnings:
    print(f"\nWarnings ({len(warnings)}):")
    for w in warnings:
        print(f"  - {w[0]}: {w[1]}")

# Show any remaining diffs (shouldn't be many)
residual = [c for c in changes if not c["now_identical_to_original"]]
if residual:
    print("\nFiles that still differ after Phase 1 (first 10):")
    for c in residual[:10]:
        print(f"  - {c['file']}   ops={c['ops']}")

# Save log
Path("/app/phase1_execution.json").write_text(json.dumps({
    "changed_count": len(changes),
    "identical_after_restore": identical,
    "residual_count": len(residual),
    "warnings": warnings,
    "changes": changes,
}, indent=2))
print("\nExecution log: /app/phase1_execution.json")
