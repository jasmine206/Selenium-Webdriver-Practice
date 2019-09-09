import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverAPI:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator, locator_type=By.ID):
        element = None
        try:
            element = self.driver.find_element(locator_type, locator)
        except:
            print("Element not found")
        return element

    def get_elements(self, locator_type, locator):
        elements = None
        try:
            locator_type = locator_type.lower()
            elements = self.driver.find_elements(locator_type, locator)
        except:
            print("Element not found")
        return elements

    def wait_until_visibility_of_element_located(self, locator, locator_type=By.ID, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            EC.visibility_of_element_located((locator_type, locator))
        )

    def wait_until_visibility_of_elements_located(self, locator, locator_type=By.ID, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            EC.visibility_of_any_elements_located((locator_type, locator))
        )

    def wait_until_element_to_be_clickable(self, locator, locator_type=By.ID, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            EC.element_to_be_clickable((locator_type, locator))
        )

    def wait_then_click_element(self, locator, locator_type=By.ID, timeout=10):
        self.wait_until_visibility_of_element_located(locator, locator_type, timeout)
        self.wait_until_element_to_be_clickable(locator, locator_type, timeout).click()

    def is_element_clickable(self, locator, locator_type=By.ID, timeout=10):
        try:
            element = self.wait_until_element_to_be_clickable(locator, locator_type, timeout)
            if element is not None:
                return True
            else:
                return False
        except:
            return False

    def is_element_visible(self, locator, locator_type=By.ID, timeout=10):
        try:
            element = self.wait_until_visibility_of_element_located(locator, locator_type, timeout)
            if element is not None:
                return True
            else:
                return False
        except:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_windows_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    def take_screenshot(self, step, scenario, screen_directory):
        file_name = str(round(time.time())) + "_" + str(scenario) + "_" + str(step) + ".png"
        destination_file = screen_directory + file_name

        try:
            self.driver.save_screenshot(destination_file)
        except NotADirectoryError:
            print("Something went wrong")



