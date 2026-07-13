# Phase 3 — Buna section content restoration report

## Restore points

| Marker | Value |
|---|---|
| Pre-Phase-3 tag | `phase-2-locked` → `a433a69` |
| Post-Phase-3 tag | `phase-3-complete` → `4aa3703` |
| Tarball | `/app/phase3_backup.tar.gz` (23 MB) |
| Original snapshot | `/app/_original_snapshot/KOFFYKRAFT-main/` |

Rollback: `git checkout phase-2-locked -- KOFFYKRAFT-main/`

## Exact files changed by Phase 3 (only these)

```
KOFFYKRAFT-main/assets/site/buna-content.css       (new, 135 lines, Buna-only)
KOFFYKRAFT-main/buna/index.html                    (rewritten body)
KOFFYKRAFT-main/buna/traditions/index.html         (rewritten body)
KOFFYKRAFT-main/buna/brewing/index.html            (rewritten body, 5-item list restored)
KOFFYKRAFT-main/buna/learn/index.html              (rewritten body)
KOFFYKRAFT-main/buna/library/index.html            (rewritten body)
+ docs/phase-3-screenshots/*.png                   (20 evidence images)
```

`git diff --stat phase-2-locked f686be9 -- KOFFYKRAFT-main/` shows only these files (and only inside `buna/` + the new `buna-content.css`). Nothing else changed.

## Invented passages removed (verbatim list)

### `buna/index.html`
- Title changed back: `Buna | KoffyKraft` (was already correct)
- Meta description swapped: *"Buna: coffee leaf beverage, cultural brewing traditions, and methods."* → **restored** to *"Buna at KoffyKraft: coffee leaf beverage, cultural brewing traditions, methods, learning, and library."*
- Invented subhead removed: `<p class="text-muted">Coffee leaf beverage traditions</p>`
- Invented per-door descriptions removed: *"Cultural practices and history"*, *"Preparation methods and recipes"*, *"Understanding coffee leaf"*, *"References and research"*
- `.content-grid` / `.content-card` layout replaced with the original `.door-list` / `.door` structure and the original `.image-space` placeholder

### `buna/traditions/index.html`
- Title changed back: *"Buna Traditions | KoffyKraft"* → **restored** to *"Traditions | KoffyKraft"*
- Meta description swapped: *"Coffee leaf beverage cultural traditions and history."* → **restored** to *"Cultural coffee leaf beverage traditions in the Buna library."*
- Invented H1 corrected: *"Buna Traditions"* → **restored** to *"Traditions"*
- Invented subhead removed: `<p class="text-muted">Cultural practices and history</p>`
- Invented placeholder paragraph removed: *"Exploring the cultural heritage of coffee leaf beverages"*
- Footer text corrected: *"Buna Traditions"* → **restored** to *"Traditions"*
- **Content restored**: the `sample-leaf-fresh.jpg` image (was missing) and the 4-door door-list (Engere / Chemo / Kawa Daun / Kuti), all with the original targets `../brewing/{engere,chemo,kawa-daun,kuti}/`

### `buna/brewing/index.html`
- Title changed back: *"Buna Brewing | KoffyKraft"* → **restored** to *"Brewing | KoffyKraft"*
- Meta description swapped: *"Coffee leaf brewing methods and preparation guides."* → **restored** to *"Buna brewing traditions and preparation papers."*
- Invented H1 corrected: *"Buna Brewing"* → **restored** to *"Brewing"*
- Invented subhead removed: `<p class="text-muted">Preparation methods and recipes</p>`
- Invented per-door descriptions removed: *"Ethiopian style preparation"*, *"Traditional method"*, *"Indonesian coffee leaf tea"*, *"Regional preparation"*
- Missing 5th door **Preparation Studies** restored
- Door order restored to original: Engere / Chemo / Kawa Daun / Kuti / Preparation Studies
- Footer text corrected: *"Buna Brewing"* → **restored** to *"Brewing"*
- **Content restored**: `brewing-mark.svg` icon + the **5-item curated stock-list**, verbatim (see next section)

### `buna/learn/index.html`
- Title changed back: *"Learn About Buna | KoffyKraft"* → **restored** to *"Learn | KoffyKraft"*
- Meta description swapped: *"Understanding coffee leaf beverages."* → **restored** to *"Buna learning course and sensory school."*
- Invented H1 corrected: *"Learn About Buna"* → **restored** to *"Learn"*
- Invented subhead removed: `<p class="text-muted">Understanding coffee leaf</p>`
- Invented placeholder paragraph removed: *"Educational resources about coffee leaf beverages"*
- Footer text corrected: *"Learn About Buna"* → **restored** to *"Learn"*
- **Content restored**: `buna-landscape.jpg` reference image + the 4-door door-list (Traditions / Brewing / Preparation Studies / Library)

