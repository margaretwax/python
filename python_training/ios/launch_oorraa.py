__author__ = 'm.voskresenskaya'
# -*- coding: utf-8 -*-
import os.path
from selenium import webdriver
import unittest

success = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '8.4'
desired_caps['deviceName'] = 'iPhone 6'
desired_caps['app'] = os.path.abspath('/Users/m.voskresenskaya/Desktop/Oorraa-sellerDev.app')

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)


class Untitled(unittest.TestCase):
    def is_alert_present(wd):
        try:
            wd.switch_to_alert().text
            return True
        except:
            return False

    try:
        wd.find_element_by_name("OK").click()
        wd.find_element_by_name("Next").click()
        wd.find_element_by_name("Next").click()
        wd.find_element_by_name("Next").click()
        wd.find_element_by_name("Next").click()
        wd.find_element_by_name("Start").click()

    finally:
        wd.quit()
        if not success:
            raise Exception("Test failed")
