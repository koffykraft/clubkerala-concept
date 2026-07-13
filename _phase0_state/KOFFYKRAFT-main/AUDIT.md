# KoffyKraft — Live Site Audit
_Prepared before any repair work. No files are modified by this document._

Origin snapshot used for comparison: `/tmp/kk-original/KOFFYKRAFT-main` (unzipped from the ZIP you uploaded on 13 July, 2026).
Current live tree: `/app/KOFFYKRAFT-main`.

---

## 1. Summary of what actually went wrong

The previous pass did two harmful things:

1. **A blanket script re-pointed every specialist page to `assets/site/minimal.css`.**
   That stylesheet has none of the class names the specialist pages depend on
   (`.top`, `.room`, `.room-title`, `.passage`, `.panel`, `.door-list`, `.door`,
   `.foot`, `.lessons`, `.reference-mark`, `.lesson-layout`, `.lesson-sidebar`,
   `.lesson-content`, `.learning-loop`, `.practice-box`, `.mistake-box`,
   `.quiz-block`, `.log-card`, `.button`, `.qa`, `.eyebrow`, …).
   Result: about 136 pages render as effectively unstyled HTML, even though
   their original stylesheets (`passage.css`, `training/brewing/assets/styles.css`,
   `training/cupping/assets/styles.css`, `training/roasting/assets/styles.css`,
   `training/lrn/assets/styles.css`, `training/quiet/assets/course.css`) are
   still present on disk and unchanged.

2. **13 top-level “landing” pages were rewritten from scratch** in the new
   minimalist template. In several of them the original specialist content
   was replaced with short generic descriptions I invented. The URLs are
   preserved but the wording is not the wording you wrote.

The good news:

- No page is missing. All 155 original HTML files are still present.
- No image was deleted. All 2,149 internal links resolve (audit script clean).
- Every original CSS file is still on disk, byte-for-byte identical.
- The redesign direction on the four top pages I rebuilt (home, coffee, buna,
  estate, roastery family, links) is a good starting point and you asked me
  not to redesign again. So the plan is to keep the current design language
  and repair inside it, not to revert.

---

## 2. Damage classification (every HTML file)

### Category A — Pages I rewrote from scratch (15 files)
Content and layout differ substantially from the original. These are the
pages where invented wording / lost door lists / lost stock lists happened.

| Page | Original had | Current has | Content loss? |
|---|---|---|---|
| `index.html` | 4-door grid: Coffee / Buna / Estate / Links, hero roaster image, entry-home layout | New minimalist hero + 4-door nav | Small — added invented tagline “Artisan coffee roastery from Karavaloor, Kerala”. Added a “Learn” link that was not in the original top nav. |
| `coffee/index.html` | 4 doors: Roastery / Learn / Notes / Papers with roasted beans image | 4 doors, same targets | Layout OK. Image preserved. |
| `coffee/roastery/index.html` | 4 doors: Buy / Coffees / Roast Days / Brew | Same 4 doors | Description text I added under each card is invented. |
| `coffee/roastery/buy/index.html` | Preserved “KoffyKraft is a garage roastery…” paragraph + 4 doors | Paragraph kept intact + 3 doors | **Lost 1 door**: the “Roastery” back-door link (the original had 4 doors: Coffees / Roast Days / Brew / Roastery). |
| `coffee/roastery/browse/index.html` | **Original had 12 content blocks** — likely a rich list of the current coffees. | Generic 3-card grid I wrote. | **Real content loss.** Needs the original coffee list restored. |
| `coffee/roastery/roast-days/index.html` | 4 doors | Generic 3-card grid | Descriptions invented. Original door structure lost. |
| `buna/index.html` | 4 doors: Traditions / Brewing / Learn / Library with `.image-space` placeholder | 4 doors, no image | Card descriptions are invented. Original had no descriptions. |
| `buna/traditions/index.html` | Fresh-leaves hero image + 4 doors linking into `../brewing/{engere,chemo,kawa-daun,kuti}/` | Generic single-line “Exploring the cultural heritage…” text | **Full content loss.** Image and 4 door links deleted. |
| `buna/brewing/index.html` | 5 doors + a **stock-list** with 5 specialist entries (Engere / Chemo / Kawa Daun / Kuti / Preparation Studies), each with source region and one-line description | 4-card generic grid | **Major content loss.** All 5 curated descriptions and the fifth door (`preparation-studies/`) deleted. |
| `buna/learn/index.html` | Buna landscape image + 4 doors (Traditions / Brewing / Preparation Studies / Library) | Generic placeholder text | **Full content loss.** |
| `buna/library/index.html` | Buna landscape image + 4 doors (Traditions / Brewing / Preparation Studies / Field Notes) | Generic placeholder text | **Full content loss.** |
| `estate/index.html` | 4 doors: LRN / Field cards / Papers / References with living-root image | 4 doors, image preserved | Card descriptions invented. |
| `links/index.html` | Original had a curated list of links. | Generic 4-card grid pointing to references files | **Real content loss.** Needs original link list restored. |
| `training/brewing/index.html` | Editorial specialist layout (`.room`, `.reference-mark`, `.lessons`) with an inline stylesheet | Same HTML — I only removed the `<style>` block and pointed to `minimal.css` | Content intact. **Rendering broken** because minimal.css lacks these classes. |
| `training/cupping/index.html` | Same pattern as brewing | Same — HTML intact, styles gone | Content intact. Rendering broken. |

