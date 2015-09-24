# -*- coding: utf-8 -*-
import os
import unittest
from selenium import webdriver
from ..utils import do_login
from ..utils.env import IPHONE


class IosTest(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', IPHONE)
        self.driver.implicitly_wait(4)

    def test_untitled(self):
        do_login(self.driver)

    def tearDown(self):
        self.driver.quit()
