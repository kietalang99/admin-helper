from selenium import webdriver
import unittest
from Pages.loginPage import LoginPage
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
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[4]').click()
        row_data = self.driver.find_elements_by_xpath("//table/tbody/tr/td[1]")
        self.driver.find_element_by_xpath("//table/thead/tr/th[text()=' Name ']").click()
        time.sleep(5)
        print("Table before sort clicked: ")
        for row in row_data:
             print(row.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
