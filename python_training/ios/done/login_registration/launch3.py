__author__ = 'm.voskresenskaya'
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from ..utils.env import IPHONE


class IosTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', IPHONE)
        self.driver.implicitly_wait(4)

    def test_skipscreen(self):
        for index in ['OK', 'Next', 'Next', 'Next', 'Next', 'Start']:
            self.driver.find_element_by_name(index).click()

    def tearDown(self):
        self.driver.quit()
