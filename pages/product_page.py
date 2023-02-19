import time

from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_but_add_to_basket()
        self.should_be_product_add_to_basket()


    def should_be_product_add_to_basket(self):
        global product_name
        global product_price
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        add_button = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_BUT)
        add_button.click()


    def should_be_product_but_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_BUT), "add_to_basket but is not presented"

    def should_match_product_name(self):
        print("\nchecking product name...", end='\t')
        product_name_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text
        assert product_name == product_name_in_alert, "Product name not match"
        print("Sucsess")
        # print(product_name_check, product_name)

    def should_match_product_price(self):
        print("\nchecking product price...", end='\t')
        cart_price_in_alert = self.browser.find_element(*ProductPageLocators.CART_PRICE_IN_ALERT).text
        assert product_price == cart_price_in_alert, "Product price not match"
        print("Sucsess")
        # print(product_price_check, product_price)