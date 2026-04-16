import pytest
import random
import allure
# from allure.constants import AttachmentType

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

from pages.folder_product_desk_page import FolderProductDeskPage
from pages.cart_page import CartPage
from pages.cart_modal_window import CartModalWindow
from pages.product_page import ProductPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('window-size=1920,1080')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')  
    options.add_argument('--disable-dev-shm-usage')  
    options.add_argument('--disable-gpu')
    driver: WebDriver = webdriver.Chrome(options=options)
    yield driver
    driver.save_screenshot(f'{random.randint(100, 100000)}.png')
    # allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@pytest.fixture()
def folder_product_desk_page(driver):
    return FolderProductDeskPage(driver)


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture()
def cart_modal_window(driver):
    return CartModalWindow(driver)


@pytest.fixture()
def product_page(driver):
    return ProductPage(driver)


@pytest.fixture()
def cart_with_product(driver, folder_product_desk_page, cart_modal_window, cart_page):
    folder_product_desk_page.open_page()
    folder_product_desk_page.add_to_cart_hover()
    cart_modal_window.go_to_cart()
    return cart_page
