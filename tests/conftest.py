import pytest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

from pages.product_desk_page import ProductDeskPage
from pages.cart_page import CartPage
from pages.cart_modal_window import CartModalWindow


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver: WebDriver = webdriver.Chrome(options=options)
    yield driver


@pytest.fixture()
def product_desk_page(driver):
    return ProductDeskPage(driver)


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture()
def cart_modal_window(driver):
    return CartModalWindow(driver)

