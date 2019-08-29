import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from practice_2.driver import GetDriver
from practice_2.config import Config


class ExpertPortal:
    def __init__(self):
        self.driver = GetDriver().get_driver(Config.EXPERT_BASE_URL)

    def login_facebook(self, email, password):
        parent_handle = self.driver.current_window_handle

        # Click on LOG IN button from landing page
        self.driver.find_element(By.CSS_SELECTOR, Config.LOGIN_LANDING_BTN_CSS).click()

        time.sleep(3)
        # Click on LOG IN WITH FACEBOOK button
        self.driver.find_element(By.CSS_SELECTOR, Config.LOGIN_WITH_FB_BTN_CSS).click()

        # Window handling
        handles = self.driver.window_handles
        for handle in handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                current_url = self.driver.current_url
                expect_url = "https://www.facebook.com"
                if current_url[:len(expect_url)] == expect_url:
                    # Input Facebook account
                    email_field = self.driver.find_element(By.ID, Config.EMAIL_ID)
                    email_field.send_keys(email)
                    password_field = self.driver.find_element(By.ID, Config.PASSWORD_ID)
                    password_field.send_keys(password)
                    break

        # Click on Log in button
        self.driver.find_element(By.ID, Config.LOGIN_FB_BTN_ID).click()
        # Switch back to Excelchat Window
        self.driver.switch_to.window(parent_handle)

        time.sleep(3)
        # Click on SKIP button from Welcome page
        self.driver.find_element(By.ID, Config.SKIP_WELCOME_BTN_ID).click()

    def start_working(self):
        time.sleep(3)
        # Click on START WORKING button
        self.driver.find_element(By.CSS_SELECTOR, Config.START_WORKING_BTN_CSS).click()

    def skip_question(self):
        time.sleep(3)
        # Click on SKIP button
        self.driver.find_element(By.ID, Config.SKIP_BTN_ID).click()
        # Select 1st skip reason
        self.driver.find_element(By.CSS_SELECTOR, Config.FIRST_SKIP_REASON_RADIO_CSS).click()
        # Submit skip to be back working screen
        time.sleep(3)
        self.driver.find_element(By.ID, Config.SUBMIT_SKIP_BTN_ID).click()
        time.sleep(3)

    def claim_question(self):
        # Click on CLAIM button
        self.driver.find_element(By.ID, Config.CLAIM_BTN_ID).click()

        time.sleep(3)
        # Click on BID button
        self.driver.find_element(By.ID, Config.BID_BTN_ID).click()

    def wait_to_claim_question_by_title(self, posted_question):
        # verify to see bidding screen
        # Wait until meet a question
        wait = WebDriverWait(self.driver, 100, poll_frequency=1)
        wait.until(EC.element_to_be_clickable((By.ID, Config.CLAIM_BTN_ID)))
        question = self.driver.find_element(By.CSS_SELECTOR, Config.QUESTION_TEXT_CSS)

        while question.text != posted_question:
            self.skip_question()
            time.sleep(5)
            wait.until(EC.element_to_be_clickable((By.ID, Config.CLAIM_BTN_ID)))
            question = self.driver.find_element(By.CSS_SELECTOR, Config.QUESTION_TEXT_CSS)
        self.claim_question()

        # Wait until get in chat session
        # wait.until(EC.element_to_be_clickable((By.ID, Config.CHAT_FIELD_ID)))

    def check_be_in_session(self):
        time.sleep(30)
        chat_field = self.driver.find_element(By.ID, Config.CHAT_FIELD_ID)
        if chat_field is not None:
            return True
        else:
            return False

    def check_message(self, sent_message):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 15, poll_frequency=1)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Config.MESSAGES_LIST_CSS)))
        messages_list = self.driver.find_elements(By.CSS_SELECTOR, Config.MESSAGES_LIST_CSS)
        len_msg_list = len(messages_list)
        if messages_list[len_msg_list-1].text == sent_message:
            return True
        else:
            return False


