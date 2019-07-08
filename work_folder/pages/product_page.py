from .base_page import BasePage
from .locators import AddBasketLocators


class ProductPage(BasePage):

    def put_product_in_basket(self):
        button = self.browser.find_element(
            *AddBasketLocators.SHOULD_BE_ADD_TO_BASKET_BUTTON)
        button.click()

    def product_in_basket(self):
        assert self.browser.find_element(
            *AddBasketLocators.SHOULD_BE_PRODUCT_NAME).text == self.browser.find_element(
            *AddBasketLocators.SHOULD_BE_PRODUCT_NAME_IN_BASKET).text

    def price_correct_in_basket(self):
        assert self.browser.find_element(
            *AddBasketLocators.SHOULD_BE_PRICE).text == self.browser.find_element(
            *AddBasketLocators.SHOULD_BE_COST_IN_BASKET).text
