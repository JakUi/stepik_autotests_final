from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    
    def register_new_user(self)
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        self.email_input = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email = str(time.time()) + "@jakui.org"
        self.email_input.send_keys(email)
        self.password1 = self.browser.find_element(*LoginPageLocators.REG_PASS1)
        password = "jakui_121212"
        self.password1.send_keys(password)
        self.password2 = self.browser.find_element(*LoginPageLocators.REG_PASS2)
        self.password2.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_ENTER)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.MainPageLocators.LOGIN_LINK.click()
        assert self.browser.current_url.count('login') != 0, 'Подстроки login нет в текущем url браузера'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма регистрации не найдена"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Форма регистрации найдена"