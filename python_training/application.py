from selenium.webdriver.firefox.webdriver import WebDriver


class Application:

        def __init__(self):
                self.wd = WebDriver()
                self.wd.implicitly_wait(60)


        def test_delivery(self):
                wd = self.wd
                wd.get("http://delivery.oorraa.com/")
                wd.find_element_by_css_selector("p.gabarith_labels").click()
                wd.find_element_by_css_selector("input.price_submit").click()
                wd.find_element_by_xpath("//div[@id='price_marker_container']/div[1]").click()


        def to_city_name(self, group):
                wd = self.wd
                wd.find_element_by_id("to_city_name").click()
                wd.find_element_by_id("to_city_name").clear()
                wd.find_element_by_id("to_city_name").send_keys(group.to_city_name)
                wd.find_element_by_link_text(group.to_city_name_from_the_list).click()

        def from_city_name(self, from_city_name, from_city_name_from_the_list):
                wd = self.wd
                wd.find_element_by_id("from_city_name").click()
                wd.find_element_by_id("from_city_name").clear()
                wd.find_element_by_id("from_city_name").send_keys(from_city_name)
                wd.find_element_by_link_text(from_city_name_from_the_list).click()

        def length(self, length):
                wd = self.wd
                wd.find_element_by_id("gab_x").click()
                wd.find_element_by_id("gab_x").clear()
                wd.find_element_by_id("gab_x").send_keys(length)

        def weight(self, weight):
                wd = self.wd
                wd.find_element_by_id("weight").click()
                wd.find_element_by_id("weight").clear()
                wd.find_element_by_id("weight").send_keys(weight)

        def width(self, width):
                wd = self.wd
                wd.find_element_by_id("gab_y").click()
                wd.find_element_by_id("gab_y").clear()
                wd.find_element_by_id("gab_y").send_keys(width)

        def height(self, height):
                wd = self.wd
                wd.find_element_by_id("gab_z").click()
                wd.find_element_by_id("gab_z").clear()
                wd.find_element_by_id("gab_z").send_keys(height)


        def destroy(self):
                self.wd.quit()