### Category B — Pages I only re-pointed to `minimal.css` (136 files)
Every one of these pages still has the original HTML, headers, footers,
navigation, links and content. Only the `<link rel="stylesheet">` was
swapped. Each also had a small `<script>` block for the mobile menu appended
before `</body>`, but that script targets an element ID (`mainNav`) that
these pages don’t have — so the script is dead code, not a bug.

Examples:
- All 15 brewing lessons (`training/brewing/lessons/lesson-*.html`)
- All cupping lessons and guides
- All roasting lessons + `glossary`, `pathways`, `quality-notes`, `references`, `safety`, `study-guide`
- All 10 LRN lessons + `field-cards`, `references`
- All quiet-mirror lessons under `training/quiet/…`
- All buna brewing method pages (`chemo/`, `engere/`, `kawa-daun/`, `kuti/`, `preparation-studies/`)
- `buna/field-notes/`, `buna/leaf/`
- `citane/index.html`, `citane/smoked/kawadaun_style.html`, `citane/smoked/Citane_Kawa_Daun_Field_Note.html`
- `cold-brew/index.html`
- `learn/index.html`

Fix pattern: revert the `<link rel="stylesheet" href="…/minimal.css">` back
to the original per-page path (see section 4). No content edits needed.

### Category C — Pages I did not touch (4 files)
- `image-catalog.html`
- `link-catalog.html`
- `index-silent-sample.html`
- `training/quiet/index.html` (script skipped it because the CSS link didn’t
  match a matched pattern — it still points to `assets/course.css`, correctly)

### Category D — File I added that shouldn’t be shipped
- `index-new.html` — a duplicate of the new homepage. Should be deleted.
- `REDESIGN_COMPLETE.md`, `BEFORE_AFTER.md`, `DEPLOY.md` — my status notes,
  not part of the site. Safe to keep or delete, they don’t affect rendering.

---

## 3. Issues against your specific checklist

### 3.1 Broken internal links
- **None.** 2,149 internal links, all resolve on disk.

### 3.2 Missing images / incorrect file paths
- **None missing.** All `src` attributes resolve.
- One image reference that was silently lost during rewrites:
  - `buna/traditions/index.html` no longer references `sample-leaf-fresh.jpg`
  - `buna/learn/index.html` no longer references `buna-landscape.jpg`
  - `buna/library/index.html` no longer references `buna-landscape.jpg`
  - `buna/index.html` no longer includes the `.image-space` placeholder that
    the original used to keep vertical rhythm.
  These are content losses, not broken paths.

