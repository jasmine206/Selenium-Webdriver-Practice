import json
import time
import os

import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class Working:
    def login_facebook(self, driver):
        driver.implicitly_wait(3)

        parent_handle = driver.current_window_handle

        # Click on LOG IN button from landing page
        driver.find_element(By.XPATH, '//*[@id="navbar"]/ul/li/a').click()

        time.sleep(3)
        # Click on LOG IN WITH FACEBOOK button
        driver.find_element(By.XPATH, '//*[@id="navbar"]/ul/li/div/div/span/button').click()

        # Window handling
        handles = driver.window_handles

        for handle in handles:
            if handle not in parent_handle:
                # Switch to Facebook window
                driver.switch_to.window(handle)
                email = driver.find_element(By.ID, 'email')
                email.send_keys('honghaijumili206@gmail.com')

                password = driver.find_element(By.ID, 'pass')
                password.send_keys('bienhong206')

                # Click on Log in button
                driver.find_element(By.ID, 'u_0_0').click()

        # Switch back to Excelchat Window
        driver.switch_to.window(parent_handle)

        # Click on SKIP button from Welcome page
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="js-introSkip"]').click()

        # Click on START WORKING button
        time.sleep(5)
        driver.refresh()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div/div/div[2]/div/a').click()
        time.sleep(10)

    def claim(self, driver):
        self.login_facebook(driver)
        driver.implicitly_wait(3)

        # Post a question use API
        post_question_API()

        # Wait until meet a question
        wait = WebDriverWait(driver, 1200, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        claim_button = wait.until(EC.element_to_be_clickable((By.ID, 'claim-button')))
        claim_button.click()

        # Click on BID button
        driver.find_element(By.ID, 'confirm-claim-button').click()


def get_driver():
    driver_chrome_location = "/Users/gotit/Downloads/chromedriver"
    os.environ["webdriver.chrome.driver"] = driver_chrome_location
    driver = webdriver.Chrome(driver_chrome_location)
    baseUrl = "https://expert-excel.got-it.io/"
    driver.get(baseUrl)
    return driver


def log_in_API():
    url_login = 'https://api.got-it.io/log-in/asker/email'
    headers_login = {
        'Origin': 'https://www.got-it.io',
        'X-GotIt-Product': 'excelchat',
        'Content-Type': 'application/json',
        'X-GotIt-Site': 'excelchat',
        'X-GotIt-Vertical': 'excel'
    }
    data_login = {
        "has_accepted_privacy_policy": False,
        "has_allowed_email": False,
        "is_e_u": False,
        "email": "jasmine@gotitapp.co",
        "password": "1234Aa",
        "utm_meta": {
            "utm_source": "https://www.got-it.io/solutions/excel-chat/",
            "utm_medium": None,
            "utm_term": None,
            "utm_content": None
        }
    }

    response = requests.post(url_login, headers=headers_login, data=json.dumps(data_login))
    response_data = response.json()
    return response_data['data']['access_token']


def post_question_API():
    # Log in first
    access_token = log_in_API()

    # Then post question
    url_post = 'https://api.got-it.io/askers/me/problems'
    headers_post = {
        'Origin': 'https://www.got-it.io',
        'X-GotIt-Product': 'excelchat',
        'X-GotIt-Site': 'excelchat',
        'X-GotIt-Vertical': 'excel'
    }
    headers_post.update({'Authorization': 'Bearer ' + access_token})
    data_post = {
        'topic_id': -1000,
        'text': '[Jasmine] I need a formula to combine column C with the numbers in columns L10 to L20'
    }

    requests.post(url_post, headers=headers_post, data=data_post)


if __name__ == "__main__":
    _driver = get_driver()
    test = Working()
    test.claim(_driver)
