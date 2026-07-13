# Phase 6 — training/brewing/index.html + training/cupping/index.html restoration report

## Restore points

| Marker | Value |
|---|---|
| Pre-Phase-6 tag | `phase-5-locked` |
| Post-Phase-6 tag | `phase-6-complete` |
| Tarball | `/app/phase6_backup.tar.gz` (25 MB) |
| Original snapshot | `/app/_original_snapshot/KOFFYKRAFT-main/` |

Rollback: `git checkout phase-5-locked -- KOFFYKRAFT-main/`

## Exact files changed by Phase 6

```
KOFFYKRAFT-main/training/brewing/index.html    (restored to byte-identical original)
KOFFYKRAFT-main/training/cupping/index.html    (restored to byte-identical original)
+ docs/phase-6-screenshots/*.png               (8 evidence images)
```

`git show --stat 9e8cb20` confirms exactly 2 code files changed: +340 insertions / −14 deletions (177 lines of the inline stylesheet restored + 7 removed link/script lines, on each of the two files).

## What was restored

On each of the two files, the earlier redesign had:
- **Stripped a ~170-line inline `<style>` block** and replaced it with `<link rel="stylesheet" href="../../assets/site/minimal.css">`.
- **Appended a 6-line `<script>toggleMenu()</script>` block** just before `</body>`.

Phase 6 removed both edits and reinstated the original inline `<style>` block verbatim.

### training/brewing/index.html — original inline stylesheet restored
Custom design tokens (`--ink #2b261f`, `--muted #8a8378`, `--line #eeeae2`, `--paper #fff`, `--gutter clamp(24px,6vw,92px)`), the "Arial Narrow" typographic system, the `.top` header row layout, the `.brand` mark, the `.top nav a[aria-current="page"]` underline, the `.room` full-height section with the centered `.reference-mark` figure, the H1 in tracked uppercase, the `.lessons` two-column list with 15 lesson rows and hairline dividers, the `.foot` two-column footer, and the mobile media query at 700 px.

### training/cupping/index.html — original inline stylesheet restored
Same design system as brewing (same variables, same header/footer/nav/room/lessons/mark/reference-mark rules), applied to the cupping-course landing which lists **18 items** (Start + 01–17).

## What was NOT changed on these two files

- Body content, headings, wording — untouched (already identical to original bodies)
- Nav links, targets — untouched (already identical)
- Lesson list contents (15 for brewing, 18 for cupping) — untouched
- Filenames, URLs — untouched
- All other pages on the site — untouched

## Content comparison against the original snapshot

```
diff /app/_original_snapshot/KOFFYKRAFT-main/training/brewing/index.html /app/KOFFYKRAFT-main/training/brewing/index.html
diff /app/_original_snapshot/KOFFYKRAFT-main/training/cupping/index.html /app/KOFFYKRAFT-main/training/cupping/index.html
```

Both diffs produce **zero output**. Both files are **byte-identical** to the original snapshot.

## Whole-site link and asset validation

`python3 /app/audit_links.py`:
- Files scanned: **155**
- Local links: **2,137**
- Broken links: **0**
- Missing CSS targets: **0**
- Missing images: **0**

`python3 /app/phase1_verify.py`:
- Category-B pages byte-identical to original: **140 / 140** ✓ (unchanged; the two Phase-6 files are Category-A / rewritten pages so they were not in that check)
- With Phase 6 restore, the total count of pages byte-identical to their original is now effectively **142** (the 140 Phase-1 + the 2 Phase-6 files).

## Confirmation Phases 1–5 remain unchanged

| Phase | Verification | Result |
|---|---|---|
| Phase 1 | `phase1_verify.py` — 140 pages byte-identical to original | **140 / 140** ✓ |
| Phase 2 Coffee | `git diff phase-2-locked HEAD -- coffee/ coffee-content.css` | **empty** ✓ |
| Phase 3 Buna | `git diff phase-3-locked HEAD -- buna/ buna-content.css` | **empty** ✓ |
| Phase 4 Links | `git diff phase-4-locked HEAD -- links/ links-content.css` | **empty** ✓ |
| Phase 5 Estate | `git diff phase-5-locked HEAD -- estate/ estate-content.css` | **empty** ✓ |
| Homepage | `git diff phase-5-locked HEAD -- index.html` | **empty** ✓ |
| Global `minimal.css` | not modified since Phase 0 | ✓ |

## Screenshots

8 PNGs at `docs/phase-6-screenshots/` — 2 pages × 2 stages (before / after) × 2 viewports (desktop / mobile).

The before/after pair shows:
- **Before**: page rendered as an unstyled linear stack — nav labels on one line, oversized H1, all 15 (or 18) lesson entries collapsed into one wrapping paragraph.
- **After**: the original editorial layout is back — brand-mark left / nav right with `aria-current` underline, centered `.reference-mark` figure, uppercase tracked H1 "BREWING REFERENCE NOTES" (or "CUPPING REFERENCE NOTES"), the reference-note, the numbered two-column lesson list with hairline dividers, and the two-column footer.

## Stopped

Phase 6 is closed. Awaiting your approval before the final KoffyKraft V1 Recovery Report.
