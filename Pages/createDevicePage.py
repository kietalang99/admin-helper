from keyboard import press
import time
from selenium.webdriver.support.ui import Select

class CreateDevicePage():
    def __init__(self, driver):
        self.driver = driver

        self.btn_create_device_path = "//button[text()=' Create Device ']"
        self.device_name_textbox_path = "//input[@id='name']"
        self.price_textbox_path = "//input[@id='price']"
        self.device_category_select_path = "//select[@formcontrolname = 'deviceCategoryId']"
        self.description_textarea_path = "//textarea[@id='description']"
        self.btn_close_path = "//button[text()=' Close ']"
        self.btn_save_path = "//button[@type='submit']"

    def click_create_device(self):
        self.driver.find_element_by_xpath(self.btn_create_device_path).click()

    def enter_device_name(self, name):
        self.driver.find_element_by_xpath(self.device_name_textbox_path).clear()
        self.driver.find_element_by_xpath(self.device_name_textbox_path).send_keys(name)

    def enter_device_name(self, price):
        self.driver.find_element_by_xpath(self.price_textbox_path).clear()
        self.driver.find_element_by_xpath(self.price_textbox_path).send_keys(price)

    def select_device_category(self, category):
        Select(self.driver.find_element_by_xpath(self.device_category_select_path)).select_by_value(category)
        time.sleep(3)

    def enter_device_description(self, description):
        self.driver.find_element_by_xpath(self.description_textarea_path).clear()
        self.driver.find_element_by_xpath(self.description_textarea_path).send_keys(description)

    def click_save(self):
        self.driver.find_element_by_xpath(self.btn_save_path).click()

    def click_close(self):
        self.driver.find_element_by_xpath(self.btn_close_path).click()