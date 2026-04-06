import logging
import allure

from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import product_page_locators as loc


class ProductPage(BasePage):
    PAGE_URL = '/furn-9999-office-design-software-7?category=9'

    def check_name(self, expected_name):
        logging.info('Проверка имени')
        with allure.step('АААА'):
            actual_name = self.find(loc.name_product_loc)
            assert actual_name.text == expected_name, f'Неверное имя товара. ' \
                                             f'Ожидаемое имя: {expected_name}, текущее имя: {actual_name}'

    def check_price(self, expected_price):
        logging.info('Проверка цены')
        with allure.step('АААА'):
            actual__price = self.find(loc.price_product_loc)
            assert actual__price.text == expected_price, \
                f'Неверная цена товара. Ожидаемая цена: {expected_price}, текущая цена: {actual__price}'

    def check_image(self):
        logging.info('Проверка наличия изображения')
        with allure.step('АААА'):
            image_product = self.wait.until(EC.visibility_of_element_located(loc.image_product_loc))
            src = image_product.get_attribute("src")
            assert src, "Атрибут src отсутствует или пуст"

    def add_plus_one(self):
        self.find(loc.add_one).click()

    def add_to_cart(self):
        self.find(loc.add_to_cart).click()

    def verify_added_to_cart_notification(self, expected_text):
        product_in_cart_notification = self.wait.until(EC.visibility_of_element_located(loc.product_name_in_cart_loc))
        assert product_in_cart_notification.text == expected_text, f'Ожидалось: {expected_text}. \n' \
                                                                   f'Текущее: {product_in_cart_notification.text}'

    def change_currency_to_euro(self):
        currency = self.find(loc.currency_loc)
        currency.click()
        eur = self.wait.until(EC.element_to_be_clickable(loc.eur_loc))
        eur.click()

    def check_price_eur(self, expected_price):
        price_eur = self.find(loc.price_product_loc)
        assert price_eur == expected_price, f'Ожидаласб цена: {expected_price}. \n' \
                                            f'Текущая цена: {price_eur}'








