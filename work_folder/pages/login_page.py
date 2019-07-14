from .base_page import BasePage
from .locators import LoginPageLocators

import pytest
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert '/accounts/login/' in self.browser.current_url, "not correct url"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.SHOULD_BE_LOGIN_FORM), "Login form not in this page"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.SHOULD_BE_REGISTER_FORM), "Register form not in this page"

    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_MAIL).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_PASS).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_PASS_CONFIRM).send_keys(password)
        button = self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_BUTTON)
        button.click()
