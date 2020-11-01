from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.locators import ProductPageLocators

import time
import pytest
@pytest.mark.skip
@pytest.mark.parametrize('links', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, links):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = f'{links}'
    page = ProductPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                    #Открываем страницу
    page.add_to_cart()             #Добавляем товар в корзину 
    page.solve_quiz_and_get_code() #Решаем задачу в alert-окне и вводим код
    #получаем название товара добавленного в корзину
    name = browser.find_elements(*ProductPageLocators.PRODUCT_ADDED_IN_CART)
    name = name[0].text
    #получаем стоиомсть товара добавленного в корзину
    price = browser.find_element(*ProductPageLocators.PRICE_PRODUCT_ADDED_IN_CART).text
    #проверяем, что название и стоимость товара добавляемого в корзину равны названию и стоимости товаров в корзине
    assert name == page.get_name(), 'Название товара добавленного в корзину не соответствует названию товара добавляемого в корзину'
    assert price  == page.get_price(), 'Цена товара добавленного в корзину не соответствует цене товара добавляемого в корзину'

@pytest.mark.xfail   
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)    #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                          #открываем страницу
    page.add_to_cart()                   #Добавляем товар в корзину 
    page.should_not_be_success_message_is_not_element_present() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                    #открываем страницу
    page.should_not_be_success_message_is_not_element_present() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    
@pytest.mark.xfail   
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                    #открываем страницу
    page.add_to_cart()                   #Добавляем товар в корзину 
    page.should_not_be_success_message_element_is_disappeared() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present