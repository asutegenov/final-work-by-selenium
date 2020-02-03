from selenium.webdriver import Remote as RemoteWebDriver
from pages.product_page import ProductPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time, pytest

class TestLoginAndProductPage():
    @pytest.mark.parametrize('link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
        ])
    def test_guest_should_see_login_link_on_product_page(self, browser, link):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket()
        page.basket_not_items()
        page.basket_have_a_text()
    
    @pytest.mark.parametrize("link" ,[pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/", marks=pytest.mark.xfail)])
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.product_add_to_basket()
        product_page.should_not_be_success_message()

    @pytest.mark.parametrize("link" ,[pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/", marks=pytest.mark.xfail)])
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.product_add_to_basket()
        product_page.should_is_disappeared()

    @pytest.mark.need_review
    @pytest.mark.parametrize("link" ,["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        product_page = ProductPage(browser,link)
        product_page.open()
        product_page.product_add_to_basket()
        product_page.price_basket_equal_price_product()
        product_page.name_message()

@pytest.mark.register
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page.register_new_user(email,password)
        login_page.should_be_authorized_user()

        
    @pytest.mark.parametrize("link" ,["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
    def test_user_cant_see_success_message(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    @pytest.mark.parametrize("link" ,["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
    def test_user_can_add_product_to_basket(self, browser, link):
        product_page = ProductPage(browser,link)
        product_page.open()
        product_page.product_add_to_basket()
        product_page.price_basket_equal_price_product()
        product_page.name_message()