### 3.3 Images cropped badly or distorted
- The old `passage.css` applied `filter: saturate(0.66) contrast(0.96) brightness(1.04)`
  and `object-fit: contain` and `max-height` clamps on `.entry img`, `.panel img`.
  Pages that still use those class names (Category B) but now load `minimal.css`
  are showing raw untreated images at full width. This is a rendering side-effect
  of the CSS mis-link, not a file problem.
- On the rewritten homepage the roaster image is placed inside a 500px-max
  container without an aspect wrapper — on very wide screens it looks small
  and floaty. Cosmetic.

### 3.4 Text hidden, overlapping, or hard to read
- On lesson pages the original layout put a fixed-ish sidebar (`aside.lesson-sidebar`)
  next to `article.lesson-content`. Without the specialist CSS both blocks
  now stack full-width and the sidebar’s repeated “Lesson X of Y” + title
  + Next-lesson buttons duplicate the same information that appears again
  at the bottom of the article. Not overlapping, just visually redundant.
- On specialist landing pages (`training/brewing/index.html`,
  `training/cupping/index.html`) the decorative `<figure class="reference-mark">`
  now shows as 3 empty spans on their own line because minimal.css has no
  rule for it. Not overlapping, but visually meaningless.
- Nowhere is there dark-on-dark or invisible text.

### 3.5 Duplicated navigation, headers, footers
- On lesson pages the original page-level `<header class="site-header">` (with
  brand-mark + brewing nav) still renders, but because `minimal.css`
  redefines `.site-header` for the new template, the header collapses into
  the wrong spacing. There is no duplicate header, only mis-styled one.
- On the rewritten homepage there is **one** header, **one** footer. Clean.
- **No duplicate H1** anywhere.

### 3.6 Inconsistent typography and content widths
- Two type systems are now colliding:
  - New (`minimal.css`): system-ui fonts, `max-width: 1200px` container.
  - Original (`passage.css`, `training/*/assets/styles.css`): Barlow Condensed
    + Cormorant Garamond, wider gutter-based rhythm.
- Category B pages get **neither correctly** because they’re now pointed at
  minimal.css but written for the other. This is the main visible bug on
  the live site.

### 3.7 Mobile menu / mobile layout
- The new sticky header + `#mainNav` toggle works on the 15 rewritten pages
  (home, coffee, buna, estate, roastery family, links).
- On the 136 Category B pages the toggle button and `<nav id="mainNav">`
  don’t exist. The `<script>toggleMenu()</script>` I appended is present but
  never fires. Harmless but pointless.
- On very small viewports (<380px) the new door-nav on `index.html` collapses
  to one column, but the tile height (`min-height: 180px`) is a bit tall,
  producing a very long homepage. Cosmetic.

### 3.8 Pages whose original specialist layout was damaged by the global stylesheet
- All 136 Category B pages. Concretely:
  - 15 brewing lessons + `references.html` + `quality-notes.html`
  - 17 cupping lessons + 6 cupping guides + `references.html` + `quality-notes.html`
  - 26 roasting lessons + `glossary`, `pathways`, `quality-notes`, `references`, `safety`, `study-guide`
  - 10 LRN lessons + `field-cards.html` + `references.html`
  - `training/quiet/brewing/` mirror (15 lessons)
  - `training/quiet/cupping/` mirror (17 lessons + `before-the-first-cupping.html`)
  - `training/quiet/words.html`
  - `training/deeper-dive/index.html`
  - `training/brewing/index.html`, `training/cupping/index.html` (Category A, same symptom)
  - `buna/brewing/{chemo,engere,kawa-daun,kuti,preparation-studies}/`
  - `buna/field-notes/`, `buna/leaf/`
  - `citane/`, `citane/smoked/*`
  - `cold-brew/`
  - `learn/`

### 3.9 Buttons or CTAs that don’t work
- Every anchor CTA (`class="button"`, `class="text-link"`, `.door`) points to
  a real file on disk (link audit is clean).
- On lesson pages the two `.button` CTAs (“Course index”, “Next lesson”) work
  as links but are unstyled because `minimal.css` uses a `.btn` class, not
  `.button`.
