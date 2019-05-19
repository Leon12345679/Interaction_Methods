from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import *

import pickle

from random import randint

# contains all of the needed methods to interact with web pages


class Methods:
    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, element):
        self.scroll_to_element(element)
        self.click_at_point()

    def save_cookies(self, cookie_filename):
        pickle.dump(self.driver.get_cookies(), open(cookie_filename, "wb"))

    def load_cookies(self, cookie_filename):
        cookies = pickle.load(open(cookie_filename, "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    # Scrolling functions use ChromeDriver in Safari use JS to scroll

    def scroll_a_bit(self):
        actions = ActionChains(self.driver)
        [actions.send_keys(Keys.ARROW_DOWN) for _ in range(4)]
        actions.perform()

    def scroll_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    # _click_at_point() bypasses a ChromeDriver bug which thinks
    # that element is non intractable by clicking at it's point

    def click_at_point(self):
        actions = ActionChains(self.driver)
        actions.click()
        actions.perform()

    # _fill_field is a function that takes in data and inputs it into a preselected textfield

    def fill_field(self, data):
        actions = ActionChains(self.driver)
        actions.send_keys(data)
        actions.send_keys(Keys.RETURN)
        actions.perform()

    # _check_exists_by_X are functions that try to find an element by X -> True if found; False if not

    def check_exists_by_class(self, class_name):
        try:
            self.driver.find_element_by_css_selector("[class='{0}']".format(class_name))
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_id(self, id_name):
        try:
            self.driver.find_element_by_id(id_name)
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_text(self, text):
        try:
            self.driver.find_element_by_xpath("//*[contains(text(), '{0}')]".format(text))
        except NoSuchElementException:
            return False
        return True

    def move_mouse_randomly(self):
        actions = ActionChains(self.driver)
        actions.move_by_offset(randint(500, 1000), randint(500, 1000))
        actions.perform()
