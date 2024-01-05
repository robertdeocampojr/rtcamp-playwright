import time

from playwright.sync_api import Page
from common.locators import *


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def add_to_cart(self):
        self.page.locator(CHECKOUT_ADD_TO_CART).click()
        self.page.wait_for_selector(CHECKOUT_PROCEED_TO_RETAIL)

    def proceed_to_checkout(self):
        self.page.locator(CHECKOUT_PROCEED_TO_RETAIL).click()
        self.page.wait_for_selector(CHECKOUT_PLACE_ORDER)
        self.page.locator(CHECKOUT_PLACE_ORDER).count() > 0

    def add_to_wishlist(self):
        self.page.locator('//span[@id="wishListMainButton"]').click()
        self.page.wait_for_selector('//h4[@id="a-popover-header-2" and text()="Add to List"]')
        assert self.page.locator('//h4[@id="a-popover-header-2" and text()="Add to List"]').is_visible()