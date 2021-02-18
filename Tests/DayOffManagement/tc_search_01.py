from selenium import webdriver
import unittest
import time
from keyboard import press
from Pages.loginPage import LoginPage

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

    def test_search_01(self):
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[4]').click()
        self.driver.find_element_by_id("inlineFormInputGroupUsername").send_keys("admin")
        press("enter")
        time.sleep(4)
        self.driver.find_element_by_id("inlineFormInputGroupUsername").clear()
        self.driver.find_element_by_id("inlineFormInputGroupUsername").send_keys("2000")
        press("enter")
        time.sleep(3)
        self.driver.find_element_by_id("inlineFormInputGroupUsername").clear()
        self.driver.find_element_by_id("inlineFormInputGroupUsername").send_keys("user admin")
        time.sleep(3)
        self.driver.find_element_by_id("inlineFormInputGroupUsername").clear()
        self.driver.find_element_by_id("inlineFormInputGroupUsername").send_keys(" ")
        press("enter")
        time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test search function was completed")
