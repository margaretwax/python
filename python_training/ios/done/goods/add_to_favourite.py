#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import time
from selenium import webdriver


from ..utils.env import IPHONE
from ..utils import do_reg



class iostest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', IPHONE)
        self.driver.implicitly_wait(6)

    def test_untitled(self):
        find_name = self.driver.find_element_by_name
        find_xpath = self.driver.find_element_by_xpath

        do_reg(self.driver)
        find_name("navbar search icon").click() #search on the main page
        time.sleep(2)
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[2]/UIASearchBar[1]").send_keys("active forever") #find a product
        time.sleep(2)
        find_name("Search").click() #tap a search button on a keyboard
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[1]").click() #tap a founded product

        find_name("navbar favorites off icon").click() #tap on favourites button
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[2]/UIAButton[2]").click() #go back
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[2]").click() # go to favourites
        find_name("Change").click() #tap on change button
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[1]").click() #choose an item to delete
        find_name("DELETE").click() # delete item
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

