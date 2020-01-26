from selenium.webdriver import Remote as RemoteWebDriver
from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    login = LoginPage(browser, link)
    login.open()
    login.should_be_login_page()
