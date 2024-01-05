import time

from playwright.sync_api import Page
from common.locators import *


class SearchPage:
    def __init__(self, page: Page):
        self.page = page

    def search_item(self, value):
        self.page.locator(HOME_SEARCH_FIELD).fill(value)
        self.page.locator(HOME_SEARCH_BTN).click()
        self.page.wait_for_selector(SEARCH_PAGE_RESULT_ROWS)

    def go_to_item_page(self, value):
        locator = SEARCH_PAGE_RESULT_ROW_VALUE.replace('VALUE', value)
        self.page.wait_for_selector(locator)
        self.page.locator(locator).click()

