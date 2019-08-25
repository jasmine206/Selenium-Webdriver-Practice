import json

import requests


class LogIn:
    def __init__(self, url_login, headers_login):
        self.url_login = url_login
        self.headers_login = headers_login
        self.data_login = {
            "has_accepted_privacy_policy": False,
            "has_allowed_email": False,
            "is_e_u": False,
            "email": "jasmine@gotitapp.co",
            "password": "1234Aa",
            "utm_meta": {
                "utm_source": "https://www.got-it.io/solutions/excel-chat/",
                "utm_medium": None,
                "utm_term": None,
                "utm_content": None
            }
        }

    def log_in_API(self):
        response = requests.post(self.url_login, headers=self.headers_login, data=json.dumps(self.data_login))
        response_data = response.json()
        return response_data['data']['access_token']


class PostQuestion:
    def __init__(self, url_post, headers_post):
        self.url_post = url_post
        self.headers_post = headers_post
        self.data_post = {
            'topic_id': -1000,
            'text': '[Jasmine] I need a formula to combine column C with the numbers in columns L10 to L20'
        }

        # self.data_post = data_post

    def post_question_API(self):
        post_response = requests.post(self.url_post, headers=self.headers_post, data=self.data_post)
        post_response_json = post_response.json()
        problem_id = post_response_json['data']['id']
        return problem_id


class SendMessage:
    def __init__(self, url_send, headers_send):
        self.url_send = url_send
        self.headers_send = headers_send
        self.data_send = {
            'message': 'thank you, next'
        }

    def send_message_API(self):
        requests.post(self.url_send, headers=self.headers_send, data=self.data_send)
