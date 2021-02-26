from Pages.dayOffManagementPage import DayOffManagementPage
from Pages.createDevicePage import DeviceManagemntPage

class Filter():

    def __init__(self, driver):
        self.driver = driver

    def day_off_cateogory(self):
        day_off_category = DayOffManagementPage(self.driver)
        day_off_category.select_day_off_category("VACATION")
        day_off_category.select_day_off_category("ILLNESS")
        day_off_category.select_day_off_category("MATERNITY")
        day_off_category.select_day_off_category("SOMETHING")
    def device_status(self):
        device_status = DeviceManagemntPage(self.driver)
        device_status.select_device_category("ASSIGNED")
        device_status.select_device_category("DISCARDED")
        device_status.select_device_category("IN_INVENTORY")

