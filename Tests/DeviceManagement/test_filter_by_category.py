from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import Select
from Pages.loginPage import LoginPage
from Pages.deviceMangementPage import DeviceManagementPage

class filterByStatus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Admin/PycharmProjects/admin/Drivers/chromedriver.exe")
        cls.driver.maximize_window()
        driver = cls.driver
        driver.get("https://admin-helper-f21c1.web.app/login")
        login = LoginPage(driver)
        login.enter_email("admin@gmail.com")
        login.enter_password("123456")
        login.click_login()
        cls.driver.implicitly_wait(10)

    def test_filter_by_category(self):
        driver = self.driver
        device_management = DeviceManagementPage(driver)
        driver.find_element_by_xpath(device_management.device_management_tab_path).click()

        # Test filter by all status
        device_management.filter_by_category("All")

        # Test filter Laptop category
        device_management.filter_by_category(" Laptop ")

        # Test filter Phone category
        device_management.filter_by_category(" Phone ")

        # Test filter by Tablet category
        device_management.filter_by_category(" Tablet ")

        # Test filter by In Monitor category
        device_management.filter_by_category(" Monitor ")

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test filter by Category was completed")
