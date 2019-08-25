import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from practice.driver import GetDriver
from practice.asker import *


class LogInFacebook:
    def login_facebook(self, driver):
        driver.implicitly_wait(3)

        parent_handle = driver.current_window_handle

        # Click on LOG IN button from landing page
        driver.find_element(By.CSS_SELECTOR, "li[class='dropdown']").click()

        time.sleep(3)
        # Click on LOG IN WITH FACEBOOK button
        driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-block btn-social btn-facebook metro']").click()

        # Window handling
        handles = driver.window_handles
        driver.switch_to.window(handles[1])

        # Input Facebook account
        email = driver.find_element(By.ID, 'email')
        email.send_keys('honghaijumili206@gmail.com')

        password = driver.find_element(By.ID, 'pass')
        password.send_keys('bienhong206')

        # Click on Log in button
        driver.find_element(By.ID, 'u_0_0').click()

        # Switch back to Excelchat Window
        driver.switch_to.window(parent_handle)

        # Click on SKIP button from Welcome page
        time.sleep(3)
        driver.find_element(By.ID, 'js-introSkip').click()

        # Click on START WORKING button
        driver.refresh()
        driver.find_element(By.CSS_SELECTOR, "a[class='link-item btn']").click()
        time.sleep(3)


class Claim:
    def claim(self, driver, posted_question):
        driver.implicitly_wait(3)

        # Wait until meet a question
        wait = WebDriverWait(driver, 1200, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        claim_button = wait.until(EC.element_to_be_clickable((By.ID, 'claim-button')))
        question_text = driver.find_element(By.CSS_SELECTOR, 'li:nth-child(2) > div.gi-BiddingQuestionInfo-text')

        while question_text.text != posted_question:
            # Click on SKIP button
            driver.find_element(By.ID, 'skip-button').click()
            # Select 1st skip reason
            driver.find_element(By.CSS_SELECTOR, '#skip-reasons > div:nth-child(1) > div').click()
            # Submit skip to be back working screen
            driver.find_element(By.ID, 'confirm-skip-button').click()

            time.sleep(5)

            claim_button = wait.until(EC.element_to_be_clickable((By.ID, 'claim-button')))
            question_text = driver.find_element(By.CSS_SELECTOR, 'li:nth-child(2) > div.gi-BiddingQuestionInfo-text')

        # Click on CLAIM button
        claim_button.click()

        # Click on BID button
        driver.find_element(By.ID, 'confirm-claim-button').click()

        # Wait until get in chat session
        wait.until(EC.element_to_be_clickable((By.ID, 'composer-attach-file-button')))

    def check_message(self, driver, sent_message):
        messages_list = driver.find_elements(By.CSS_SELECTOR, "li[class='ex-message'] > div[class='chat-message']")
        for message in messages_list:
            # print(message.text)
            if message.text == sent_message:
                return True
        return False


if __name__ == "__main__":
    _driver = GetDriver().get_driver()

    # Expert log in and go to Working screen
    LogInFacebook().login_facebook(_driver)

    # Asker logs in using API
    url = 'https://api.got-it.io/'
    headers = {
        'Origin': 'https://www.got-it.io',
        'X-GotIt-Product': 'excelchat',
        'Content-Type': 'application/json',
        'X-GotIt-Site': 'excelchat',
        'X-GotIt-Vertical': 'excel'
    }
    access_token = LogIn(url + 'log-in/asker/email', headers).log_in_API()

    # Asker posts question using API
    headers_post = headers.copy()
    headers_post.pop('Content-Type')
    headers_post.update({'Authorization': 'Bearer ' + access_token})
    post_question = PostQuestion(url + 'askers/me/problems', headers_post)
    problem_id = post_question.post_question_API()

    # Expert claims question
    claim_question = Claim()
    claim_question.claim(_driver, post_question.data_post['text'])
    time.sleep(10)

    # Asker sends message using API
    send_message_API = SendMessage(url + 'askers/me/explanation_messages', headers_post)
    send_message_API.data_send.update({'explanation_id': problem_id})
    send_message_API.send_message_API()

    # Check if expert saw asker's message
    result_send_mesasge = claim_question.check_message(_driver, send_message_API.data_send['message'])
    if result_send_mesasge:
        print("Expert has seen asker's message correctly")
    else:
        print("Expert does not see asker's message sent by API")
    time.sleep(5)
