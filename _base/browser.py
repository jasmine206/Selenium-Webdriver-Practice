import os

from selenium import webdriver


def get_chrome_browser(base_url):
    driver_chrome_location = "/Users/gotit/Selenium-Webdriver-Practice/libs/chromedriver"
    os.environ["webdriver.chrome.driver"] = driver_chrome_location
    driver = webdriver.Chrome(driver_chrome_location)
    driver.get(base_url)
    driver.implicitly_wait(3)
    return driver
