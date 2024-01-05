from playwright.sync_api import Page, expect
import pytest
from playwright.sync_api import sync_playwright
import os


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    page.set_default_timeout(60000)
    yield page
    page.close()
