import pytest

from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.checkout_page import CheckoutPage
from common.locators import *
from common.data_file import load_json


@pytest.mark.checkout
@pytest.mark.all
def test_checkout_page(page):
    data = load_json()

    # login to application
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()
    login_page.login_to_set_app()

    # search for an item and verify there's a result returned
    search_page = SearchPage(page)
    search_page.search_item(data['checkout_search_item'])
    assert page.locator(SEARCH_PAGE_RESULT_ROWS).count() > 0

    # add item to cart and check out
    search_page.go_to_item_page(data['checkout_item'])
    checkout_page = CheckoutPage(page)
    checkout_page.add_to_cart()
    checkout_page.proceed_to_checkout()

    # TODO - Need additional steps to proceed to checkout since it needs payment methods
