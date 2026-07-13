#!/usr/bin/env python3
"""Take representative before/after screenshots using Playwright."""
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path("/app/_screens")
OUT.mkdir(exist_ok=True)

PAGES = [
    ("training/brewing/index.html",                                           "brewing_landing"),
    ("training/brewing/lessons/lesson-1-introduction-to-coffee-and-brewing-basics.html", "brewing_lesson"),
    ("training/cupping/lessons/lesson-1-1-aroma-mastery.html",                "cupping_lesson"),
    ("training/roasting/lessons/lesson-1-1-what-changes-during-coffee-roasting.html", "roasting_lesson"),
    ("training/lrn/lessons/lesson-1-what-is-living-root-network.html",        "lrn_lesson"),
    ("training/quiet/brewing/lessons/lesson-1-introduction-to-coffee-and-brewing-basics.html", "quiet_lesson"),
    ("buna/brewing/kawa-daun/index.html",                                     "buna_method"),
    ("buna/field-notes/index.html",                                           "buna_field_notes"),
    ("citane/index.html",                                                     "citane_landing"),
    ("cold-brew/index.html",                                                  "cold_brew"),
    ("learn/index.html",                                                      "learn_landing"),
]

DESKTOP = {"width": 1280, "height": 900}
MOBILE  = {"width":  390, "height": 780}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for viewport, tag in [(DESKTOP, "desktop"), (MOBILE, "mobile")]:
        ctx = browser.new_context(viewport=viewport, device_scale_factor=1)
        page = ctx.new_page()
        for path, slug in PAGES + [("", "home")]:
            for stage, port in [("before", 8081), ("after", 8080)]:
                url = f"http://localhost:{port}/{path}"
                out = OUT / f"{slug}_{stage}_{tag}.png"
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=8000)
                    page.wait_for_timeout(400)
                    page.screenshot(path=str(out), full_page=False, type="png")
                except Exception as e:
                    print(f"  FAIL {out.name}: {e}")
        ctx.close()
    browser.close()

files = sorted(OUT.iterdir())
print(f"\n{len(files)} screenshots produced in {OUT}")
