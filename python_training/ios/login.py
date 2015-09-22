__author__ = 'm.voskresenskaya'
import os.path
from selenium import webdriver

success = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '8.4'
desired_caps['deviceName'] = 'iPhone 6'
desired_caps['app'] = os.path.abspath('/Users/m.voskresenskaya/Desktop/Oorraa-sellerDev.app')

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)

def is_alert_present(wd):
	try:
		wd.switch_to_alert().text
		return True
	except:
		return False

try:
	wd.find_element_by_name("OK").click()
	wd.find_element_by_name("Skip").click()
	wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[4]").click()
	wd.find_element_by_name("Phone").click()
	wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").click()
	wd.find_element_by_name("0").click()
	wd.find_element_by_name("0").click()
	wd.find_element_by_name("0").click()
	wd.find_element_by_name("0").click()
	wd.find_element_by_name("0").click()
	wd.find_element_by_name("0").click()
	wd.find_element_by_name("9").click()
	wd.find_element_by_name("1").click()
	wd.find_element_by_name("9").click()
	wd.find_element_by_name("2").click()
	wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]").click()
	wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]").send_keys("123")
	wd.find_element_by_name("Login").click()
	wd.find_element_by_name("navbar search icon").click()
	wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIASearchBar[1]/UIASearchBar[1]").send_keys("123")
	wd.find_element_by_name("Search").click()
	wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[1]/UIAStaticText[1]").click()


finally:
	wd.quit()
	if not success:
		raise Exception("Test failed.")
