import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="select language for browser")


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    print("\nstart browser for test..")
    options.add_experimental_option('prefs',
                                    {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(
        executable_path='C:\chromedriver\chromedriver.exe', options=options)
    yield browser
    print("\nquit browser")
    browser.quit()
