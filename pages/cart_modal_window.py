import logging
import allure

from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import cart_modal_window_locators as loc


class CartModalWindow(BasePage):

    def go_to_cart(self):
        logging.info('АААА')
        with allure.step(''):
            self.wait.until(EC.visibility_of_element_located(loc.btn_proceed_to_checkout)).click()