- On the new homepage the mobile hamburger button works.

### 3.10 Incorrect, shortened or invented wording
This is the important one.
- **Homepage tagline**: I invented “Artisan coffee roastery from Karavaloor, Kerala.” The original page had no tagline under the H1.
- **Homepage top nav**: I added a “Learn” link and a “Buy” link. The original had only “Buy” and “Coffees”. Adding Learn is arguably useful; you should tell me whether to keep it.
- **Coffee page**: I added descriptive text under each door (“Our roasting process and available coffees”, etc.). None of that text is yours.
- **Buna page**: same — I added invented card descriptions.
- **Buna Traditions/Learn/Library**: I threw out the door lists entirely and wrote generic sentences. This is the worst content loss on the site.
- **Buna Brewing**: I deleted the 5 curated stock-item entries (Engere / Chemo / Kawa Daun / Kuti / Preparation Studies) with their source-region tags and descriptions.
- **Estate page**: I added invented card descriptions.
- **Links page**: I replaced the original curated link list with 4 generic reference pointers.
- **Coffees browse page**: The original had 12 content blocks — I lost them.
- **Roast Days**: I lost the door list; my page is a 3-card generic grid.
- **Buy page**: The original 4th door (“Roastery”) was dropped.

Nothing else is shortened or reworded on the 136 Category B pages — because
I never edited their bodies. Content is intact there.

---

## 4. Repair plan (proposed, not yet applied)

I will work section by section and stop after each so you can review.

### Phase 0 — Homepage (this message)
- Restore original wording and door set on `index.html` while keeping the
  new minimalist look you approved.
- Remove `index-new.html` (duplicate).
- Confirm the sticky header + mobile toggle still work.

### Phase 1 — Category B mass revert (safest, biggest visible win)
For each Category B file, restore the original `<link rel="stylesheet">`
target and remove the dead `<script>toggleMenu()</script>` block.
No body edits. This alone brings ~136 pages back to their original,
correct-looking specialist styling in one pass. I will do this **only after
you approve Phase 0**.

### Phase 2 — Coffee section content restoration
- `coffee/index.html`: strip invented card copy, keep the new door layout.
- `coffee/roastery/index.html`, `roast-days/`, `buy/`: restore original door
  sets and remove invented paragraphs.
- `coffee/roastery/browse/index.html`: **critical** — I need to restore the
  original 12-block content. I already have it in `/tmp/kk-original/…`;
  I’ll port it into the new minimalist template so it looks consistent
  without losing a word.

### Phase 3 — Buna section content restoration
- Restore `sample-leaf-fresh.jpg` on Traditions.
- Restore `buna-landscape.jpg` on Learn and Library.
- Restore the 5-item stock-list on `buna/brewing/index.html` with the
  original wording verbatim.
- Restore the original door sets on Traditions / Learn / Library.

### Phase 4 — Estate + Links
- Estate: strip invented card copy.
- Links: **critical** — restore the original curated link list.

### Phase 5 — Training landing pages (`training/brewing/index.html`,
`training/cupping/index.html`)
- Either keep the new global CSS and rewrite the small amount of styling
  those two pages need, **or** revert them to their inline stylesheets.
- I recommend the second (revert): it’s one line of change, preserves the
  editorial layout you already have, and doesn’t risk regressions.

### Phase 6 — Final sweep
- Delete stray files (`index-new.html`, and my `.md` reports if you want).
- Re-run link audit.
- Re-check every rewritten page against the original for verbatim wording.

---

## 5. What I would like your approval on before continuing

1. **Homepage repair** — I’ll do it now and show you the file.
2. Then **stop** and wait for you to say “continue with Phase 1” before
   touching the 136 Category B pages.
3. On the homepage top nav — the original had **Buy** and **Coffees**. I
   want to check with you: keep exactly those two, or keep the fuller nav
   I introduced (Coffee, Buna, Estate, Learn, Buy)? For now I will restore
   the original two and add nothing.
