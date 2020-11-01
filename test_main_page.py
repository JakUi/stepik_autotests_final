from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb"
        page = MainPage(browser, link) #инициализируем класс MainPage, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                    #открываем страницу методом (функцией) open из класса MainPage
        page.go_to_login_page()        #выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page() #выполняем проверку should_be_login_page из класса BasePage (MainPage наследник его и наследует все его методы)


    def test_guest_should_see_login_link(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb"
        page = MainPage(browser, link) #инициализируем класс MainPage, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                    #открываем страницу методом (функцией) open из класса MainPage
        page.should_be_login_link()    #выполняем проверку should_be_login_link из класса BasePage (MainPage наследник его и наследует все его методы)
    


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb"
    page = BasePage(browser, link) #инициализируем класс BasePage чтобы использовать его методы
    page.open() #Открываем страницу (link передаём, поэтому откроется та страница, ссылку на которую мы передали)             
    page.go_to_cart() #используем метод (выполняем функцию) go_to_cart (переход в корзину) класса BasePage
    basket = BasketPage(browser, link) #инициализируем класс BasketPage чтобы использовать его методы
    basket.basket_is_empty() #Проверяем, что корзина пуста
    basket.basket_is_empty_message() #Проверяем, что есть сообщение о том, что корзина пуста
