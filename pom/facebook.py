from selenium.webdriver.common.by import By

from driver import Driver


class FacebookVerification:
    def __init__(self, driver):
        self.driver = Driver(driver)
        self.email_id = 'email'
        self.password_id = 'pass'
        self.login_fb_btn_id = 'u_0_0'

    def log_in(self, parent_handle, email, password):
        # Window handling
        handles = self.driver.get_windows_handles()
        for handle in handles:
            if handle != parent_handle:
                self.driver.switch_to_window(handle)
                current_url = self.driver.get_current_url()
                expect_url = "https://www.facebook.com"
                if current_url[:len(expect_url)] == expect_url:
                    # Input Facebook account
                    email_field = self.driver.wait_until_visibility_of_element_located(By.ID, self.email_id)
                    email_field.send_keys(email)
                    password_field = self.driver.wait_until_visibility_of_element_located(By.ID, self.password_id)
                    password_field.send_keys(password)
                    break

        # Click on Log in button
        self.driver.wait_then_click_element(By.ID, self.login_fb_btn_id)
        # Switch back to Excelchat Window
        self.driver.switch_to_window(parent_handle)
