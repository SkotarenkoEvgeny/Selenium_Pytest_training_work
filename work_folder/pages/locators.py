from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_PAGE = (By.XPATH, "//li[@class='active']")
    BASKET_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")
    BASKET_TABLE = (By.XPATH, "//div[@id='basket_totals']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators(object):
    SHOULD_BE_LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    SHOULD_BE_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_MAIL = (By.XPATH, '//input[@id="id_registration-email"]')
    REGISTER_FORM_PASS = (By.XPATH, '//input[@id="id_registration-password1"]')
    REGISTER_FORM_PASS_CONFIRM = (By.XPATH, '//input[@id="id_registration-password2"]')
    REGISTER_FORM_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')


class AddBasketLocators(object):
    SHOULD_BE_ADD_TO_BASKET_BUTTON = (
        By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    SHOULD_BE_PRICE = (By.XPATH, "//p[@class='price_color']")
    SHOULD_BE_COST_IN_BASKET = (
        By.XPATH, "//div[@class='alertinner ']/p/strong")
    SHOULD_BE_PRODUCT_NAME = (
        By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    SHOULD_BE_PRODUCT_NAME_IN_BASKET = (
        By.XPATH, "//div[@class='alertinner ']/strong")
    SUCCESS_MESSAGE = (
        By.XPATH, "//div[@class='alertinner']")
