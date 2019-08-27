import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from practice_2.driver import GetDriver


class ExpertPortal:
    login_landing_btn_css = "#navbar .navbar-btn"
    login_with_fb_btn_css = "#navbar .btn-facebook"
    email_id = 'email'
    password_id = 'pass'
    login_fb_btn_id = 'u_0_0'

    skip_welcome_btn_id = 'js-introSkip'

    start_working_btn_css = ".expert-home-right .link-item"

    question_text_css = '.gi-BiddingQuestion li:nth-child(2) .gi-BiddingQuestionInfo-text'
    skip_btn_id = 'skip-button'
    first_skip_reason_radio_css = '#skip-reasons div:nth-child(1) .gi-InputCustom--radio'
    submit_skip_btn_id = 'confirm-skip-button'

    claim_btn_id = 'claim-button'
    bid_btn_id = 'confirm-claim-button'
    chat_field_id = 'composer-attach-file-button'
    messages_list_css = ".Pane.vertical.Pane1 .chat-message"
    driver = GetDriver().get_driver()

    def login_facebook(self, email, password):
        parent_handle = ExpertPortal.driver.current_window_handle

        # Click on LOG IN button from landing page
        ExpertPortal.driver.find_element(By.CSS_SELECTOR, ExpertPortal.login_landing_btn_css).click()

        time.sleep(3)
        # Click on LOG IN WITH FACEBOOK button
        ExpertPortal.driver.find_element(By.CSS_SELECTOR, ExpertPortal.login_with_fb_btn_css).click()

        # Window handling
        handles = ExpertPortal.driver.window_handles
        for handle in handles:
            if handle != parent_handle:
                ExpertPortal.driver.switch_to.window(handle)
                current_url = ExpertPortal.driver.current_url
                expect_url = "https://www.facebook.com"
                if current_url[:len(expect_url)] == expect_url:
                    # Input Facebook account
                    email_field = ExpertPortal.driver.find_element(By.ID, ExpertPortal.email_id)
                    email_field.send_keys(email)
                    password_field = ExpertPortal.driver.find_element(By.ID, ExpertPortal.password_id)
                    password_field.send_keys(password)

        # Click on Log in button
        ExpertPortal.driver.find_element(By.ID, ExpertPortal.login_fb_btn_id).click()
        # Switch back to Excelchat Window
        ExpertPortal.driver.switch_to.window(parent_handle)

        time.sleep(3)
        # Click on SKIP button from Welcome page
        ExpertPortal.driver.find_element(By.ID, ExpertPortal.skip_welcome_btn_id).click()

    def start_working(self):
        time.sleep(3)
        # Click on START WORKING button
        ExpertPortal.driver.find_element(By.CSS_SELECTOR, ExpertPortal.start_working_btn_css).click()

    def skip_question(self):
        # Click on SKIP button
        ExpertPortal.driver.find_element(By.ID, ExpertPortal.skip_btn_id).click()
        # Select 1st skip reason
        ExpertPortal.driver.find_element(By.CSS_SELECTOR, ExpertPortal.first_skip_reason_radio_css).click()
        # Submit skip to be back working screen
        time.sleep(3)
        ExpertPortal.driver.find_element(By.ID, ExpertPortal.submit_skip_btn_id).click()
        time.sleep(3)

    def claim_question(self):
        # Click on CLAIM button
        ExpertPortal.driver.find_element(By.ID, ExpertPortal.claim_btn_id).click()

        time.sleep(3)
        # Click on BID button
        ExpertPortal.driver.find_element(By.ID, ExpertPortal.bid_btn_id).click()

    def wait_question_by_description(self, posted_question):
        # Wait until meet a question
        wait = WebDriverWait(ExpertPortal.driver, 1200, poll_frequency=1)
        wait.until(EC.element_to_be_clickable((By.ID, ExpertPortal.claim_btn_id)))
        question = ExpertPortal.driver.find_element(By.CSS_SELECTOR, ExpertPortal.question_text_css)

        while question.text != posted_question:
            self.skip_question()
            time.sleep(5)
            wait.until(EC.element_to_be_clickable((By.ID, ExpertPortal.claim_btn_id)))
            time.sleep(3)
        self.claim_question()

        # Wait until get in chat session
        wait.until(EC.element_to_be_clickable((By.ID, ExpertPortal.chat_field_id)))

    def check_message(self, sent_message):
        wait = WebDriverWait(ExpertPortal.driver, 10, poll_frequency=1)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ExpertPortal.messages_list_css)))
        messages_list = ExpertPortal.driver.find_elements(By.CSS_SELECTOR, ExpertPortal.messages_list_css)
        len_msg_list = len(messages_list)
        assert (messages_list[len_msg_list-1].text == sent_message), "Expert has not seen asker's API message"
        return "Expert has seen asker's API message"


