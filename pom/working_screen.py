from pom.expert_base import ExpertBase


class WorkingScreen(ExpertBase):
    chat_field_id = 'composer-attach-file-button'

    def is_in_session(self):
        return self.driver.is_element_clickable(self.chat_field_id, timeout=60)
