#!/usr/bin/env python3
"""Phase 2 before/after screenshots of all 5 coffee pages, desktop + mobile."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path("/app/KOFFYKRAFT-main/docs/phase-2-screenshots")
OUT.mkdir(parents=True, exist_ok=True)

PAGES = [
    ("coffee/",                       "coffee_landing"),
    ("coffee/roastery/",              "roastery_landing"),
    ("coffee/roastery/buy/",          "buy"),
    ("coffee/roastery/browse/",       "browse"),
    ("coffee/roastery/roast-days/",   "roast_days"),
]

DESKTOP = {"width": 1280, "height": 900}
MOBILE  = {"width":  390, "height": 780}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for viewport, tag in [(DESKTOP, "desktop"), (MOBILE, "mobile")]:
        ctx = browser.new_context(viewport=viewport, device_scale_factor=1)
        page = ctx.new_page()
        for path, slug in PAGES:
            for stage, port in [("before", 8081), ("after", 8080)]:
                url = f"http://localhost:{port}/{path}"
                out = OUT / f"{slug}_{stage}_{tag}.png"
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=8000)
                    page.wait_for_timeout(400)
                    page.screenshot(path=str(out), full_page=True, type="png")
                except Exception as e:
                    print(f"  FAIL {out.name}: {e}")
        ctx.close()
    browser.close()

files = sorted(OUT.iterdir())
print(f"{len(files)} screenshots produced in {OUT}")
