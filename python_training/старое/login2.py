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
        self.open_home_page(wd)
        self.enter_login(wd)
        self.enter_phone(wd, mobile_phone="(000) 000-91-92")
        self.enter_password(wd, password="123")

# проба пера дальше кусок
    def empty_password(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.enter_login(wd)
        self.enter_phone(wd, mobile_phone="(000) 000-91-92")
        self.enter_password(wd, password="")


    def open_home_page(self, wd):
        # open home page
        wd.get("https://front1.test.oorraa.net/")

    def enter_login(self, wd):
        # login
        wd.find_element_by_link_text("Регистрация и вход").click()
        wd.find_element_by_link_text("Вход").click()
        wd.find_element_by_xpath("//label[@for='rs_loginWith_phone']/span/span").click()
        if not wd.find_element_by_id("rs_loginWith_phone").is_selected():
            wd.find_element_by_id("rs_loginWith_phone").click()

    def enter_phone(self, wd, mobile_phone):
        # enter phone
        wd.find_element_by_name("phone").click()
        wd.find_element_by_name("phone").clear()
        wd.find_element_by_name("phone").send_keys(mobile_phone)

    def enter_password(self, wd, password):
        # enter password
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//section[@class='layout__auth']//button[.='Войти']").click()





    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
