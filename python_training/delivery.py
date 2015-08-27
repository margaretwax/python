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

class delivery(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_delivery(self):
        success = True
        wd = self.wd
        wd.get("http://delivery.oorraa.com/")
        self.from_city_name(wd, "Москва", "Москва, г. Москва")
        self.to_city_name(wd, "Санкт-Петербург", "Санкт-Петербург, г. Санкт-Петербург")
        wd.find_element_by_css_selector("p.gabarith_labels").click()
        self.length(wd, "20")
        self.width(wd, "30")
        self.height(wd, "40")
        self.weight(wd, "50")
        wd.find_element_by_css_selector("input.price_submit").click()
        wd.find_element_by_xpath("//div[@id='price_marker_container']/div[1]").click()
        self.assertTrue(success)

    def to_city_name(self, wd, to_city_name, to_city_name_from_the_list):
        wd.find_element_by_id("to_city_name").click()
        wd.find_element_by_id("to_city_name").clear()
        wd.find_element_by_id("to_city_name").send_keys(to_city_name)
        wd.find_element_by_link_text(to_city_name_from_the_list).click()

    def from_city_name(self, wd, from_city_name, from_city_name_from_the_list):
        wd.find_element_by_id("from_city_name").click()
        wd.find_element_by_id("from_city_name").clear()
        wd.find_element_by_id("from_city_name").send_keys(from_city_name)
        wd.find_element_by_link_text(from_city_name_from_the_list).click()

    def length(self, wd, length):
        wd.find_element_by_id("gab_x").click()
        wd.find_element_by_id("gab_x").clear()
        wd.find_element_by_id("gab_x").send_keys(length)

    def weight(self, wd, weight):
        wd.find_element_by_id("weight").click()
        wd.find_element_by_id("weight").clear()
        wd.find_element_by_id("weight").send_keys(weight)

    def width(self, wd, width):
        wd.find_element_by_id("gab_y").click()
        wd.find_element_by_id("gab_y").clear()
        wd.find_element_by_id("gab_y").send_keys(width)

    def height(self, wd, height):
        wd.find_element_by_id("gab_z").click()
        wd.find_element_by_id("gab_z").clear()
        wd.find_element_by_id("gab_z").send_keys(height)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
