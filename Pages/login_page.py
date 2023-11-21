from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()
	
	def should_be_login_url(self):
		# проверка на корректный url адрес
		assert 'login' in self.browser.current_url, "url is not contain text LOGIN"
	
	def should_be_login_form(self):
		# проверка, что есть форма логина
		assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"
	
	def should_be_register_form(self):
		# проверка, что есть форма регистрации на странице
		assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register Form is not presented"
	
	def register_new_user(self, email, password):
		email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD_ON_REGISTER_FORM)
		email_field.send_keys(email)
		psw_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_ON_REGISTER_FORM)
		psw_field.send_keys(password)
		confirm_psw = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
		confirm_psw.send_keys(password)
		btn_register = self.browser.find_element(*LoginPageLocators.BTN_REGISTER)
		btn_register.click()
		assert self.is_not_element_present(*LoginPageLocators.REGISTER_FORM), "Register Form is presented"
		