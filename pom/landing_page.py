import time

from selenium.webdriver.common.by import By

from driver import Driver


class LandingPage:
    def __init__(self, driver):
        self.driver = Driver(driver)

        self.login_landing_btn_css = "#navbar .navbar-btn"
        self.login_with_fb_btn_css = "#navbar .btn-facebook"

    def login_facebook(self):
        parent_handle = self.driver.get_current_window_handle()

        # Click on LOG IN button from landing page
        self.driver.wait_then_click_element(By.CSS_SELECTOR, self.login_landing_btn_css)

        # Click on LOG IN WITH FACEBOOK button
        time.sleep(1)
        self.driver.wait_then_click_element(By.CSS_SELECTOR, self.login_with_fb_btn_css)
        return parent_handle
