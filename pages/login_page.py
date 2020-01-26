from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        temp = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        temp.click()

        print(self.browser.current_url)
        print("login url: ", "login" in self.browser.current_url)
        assert "login" in self.browser.current_url, "!!!'login' don't in url!!!"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        print("login form: ", self.is_element_present(*LoginPageLocators.LOGIN_FORM))
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)



    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        print("registration form: ", self.is_element_present(*LoginPageLocators.REGISTRATION_FORM))
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM)
