from playwright.sync_api import sync_playwright
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'screenshots'
OUT.mkdir(exist_ok=True)

html_path = (ROOT / 'index.html').resolve().as_uri()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 900})

    page.goto(html_path, wait_until='networkidle')
    page.screenshot(path=str(OUT / 'home-page.png'), full_page=True)

    page.locator('#movie-input').fill('inception')
    page.locator('#search-btn').click()
    page.wait_for_timeout(3000)
    page.screenshot(path=str(OUT / 'movie-suggestion-page.png'), full_page=True)

    browser.close()

print('Captured screenshots to', OUT)
