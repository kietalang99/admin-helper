from selenium.webdriver.support.ui import Select
import time

class DayOffRequestManagementPage():
    def __init__(self, driver):
        self.driver = driver

        # Get day off request management tab
        self.day_off_request_tab_path = '//*[@id="sidebar"]/ul/li[6]/a'

        # Filter
        self.filter_by_employee_path = "//ngx-select/div/div[2]/div"
        self.filter_by_day_off_category_id = "day-off-type"
        self.filter_by_from_date_id = "from-date"
        self.filter_by_to_date_id = "to-date"

        # action
        self.dor_action_path = '//*[@id="dropdownBtn0"]'
        self.edit_path = "//a[contains(.,'Edit')]"
        self.delete_path = "//a[contains(.,'Delete')]"

    def filter_by_employee(self):
        Select(self.driver.find_element_by_xpath(self.filter_by_employee_path))\
            .select_by_index(1)

    def filter_by_category(self, category):
        Select(self.driver.find_element_by_id(self.filter_by_day_off_category_id))\
            .select_by_visible_text(category)

    def filter_by_from_date(self, date):
        self.driver.find_element_by_id(self.filter_by_from_date_id).send_keys(date)

    def filter_by_to_date(self, date):
        self.driver.find_element_by_id(self.filter_by_to_date_id).send_keys(date)

    def click_action(self):
        self.driver.find_element_by_xpath(self.dor_action_path).click()

    def click_edit(self):
        self.driver.find_element_by_xpath(self.edit_path).click()

    def click_delete(self):
        self.driver.find_element_by_xpath(self.delete_path).click()