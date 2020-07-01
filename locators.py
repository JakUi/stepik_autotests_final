from selenium.webdriver.common.by import By


class MainPageLocators(): #каждый селектор — это пара: как искать и что искать!

    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link') #селектор на переход на страницу логина

class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form') #Селектор на форму логина
    REG_FORM = (By.CSS_SELECTOR, '#register_form') #Селектор на форму регистрации
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username') #Селектор на ввод почты в поле входа
    LOGIN_PASS = (By.CSS_SELECTOR, '#id_login-password') #Селектор на ввод пароля в поле входа
    LOGIN_ENTER = (By.CSS_SELECTOR, 'name="login_submit"') #Селектор на кнопку "Войти" в поле входа
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASS1 = (By.CSS_SELECTOR, '#id_registration-password1') #Селектор на ввод пароля в поле регистрации
    REG_PASS2 = (By.CSS_SELECTOR, '#id_registration-password2') #Селектор на ввод пароля в поле регистрации
    REG_ENTER = (By.CSS_SELECTOR, 'name="registration_submit"') #Селектор на кнопку "Зарегестироваться" в поле регистрации

class ProductPageLocators():

    PRODUCT_NAME = (By.CSS_SELECTOR, '[class="col-sm-6 product_main"] h1') #селектор на название товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class="price_color"]') #селектор на стоимость товара 
    ADD_TO_CART = (By.CSS_SELECTOR, '#add_to_basket_form') #селектор на кнопку "Добавить в корзину"
    PRODUCT_ADDED_IN_CART = (By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-success  fade in"] strong') #селектор на название товара
    #добавленного в корзину
    PRICE_PRODUCT_ADDED_IN_CART = (By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-info  fade in"] strong') #селектор на стоимость 
    #товара добавленного в корзину
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-success  fade in"]') #сеоектор на сообщение, что товар добавлен в корзину