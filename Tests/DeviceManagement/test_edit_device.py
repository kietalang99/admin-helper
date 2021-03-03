from selenium import webdriver
import unittest
import time
from Pages.loginPage import LoginPage
from Pages.deviceMangementPage import DeviceManagementPage
from Pages.createDevicePage import CreateDevicePage

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

    # Edit device successful with valid data
    def test_edit_device_01(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a').click()
        edit_device = DeviceManagementPage(driver)
        edit_device.click_action()
        edit_device.click_edit()
        form = CreateDevicePage(driver)
        form.enter_device_name("Dell Precision 7540")
        form.enter_price("5000000")
        form.click_save()

        check = driver.find_element_by_xpath(
            "//div[@class='card-header']/div/div[contains(.,'Dell Precision 7540')]").is_displayed()
        self.assertEquals(True, check)
        time.sleep(3)

    # Disable save button after clear Name/price field
    def test_edit_device_02(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a').click()

        edit_device = DeviceManagementPage(driver)
        edit_device.click_action()
        edit_device.click_edit()

        form = CreateDevicePage(driver)
        driver.find_element_by_xpath(form.device_name_textbox_path).clear()
        driver.find_element_by_xpath(form.price_textbox_path).clear()

        check = driver.find_element_by_xpath(form.btn_save_path).is_enabled()
        self.assertEquals(False, check)

        time.sleep(3)

    # Edit device failed with wrong format
    def test_edit_device_04(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a').click()

        edit_device = DeviceManagementPage(driver)
        edit_device.click_action()
        edit_device.click_edit()

        form = CreateDevicePage(driver)

        # Error message display when enter space name
        form.enter_device_name("  ")
        driver.find_element_by_xpath(form.description_textarea_path).click()
        check = driver.find_element_by_xpath("//div[text()=' Device name is required. ']").is_displayed()
        self.assertEquals(True, check)
        time.sleep(2)

        # Error message display when enter name only 1 charater
        form.enter_device_name("a")
        driver.find_element_by_xpath(form.description_textarea_path).click()
        check = driver.find_element_by_xpath(
            "//div[text()=' Description must be at least 2 characters ']").is_displayed()
        self.assertEquals(True, check)
        time.sleep(2)

        # Error message display when enter name more than 40 charaters
        form.enter_device_name("alangthikietalangthikietalangthikietalangthikiet")
        driver.find_element_by_xpath(form.description_textarea_path).click()
        check = driver.find_element_by_xpath(
            "//div[text()=' Device name must not exceed 40 characters. ']").is_displayed()
        self.assertEquals(True, check)
        time.sleep(2)

        # Error message displayed when leaving price 0d
        form.enter_price("   ")
        driver.find_element_by_xpath(form.description_textarea_path).click()
        check = driver.find_element_by_xpath("//div[text()=' Price is required. ']").is_displayed()
        self.assertEquals(True, check)
        time.sleep(2)

        # Error message displayed when leaving price 0d
        form.enter_price("0")
        driver.find_element_by_xpath(form.description_textarea_path).click()
        check = driver.find_element_by_xpath("//div[text()=' Price must be at least 1d ']").is_displayed()
        self.assertEquals(True, check)
        time.sleep(2)

        # Error message displayed when leaving price 0d
        form.enter_price("8264328783698324732499")
        driver.find_element_by_xpath(form.description_textarea_path).click()
        check = driver.find_element_by_xpath("//div[text()=' Price must be a positive number ']").is_displayed()
        self.assertEquals(True, check)
        time.sleep(2)

        time.sleep(3)

    # Edit device form closed after click on Close button
    def test_create_device_04(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a').click()
        device_form = CreateDevicePage(driver)
        device_page = DeviceManagementPage(driver)

        device_page.click_action()
        device_page.click_edit()

        device_form.click_close()
        check = driver.find_element_by_xpath("//h4[text()=' Edit Device ']").is_displayed()

        self.assertEquals(False, check)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Edit device completed")