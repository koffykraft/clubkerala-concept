#!/usr/bin/env python3
"""
Phase 1 dry-run: enumerate every Category-B file (small diff, only CSS+script touched)
and record the exact original <link rel="stylesheet" ...> line we need to restore.
Writes a plan file. Does NOT modify any HTML.
"""
import re
from pathlib import Path
import json

ROOT_CUR = Path("/app/KOFFYKRAFT-main")
ROOT_ORIG = Path("/app/_original_snapshot/KOFFYKRAFT-main")

# The 15 pages I rewrote from scratch — NEVER touch these in Phase 1.
REWRITTEN = {
    "index.html",  # already repaired in Phase 0
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
    "training/brewing/index.html",  # inline <style> stripped, HTML intact but Category-A per audit
    "training/cupping/index.html",  # same
}

# Files I never touched (Category C) — skip them; nothing to revert.
UNTOUCHED = set()

LINK_RE = re.compile(
    r'<link\s+rel=["\']stylesheet["\']\s+href=["\']([^"\']+)["\']\s*/?>',
    re.IGNORECASE,
)

def read(p):
    return p.read_text(encoding="utf-8", errors="replace")

def find_first_stylesheet(html):
    m = LINK_RE.search(html)
    return m.group(0) if m else None, m.group(1) if m else None

plan = []
skipped_untouched = []
skipped_rewritten = []
anomalies = []

html_files = sorted([p for p in ROOT_CUR.rglob("*.html")])
for cur in html_files:
    rel = cur.relative_to(ROOT_CUR).as_posix()

    if rel in REWRITTEN:
        skipped_rewritten.append(rel)
        continue

    orig = ROOT_ORIG / rel
    if not orig.exists():
        anomalies.append((rel, "no original counterpart"))
        continue

    cur_text = read(cur)
    orig_text = read(orig)

    if cur_text == orig_text:
        skipped_untouched.append(rel)
        continue

    # Find the CSS link in each
    cur_link_tag, cur_link_href = find_first_stylesheet(cur_text)
    orig_link_tag, orig_link_href = find_first_stylesheet(orig_text)

    if not orig_link_tag:
        anomalies.append((rel, "original had no <link rel=stylesheet>"))
        continue
    if not cur_link_tag:
        anomalies.append((rel, "current has no <link rel=stylesheet>"))
        continue

    if cur_link_href == orig_link_href:
        anomalies.append((rel, f"CSS already matches original ({orig_link_href}) but file still differs"))

    # Does the current file also carry the appended toggleMenu script?
    has_toggle_script = "function toggleMenu()" in cur_text

    # Verify the referenced original CSS file exists on disk
    css_target_rel = orig_link_href
    # resolve relative to the HTML file's directory
    resolved = (cur.parent / css_target_rel).resolve()
    css_exists = resolved.exists()

    plan.append({
        "file": rel,
        "current_link_href": cur_link_href,
        "restore_link_href": orig_link_href,
        "restore_link_tag": orig_link_tag,
        "current_link_tag": cur_link_tag,
        "has_toggle_script": has_toggle_script,
        "css_resolves": css_exists,
        "css_resolved_path": str(resolved),
    })

# Write plan
out = Path("/app/phase1_plan.json")
out.write_text(json.dumps({
    "phase0_restore_point": "git 3560389 / /app/phase0_backup.tar.gz",
    "counts": {
        "to_change": len(plan),
        "skipped_rewritten": len(skipped_rewritten),
        "skipped_untouched": len(skipped_untouched),
        "anomalies": len(anomalies),
        "total_html": len(html_files),
    },
    "anomalies": anomalies,
    "skipped_rewritten": sorted(skipped_rewritten),
    "skipped_untouched": sorted(skipped_untouched),
    "plan": plan,
}, indent=2))

print(f"Total HTML files:            {len(html_files)}")
print(f"To change (Category B):       {len(plan)}")
print(f"Skipped — rewritten (A):      {len(skipped_rewritten)}")
print(f"Skipped — untouched (C):      {len(skipped_untouched)}")
print(f"Anomalies to review:          {len(anomalies)}")
if anomalies:
    print("\nAnomalies:")
    for a in anomalies:
        print(f"  - {a[0]}: {a[1]}")

# CSS target validation summary
missing_css = [p for p in plan if not p["css_resolves"]]
print(f"\nOriginal CSS targets missing on disk: {len(missing_css)}")
for p in missing_css[:10]:
    print(f"  - {p['file']}  ->  {p['restore_link_href']}  (resolves to {p['css_resolved_path']})")

# Distribution of target stylesheets we'll be restoring
from collections import Counter
by_target = Counter(p["restore_link_href"] for p in plan)
print("\nRestore-target distribution:")
for k, v in by_target.most_common():
    print(f"  {v:4d}  {k}")

print("\nPlan written to /app/phase1_plan.json")
