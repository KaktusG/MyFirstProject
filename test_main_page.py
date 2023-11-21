from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage
from .Pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"
	
def test_guest_should_see_login_link(browser): 
	page = MainPage(browser, link)	# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()						# открываем страницу
	page.should_be_login_link()		# выполняем метод страницы — проверяем наличие ссылки логина

def test_guest_can_go_to_login_page(browser):
	page = MainPage(browser, link)
	page.open()
	page.go_to_login_page()			# выполняем метод страницы — переходим на страницу логина
	login_page = LoginPage(browser, browser.current_url) # инициализируем страницу Login
	login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	page = MainPage(browser, link)
	page.open()
	page.go_to_basket_page()
	basket_page = BasketPage(browser, browser.current_url)
	basket_page.should_be_empty_basket()
	