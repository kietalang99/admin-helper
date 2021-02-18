from selenium import webdriver
import unittest
import time
from Pages.loginPage import LoginPage


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

    def test_navigation_01(self):
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath("//li[@class='pagination-last page-item']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//li[@class='pagination-first page-item']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//li[@class='pagination-next page-item']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//li[@class='pagination-prev page-item']").click()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test device management navigation was completed")