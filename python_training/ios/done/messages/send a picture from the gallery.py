# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from ..utils import do_login
from ..utils.env import IPHONE


class iostest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', IPHONE)
        self.driver.implicitly_wait(6)

    def test_untitled(self):
        find_name = self.driver.find_element_by_name
        find_xpath = self.driver.find_element_by_xpath

        do_login(self.driver)

        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[3]").click()  # go to messages
        find_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAStaticText[1]").click()  # user's name
        find_xpath("//UIAApplication[1]/UIAWindow[2]/UIAButton[1]").click()  # tap on X
        find_xpath("//UIAApplication[1]/UIAWindow[2]/UIAButton[6]").click()  # tap on gallery
        time.sleep(1)
        find_name("OK").click()  # springboard access to user's photos
        time.sleep(1)
        find_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]").click()  # choose moments folder
        time.sleep(1)
        find_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[4]").click()  # choose a picture
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()


'''wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[3]").click()
wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAStaticText[1]").click()
wd.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]/UIAButton[1]").click()'''
