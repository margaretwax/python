# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium import WebDriver
#from selenium.webdriver.Chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class delivery_selenium(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_delivery_selenium(self):
        success = True
        wd = self.wd
        wd.get("http://delivery.oorraa.com/")
        wd.find_element_by_id("from_city_name").click()
        wd.find_element_by_id("from_city_name").clear()
        wd.find_element_by_id("from_city_name").send_keys(u"Москва")
        wd.find_element_by_link_text(u"Москва, г. Москва").click()
        wd.find_element_by_id("to_city_name").click()
        wd.find_element_by_id("to_city_name").clear()
        wd.find_element_by_id("to_city_name").send_keys(u"Санкт-Петербург")
        wd.find_element_by_link_text(u"Санкт-Петербург, г. Санкт-Петербург").click()
        wd.find_element_by_id("gab_x").click()
        wd.find_element_by_id("gab_x").clear()
        wd.find_element_by_id("gab_x").send_keys("12")
        wd.find_element_by_id("gab_y").click()
        wd.find_element_by_id("gab_y").clear()
        wd.find_element_by_id("gab_y").send_keys("12")
        wd.find_element_by_id("gab_z").click()
        wd.find_element_by_id("gab_z").clear()
        wd.find_element_by_id("gab_z").send_keys("12")
        wd.find_element_by_id("weight").click()
        wd.find_element_by_id("weight").clear()
        wd.find_element_by_id("weight").send_keys("12")
        wd.find_element_by_css_selector("input.price_submit").click()
        wd.find_element_by_xpath("//div[@id='price_marker_container']/div[1]").click()
        wd.find_element_by_css_selector("button.tariff_order").click()
        wd.find_element_by_id("fio_sender").click()
        wd.find_element_by_id("fio_sender").clear()
        wd.find_element_by_id("fio_sender").send_keys(u"Мила")
        wd.find_element_by_id("phone_sender").click()
        wd.find_element_by_id("phone_sender").clear()
        wd.find_element_by_id("phone_sender").send_keys("+7 926 181-81-88")
        wd.find_element_by_id("fio_recipient").click()
        wd.find_element_by_id("fio_recipient").clear()
        wd.find_element_by_id("fio_recipient").send_keys(u"Антон")
        wd.find_element_by_id("phone_recipient").click()
        wd.find_element_by_id("phone_recipient").clear()
        wd.find_element_by_id("phone_recipient").send_keys("+7 258 888-88-88")
        wd.find_element_by_id("what_inside").click()
        wd.find_element_by_id("what_inside").clear()
        wd.find_element_by_id("what_inside").send_keys(u"Сумка")
        wd.find_element_by_id("assessed_value").click()
        wd.find_element_by_id("assessed_value").clear()
        wd.find_element_by_id("assessed_value").send_keys("12")
        wd.find_element_by_xpath("//div[@id='price_marker_container']/div[1]").click()
        wd.find_element_by_css_selector("button.send_order.right").click()
        wd.find_element_by_name("mail").click()
        wd.find_element_by_name("mail").clear()
        wd.find_element_by_name("mail").send_keys("123@123.ru")
        wd.find_element_by_css_selector("input.success_mail_submit").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
