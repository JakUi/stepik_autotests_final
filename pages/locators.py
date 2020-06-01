from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #селектор на переход на страницу логина

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