from selenium.webdriver.support.ui import Select
import time

class TimeOffForm():

    def __init__(self, driver):
        self.driver = driver

        self.time_off_form_path = "//button/i[@class='fa fa-calendar-plus-o']"
        self.from_date_id = "exampleFormControlInput2"
        self.to_date_id = "exampleFormControlInput3"
        self.morning_checkbox_id = "defaultCheck1"
        self.afternoon_checkbox_id = "defaultCheck2"
        self.day_off_category_id = "exampleFormControlSelect1"
        self.btn_close_path = "//button[contains(., 'Close')]"
        self.btn_save_path = "//button[contains(., 'Save')]"

    def enter_from_date(self, date):
        self.driver.find_element_by_id(self.from_date_id).clear()
        self.driver.find_element_by_id(self.from_date_id).send_keys(date)

    def enter_to_date(self, date):
        self.driver.find_element_by_id(self.to_date_id).clear()
        self.driver.find_element_by_id(self.to_date_id).send_keys(date)

    def click_morning_checkbox(self):
        self.driver.find_element_by_xpath(self.morning_checkbox_id).click()

    def click_afternoon_checkbox(self):
        self.driver.find_element_by_xpath(self.afternoon_checkbox_id).click()

    def select_day_off_category(self, category):
        Select(self.driver.find_element_by_id(self.day_off_category_id)).select_by_value(category)
        time.sleep(3)

    def click_save(self):
        self.driver.find_element_by_xpath(self.btn_save_path).click()

    def click_close(self):
        self.driver.find_element_by_xpath(self.btn_close_path).click()

