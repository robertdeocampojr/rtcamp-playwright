# Filename: login_page.py
import configparser
import os.path
import time
from os import path
from playwright.sync_api import Page
from common.locators import *


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.config = configparser.ConfigParser()
        self.config.read(path.join(os.getcwd(), 'config/config.ini'))

        self.base_url = self.config.get('URL', 'base_url')
        self.username = self.config.get('Credentials', 'username')
        self.password = self.config.get('Credentials', 'password')

    def navigate_to_login_page(self):
        self.page.goto(self.base_url)
        time.sleep(10)

    def login_to_app(self, email, password):
        self.page.locator(LOGIN_SIGN_IN_LINK).click()
        self.page.locator(LOGIN_SIGN_EMAIL_FIELD).fill(email)
        self.page.locator(LOGIN_SIGN_CONTINUE_BTN).click()
        self.page.locator(LOGIN_SIGN_PASSWORD_FIELD).fill(password)
        self.page.locator(LOGIN_SIGN_SUBMIT_BTN).click()
        self.page.wait_for_selector(HOME_SEARCH_FIELD)
        assert self.page.locator(HOME_SEARCH_FIELD).is_visible()

    def login_to_set_app(self):
        self.page.locator(LOGIN_SIGN_IN_LINK).click()
        self.page.locator(LOGIN_SIGN_EMAIL_FIELD).fill(self.username)
        self.page.locator(LOGIN_SIGN_CONTINUE_BTN).click()
        self.page.locator(LOGIN_SIGN_PASSWORD_FIELD).fill(self.password)
        self.page.locator(LOGIN_SIGN_SUBMIT_BTN).click()
        self.page.wait_for_selector(HOME_SEARCH_FIELD)
        assert self.page.locator(HOME_SEARCH_FIELD).is_visible()