### `buna/library/index.html`
- Title changed back: *"Buna Library | KoffyKraft"* → **restored** to *"Library | KoffyKraft"*
- Meta description swapped: *"Coffee leaf beverage references and research."* → **restored** to *"Buna library and references."*
- Invented H1 corrected: *"Buna Library"* → **restored** to *"Library"*
- Invented subhead removed: `<p class="text-muted">References and research</p>`
- Invented placeholder paragraph removed: *"Collection of resources about coffee leaf beverages"*
- Footer text corrected: *"Buna Library"* → **restored** to *"Library"*
- **Content restored**: `buna-landscape.jpg` reference image + the 4-door door-list (Traditions / Brewing / Preparation Studies / Field Notes)

## Original passages restored (verbatim from `/app/_original_snapshot/KOFFYKRAFT-main/`)

### `buna/index.html`
- Title: `Buna | KoffyKraft`
- Meta: *"Buna at KoffyKraft: coffee leaf beverage, cultural brewing traditions, methods, learning, and library."*
- H1: `Buna`
- `.image-space` decorative placeholder (aria-hidden) — original had this too
- 4-door door-list: **Traditions**, **Brewing**, **Learn**, **Library** (with targets `traditions/`, `brewing/`, `learn/`, `library/`)
- Footer: `Buna` + `Home` link

### `buna/traditions/index.html`
- Title: `Traditions | KoffyKraft`
- Meta: *"Cultural coffee leaf beverage traditions in the Buna library."*
- H1: `Traditions`
- Image: `../../assets/site/sample-leaf-fresh.jpg`, alt `"Fresh coffee leaves"`
- 4-door door-list: **Engere**, **Chemo**, **Kawa Daun**, **Kuti** (linking to `../brewing/{engere,chemo,kawa-daun,kuti}/`)
- Footer: `Traditions` + `Home` link

### `buna/brewing/index.html`
- Title: `Brewing | KoffyKraft`
- Meta: *"Buna brewing traditions and preparation papers."*
- H1: `Brewing`
- Image: `../../assets/site/brewing-mark.svg`, alt `"Brewing mark"`
- 5-door door-list, in original order: **Engere**, **Chemo**, **Kawa Daun**, **Kuti**, **Preparation Studies** (targets `engere/`, `chemo/`, `kawa-daun/`, `kuti/`, `preparation-studies/`)
- **5-item curated stock-list**, each verbatim from the original:
  1. `Milk brew` — **Engere** — *"Coffee leaf brew strained, then combined with fresh milk. Documented in South Ethiopia."* — link `Open` → `engere/`
  2. `Leaf and herbs` — **Chemo** — *"Coffee leaves prepared with local aromatics. Documented in Tepi, Southwestern Ethiopia."* — link `Open` → `chemo/`
  3. `Smoke dried` — **Kawa Daun** — *"Smoked coffee leaf decoction from the Minangkabau highlands of West Sumatra."* — link `Open` → `kawa-daun/`
  4. `Fallen leaf` — **Kuti** — *"Sun-dried mature or fallen coffee leaves, usually prepared by decoction."* — link `Open` → `kuti/`
  5. `Modern methods` — **Preparation Studies** — *"Temperature, time, decoction, processing, aroma, and consumer perception."* — link `Open` → `preparation-studies/`
- Footer: `Brewing` + `Home` link

### `buna/learn/index.html`
- Title: `Learn | KoffyKraft`
- Meta: *"Buna learning course and sensory school."*
- H1: `Learn`
- Image: `../../assets/site/buna-landscape.jpg`, alt `"Buna reference sheet"`
- 4-door door-list: **Traditions**, **Brewing**, **Preparation Studies**, **Library** (targets `../traditions/`, `../brewing/`, `../brewing/preparation-studies/`, `../library/`)
- Footer: `Learn` + `Home` link

### `buna/library/index.html`
- Title: `Library | KoffyKraft`
- Meta: *"Buna library and references."*
- H1: `Library`
- Image: `../../assets/site/buna-landscape.jpg`, alt `"Buna reference sheet"`
- 4-door door-list: **Traditions**, **Brewing**, **Preparation Studies**, **Field Notes** (targets `../traditions/`, `../brewing/`, `../brewing/preparation-studies/`, `../field-notes/`)
- Footer: `Library` + `Home` link

