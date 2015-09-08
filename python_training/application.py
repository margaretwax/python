# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver


class Application:

        def __init__(self):
            self.wd = WebDriver()
            self.wd.implicitly_wait(60)

        def open_home_page(self):
            wd = self.wd
            wd.get("http://delivery.oorraa.com/")

        def parameters_of_the_good(self, group):
            # parameters of the good
            wd = self.wd
            wd.find_element_by_id("gab_x").click()
            wd.find_element_by_id("gab_x").clear()
            wd.find_element_by_id("gab_x").send_keys(group.length)
            wd.find_element_by_id("gab_y").click()
            wd.find_element_by_id("gab_y").clear()
            wd.find_element_by_id("gab_y").send_keys(group.width)
            wd.find_element_by_id("gab_z").click()
            wd.find_element_by_id("gab_z").clear()
            wd.find_element_by_id("gab_z").send_keys(group.height)
            wd.find_element_by_id("weight").click()
            wd.find_element_by_id("weight").clear()
            wd.find_element_by_id("weight").send_keys(group.weight)

        def from_and_to_the_city(self, from_city_name, to_city_name):
            # from and to the city
            wd = self.wd
            self.open_home_page()
            wd.find_element_by_id("from_city_name").click()
            wd.find_element_by_id("from_city_name").clear()
            wd.find_element_by_id("from_city_name").send_keys(from_city_name)
            wd.find_element_by_link_text(u"Москва, г. Москва").click()
            wd.find_element_by_id("to_city_name").click()
            wd.find_element_by_id("to_city_name").clear()
            wd.find_element_by_id("to_city_name").send_keys(to_city_name)
            wd.find_element_by_link_text(u"Санкт-Петербург, г. Санкт-Петербург").click()

        def press_submit_button(self):
            # submit button
            wd = self.wd
            wd.find_element_by_css_selector("input.price_submit").click()

        def result_page(self):
            # new page
            wd = self.wd
            wd.find_element_by_xpath("//div[@id='price_marker_container']/div[1]").click()

        def destroy(self):
            self.wd.quit()

