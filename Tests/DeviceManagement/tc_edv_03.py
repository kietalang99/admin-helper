from selenium import webdriver
import unittest
import time
from keyboard import press
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

    def test_edit_device_03(self):
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="dropdownBtn0"]/i').click()
        self.driver.find_element_by_xpath('//ah-device-table/div/div[3]/div[1]/div/div[5]/div/div/a[2]').click()
        self.driver.find_element_by_id("name").clear()
        self.driver.find_element_by_id("name").send_keys("a")
        press("enter")
        self.driver.find_element_by_id("name").clear()
        self.driver.find_element_by_id("name").send_keys("laptoplaptoplaptoplaptoplaptoplaptoplaptoplaptop")
        press("enter")
        self.driver.find_element_by_id("price").click()
        self.driver.find_element_by_id("price").send_keys("0")
        press("enter")
        self.driver.find_element_by_id("price").clear()
        self.driver.find_element_by_id("price").send_keys("1234567891234567891234")
        press("enter")

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test error message displayed when enter wrong format name and price was completed")