import os

from behave import fixture
from selenium import webdriver


@fixture
def get_chrome_browser(context):
    # Setup browser
    driver_chrome_location = "../Selenium-Webdriver-Practice/libs/chromedriver"
    os.environ["webdriver.chrome.driver"] = driver_chrome_location
    context.browser = webdriver.Chrome(driver_chrome_location)
    context.browser.implicitly_wait(5)

    yield context.browser

    # Teardown
    context.browser.close()
