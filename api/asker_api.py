import json
import requests

from requests_toolbelt.multipart import MultipartEncoder
from config import Config


class AskerAPI:
    def __init__(self):
        self.problem_id = None
        self.headers = Config.headers_asker.copy()

    def log_in(self, email, password):
        data_login = {
            "has_accepted_privacy_policy": False,
            "has_allowed_email": False,
            "is_e_u": False,
            "email": None,
            "password": None,
            "utm_meta": {
                "utm_source": "https://www.got-it.io/solutions/excel-chat/",
                "utm_medium": None,
                "utm_term": None,
                "utm_content": None
            }
        }
        data_login.update({'email': email, 'password': password})
        response = requests.post(Config.base_url_asker + 'log-in/asker/email', headers=self.headers,
                                 data=json.dumps(data_login))
        response_data = response.json()
        access_token = response_data['data']['access_token']
        self.headers.update({'Authorization': 'Bearer ' + access_token})
        self.headers.pop('Content-Type')

    def post_question(self, subject_id, question):
        data_post = {
            'topic_id': subject_id,
            'text': question
        }
        # Asker posts question using API
        post_response = requests.post(Config.base_url_asker + 'askers/me/problems', headers=self.headers,
                                      data=data_post)
        post_response_json = post_response.json()
        self.problem_id = post_response_json['data']['id']

    # Content-type must have in headers
    def send_text_message(self, problem_id, message):
        data_send_text = {
            'message': message,
            'explanation_id': problem_id
        }
        requests.post(Config.base_url_asker + 'askers/me/explanation_messages', headers=self.headers,
                      data=data_send_text)

    def send_image_message(self, problem_id, file_path):
        expert_message = MultipartEncoder(
            fields={
                # a file upload field
                'file': ('file.jpg', open(file_path, 'rb'), '../Selenium-Webdriver-Practice/test'),
                # plain text fields
                'explanation_id': str(problem_id),
                'message': 'hello',
            }
        )
        self.headers.update({'Content-Type': 'multipart/form-data'})
        r = requests.post(url=Config.base_url_asker + 'askers/me/explanation_messages',
                          headers=self.headers, data=expert_message)
        print(r.json())
        print(r.status_code)

    def send_excel_file_message(self, problem_id, file_path):
        data_send_excel_file = MultipartEncoder(
            fields={
                # a file upload field
                'file': ('file.xlsx', open(file_path, 'rb'), '../Selenium-Webdriver-Practice/test'),
                # plain text fields
                'explanation_id': str(problem_id),
                'message': 'hello',
            }
        )
        requests.post(Config.base_url_asker + 'askers/me/explanation_messages', headers=self.headers,
                      data=data_send_excel_file)
