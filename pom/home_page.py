import time

from selenium.webdriver.common.by import By

from driver import Driver


class HomePage:
    def __init__(self, driver):
        self.driver = Driver(driver)
        self.skip_welcome_btn_id = 'js-introSkip'

        self.start_working_btn_css = ".expert-home-right .link-item"

    def start_working(self):
        # Click on SKIP button from Welcome page
        self.driver.wait_then_click_element(By.ID, self.skip_welcome_btn_id)

        # Click on START WORKING button
        self.driver.wait_then_click_element(By.CSS_SELECTOR, self.start_working_btn_css)