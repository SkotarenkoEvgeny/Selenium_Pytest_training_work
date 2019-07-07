from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    SHOULD_BE_LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    SHOULD_BE_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
