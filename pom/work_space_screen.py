from selenium.webdriver.common.by import By

from pom.expert_base import ExpertBase


class WorkSpaceScreen(ExpertBase):
    messages_list_css = ".chat-message"
    message_image_css = ".message-photo img[src='/images/icons/placeholder.svg']"
    message_excel_file_css = ".message-photo img[src='/images/samples/6.jpg']"

    def is_received_text_message(self, sent_message):
        self.driver.is_element_visible(self.messages_list_css, By.CSS_SELECTOR, timeout=15)
        messages_list = self.driver.wait_until_visibility_of_elements_located(self.messages_list_css, By.CSS_SELECTOR)
        len_msg_list = len(messages_list)
        if messages_list[len_msg_list - 1].text == sent_message:
            return True
        else:
            return False

    def is_received_image_message(self):
        return self.driver.is_element_visible(self.message_image_css, By.CSS_SELECTOR, timeout=15)

    def is_received_excel_file_message(self):
        return self.driver.is_element_visible(self.message_excel_file_css, By.CSS_SELECTOR, timeout=15)
