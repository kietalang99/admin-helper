from selenium import webdriver
import unittest
import time
from Pages.loginPage import LoginPage
from Pages.dayOffManagementPage import DayOffManagementPage

class searchDayOffList(unittest.TestCase):

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

    def test_search(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[4]').click()
        driver.implicitly_wait(2)
        search = DayOffManagementPage(driver)

        # Search by name
        search.enter_search_key("admin")

        # Search by year
        search.enter_search_key("2000")

        # Search by full name
        search.enter_search_key("user admin")

        # Search with blank space
        search.enter_search_key(" ")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test search function was completed")
