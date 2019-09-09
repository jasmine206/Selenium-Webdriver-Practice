import os
from selenium import webdriver


class SeleniumDriver:
    def get_chrome_browser(self):
        driver_chrome_location = "../Selenium-Webdriver-Practice/libs/chromedriver"
        os.environ["webdriver.chrome.driver"] = driver_chrome_location
        driver = webdriver.Chrome(driver_chrome_location)
        driver.implicitly_wait(5)
        return driver
