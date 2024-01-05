import pytest

from pages.login_page import LoginPage


@pytest.mark.login
@pytest.mark.all
def test_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()
    login_page.login_to_app("robertdeocampojr@gmail.com", "7KbX&oQKraF!jPnr")
