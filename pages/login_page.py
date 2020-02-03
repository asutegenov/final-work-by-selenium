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
        assert "login" in self.browser.current_url, "!!!'login' don't in url!!!"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM)

    def register_new_user(self, email, password):
        email_reg_input = self.browser.find_element(By.NAME, "registration-email")
        email_reg_input.send_keys(email)
        
        psw_reg_input = self.browser.find_element(By.NAME, "registration-password1")
        psw_reg_input.send_keys(password)
        
        conf_psw_reg_input = self.browser.find_element(By.NAME, "registration-password2")
        conf_psw_reg_input.send_keys(password)
        
        submit_input = self.browser.find_element(By.NAME, "registration_submit")
        submit_input.click()
