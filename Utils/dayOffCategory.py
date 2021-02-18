from Pages.dayOffManagementPage import DayOffManagementPage

class DayOffCategory():

    def __init__(self, driver):
        self.driver = driver

    def filter_list(self):
        filter = DayOffManagementPage(self.driver)
        filter.select_day_off_category("VACATION")
        filter.select_day_off_category("ILLNESS")
        filter.select_day_off_category("MATERNITY")
        filter.select_day_off_category("SOMETHING")