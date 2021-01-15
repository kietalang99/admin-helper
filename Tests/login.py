from selenium import webdriver
import unittest
import time

class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Admin/PycharmProjects/admin/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get("https://admin-helper-f21c1.web.app/login")
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys("admin@gmail.com")
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")
