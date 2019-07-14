from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest

from faker import Faker

"""
pytest -v --tb=line --language=en test_main_page.py
pytest -v --tb=line --language=en -m login_guest test_main_page.py
-m login_guest
"""


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    link = "http://selenium1py.pythonanywhere.com/"

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, TestLoginFromMainPage.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, TestLoginFromMainPage.link)
        page.open()
        page.should_be_login_link()


@pytest.mark.login_form
class TestLoginFrom(object):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

    def test_should_be_login_url(browser):
        page = LoginPage(browser, TestLoginFrom.link)
        page.open()
        page.should_be_login_url()

    def test_should_be_login_form(browser):
        page = LoginPage(browser, TestLoginFrom.link)
        page.open()
        page.should_be_login_form()

    def test_should_be_register_form(browser):
        page = LoginPage(browser, TestLoginFrom.link)
        page.open()
        page.should_be_register_form()


@pytest.mark.new_user
def test_new_user(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    user = LoginPage(browser, link)
    user.open()
    user.register_new_user(email=Faker().email(), password="123rrr345")
    user.should_be_authorized_user()


def test_user_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()


def test_user_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    assert page.not_produkt_in_basket() == True


def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    assert page.not_produkt_in_basket() == True
