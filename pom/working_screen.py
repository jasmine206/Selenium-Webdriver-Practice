from selenium.webdriver.common.by import By

from driver import Driver


class WorkingScreen:
    def __init__(self, driver):
        self.driver = Driver(driver)

        self.chat_field_id = 'composer-attach-file-button'

    def is_in_session(self):
        return self.driver.is_element_clickable(By.ID, self.chat_field_id, timeout=60)
