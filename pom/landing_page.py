import time

from selenium.webdriver.common.by import By

from pom.expert_base import ExpertBase


class LandingPage(ExpertBase):
    login_landing_btn_css = "#navbar .navbar-btn"
    login_with_fb_btn_css = "#navbar .btn-facebook"

    def click_login_facebook(self):
        parent_handle = self.driver.get_current_window_handle()
        self.driver.wait_then_click_element(self.login_landing_btn_css, By.CSS_SELECTOR)

        time.sleep(1)
        self.driver.wait_then_click_element(self.login_with_fb_btn_css, By.CSS_SELECTOR, )
        return parent_handle
