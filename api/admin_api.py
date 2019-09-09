import json

import requests

from config import Config


class AdminAPI:
    def __init__(self):
        self.headers = Config.headers_admin.copy()

    def terminate_session_by_session_id(self, session_id):
        data_terminate = {"state": "Terminated"}
        requests.put(Config.base_url_admin + '/problems/' + str(session_id), headers=self.headers,
                     data=json.dumps(data_terminate))
