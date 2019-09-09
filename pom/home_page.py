from selenium.webdriver.common.by import By

from pom.expert_base import ExpertBase


class HomePage(ExpertBase):
    skip_welcome_btn_id = 'js-introSkip'
    start_working_btn_css = ".expert-home-right .link-item"

    def click_start_working(self):
        # Click on SKIP button from Welcome page
        self.driver.wait_then_click_element(self.skip_welcome_btn_id)

        # Click on START WORKING button
        self.driver.wait_then_click_element(self.start_working_btn_css, By.CSS_SELECTOR)