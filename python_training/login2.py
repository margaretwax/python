# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class login2(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_login2(self):
        success = True
        wd = self.wd
        wd.get("https://front1.test.oorraa.net/")
        wd.find_element_by_link_text("Регистрация и вход").click()
        wd.find_element_by_link_text("Вход").click()
        wd.find_element_by_xpath("//label[@for='rs_loginWith_phone']/span/span").click()
        if not wd.find_element_by_id("rs_loginWith_phone").is_selected():
            wd.find_element_by_id("rs_loginWith_phone").click()
        wd.find_element_by_name("phone").click()
        wd.find_element_by_name("phone").clear()
        wd.find_element_by_name("phone").send_keys("(000) 000-91-92")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("123")
        wd.find_element_by_xpath("//section[@class='layout__auth']//button[.='Войти']").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
