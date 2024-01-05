import pytest

from pages.login_page import LoginPage
from pages.search_page import SearchPage
from common.locators import *
from common.data_file import load_json


@pytest.mark.search
@pytest.mark.all
def test_search_page(page):
    data = load_json()

    # login to application
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()
    login_page.login_to_set_app()

    # search for an item and verify there's a result returned
    search_page = SearchPage(page)
    search_page.search_item(data['search_item'])
    assert page.locator(SEARCH_PAGE_RESULT_ROWS).count() > 0
