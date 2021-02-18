from selenium import webdriver
import unittest
from Pages.loginPage import LoginPage
from Pages.dayOffManagementPage import DayOffManagementPage
from Utils.dayOffCategory import DayOffCategory

class filterDayOffManagement(unittest.TestCase):

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

    def test_filter_01(self):
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[4]').click()
        selection = DayOffCategory(self.driver)
        selection.filter_list()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test filter function was completed")
