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
            *AddBasketLocators.SHOULD_BE_PRODUCT_NAME_IN_BASKET).text, "product not in the Basket"

    def price_correct_in_basket(self):
        assert self.browser.find_element(
            *AddBasketLocators.SHOULD_BE_PRICE).text == self.browser.find_element(
            *AddBasketLocators.SHOULD_BE_COST_IN_BASKET).text, "price not correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *AddBasketLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def dissapered_message(self):
        assert self.is_not_element_present(
            *AddBasketLocators.SUCCESS_MESSAGE), \
            "Success message is dissapered"
