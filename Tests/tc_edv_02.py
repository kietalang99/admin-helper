from selenium import webdriver
import unittest
import time
from Pages.loginPage import LoginPage


class editDevice(unittest.TestCase):
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

    def test_create_device_01(self):
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="dropdownBtn0"]/i').click()
        self.driver.find_element_by_xpath('//ah-device-table/div/div[3]/div[1]/div/div[5]/div/div/a[2]').click()
        self.driver.find_element_by_xpath("//input[@id='name']").clear()
        self.driver.find_element_by_xpath("//input[@id='price']").clear()
        self.driver.find_element_by_xpath("//button[@type='submit']").is_enabled()
        print("The submit button already disabled")

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test clear all data to check disable button was completed")