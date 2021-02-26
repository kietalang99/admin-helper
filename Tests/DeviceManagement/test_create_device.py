from selenium import webdriver
import unittest
import time
from Pages.loginPage import LoginPage
from Pages.createDevicePage import CreateDevicePage

class testcreateDevice(unittest.TestCase):

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

    # Create device successful with valid data
    def test_create_device_01(self):
        driver = self.driver
        # Go to Device Management page
        driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a').click()

        # Get create device from the other file
        create_device_form = CreateDevicePage(driver)
        create_device_form.click_create_device()
        create_device_form.enter_device_name("Mac Pro")
        create_device_form.enter_price("30000000")
        create_device_form.select_device_category("1")
        create_device_form.enter_device_description("This is laptop for company")
        create_device_form.click_save()

        check = driver.find_element_by_xpath("//div[@class='card-header']/div/div[contains(.,'Mac Pro')]").is_displayed()
        self.assertEquals(True, check)
        time.sleep(3)

    # Button save disabled if user just click save button
    def test_create_device_02(self):
        driver = self.driver
        # Go to Device Management page
        driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a').click()
        # Get create device from the other file
        create_device_form = CreateDevicePage(driver)
        create_device_form.click_save()
        # Check save button disabled when leave name/price blank
        check = driver.find_element_by_xpath(create_device_form.btn_save_path).is_enabled()
        self.assertEquals(False, check)
        time.sleep(2)

    # Error message displayed when input wrong format
    def test_create_device_03(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a').click()
        create_device_form = CreateDevicePage(driver)
        create_device_form.click_create_device()

        # Error message display when enter space name
        create_device_form.enter_device_name("  ")
        driver.find_element_by_xpath(create_device_form.description_textarea_path).click()
        check = driver.find_element_by_xpath("//div[text()=' Device name is required. ']").is_displayed()
        self.assertEquals(True, check)
        time.sleep(2)

        # Error message display when enter name only 1 charater
        create_device_form.enter_device_name("a")
        driver.find_element_by_xpath(create_device_form.description_textarea_path).click()
        check = driver.find_element_by_xpath("//div[text()=' Description must be at least 2 characters ']").is_displayed()
        self.assertEquals(True, check)
        time.sleep(2)

        # Error message display when enter name more than 40 charaters
        create_device_form.enter_device_name("alangthikietalangthikietalangthikietalangthikiet")
        driver.find_element_by_xpath(create_device_form.description_textarea_path).click()
        check = driver.find_element_by_xpath("//div[text()=' Device name must not exceed 40 characters. ']").is_displayed()
        self.assertEquals(True, check)
        time.sleep(2)

        # Error message displayed when leaving price 0d
        driver.find_element_by_xpath(create_device_form.price_textbox_path).click()
        driver.find_element_by_xpath(create_device_form.description_textarea_path).click()
        check = driver.find_element_by_xpath("//div[text()=' Price is required. ']").is_displayed()
        self.assertEquals(True, check)
        time.sleep(2)

        # Error message displayed when leaving price 0d
        create_device_form.enter_price("0")
        driver.find_element_by_xpath(create_device_form.description_textarea_path).click()
        check = driver.find_element_by_xpath("//div[text()=' Price must be at least 1d ']").is_displayed()
        self.assertEquals(True, check)
        time.sleep(2)

        # Error message displayed when leaving price 0d
        create_device_form.enter_price("8264328783698324732499")
        driver.find_element_by_xpath(create_device_form.description_textarea_path).click()
        check = driver.find_element_by_xpath("//div[text()=' Price must be a positive number ']").is_displayed()
        self.assertEquals(True, check)
        time.sleep(2)

    # Create device form closed after click on Close button
    def test_create_device_04(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a').click()
        create_device_form = CreateDevicePage(driver)
        create_device_form.click_create_device()
        time.sleep(3)
        create_device_form.click_close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test create device completed")