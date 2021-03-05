from selenium import webdriver
import unittest
from Pages.loginPage import LoginPage
from Pages.dayOffManagementPage import DayOffManagementPage
from selenium.webdriver.support.select import By
import time

class dayOffOrderBySort(unittest.TestCase):

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

    def test_day_off_sort_asc(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[4]').click()

        day_off_management = DayOffManagementPage(driver)

        # Sort name column
        driver.find_element_by_xpath(day_off_management.name_column_path).click()
        time.sleep(2)

        # Sort birthday column
        driver.find_element_by_xpath(day_off_management.birthday_column_path).click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
