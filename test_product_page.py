from .Pages.product_page import ProductPage
from .Pages.login_page import LoginPage
from .Pages.basket_page import BasketPage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail), "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_should_see_login_link_on_product_page(browser):
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()
	login_page = LoginPage(browser, browser.current_url)
	login_page.should_be_login_page()
	
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	page = ProductPage(browser, link)
	page.open()
	page.go_to_basket_page()
	basket_page = BasketPage(browser, browser.current_url)
	basket_page.should_be_empty_basket()
	
	
# def test_guest_can_add_product_to_basket(browser): 
	# page = ProductPage(browser, link)	# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	# page.open()
	# page.add_to_basket() 				# клик епо кнопке Добавить в корзину
	# page.solve_quiz_and_get_code()
	# time.sleep(2)
	# page.should_be_text_message_with_item_name()
	# page.should_be_text_message_with_price()

# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	# page = ProductPage(browser, link)
	# page.open()
	# page.add_to_basket()
	# page.should_not_be_success_message()
	
# def test_guest_cant_see_success_message(browser):
	# page = ProductPage(browser, link)
	# page.open()
	# page.should_not_be_success_message()

# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
	# page = ProductPage(browser, link)
	# page.open()
	# page.add_to_basket()
	# page.should_disappear_success_message()

# def test_guest_should_see_login_link_on_product_page(browser):
	# page = ProductPage(browser, link)
	# page.open()
	# page.should_be_login_link()

	