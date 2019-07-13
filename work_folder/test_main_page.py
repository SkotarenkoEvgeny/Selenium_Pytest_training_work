from .pages.main_page import MainPage
from .pages.login_page import LoginPage

"""
pytest -v --tb=line --language=en test_main_page.py
"""


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#
#
# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# def test_should_be_login_url(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_url()
#
#
# def test_should_be_login_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_form()
#
#
# def test_should_be_register_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_register_form()
#
# def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()

def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
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