## Content comparison against the original snapshot

Run: `python3 /app/phase3_verify.py`

| Page | Title | Meta desc | Image alts | Image srcs | Original hrefs | Original text passages missing | Total structural issues |
|---|---|---|---|---|---|---|---|
| `buna/index.html` | ✓ identical | ✓ identical | ✓ identical | ✓ identical | ✓ all present | 0 | **0** |
| `buna/traditions/index.html` | ✓ identical | ✓ identical | ✓ identical | ✓ identical | ✓ all present | 0 | **0** |
| `buna/brewing/index.html` | ✓ identical | ✓ identical | ✓ identical | ✓ identical | ✓ all present | 0 | **0** |
| `buna/learn/index.html` | ✓ identical | ✓ identical | ✓ identical | ✓ identical | ✓ all present | 0 | **0** |
| `buna/library/index.html` | ✓ identical | ✓ identical | ✓ identical | ✓ identical | ✓ all present | 0 | **0** |

The only extras present in current-but-not-original are the approved chrome tokens (`/` breadcrumb separators, the section name inside the breadcrumb, and the sticky-nav labels `Buy` and `Coffees`). No invented copy remains.

The single href difference on each page is the CSS link swap: original `passage.css` → `minimal.css` + `buna-content.css` (approved presentational chrome, per your Phase 0 approval).

## Whole-site link and asset validation

`python3 /app/audit_links.py`:
- Files scanned: **155**
- Total local links found: **2,142**
- Broken links: **0**
- Missing CSS targets: **0**
- Missing images: **0**

## Phase 1 and Phase 2 integrity confirmation

- **Phase 1** (`python3 /app/phase1_verify.py`): 140 / 140 Category-B files still byte-identical to their originals.
- **Phase 2 Coffee section** (`git diff phase-2-locked HEAD -- KOFFYKRAFT-main/coffee/ KOFFYKRAFT-main/assets/site/coffee-content.css`): **empty diff**. Not a single Coffee file changed during Phase 3.
- **Homepage** (`git diff phase-2-locked HEAD -- KOFFYKRAFT-main/index.html`): **empty diff**. Untouched.

## Screenshots

20 PNGs committed at `KOFFYKRAFT-main/docs/phase-3-screenshots/`:

| Page | Files |
|---|---|
| `buna_landing` | before/after × desktop/mobile |
| `traditions` | before/after × desktop/mobile |
| `brewing` | before/after × desktop/mobile |
| `learn` | before/after × desktop/mobile |
| `library` | before/after × desktop/mobile |

"before" = Phase 2 state (my invented copy still present, missing images, missing 5th door, invented H1s). "after" = Phase 3 state (original content restored verbatim).

## What was NOT changed (as required)

- **Coffee section** — untouched. `git diff phase-2-locked HEAD -- KOFFYKRAFT-main/coffee/` is empty.
- **Homepage** `index.html` — untouched.
- **Estate**, **Links**, **Training**, **Citane**, **cold-brew**, **learn/**, all `buna/brewing/{engere,chemo,kawa-daun,kuti,preparation-studies}/`, `buna/field-notes/`, `buna/leaf/` — untouched.
- Any of the 140 Phase-1-restored specialist pages — still byte-identical to their originals.
- `minimal.css`, `coffee-content.css` — not modified.
- No URL, no filename, no image src, no citation, no source-link changed.
- No tradition or method renamed.
- No page merged with another.

## Presentational choice matching Phase 2

On the Buna pages I trimmed the sticky top-nav from the previous 5 items (Coffee / Buna / Estate / Learn / Buy) to the same 2 items the homepage and Coffee section use (**Buy | Coffees**). This is the same policy already approved for Phase 2 and keeps chrome consistent across restored sections. The original Buna pages had only "Home" in the header; the reduced sticky nav does not shorten, obscure or reorder any original content.

## Stopped

Phase 3 is complete. I will not touch any other section without your approval.

Suggested Phase 4 targets, ordered by how much invented copy each still holds:

1. **`links/index.html`** — currently a 4-tile generic references grid I wrote; the original had a curated list of links. Highest content-loss remaining.
2. **`estate/index.html`** — currently has invented card descriptions but the four doors + image are correct.
3. **`training/brewing/index.html`** and **`training/cupping/index.html`** — inline `<style>` was stripped in the initial pass. Content intact; presentation needs restoration.

Say the word and I'll produce a restoration plan against the original snapshot before touching any file.
