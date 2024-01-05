# Filename: common_playwright.py
from playwright.sync_api import sync_playwright


def setup_browser():
    browser_name = 'chrome'
    with sync_playwright() as playwright:
        match browser_name:
            case 'chrome':
                browser = playwright.chromium.launch(headless=False)
                browser = browser.new_context(viewport_size={'width': 1920, 'height': 1080})  # Set an initial size
            case 'firefox':
                browser = playwright.firefox.launch(headless=False)
            case 'webkit':
                browser = playwright.webkit.launch(headless=False)
        page = browser.new_page()
        return browser, page


def teardown_browser(browser):
    browser.close()
