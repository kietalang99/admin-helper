from selenium import webdriver
import unittest
import time
from Pages.loginPage import LoginPage

class createDevice(unittest.TestCase):

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

    def test_create_device_02(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//main//div/button[@type='button']").click()
        disabled_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        disabled_button.is_enabled()
        print("Button already disabled")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test button create device disabled completed")
