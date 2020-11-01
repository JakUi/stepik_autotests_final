from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):

    def basket_is_empty(self): #Проверяем, что корзина пуста
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), 'Basket is no empty, but should be'

    def basket_is_empty_message(self): #Проверяем, что есть текст о том что корзина пуста
        message = self.browser.find_element(*BasketPageLocators.BASKET_STATUS).text
        assert message.count('empty') != 0
