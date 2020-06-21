from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.locators import ProductPageLocators
import time



def test_guest_can_add_product_to_cart(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                    #открываем страницу
    page.add_to_cart()             #выполняем метод страницы - переходим на страницу логина
    page.solve_quiz_and_get_code() #Решаем задачу в alert-окне и вводим код
    #получаем название товара добавленного в корзину
    name = browser.find_elements(*ProductPageLocators.PRODUCT_ADDED_IN_CART)
    name = name[0].text
    #получаем стоиомсть товара добавленного в корзину
    price = browser.find_element(*ProductPageLocators.PRICE_PRODUCT_ADDED_IN_CART).text
    #проверяем, что название и стоимость товара добавляемого в корзину равны названию и стоимости товаров в корзине
    assert name == page.get_name(), 'Название товара добавленного в корзину не соответствует названию товара добавляемого в корзину'
    assert price  == page.get_price(), 'Цена товара добавленного в корзину не соответствует цене товара добавляемого в корзину'
    
