from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_not_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_HAVE_ITEMS), "Item's have in basket"
    
    def basket_have_a_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_HAVE_A_TEXT), "Basket not have a text"

