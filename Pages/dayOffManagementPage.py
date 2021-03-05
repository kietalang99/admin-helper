from keyboard import press
import time
from selenium.webdriver.support.ui import Select

class DayOffManagementPage():

    def __init__(self, driver):
        self.driver = driver

        self.search_id = "inlineFormInputGroupUsername"
        self.day_off_category_id = "day-off-type"
        self.edit_day_off_path = "//div//button/i[@class='cil-brush']"
        self.submit_time_off_path = "//div/button/i[@class='fa fa-calendar-plus-o']"
        self.name_column_path = "//table/thead/tr/th[@class='col-name']"
        self.birthday_column_path = "//table/thead/tr/th[@class='col-birthday']"

    def enter_search_key(self, key):
        self.driver.find_element_by_id(self.search_id).clear()
        self.driver.find_element_by_id(self.search_id).send_keys(key)
        press("enter")
        time.sleep(3)

    def select_day_off_category(self, category):
        Select(self.driver.find_element_by_id(self.day_off_category_id)).select_by_value(category)
        time.sleep(3)

    def click_edit_day_off(self):
        self.driver.find_element_by_xpath(self.edit_day_off_path).click()

    def click_submit_time_off(self):
        self.driver.find_element_by_xpath(self.submit_time_off_path).click()