from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def get_name(self): #Функция будет получать название добавляемого в корзину товара
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return name

    def get_price(self): #Функция будет получать цену добавляемого в корзину товара
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return price

    def add_to_cart(self): #Функция добавляет товар в корзину
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()
