# Phase 5 — estate/index.html content restoration report

## Restore points

| Marker | Value |
|---|---|
| Pre-Phase-5 tag | `phase-4-locked` |
| Post-Phase-5 tag | `phase-5-complete` |
| Tarball | `/app/phase5_backup.tar.gz` (25 MB) |
| Original snapshot | `/app/_original_snapshot/KOFFYKRAFT-main/` |

Rollback: `git checkout phase-4-locked -- KOFFYKRAFT-main/`

## Exact files changed by Phase 5

```
KOFFYKRAFT-main/assets/site/estate-content.css     (new, Estate-only, 60 lines)
KOFFYKRAFT-main/estate/index.html                  (rewritten body)
+ docs/phase-5-screenshots/*.png                   (4 evidence images)
```

## Invented passages removed

1. **Meta description**: *"Thumpassery Estate: Living Root Network farming, produce, and sustainable practices."* → restored to original
2. **Invented subhead** under H1: `<p class="text-muted">Thumpassery Estate, Living Root Network</p>` → removed
3. **Door 1 label** renamed: *"LRN Handbook"* → restored to **"LRN"**
4. **Door 1 description**: `<p>Living Root Network farming guide</p>` → removed
5. **Door 2 label** re-cased: *"Field Cards"* → restored to **"Field cards"** (lowercase c, verbatim from original)
6. **Door 2 description**: `<p>Quick reference guides</p>` → removed
7. **Door 3 description**: `<p>Research and references</p>` → removed
8. **Door 4 label** renamed: *"Resources"* → restored to **"References"**
9. **Door 4 description**: `<p>Additional materials</p>` → removed

## Original items restored (verbatim from `/app/_original_snapshot/KOFFYKRAFT-main/estate/index.html`)

| Element | Restored value |
|---|---|
| `<title>` | `Estate \| KoffyKraft` (unchanged, already correct) |
| Meta description | *"Thumpassery Estate, Living Root Network, produce, recipes, photos, and notes."* |
| H1 | `Estate` (unchanged) |
| Image | `../assets/site/home-living-root.jpg`, alt=`"Living root planting at Thumpassery Estate"` |
| Footer | `Estate` + `Home` link (unchanged) |

**4-door door-list — in exact original order, with exact original labels and targets:**

| # | Label | Href |
|---|---|---|
| 1 | **LRN** | `../training/lrn/` |
| 2 | **Field cards** | `../training/lrn/field-cards.html` |
| 3 | **Papers** | `../training/lrn/references.html` |
| 4 | **References** | `../links/` |

## Content comparison against the original snapshot

Run: `python3 /app/phase5_verify.py`

| Check | Result |
|---|---|
| Title identical | ✓ |
| Meta description identical | ✓ |
| Image alts identical | ✓ |
| Image srcs identical | ✓ |
| 4 door hrefs in exact original order | ✓ |
| All 4 door labels with exact case ("LRN", "Field cards", "Papers", "References") | ✓ |
| No original text passage missing | ✓ |
| **Total structural issues** | **0** |

Extras flagged: `/` breadcrumb separator and 1 extra "Estate" occurrence (breadcrumb crumb) — both approved Phase 0 chrome.

## Whole-site link and asset validation

`python3 /app/audit_links.py`:
- Files scanned: **155**
- Local links: **2,139**
- Broken links: **0**
- Missing CSS targets: **0**
- Missing images: **0**

## Confirmation Phases 1–4 remain unchanged

| Phase | Verification | Result |
|---|---|---|
| Phase 1 | 140 Category-B files byte-identical to original | **140 / 140** ✓ |
| Phase 2 Coffee | `git diff phase-2-locked HEAD -- coffee/ coffee-content.css` | **empty** ✓ |
| Phase 3 Buna | `git diff phase-3-locked HEAD -- buna/ buna-content.css` | **empty** ✓ |
| Phase 4 Links | `git diff phase-4-locked HEAD -- links/ links-content.css` | **empty** ✓ |
| Homepage | `git diff phase-4-locked HEAD -- index.html` | **empty** ✓ |
| Training / Citane / cold-brew / learn | untouched | ✓ |
| Global `minimal.css` | not modified | ✓ |

## Screenshots

4 PNGs at `docs/phase-5-screenshots/`:
- `estate_before_desktop.png` — Phase 4 state (5-item invented top-nav, invented subhead, invented labels & descriptions)
- `estate_after_desktop.png` — Phase 5 state (2-item Buy | Coffees nav, no subhead, verbatim LRN / Field cards / Papers / References)
- `estate_before_mobile.png`
- `estate_after_mobile.png`

## Presentational consistency (matching Phases 2–4)

The sticky top-nav was trimmed to **Buy | Coffees** to match the homepage, Coffee, Buna and Links sections. This continues the approved policy. The original Estate page had only "Home" in its header; nothing in the original was shortened, obscured, merged or reordered.

## Stopped

Phase 5 is closed. Awaiting your approval before the final phase.

Suggested **Phase 6** — the two remaining pages you flagged in the original audit:

- **`training/brewing/index.html`** — inline `<style>` stripped in the initial pass; content is intact and byte-identical to original except the CSS link. The simplest fix is to restore the original inline `<style>` block, so the page renders exactly as originally designed.
- **`training/cupping/index.html`** — same situation, same fix.

Both are one-line CSS-link reverts + a small stylesheet block restore. Say the word and I'll produce the plan against the original snapshot before touching either file.

After Phase 6, I will produce the **final KoffyKraft V1 Recovery Report** as requested.
