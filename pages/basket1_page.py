from .base_page import BasePage
from .locators import BaskettPageLocators
import time


class BaskettPage(BasePage, BaskettPageLocators):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def click_button_add_to_basket(self):
        button = self.browser.find_element(*BaskettPageLocators.ORIGIN_BUY_BUTTON)
        button.click()

    def display_price(self):
        assert self.is_element_present(*BaskettPageLocators.TOTAL_PRICE), \
            "Basket is empty"

    def guest_can_add_promo_code(self, promocode):
        current_price_txt = self.browser.find_element(*BaskettPageLocators.TOTAL_PRICE).text
        current_price = float(current_price_txt.replace('₽', '').replace(' ', ''))
        self.browser.find_element(*BaskettPageLocators.PROMOCODE_LINK).click()
        input_field = self.browser.find_element(*BaskettPageLocators.PROMOCODE_FIELD)
        time.sleep(4)
        input_field.send_keys(promocode)
        time.sleep(3)
        self.browser.find_element(*BaskettPageLocators.PROMOCODE_ADD_BUTTON).click()
        time.sleep(3)
        new_price_txt = self.browser.find_element(*BaskettPageLocators.TOTAL_PRICE).text
        new_price = float(new_price_txt.replace('₽', '').replace(' ', ''))
        time.sleep(3)
        assert new_price < current_price, f"Новая цена ({new_price}) не меньше начальной цены ({current_price})"
        time.sleep(5)
