from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	ITEM_NAME = (By.XPATH, "//div[@id='content_inner']/article/div/div[2]/h1")
	ITEM_PRICE = (By.XPATH, "//div[@id='content_inner']/article/div/div[2]/p")
	MESSAGE_BLOCK_WITH_TXT = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
	MESSAGE_BLOCK_WITH_PRICE = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")