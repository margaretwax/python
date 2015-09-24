#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import time
from selenium import webdriver
from ..utils.env import IPHONE
from ..utils import nextscreen
from ..utils import click_and_send_keys


class IosTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', IPHONE)
        self.driver.implicitly_wait(4)

    def test_untitled(self):
        find_xpath = self.driver.find_element_by_xpath

        nextscreen(self.driver)
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[3]").click()  # login button (messages)
        time.sleep(3)
        click_and_send_keys(self.driver, "//UIAApplication[1]/UIAWindow[1]/UIATextField[2]", "oorraatest_123qweasd@oorraa.com")  # tap on login field and send login

        click_and_send_keys(self.driver, "//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[2]", "123456")  # tap on password field and send password

        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[3]").click()
        find_xpath(
            "//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[1]/UIAButton[1]").click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
