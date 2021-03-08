from selenium import webdriver
import unittest
import time
from Pages.loginPage import LoginPage
from Pages.time_off_form import TimeOffForm

class editTimeOff(unittest.TestCase):

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

    def test_edit_request_time_off_01(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[4]').click()
        time_off_form = TimeOffForm(driver)

        driver.find_element_by_xpath(time_off_form.time_off_form_path).click()
        time_off_form.enter_from_date("05032021")
        time_off_form.enter_to_date("09032021")
        time_off_form.click_save()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test edit time off function was completed")