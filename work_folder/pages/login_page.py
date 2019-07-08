from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert  '/accounts/login/' in self.browser.current_url, "not correct url"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.SHOULD_BE_LOGIN_FORM), "Login form not in this page"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.SHOULD_BE_REGISTER_FORM), "Register form not in this page"
