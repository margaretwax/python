# -*- coding: utf-8 -*-
import unittest
import os
from selenium import webdriver


class iostest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '8.4'
        desired_caps['deviceName'] = 'iPhone 6'
        desired_caps['app'] = os.path.abspath('/Users/m.voskresenskaya/Desktop/Oorraa-sellerDev.app')

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(4)

    def test_untitled(self):
        find_name = self.driver.find_element_by_name
        find_name("OK").click()
        find_name("Next").click()
        find_name("Next").click()
        find_name("Next").click()
        find_name("Next").click()
        find_name("Start").click()

    def tearDown(self):
        self.driver.quit()
