import time

from selenium.webdriver.common.by import By

from pom.expert_base import ExpertBase


class BiddingScreen(ExpertBase):
    question_text_css = '.gi-BiddingQuestion li:nth-child(2) .gi-BiddingQuestionInfo-text'
    skip_btn_id = 'skip-button'
    first_skip_reason_radio_css = '#skip-reasons div:nth-child(1) .gi-InputCustom--radio'
    submit_skip_btn_id = 'confirm-skip-button'

    claim_btn_id = 'claim-button'
    bid_btn_id = 'confirm-claim-button'

    def skip_question(self):
        self.driver.wait_then_click_element(self.skip_btn_id)
        self.driver.wait_then_click_element(self.first_skip_reason_radio_css, By.CSS_SELECTOR)
        self.driver.wait_then_click_element(self.submit_skip_btn_id)

    def claim_question(self):
        self.driver.wait_then_click_element(self.claim_btn_id)
        self.driver.wait_then_click_element(self.bid_btn_id)

    def wait_to_claim_question_by_title(self, posted_question):
        while True:
            question = self.driver.wait_until_visibility_of_element_located(
                self.question_text_css, By.CSS_SELECTOR, timeout=30
            )

            if question.text != posted_question:
                self.skip_question()
                time.sleep(5)
            else:
                break

        self.claim_question()
