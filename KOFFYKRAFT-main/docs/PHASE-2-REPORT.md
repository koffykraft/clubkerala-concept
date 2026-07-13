# Phase 2 — Coffee section content restoration report

## Restore points

| Marker | git ref / path |
|---|---|
| Phase 1 tag (pre-Phase-2) | `phase-1-complete` → `d943a0b` |
| Phase 1 tarball | `/app/phase1_backup.tar.gz` |
| Phase 2 tag (post) | `phase-2-complete` → `73ca279` |
| Phase 2 tarball | `/app/phase2_backup.tar.gz` |
| Original ZIP snapshot | `/app/_original_snapshot/KOFFYKRAFT-main/` |

Rollback command if needed: `git checkout phase-1-complete -- KOFFYKRAFT-main/`

## Files changed by Phase 2 (excluding evidence screenshots)

| File | Op |
|---|---|
| `assets/site/coffee-content.css` | **added** (144 lines, coffee-section-only supplemental) |
| `coffee/index.html` | rewritten body to restore original doors + wording |
| `coffee/roastery/index.html` | rewritten body to restore original doors + wording |
| `coffee/roastery/buy/index.html` | rewritten body to restore original 4-door list + wording |
| `coffee/roastery/browse/index.html` | rewritten body to restore original 6-item stock-list + wording |
| `coffee/roastery/roast-days/index.html` | rewritten body to restore original image + note + doors |

No other files were modified. Confirmed by `git show --stat 73ca279`.

## Invented passages removed (verbatim list)

### `coffee/index.html`
- Meta description "KoffyKraft coffee: roastery, learning, notes, and resources." (restored to original)
- `<p>Our roasting process and available coffees</p>`
- `<p>Coffee brewing and cupping courses</p>`
- `<p>Detailed brewing and roasting notes</p>`
- `<p>Research and reference materials</p>`

### `coffee/roastery/index.html`
- Meta description "KoffyKraft roastery: our coffees, roast days, and brewing guides." (restored)
- `<p>Purchase our roasted coffees</p>`
- `<p>Browse our current selection</p>`
- `<p>Our roasting schedule</p>`
- `<p>How to brew our coffee</p>`

### `coffee/roastery/buy/index.html`
- Title "Buy Coffee | KoffyKraft" → restored to original "Buy | KoffyKraft"
- Meta description "Buy freshly roasted coffee from KoffyKraft." → restored to "Buy KoffyKraft coffee."
- Door label "Browse Coffees" → restored to original "Coffees"
- Door label "Brewing Guide" → restored to original "Brew"
- `<p>View our current selection</p>`
- `<p>Check our schedule</p>`
- `<p>Learn to brew</p>`

### `coffee/roastery/browse/index.html`
- Title "Browse Coffees | KoffyKraft" → restored to original "Coffees | KoffyKraft"
- Meta description "Browse KoffyKraft's current coffee selection." → restored to "Coffees available for KoffyKraft roast days."
- H1 kept as **Coffees** (was already correct)
- Footer text "Browse Coffees" → restored to "Coffees"
- Introductory line I invented: "Current selection updated based on roast days"
- Entire invented 3-card grid: `Purchase / Roast Schedule / Brewing` and its 3 invented `<p>` descriptions

### `coffee/roastery/roast-days/index.html`
- Meta description "KoffyKraft roasting schedule." → restored to "KoffyKraft roast days and roast-to-order practice."
- Subhead I invented under H1: `<p class="text-muted">Our roasting schedule</p>`
- Invented line: "Roasting schedule and availability information"
- Entire invented 3-card grid: `Order Coffee / Browse / Brewing` and its 3 invented `<p>` descriptions

## Original passages restored (verbatim from `/app/_original_snapshot/KOFFYKRAFT-main/`)

### `coffee/index.html`
- Original meta description: *"KoffyKraft coffee: roastery, learning, notes, photos, and papers."*
- Original 4-door door-list: **Roastery**, **Learn** (→ `../training/quiet/`), **Notes** (→ `../training/deeper-dive/`), **Papers** (→ `../links/`)
- Original hero image `home-beans.jpg`, alt `"Roasted coffee beans"`
- Original footer: `Coffee` + `Home` link

### `coffee/roastery/index.html`
- Original meta description: *"KoffyKraft roastery page."*
- Original 4-door door-list: **Buy**, **Coffees** (→ `browse/`), **Roast Days**, **Brew** (→ `../../training/quiet/brewing/`)
- Original hero image `home-roaster-detail.jpg`, alt `"Coffee roaster detail"`
- Original footer: `Roastery` + `Home` link

### `coffee/roastery/buy/index.html`
- Original title: `Buy | KoffyKraft`
- Original meta description: *"Buy KoffyKraft coffee."*
- Original paragraph (already intact, preserved): *"KoffyKraft is a garage roastery. Coffees are usually roasted to order on roast days. Washed coffees are the usual focus; other processes appear when they make sense."*
- Original 4-door door-list, in order: **Coffees**, **Roast Days**, **Brew**, **Roastery** (the missing 4th door restored)
- Original hero image `koffykraft-coffee-bag.jpg`, alt `"KoffyKraft roasted coffee bag"`

