from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
	def should_be_empty_basket(self):
		self.should_be_basket_url()
		self.should_not_be_items_in_basket()
		self.should_be_message_empty_basket()
		
	def should_be_basket_url(self):
		# проверка на корректный url адрес
		assert 'basket' in self.browser.current_url, "url is not contain text BASKET"
	
	def should_not_be_items_in_basket(self):
		# проверка, что в корзине нет товаров
		assert self.is_not_element_present(*BasketPageLocators.BLOCK_WITH_ITEMS), "Basket is not empty"
	
	def should_be_message_empty_basket(self):
		# проверка, что есть текст о том что корзина пуста 
		assert 'Your basket is empty' in self.browser.find_element(*BasketPageLocators.TEXT_EMPTY_BASKET).text, "Message Empty Basket is not present"