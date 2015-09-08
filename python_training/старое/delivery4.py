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

class delivery4(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_delivery4(self):
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
        wd.find_element_by_id("gab_x").send_keys("10")
        wd.find_element_by_id("gab_y").click()
        wd.find_element_by_id("gab_y").clear()
        wd.find_element_by_id("gab_y").send_keys("20")
        wd.find_element_by_id("gab_z").click()
        wd.find_element_by_id("gab_z").clear()
        wd.find_element_by_id("gab_z").send_keys("30")
        wd.find_element_by_id("weight").click()
        wd.find_element_by_id("weight").clear()
        wd.find_element_by_id("weight").send_keys("40")
        wd.find_element_by_css_selector("input.price_submit").click()
        wd.find_element_by_xpath("//div[@id='price_marker_container']/div[1]").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

