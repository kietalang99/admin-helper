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

    def test_edit_device_01(self):
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a').click()
        
        time.sleep(2)

        self.driver.find_element_by_xpath('//*[@id="dropdownBtn1"]/i').click()
        self.driver.find_element_by_xpath("//div/div/a[4]").click()
        self.driver.find_element_by_xpath("//input[@id='name']").clear()
        self.driver.find_element_by_xpath("//input[@id='name']").send_keys("Samsung galaxy A28")
        self.driver.find_element_by_xpath("//input[@id='price']").clear()
        self.driver.find_element_by_xpath("//input[@id='price']").send_keys("10000000")
        self.driver.find_element_by_xpath("//select[@id='device-category']/option[text()=' Phone ']").click()
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test create device completed")