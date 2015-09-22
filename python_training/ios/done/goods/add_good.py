__author__ = 'm.voskresenskaya'
# -*- coding: utf-8 -*-
from time import sleep
import unittest
from selenium import webdriver
from ..utils import do_login
from ..utils.env import IPHONE

wait = lambda: sleep(1)


class iostest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', IPHONE)
        self.driver.implicitly_wait(4)

    def test_untitled(self):
        find_name = self.driver.find_element_by_name
        find_xpath = self.driver.find_element_by_xpath

        do_login(self.driver)

        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[4]").click()  # go to profile

        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()  # shop
        find_name("Add a product").click()
        find_name("OK").click()  # access to user's photos
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()  # tap on gallery button
        find_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[5]/UIAImage[1]").click()  # tap on image
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()  # tap on select button
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[5]").click()  # tap on 'add a description'

        for i in range(5):
            el_cat = find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]")
            el_cat.click()
            wait()

        wait()
        find_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIATextField[1]").click()  # tap on name field
        wait()
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIATextField[1]").send_keys(
            "Blazer men autotest mobile")  # set a name of a product
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[6]/UIATextField[1]").send_keys(
            "25")  # set a minimum quantity
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[7]/UIATextField[1]").send_keys(
            "1700")  # price
        find_name("Done").click()
        find_name("PUBLISH").click()
        find_name("OK").click()  # springboard

    def tearDown(self):
        self.driver.quit()

