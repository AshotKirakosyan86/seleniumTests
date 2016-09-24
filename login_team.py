# login - laura@teamable.me
# pass  - changeme123
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

class Sign:
	BASE_URL = 'https://selenium.teamable.me/'
	LOGIN = 'laura@teamable.me'
	PASSWORD = 'changeme123'

	def set_up(self):
		self.driver = webdriver.Firefox()
		self.driver.get(self.BASE_URL)
	
	def tear_down(self):
		self.driver.quit()


	def sign_in(self):
		self.driver.maximize_window()
		WebDriverWait(self.driver,10).until(lambda driver:driver.find_element_by_id(Locators.SIGN_IN_BUTTON)).click()
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_name(Locators.LOGIN_FIELD).send_keys(self.LOGIN)
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_name(Locators.PASSWORD_FIELD).send_keys(self.PASSWORD)	
		self.driver.find_element_by_id(Locators.SUBMIT_BUTTON).click()
		
		
		
	def log_out(self):
		
		self.driver.find_element_by_class_name(Locators.Drop_Down).click()
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_id(Locators.LOG_OUT_BUTTON).click()


if __name__ == "__main__":	
	sign = Sign()
	sign.set_up()
	sign.sign_in()
	#sign.log_out()
	#sign.tear_down()


