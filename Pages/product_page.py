from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
	def add_to_basket(self):
		btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
		btn_add_to_basket.click()
		
	def item_name (self):
		return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
		
	def item_price (self):
		return self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text

	def should_be_text_message_with_item_name(self): 
		message_text = self.browser.find_element(*ProductPageLocators.MESSAGE_BLOCK_WITH_TXT).text
		item_name = self.item_name()
		assert message_text == item_name, " The text doesn't match"
		
	def should_be_text_message_with_price(self):
		message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_BLOCK_WITH_PRICE).text
		item_price = self.item_price()
		assert message_price == item_price, "The price doesn't match"
		
	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.MESSAGE_BLOCK_WITH_TXT),\
			 "Success message is presented, but should not be"
	
	def should_disappear_success_message(self):
		assert self.is_disappeared(*ProductPageLocators.MESSAGE_BLOCK_WITH_TXT),\
				"Success message is still displayed"