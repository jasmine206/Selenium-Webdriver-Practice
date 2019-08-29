import json

import requests


class AskerAPI:
    headers = {
        'Origin': 'https://www.got-it.io',
        'X-GotIt-Product': 'excelchat',
        'Content-Type': 'application/json',
        'X-GotIt-Site': 'excelchat',
        'X-GotIt-Vertical': 'excel'
    }
    base_url = 'https://api.got-it.io/'

    def __init__(self):
        self.problem_id = None

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

        access_token = response_data['data']['access_token']
        AskerAPI.headers.update({'Authorization': 'Bearer ' + access_token})
        AskerAPI.headers.pop('Content-Type')

    def post_question(self, subject_id, question):
        data_post = {
            'topic_id': subject_id,
            'text': question
        }
        # Asker posts question using API
        post_response = requests.post(AskerAPI.base_url + 'askers/me/problems', headers=AskerAPI.headers, data=data_post)
        post_response_json = post_response.json()
        self.problem_id = post_response_json['data']['id']

    def send_message(self, problem_id, message):
        data_send = {
            'message': message,
            'explanation_id': problem_id
        }
        requests.post(AskerAPI.base_url + 'askers/me/explanation_messages', headers=AskerAPI.headers, data=data_send)