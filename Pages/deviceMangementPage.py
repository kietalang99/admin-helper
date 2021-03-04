from selenium.webdriver.support.ui import Select
import time

class DeviceManagementPage():
    def __init__(self, driver):
        self.driver = driver

        self.device_management_tab_path = '//*[@id="sidebar"]/ul/li[2]/a'

        # Filter id
        self.filter_by_status_id = "device-status"
        self.filter_by_device_category_id = "device-category"

        # action in device table
        self.btn_action_path = '//a[@id="dropdownBtn0"]'
        self.btn_move_inventory_path = "//a[contains(., 'Move')]"
        self.btn_assign_path = "//a[contains(., 'Assign')]"
        self.btn_history_path = "//a[contains(., 'History')]"
        self.btn_edit_path = "//a[contains(., 'Edit')]"
        self.btn_discard_path = "//a[contains(., 'Discard')]"

        # Collapsed function
        self.collapsed_path = "//ah-device-table/div/div[3]/div[1]/div/div[5]/a/i"

    def filter_by_status(self, status):
        Select(self.driver.find_element_by_id(self.filter_by_status_id))\
            .select_by_visible_text(status)

    def filter_by_category(self, category):
        Select(self.driver.find_element_by_id(self.filter_by_device_category_id))\
            .select_by_visible_text(category)

    def click_action(self):
        self.driver.find_element_by_xpath(self.btn_action_path).click()

    def click_move_to_inventory(self):
        self.driver.find_element_by_xpath(self.btn_move_inventory_path).click()

    def click_assign(self):
        self.driver.find_element_by_xpath(self.btn_assign_path).click()

    def click_edit(self):
        self.driver.find_element_by_xpath(self.btn_edit_path).click()

    def click_history(self):
        self.driver.find_element_by_xpath(self.btn_history_path).click()

    def click_discard(self):
        self.driver.find_element_by_xpath(self.btn_discard_path).click()

    def click_collapsed(self):
        self.driver.find_element_by_xpath(self.collapsed_path).click()

    def click_pagination(self, pagination):
        self.driver.find_element_by_xpath(pagination).click()
        time.sleep(3)