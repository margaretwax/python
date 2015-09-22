__author__ = 'm.voskresenskaya'
# -*- coding: utf-8 -*-
import unittest
import os
from selenium import webdriver
import time


class iostest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '8.4'
        desired_caps['deviceName'] = 'iPhone 6'
        desired_caps['app'] = os.path.abspath('/Users/m.voskresenskaya/Desktop/Oorraa-sellerDev.app')

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(4)

    def test_untitled(self):
        find_name = self.driver.find_element_by_name
        find_xpath = self.driver.find_element_by_xpath

        find_name('OK').click()
        find_name('Skip').click()
        find_xpath('//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[4]').click()
        find_name('Phone').click()
        find_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextField[1]').click()

        el_0 = find_name('0')

        for i in range(6):
            el_0.click()
        find_name('9').click()
        find_name('1').click()
        find_name('9').click()
        find_name('2').click()

        el_secure = find_xpath('//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]')
        el_secure.click()
        el_secure.send_keys('123')
        find_name('Login').click()

        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[4]").click()  # go to profile

        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]").click()  # shop
        find_name("Add a product").click()
        find_name("OK").click()  # access to user's photos
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()  # tap on gallery button
        find_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[5]/UIAImage[1]").click()  # tap on image
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()  # tap on select button
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[5]").click()  # tap on 'add a description'
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]").click()  # tap on category
        time.sleep(3)
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]").click()  # clothing
        time.sleep(3)
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]").click()  # tops
        time.sleep(3)
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]").click()  # men
        time.sleep(3)
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]").click()  # blazers
        time.sleep(3)
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIATextField[1]").click()  # tap on name field
        time.sleep(3)
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIATextField[1]").send_keys("Blazer men autotest mobile")  # set a name of a product
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[6]/UIATextField[1]").send_keys("25")  # set a minimum quantity
        find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[7]/UIATextField[1]").send_keys("1700")  # price
        find_name("Done").click()
        find_name("PUBLISH").click()
        find_name("OK").click()  # springboard

    def tearDown(self):
        self.driver.quit()
