from selenium.webdriver import Remote as RemoteWebDriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators
import time, math
from selenium.common.exceptions import NoAlertPresentException # в начале файла

class ProductPage(BasePage):
    def product_add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def price_basket_equal_price_product(self):
        basket_price_link = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        product_price_link = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        assert basket_price_link == product_price_link, "Price don't aqual"
