# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from ..utils.env import IPHONE
from ..utils import do_login


class iostest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', IPHONE)
        self.driver.implicitly_wait(5)

    def test_untitled(self):
        find_name = self.driver.find_element_by_name
        find_xpath = self.driver.find_element_by_xpath

        do_login(self.driver, role='buyer')

        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[3]").click()  # go to messages
        find_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAStaticText[1]").click()  # tap on text field
        find_xpath("//UIAApplication[1]/UIAWindow[2]/UIATextView[1]").send_keys("hi test")  # write hi test
        find_name("Send").click()  # tap on send button
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()
