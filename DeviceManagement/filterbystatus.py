from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-helper-f21c1.web.app/")
driver.maximize_window()
driver.find_element_by_xpath("//input[@type='email']").send_keys("admin@gmail.com")
driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.implicitly_wait(20)
driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]').click()
driver.implicitly_wait(20)
driver.find_element_by_xpath("//select[@id='device-status']/option[text()=' Assigned ']").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Assigned']")))
assert driver.find_element_by_xpath("//span[text()='Assigned']").is_displayed(), "Cannot find element"
# driver.quit()