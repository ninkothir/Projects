from selenium.webdriver.common.by import By


class OverviewPage:

    def __init__(self, driver):
        self.driver = driver

    total_price = (By.CLASS_NAME, "summary_total_label")

    def get_total_price(self):
        return self.driver.find_element(*self.total_price).text