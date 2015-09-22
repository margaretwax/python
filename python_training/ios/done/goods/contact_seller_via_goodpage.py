__author__ = 'm.voskresenskaya'
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from ..utils import do_login
from ..utils.env import IPHONE


class IosTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', IPHONE)
        self.driver.implicitly_wait(4)

    def test_untitled(self):
        find_name = self.driver.find_element_by_name
        find_xpath = self.driver.find_element_by_xpath

        do_login(self.driver, role='buyer')

        find_name("navbar search icon").click()
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIASearchBar[1]").send_keys("blazer")
        find_name("Search").click()
        find_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[4]/UIAStaticText[1]").click()
        find_name("CONTACT THE SELLER").click()
        find_name("ok icon").click()

    def tearDown(self):
        self.driver.quit()
