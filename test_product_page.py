from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.product_page import ProductPageLocators
from pages.base_page import BasePage
from pages.basket_page import BasketPage
import pytest


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        mainpage = MainPage(browser, link)
        page = BasePage(browser, link)
        loginpage = LoginPage(browser, link)
        basepage = BasePage(browser, link)
        page.open()
        mainpage.go_to_login_page()
        loginpage.register_new_user()
        basepage.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
        page = ProductPage(browser, link) # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # Открываем страницу
        page.should_not_be_success_message_is_not_element_present() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart() # Добавляем товар в корзину

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page() # Выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page() # Выполняем функцию should_be_login_page в модуле login_page

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
    page = BasePage(browser, link) # Инициализируем класс BasePage чтобы использовать его методы
    page.open() # Открываем страницу (link передаём, поэтому откроется та страница, ссылку на которую мы передали)
    page.go_to_cart() # Используем метод (выполняем функцию) go_to_cart (переход в корзину) класса BasePage
    basket = BasketPage(browser, link) # Инициализируем класс BasketPage чтобы использовать его методы
    basket.basket_is_empty() # Проверяем, что корзина пуста, используя метод basket_is_empty класса BasketPage
    basket.basket_is_empty_message() # Проверяем, что есть сообщение о том, что корзина пуста, используя метод basket_is_empty класса BasketPage

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_promo_to_cart(browser, link)

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
