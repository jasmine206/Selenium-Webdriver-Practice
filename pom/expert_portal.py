import time

from selenium.webdriver.common.by import By

from driver import Driver


# Thu remove time sleep  va dung implicitwait
class ExpertPortal:
    def __init__(self, driver):
        self.driver = Driver(driver)

        self.login_landing_btn_css = "#navbar .navbar-btn"
        self.login_with_fb_btn_css = "#navbar .btn-facebook"
        self.email_id = 'email'
        self.password_id = 'pass'
        self.login_fb_btn_id = 'u_0_0'

        self.skip_welcome_btn_id = 'js-introSkip'

        self.start_working_btn_css = ".expert-home-right .link-item"

        self.question_text_css = '.gi-BiddingQuestion li:nth-child(2) .gi-BiddingQuestionInfo-text'
        self.skip_btn_id = 'skip-button'
        self.first_skip_reason_radio_css = '#skip-reasons div:nth-child(1) .gi-InputCustom--radio'
        self.submit_skip_btn_id = 'confirm-skip-button'

        self.claim_btn_id = 'claim-button'
        self.bid_btn_id = 'confirm-claim-button'
        self.ask_for_a_file_btn_id = 'ask-for-a-file-button'
        self.chat_field_id = 'composer-attach-file-button'
        self.messages_list_css = ".Pane.vertical.Pane1 .chat-message"

    def login_facebook(self, email, password):
        parent_handle = self.driver.get_current_window_handle()

        # Click on LOG IN button from landing page
        self.driver.wait_then_click_element(By.CSS_SELECTOR, self.login_landing_btn_css)

        # Click on LOG IN WITH FACEBOOK button
        time.sleep(0.5)
        self.driver.wait_then_click_element(By.CSS_SELECTOR, self.login_with_fb_btn_css)

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

        # Click on SKIP button from Welcome page
        self.driver.wait_then_click_element(By.ID, self.skip_welcome_btn_id)

    def start_working(self):
        # Click on START WORKING button
        self.driver.wait_then_click_element(By.CSS_SELECTOR, self.start_working_btn_css)

    def skip_question(self):
        # Click on SKIP button
        self.driver.wait_then_click_element(By.ID, self.skip_btn_id)
        # Select 1st skip reason
        self.driver.wait_then_click_element(By.CSS_SELECTOR, self.first_skip_reason_radio_css)
        # Submit skip to be back working screen
        self.driver.wait_then_click_element(By.ID, self.submit_skip_btn_id)

    def claim_question(self):
        # Click on CLAIM button
        self.driver.wait_then_click_element(By.ID, self.claim_btn_id)

        # Click on BID button
        self.driver.wait_then_click_element(By.ID, self.bid_btn_id)

    def wait_to_claim_question_by_title(self, posted_question):
        while True:
            question = self.driver.wait_until_visibility_of_element_located(
                By.CSS_SELECTOR, self.question_text_css, timeout=30
            )

            if question.text != posted_question:
                self.skip_question()
                time.sleep(5)
            else:
                break

        self.claim_question()

    def is_in_session(self):
        return self.driver.is_element_clickable(By.ID, self.chat_field_id, timeout=60)

    def is_received_message(self, sent_message):
        self.driver.is_element_visible(By.CSS_SELECTOR, self.messages_list_css)
        messages_list = self.driver.wait_until_visibility_of_elements_located(By.CSS_SELECTOR, self.messages_list_css)
        len_msg_list = len(messages_list)
        if messages_list[len_msg_list - 1].text == sent_message:
            return True
        else:
            return False
