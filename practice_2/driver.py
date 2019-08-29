import os

from selenium import webdriver


class GetDriver:
    # @staticmethod
    def get_driver(self, base_url):
        driver_chrome_location = "../libs/chromedriver"
        os.environ["webdriver.chrome.driver"] = driver_chrome_location
        driver = webdriver.Chrome(driver_chrome_location)
        driver.get(base_url)
        return driver
