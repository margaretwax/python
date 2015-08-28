# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_delivery(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_delivery(self):
        wd = self.wd
        self.open_home_page(wd)
        self.from_and_to_the_city(wd, from_city_name=u"Москва", to_city_name=u"Санкт-Петербург")
        self.parameters_of_the_good(wd, Group(length="10", width="20", height="30", weight="40"))
        self.press_submit_button(wd)
        self.result_page(wd)

    def test_one_delivery(self):
        wd = self.wd
        self.open_home_page(wd)
        self.from_and_to_the_city(wd, from_city_name=u"Москва", to_city_name=u"Санкт-Петербург")
        self.parameters_of_the_good(wd, Group(length="1", width="1", height="1", weight="1"))
        self.press_submit_button(wd)
        self.result_page(wd)





    def result_page(self, wd):
        # new page
        wd.find_element_by_xpath("//div[@id='price_marker_container']/div[1]").click()

    def press_submit_button(self, wd):
        # submit button
        wd.find_element_by_css_selector("input.price_submit").click()

    def parameters_of_the_good(self, wd, group):
        # parameters of the good
        wd.find_element_by_id("gab_x").click()
        wd.find_element_by_id("gab_x").clear()
        wd.find_element_by_id("gab_x").send_keys(group.length)
        wd.find_element_by_id("gab_y").click()
        wd.find_element_by_id("gab_y").clear()
        wd.find_element_by_id("gab_y").send_keys(group.width)
        wd.find_element_by_id("gab_z").click()
        wd.find_element_by_id("gab_z").clear()
        wd.find_element_by_id("gab_z").send_keys(group.height)
        wd.find_element_by_id("weight").click()
        wd.find_element_by_id("weight").clear()
        wd.find_element_by_id("weight").send_keys(group.weight)

    def from_and_to_the_city(self, wd, from_city_name, to_city_name):
        # from and to the city
        wd.find_element_by_id("from_city_name").click()
        wd.find_element_by_id("from_city_name").clear()
        wd.find_element_by_id("from_city_name").send_keys(from_city_name)
        wd.find_element_by_link_text(u"Москва, г. Москва").click()
        wd.find_element_by_id("to_city_name").click()
        wd.find_element_by_id("to_city_name").clear()
        wd.find_element_by_id("to_city_name").send_keys(to_city_name)
        wd.find_element_by_link_text(u"Санкт-Петербург, г. Санкт-Петербург").click()

    def open_home_page(self, wd):
        # open the main page
        wd.get("http://delivery.oorraa.com/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
