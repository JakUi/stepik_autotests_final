from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb"
    page = MainPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                    #открываем страницу
    page.should_be_login_link()    #выполняем метод страницы - переходим на страницу логина
 
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb"
    page = MainPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                    #открываем страницу
    page.go_to_login_page()        #выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page() #Выполняем функцию should_be_login_page в модуле login_page

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb"
    page = MainPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                    #открываем страницу
    open_basket = BasePage(browser, link)
    open_basket.go_to_cart()
    basket = BasketPage(browser, link)
    basket.basket_is_empty() #Проверяем, что корзина пуста
    basket.basket_is_empty_message() #Проверяем, что есть сообщение о том, что корзина пуста

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
    page = MainPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                    #открываем страницу
    open_basket = BasePage(browser, link)
    open_basket.go_to_cart()
    basket = BasketPage(browser, link)
    basket.basket_is_empty() #Проверяем, что корзина пуста
    basket.basket_is_empty_message() #Проверяем, что есть сообщение о том, что корзина пуста