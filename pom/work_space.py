from selenium.webdriver.common.by import By

from driver import Driver


class WorkSpace:
    def __init__(self, driver):
        self.driver = Driver(driver)

        self.messages_list_css = ".chat-message"
        self.message_image_css = ".message-photo img[src='/images/icons/placeholder.svg']"
        self.message_excel_file_css = ".message-photo img[src='/images/samples/6.jpg']"

    def is_received_text_message(self, sent_message):
        self.driver.is_element_visible(By.CSS_SELECTOR, self.messages_list_css, timeout=15)
        messages_list = self.driver.wait_until_visibility_of_elements_located(By.CSS_SELECTOR, self.messages_list_css)
        len_msg_list = len(messages_list)
        if messages_list[len_msg_list - 1].text == sent_message:
            return True
        else:
            return False

    def is_received_image_message(self):
        return self.driver.is_element_visible(By.CSS_SELECTOR, self.message_image_css, timeout=15)

    def is_received_excel_file_message(self):
        return self.driver.is_element_visible(By.CSS_SELECTOR, self.message_excel_file_css, timeout=15)