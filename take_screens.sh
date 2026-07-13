#!/usr/bin/env bash
# Take before/after screenshots at desktop + mobile widths for representative pages.
set -e
OUT=/app/_screens
mkdir -p "$OUT"

# Representative pages, one from each affected section
PAGES=(
  "training/brewing/index.html:brewing_landing"
  "training/brewing/lessons/lesson-1-introduction-to-coffee-and-brewing-basics.html:brewing_lesson"
  "training/cupping/lessons/lesson-1-1-aroma-mastery.html:cupping_lesson"
  "training/roasting/lessons/lesson-1-1-what-changes-during-coffee-roasting.html:roasting_lesson"
  "training/lrn/lessons/lesson-1-what-is-living-root-network.html:lrn_lesson"
  "training/quiet/brewing/lessons/lesson-1-introduction-to-coffee-and-brewing-basics.html:quiet_lesson"
  "buna/brewing/kawa-daun/index.html:buna_method"
  "buna/field-notes/index.html:buna_field_notes"
  "citane/index.html:citane_landing"
  "cold-brew/index.html:cold_brew"
  "learn/index.html:learn_landing"
)

shot() {
  local url="$1"; local w="$2"; local h="$3"; local out="$4"
  google-chrome --headless=new --disable-gpu --hide-scrollbars --no-sandbox \
    --window-size="${w},${h}" --screenshot="$out" "$url" >/dev/null 2>&1
}

for entry in "${PAGES[@]}"; do
  path="${entry%%:*}"; slug="${entry##*:}"
  echo "-> $slug ($path)"
  shot "http://localhost:8081/$path" 1280 900 "$OUT/${slug}_before_desktop.png"
  shot "http://localhost:8080/$path" 1280 900 "$OUT/${slug}_after_desktop.png"
  shot "http://localhost:8081/$path"  390 780 "$OUT/${slug}_before_mobile.png"
  shot "http://localhost:8080/$path"  390 780 "$OUT/${slug}_after_mobile.png"
done

# Also the homepage as a sanity check (Phase-0 vs Phase-1 should be identical there)
shot "http://localhost:8081/" 1280 900 "$OUT/home_before_desktop.png"
shot "http://localhost:8080/" 1280 900 "$OUT/home_after_desktop.png"

ls -1 "$OUT" | wc -l
echo "Screenshots in $OUT"