### `coffee/roastery/browse/index.html`
- Original title: `Coffees | KoffyKraft`
- Original meta description: *"Coffees available for KoffyKraft roast days."*
- Original `.image-space` placeholder tile (aria-hidden decorative box) restored
- Original small-note: *"These are coffees in hand for roast days. Most are kept green and roasted after orders are gathered."*
- Original **6-item stock-list**, each verbatim:
  1. `Cauvery Peak` — **Shevaroys Estate Reserve** — link: `https://cauverypeakestate.com/` (Estate source)
  2. `Cauvery Peak` — **Cauvery Peak Estate Heritage** — link: `https://cauverypeakestate.com/` (Estate source)
  3. `Cauvery Peak` — **Glenfell Estate Classic** — link: `https://cauverypeakestate.com/` (Estate source)
  4. `Loyola Estate / Lower Pulney Hills` — **Washed Arabica** — description: *"Shade-grown around 4000-4300 ft; hand-picked, pulped, fermented, washed, and sun-dried on tables."* — link: `http://www.loyolaestate.com/gallery/brochure/LoyolaEstate-Brochure.pdf` (Estate brochure)
  5. `Heggadde Estate` — **James Rodrigues Coffee** — link: `https://www.jamesrodriguescoffee.com/pages/about-us` (Estate source)
  6. `Monsooned Malabar Arabica` — **Monsooned** — link: `https://aspinwallcoffee.com/monsooned-malabar-coffee/` (Process source)
- Original 4-door door-list: **Buy**, **Roast Days**, **Brew**, **Roastery**
- Original footer: `Coffees` + `Home` link

### `coffee/roastery/roast-days/index.html`
- Original meta description: *"KoffyKraft roast days and roast-to-order practice."*
- Original hero image `home-roaster-detail.jpg`, alt `"KoffyKraft roaster detail"` (was completely missing before)
- Original small-note: *"Orders are grouped before roasting when possible. The offer may be two, three, or four coffees at a time, depending on green stock and roast day capacity."*
- Original 4-door door-list, in order: **Buy**, **Green Stock** (→ `../browse/`), **Brew**, **Roastery** (previously showed only 3 invented labels)
- Original footer: `Roast Days` + `Home` link

## Content verification result

`python3 /app/phase2_verify.py` — outcomes across all 5 pages:

- Title: **identical to original on all 5 pages**
- Meta description: **identical**
- All `<img>` alt attributes: **identical**
- All `<img>` src attributes: **identical**
- Every original href present in current: **yes, on all 5 pages**
- Every original text passage present in current: **yes, on all 5 pages** ("No original text is missing")
- Extra text present in current beyond original: only the sticky nav labels `Buy`, `Coffees`, and breadcrumb tokens `Home`, `Coffee`, `Roastery`, `Coffees`, `Roast Days`, `☰` — all part of the approved Phase 0 minimalist chrome; no invented body copy.

The single href difference on each page is the CSS link: original `passage.css` replaced by `minimal.css` + `coffee-content.css` (approved chrome swap).

## Link and asset validity

Whole-site audit after Phase 2 (`python3 /app/audit_links.py`):

- Files scanned: **155**
- Total local links found: **2,130**
- Broken links: **0**
- Missing CSS targets: **0**
- Missing images: **0**

Phase 1 integrity check (`python3 /app/phase1_verify.py`) still passes:

- Category-B files byte-identical to original: **140 / 140**
- Local link/asset paths broken: **0**
- Stray `toggleMenu` scripts on non-rewritten pages: **0**

## Screenshots

20 PNGs committed at `KOFFYKRAFT-main/docs/phase-2-screenshots/`:

- `coffee_landing` — before / after × desktop / mobile
- `roastery_landing` — before / after × desktop / mobile
- `buy` — before / after × desktop / mobile
- `browse` — before / after × desktop / mobile
- `roast_days` — before / after × desktop / mobile

"before" = Phase 1 state (my invented copy still present). "after" = Phase 2 state (original content restored).

## What was NOT changed

- Homepage `index.html` — untouched; still Phase 0 state; top nav still **Buy | Coffees**; no "Sections" link added.
- Any file outside the Coffee section — untouched (verified by `git show --stat`).
- Any of the 136 Phase-1 specialist pages — still byte-identical to their originals.
- `minimal.css` — not modified; the coffee content-support styles live in a new separate file `coffee-content.css` loaded only by the 5 Coffee-section pages.
- No original coffee, no original description, no original door was dropped.
- No URL, no filename changed.

## Notes for your review

1. On coffee-section pages I trimmed the sticky top-nav from the previous 5 items (Coffee / Buna / Estate / Learn / Buy) to the same 2 items the homepage uses (**Buy | Coffees**). Rationale: the 5-item nav was itself Phase-0 invention that didn't exist in the original coffee pages (whose header had only a "Home" link), and matching the homepage is consistent. If you want the fuller nav back, tell me and I'll restore it as its own step.

2. The `.image-space` placeholder tile on `coffee/roastery/browse/index.html` renders as a subtle grey rectangle at ~4:5 aspect. That matches the original intent (the original also had an empty placeholder, no photo). If you want an actual photo there instead, tell me which asset.

3. The two "before" screenshots for pages I had previously invented content on are intentionally different from "after". They document what invented copy was removed.

## Stopping here as instructed

Phase 2 is complete. **I will not touch any other section without your approval.** Suggested Phase 3 targets (all still holding invented copy from the earlier rewrite):

- `buna/index.html`, `buna/traditions/index.html`, `buna/brewing/index.html` (has a 5-item stock-list with real specialist copy to restore), `buna/learn/index.html`, `buna/library/index.html`
- `estate/index.html`
- `links/index.html` (needs original curated link list restored)
- `training/brewing/index.html`, `training/cupping/index.html` (their inline `<style>` was stripped in the earlier pass; content intact but styling relies on gone CSS)

Say which section to do next and I'll produce a restoration plan against the original snapshot before touching any file.
