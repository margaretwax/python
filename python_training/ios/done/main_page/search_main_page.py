# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from ..utils.env import IPHONE


class iostest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', IPHONE)
        self.driver.implicitly_wait(4)

    def test_untitled(self):
        find_name = self.driver.find_element_by_name
        find_xpath = self.driver.find_element_by_xpath
        find_name('OK').click()
        find_name('Skip').click()
        find_name("navbar search icon").click() #search on the main page
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIASearchBar[1]/UIASearchBar[1]").send_keys("active forever") #find a product
        find_name("Search").click() #tap a search button on a keyboard
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[1]").click() #tap a founded product
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()