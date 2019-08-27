import os

from selenium import webdriver


class GetDriver:
    def get_driver(self):
        driver_chrome_location = "../libs/chromedriver"
        os.environ["webdriver.chrome.driver"] = driver_chrome_location
        driver = webdriver.Chrome(driver_chrome_location)
        baseUrl = "https://expert-excel.got-it.io/"
        driver.get(baseUrl)
        return driver
