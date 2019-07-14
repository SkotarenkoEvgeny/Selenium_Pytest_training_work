from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest
from faker import Faker
import time

"""
pytest -v -s --tb=line --language=en test_product_page.py
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019
http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear
"""

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


@pytest.mark.login
class TestUserAddToCartFromProductPage(object):
    """
    create user and add product
    """

    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        user = LoginPage(browser,
                         "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        user.open()
        user.register_new_user(email=Faker().email(), password="123rrr345")
        time.sleep(2)
        user.should_be_authorized_user()

    def test_user_cant_see_success_message_after_adding_product_to_cart(self,
                                                                        browser):
        page = ProductPage(browser, TestUserAddToCartFromProductPage.link)
        page.open()
        page.put_product_in_basket()
        page.should_not_be_success_message()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, TestUserAddToCartFromProductPage.link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_go_to_login_page(browser, link):
    """
    guest cann put poroduct to basket
    """
    page = ProductPage(browser, link)
    page.open()
    page.put_product_in_basket()
    page.solve_quiz_and_get_code()
    page.product_in_basket()
    page.price_correct_in_basket()


def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    """
    guest cann see sucess message after adding product
    """
    page = ProductPage(browser, link)
    page.open()
    page.put_product_in_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """
    find sucess message on page
    """
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.put_product_in_basket()
    page.dissapered_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_from_produkt_page()
