import time

from selenium.webdriver.common.by import By

from driver import Driver


class BiddingScreen:
    def __init__(self, driver):
        self.driver = Driver(driver)
        self.question_text_css = '.gi-BiddingQuestion li:nth-child(2) .gi-BiddingQuestionInfo-text'
        self.skip_btn_id = 'skip-button'
        self.first_skip_reason_radio_css = '#skip-reasons div:nth-child(1) .gi-InputCustom--radio'
        self.submit_skip_btn_id = 'confirm-skip-button'

        self.claim_btn_id = 'claim-button'
        self.bid_btn_id = 'confirm-claim-button'

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
