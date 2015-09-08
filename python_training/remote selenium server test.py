__author__ = 'm.voskresenskaya'
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        sauce_url = "http://ondemand.saucelabs.com/wd/hub"
        self.driver = webdriver.Remote("http://mvoskresenskaya:71e1e9c5-2182-402c-85a6-8ebbac74aa61@ondemand.saucelabs.com/wd/hub", webdriver.DesiredCapabilities.FIREFOX)
        self.driver.implicitly_wait(60)
        self.base_url = "http://delivery.oorraa.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("from_city_name").click()
        driver.find_element_by_id("from_city_name").clear()
        driver.find_element_by_id("from_city_name").send_keys(u"Москва")
        driver.find_element_by_link_text(u"Москва, г. Москва").click()
        driver.find_element_by_id("to_city_name").click()
        driver.find_element_by_id("to_city_name").clear()
        driver.find_element_by_id("to_city_name").send_keys(u"Санкт-Петербург")
        driver.find_element_by_link_text(u"Санкт-Петербург, г. Санкт-Петербург").click()
        driver.find_element_by_id("gab_x").click()
        driver.find_element_by_id("gab_x").clear()
        driver.find_element_by_id("gab_x").send_keys("12")
        driver.find_element_by_id("gab_y").click()
        driver.find_element_by_id("gab_y").clear()
        driver.find_element_by_id("gab_y").send_keys("12")
        driver.find_element_by_id("gab_z").click()
        driver.find_element_by_id("gab_z").clear()
        driver.find_element_by_id("gab_z").send_keys("12")
        driver.find_element_by_id("weight").click()
        driver.find_element_by_id("weight").clear()
        driver.find_element_by_id("weight").send_keys("12")
        driver.find_element_by_css_selector("input.price_submit").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
