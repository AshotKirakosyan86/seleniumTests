# run tests - py.test -v testing_teamable.py

import pytest
from login_team import Sign
from locators import Locators
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


sign = Sign()
def test_set_up():
	sign.set_up()
	assert 'TEAMABLE' in sign.driver.title
	sign.tear_down()


def is_log_out_present():
	sign.driver.find_element_by_class_name(Locators.Drop_Down).click()
	sign.driver.implicitly_wait(10)
	try:
		sign.driver.find_element_by_id(Locators.LOG_OUT_BUTTON)
	except NoSuchElementException:
		pass
		return False
	return True
	
def test_sign_in():
	sign.set_up()
	sign.sign_in()
	assert is_log_out_present() == True
	sign.tear_down()

def is_sign_in_present():
	try:
		sign.driver.find_element_by_id(Locators.SIGN_IN_BUTTON)
	except NoSuchElementException:
		return False
	return True

def test_log_out():
	sign.set_up()
	sign.sign_in()
	sign.log_out()
	assert is_sign_in_present() == True
	sign.tear_down()


