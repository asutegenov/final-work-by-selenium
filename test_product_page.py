from selenium.webdriver import Remote as RemoteWebDriver
from pages.product_page import ProductPage

def test_product_page_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser,link)
    product_page.open()
    product_page.product_add_to_basket()
    product_page.solve_quiz_and_get_code()