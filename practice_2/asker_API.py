import json

import requests


class AskerAPI:
    def __init__(self):
        self.headers = {
            'Origin': 'https://www.got-it.io',
            'X-GotIt-Product': 'excelchat',
            'Content-Type': 'application/json',
            'X-GotIt-Site': 'excelchat',
            'X-GotIt-Vertical': 'excel'
        }
        self.access_token = None
        self.base_url = 'https://api.got-it.io/'
        self.question = None
        self.message = None

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
        response = requests.post(self.base_url + 'log-in/asker/email', headers=self.headers, data=json.dumps(data_login))
        response_data = response.json()
        self.access_token = response_data['data']['access_token']

    def post_question(self, subject_id, question):
        self.question = question
        data_post = {
            'topic_id': subject_id,
            'text': question
        }
        # Asker posts question using API
        headers_post = self.headers.copy()
        headers_post.pop('Content-Type')
        headers_post.update({'Authorization': 'Bearer ' + self.access_token})

        post_response = requests.post(self.base_url + 'askers/me/problems', headers=headers_post, data=data_post)
        post_response_json = post_response.json()
        problem_id = post_response_json['data']['id']
        return problem_id

    def send_message(self, problem_id, message):
        self.message = message
        data_send = {
            'message': message,
            'explanation_id': problem_id
        }
        headers_send = self.headers.copy()
        headers_send.pop('Content-Type')
        headers_send.update({'Authorization': 'Bearer ' + self.access_token})

        requests.post(self.base_url + 'askers/me/explanation_messages', headers=headers_send, data=data_send)
