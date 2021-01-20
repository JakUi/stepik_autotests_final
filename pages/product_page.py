from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage): # класс ProductPage наследует класс BasePage, соответственно может использовать все методы класса BasePage

    def get_added_product_name(self): # Функция будет получать название добавляемого в корзину товара
        product_added_in_cart_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_added_in_cart_name

    def get_added_product_price(self): # Функция будет получать цену добавляемого в корзину товара
        product_added_in_cart_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_added_in_cart_price

    def add_to_cart(self): # Функция добавляет товар в корзину
        product_added_in_cart_name = self.get_added_product_name()
        product_added_in_cart_price = self.get_added_product_price()
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()
        # Получаем название товара добавленного в корзину
        products_in_cart_name = self.browser.find_elements(*ProductPageLocators.PRODUCT_ADDED_IN_CART)
        product_in_cart_name = products_in_cart_name[0].text
        # Получаем стоиомсть товара добавленного в корзину
        pricings_products_in_cart = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_ADDED_IN_CART).text
        # Проверяем, что название и стоимость товара добавляемого в корзину равны названию и стоимости товаров в корзине
        assert product_in_cart_name == product_added_in_cart_name, 'Название товара добавленного в корзину не соответствует названию товара добавляемого в корзину'
        assert pricings_products_in_cart  == product_added_in_cart_price, 'Цена товара добавленного в корзину не соответствует цене товара добавляемого в корзину'

    def add_promo_to_cart(self, browser, link): # Функция добавляет промо товар в корзину
        product_added_in_cart_name = self.get_added_product_name()
        product_added_in_cart_price = self.get_added_product_price()
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()
        bp = BasePage(browser, link)
        bp.solve_quiz_and_get_code()
        products_in_cart_name = self.browser.find_elements(*ProductPageLocators.PRODUCT_ADDED_IN_CART)
        product_in_cart_name = products_in_cart_name[0].text
        pricings_products_in_cart = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_ADDED_IN_CART).text
        assert product_in_cart_name == product_added_in_cart_name, 'Название товара добавленного в корзину не соответствует названию товара добавляемого в корзину'
        assert pricings_products_in_cart  == product_added_in_cart_price, 'Цена товара добавленного в корзину не соответствует цене товара добавляемого в корзину'

    def should_not_be_success_message_is_not_element_present(self): # Проверяет, что элемент не отображается и появился
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should not be'

    def should_not_be_success_message_element_is_disappeared(self): # Проверяет, что элемент исчезает
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should not be'
