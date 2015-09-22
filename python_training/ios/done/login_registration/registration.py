__author__ = 'm.voskresenskaya'
# -*- coding: utf-8 -*-

import unittest
import time
from selenium import webdriver
from ..utils import random_email
from ..utils import random_name
from ..utils.env import IPHONE
from ..utils import nextscreen
from ..utils import do_reg


class iostest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', IPHONE)
        self.driver.implicitly_wait(4)

    def test_untitled(self):
        do_reg(self.driver)

    def tearDown(self):
        self.driver.quit()
