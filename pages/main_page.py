from selenium.webdriver import Remote as RemoteWebDriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        link.click()

    def should_by_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR,"#login_link"), "Login link is not presented"

