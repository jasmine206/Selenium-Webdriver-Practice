import time

from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumpractice.driver import Driver
from seleniumpractice.config import Config
from _base.browser import *


# Thu remove time sleep  va dung implicitwait
class ExpertPortal:
    def __init__(self):
        self.driver = Driver(get_chrome_browser(Config.EXPERT_BASE_URL))

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

        time.sleep(3)
        # Click on LOG IN WITH FACEBOOK button
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

        # time.sleep(3)
        # Click on SKIP button from Welcome page
        self.driver.wait_then_click_element(By.ID, self.skip_welcome_btn_id)

    def start_working(self):
        # time.sleep(3)
        # Click on START WORKING button
        self.driver.wait_then_click_element(By.CSS_SELECTOR, self.start_working_btn_css)

    def skip_question(self):
        # time.sleep(3)
        # Click on SKIP button
        self.driver.wait_then_click_element(By.ID, self.skip_btn_id)
        # Select 1st skip reason
        self.driver.wait_then_click_element(By.CSS_SELECTOR, self.first_skip_reason_radio_css)
        # Submit skip to be back working screen
        # time.sleep(3)
        self.driver.wait_then_click_element(By.ID, self.submit_skip_btn_id)
        # time.sleep(3)

    def claim_question(self):
        # Click on CLAIM button
        self.driver.wait_then_click_element(By.ID, self.claim_btn_id)

        # time.sleep(3)
        # Click on BID button
        self.driver.wait_then_click_element(By.ID, self.bid_btn_id)

    def wait_to_claim_question_by_title(self, posted_question):
        # self.driver.is_element_clickable(By.ID, self.claim_btn_id)
        # question = self.driver.get_element(By.CSS_SELECTOR, self.question_text_css)
        question = self.driver.wait_until_visibility_of_element_located(By.CSS_SELECTOR, self.question_text_css)

        while question.text != posted_question:
            print("I'm in while loop")
            self.skip_question()
            time.sleep(5)
            # self.driver.is_element_clickable(By.ID, self.claim_btn_id)
            question = self.driver.wait_until_visibility_of_element_located(
                By.CSS_SELECTOR, self.question_text_css, timeout=30
            )
        print("I'm out of while loop")
        self.claim_question()
        # # verify to see bidding screen
        # # Wait until meet a question
        # wait = WebDriverWait(self.driver, 100, poll_frequency=1)  # 100s
        # wait.until(EC.element_to_be_clickable((By.ID, self.claim_btn_id)))
        # question = self.driver.find_element(By.CSS_SELECTOR, self.question_text_css)
        #
        # # dung do-while instead
        # while True:
        #     # custom find_element: check visible -> check clickable
        #     wait = WebDriverWait(self.driver, 100, poll_frequency=1)  # 100s
        #     wait.until(EC.element_to_be_clickable((By.ID, self.claim_btn_id)))
        #     question = self.driver.find_element(By.CSS_SELECTOR, self.question_text_css)
        #     if question.text != posted_question:
        #         self.skip_question()
        #         # time.sleep(5)
        #         break
        #     self.claim_question()

        # while question.text != posted_question:
        #     self.skip_question()
        #     # time.sleep(5)
        #     # custom find_element: check visible -> check clickable
        #     wait.until(EC.element_to_be_clickable((By.ID, self.claim_btn_id)))
        #     question = self.driver.find_element(By.CSS_SELECTOR, self.question_text_css)
        #
        # # Wait until get in chat session
        # wait.until(EC.element_to_be_clickable((By.ID, self.chat_field_id)))

    def is_in_session(self):
        return self.driver.is_element_clickable(By.ID, self.chat_field_id)

    def is_received_message(self, sent_message):
        # time.sleep(3)
        # wait = WebDriverWait(self.driver, 15, poll_frequency=1)
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.messages_list_css)))
        self.driver.is_element_visible(By.CSS_SELECTOR, self.messages_list_css)
        messages_list = self.driver.wait_until_visibility_of_elements_located(By.CSS_SELECTOR, self.messages_list_css)
        len_msg_list = len(messages_list)
        if messages_list[len_msg_list - 1].text == sent_message:
            return True
        else:
            return False
