class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.email_textbox_path = "//input[@type='email']"
        self.password_textbox_path = "//input[@type='password']"
        self.login_button_path = "//button[@type='submit']"

    def enter_email(self, email):
        self.driver.find_element_by_xpath(self.email_textbox_path).clear()
        self.driver.find_element_by_xpath(self.email_textbox_path).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_path).clear()
        self.driver.find_element_by_xpath(self.password_textbox_path).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_path).click()