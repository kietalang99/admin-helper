from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Pages.loginPage import LoginPage

class createDevice(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Drivers/chromedriver.exe")
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
        self.driver.find_element_by_xpath("//input[@id='name']").send_keys("laptoplaptoplaptoplaptopl"
                                                                           "aptoplaptoplaptoplaptop")
        self.driver.find_element_by_xpath("//input[@id='price']").click()
        self.driver.find_element_by_xpath("//div[text()=' Device name must not exceed 40 characters. ']").is_displayed()
        print("'Device name must not exceed 40 characters' displayed")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test error message display when enter more than 21 characters in device name completed")
