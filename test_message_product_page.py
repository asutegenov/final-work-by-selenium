from selenium.webdriver import Remote as RemoteWebDriver
from pages.product_page import ProductPage
import time, pytest


@pytest.mark.parametrize("link" ,[pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/", marks=pytest.mark.xfail)])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.product_add_to_basket()
    product_page.should_not_be_success_message()

@pytest.mark.parametrize("link" ,[pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/", marks=pytest.mark.xfail)])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.product_add_to_basket()
    product_page.should_is_disappeared()