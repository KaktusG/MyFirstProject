from selenium.webdriver.common.by import By

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BTN_OPEN_BASKET = (By.XPATH, "//header/div[1]/div/div[2]/span/a")
	
	
class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	ITEM_NAME = (By.XPATH, "//div[@id='content_inner']/article/div/div[2]/h1")
	ITEM_PRICE = (By.XPATH, "//div[@id='content_inner']/article/div/div[2]/p")
	MESSAGE_BLOCK_WITH_TXT = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
	MESSAGE_BLOCK_WITH_PRICE = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")

class BasketPageLocators():
	TEXT_EMPTY_BASKET = (By.XPATH, "//div[@id='content_inner']/p")
	BLOCK_WITH_ITEMS = (By.CSS_SELECTOR, "#basket_formset")