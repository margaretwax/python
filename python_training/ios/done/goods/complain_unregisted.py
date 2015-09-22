__author__ = 'm.voskresenskaya'
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from ..utils.env import IPHONE
from ..utils import nextscreen
from time import sleep

wait = lambda: sleep(1)

class IosTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', IPHONE)
        self.driver.implicitly_wait(4)

    def test_untitled(self):
        find_name = self.driver.find_element_by_name
        find_xpath = self.driver.find_element_by_xpath

        nextscreen(self.driver)

        find_name("navbar search icon").click() #tap on search
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIASearchBar[1]").send_keys("blazer") #write 'blazer' in search field
        find_name("Search").click() #tap on search button on the keyboard
        wait()
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[4]/UIAStaticText[1]").click() #click on blazer
        wait()
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[16]").click() #tap on complain button
        wait()
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIATextField[1]").click() #tap on 'enter the phone number'
        wait()
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIATextField[1]").send_keys("70000009192") #write a contact cell
        find_name("ok icon").click() #send a complain
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[1]").click() #ok on a springboard

    def tearDown(self):
        self.driver.quit()