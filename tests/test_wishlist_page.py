import time

import pytest

from pages.login_page import LoginPage
from pages.search_page import SearchPage
from common.locators import *
from common.data_file import load_json


@pytest.mark.wishlist
@pytest.mark.all
def test_wishlist_page(page):
    data = load_json()

    # login to application
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()
    login_page.login_to_set_app()

    # search for an item and verify there's a result returned
    search_page = SearchPage(page)
    search_page.search_item(data['wishlist_search_item'])
    assert page.locator(SEARCH_PAGE_RESULT_ROWS).count() > 0

    # add item to cart and check out
    search_page.go_to_item_page(data['wishlist_item'])
    time.sleep(2)
    page.locator(CHECKOUT_ADD_TO_WISHLIST).click()
    page.wait_for_selector(CHECKOUT_ADD_TO_WISHLIST_MODAL)
    assert page.locator(CHECKOUT_ADD_TO_WISHLIST_MODAL).is_visible()
