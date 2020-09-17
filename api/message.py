import requests

from test_wework.api import wework
from test_wework.api.BaseApi import BaseApi
from test_wework.api.wework import Wework


class Message(BaseApi):
    _send_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send"

    def send_text(self, msg=None, users=[], parties=[], tags=[]):
        self.json_data = requests.post(
            self._send_url,
            params={"access_token": Wework.get_app_token()},
            headers={'content-type': 'application/json;charset=utf-8'},
            json={
                "touser": "|".join(users),
                "toparty": "|".join(parties),
                "totag": "|".join(tags),
                "msgtype": "text",
                "agentid": Wework.agentid,
                "text": {
                    "content": msg
                },
                "safe": 0,
                "enable_id_trans": 0
            }).json()
        self.verbose(self.json_data)

    def send_voice(self):
        pass
