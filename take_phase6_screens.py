#!/usr/bin/env python3
"""Phase 6 before/after screenshots — training/brewing/ and training/cupping/ landings, desktop + mobile."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path("/app/KOFFYKRAFT-main/docs/phase-6-screenshots")
OUT.mkdir(parents=True, exist_ok=True)

PAGES = [
    ("training/brewing/", "brewing_landing"),
    ("training/cupping/", "cupping_landing"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for viewport, tag in [({"width":1280,"height":900},"desktop"),({"width":390,"height":780},"mobile")]:
        ctx = browser.new_context(viewport=viewport, device_scale_factor=1)
        page = ctx.new_page()
        for path, slug in PAGES:
            for stage, port in [("before", 8081), ("after", 8080)]:
                url = f"http://localhost:{port}/{path}"
                out = OUT / f"{slug}_{stage}_{tag}.png"
                page.goto(url, wait_until="domcontentloaded", timeout=8000)
                page.wait_for_timeout(500)
                page.screenshot(path=str(out), full_page=True, type="png")
        ctx.close()
    browser.close()
files = sorted(OUT.iterdir())
print(f"{len(files)} screenshots in {OUT}")
for f in files: print(f"  {f.name} ({f.stat().st_size} bytes)")
