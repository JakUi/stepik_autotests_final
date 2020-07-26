from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                    #открываем страницу
    page.should_be_login_link()    #выполняем метод страницы - переходим на страницу логина
 
def go_to_login_page(self):
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) #В методе, который осуществляет переход к странице логина, инициализируем новый объект Page и возвращаем его
    link.click()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                    #открываем страницу
    page.go_to_login_page()        #выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page() #Выполняем функцию should_be_login_page в модуле login_page

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()        #выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page() #Выполняем функцию should_be_login_page в модуле login_page