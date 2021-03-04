from selenium import webdriver
import unittest
import time
from Pages.loginPage import LoginPage
from Pages.deviceMangementPage import DeviceManagementPage

class deviceManagementNavigation(unittest.TestCase):
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

    def test_navigation(self):
        driver = self.driver

        device_management = DeviceManagementPage(driver)
        driver.find_element_by_xpath(device_management.device_management_tab_path).click()

        # Click on Last page
        device_management.click_pagination("//li[@class='pagination-last page-item']")

        # Click on first page
        device_management.click_pagination("//li[@class='pagination-first page-item']")

        # Click on next page
        device_management.click_pagination("//li[@class='pagination-next page-item']")

        # Click on previous page
        device_management.click_pagination("//li[@class='pagination-prev page-item']")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test device management navigation was completed")