import pprint

import requests

from api.wework import Wework
from utils.Utils import Utils


class BaseApi:
    printer = pprint.PrettyPrinter(indent=2)
    json_data = None

    @classmethod
    def verbose(cls, json_object=json_data):
        print(Utils.format(json_object))
        cls.printer.pprint(json_object)

    @classmethod
    def json_path(cls, expr):
        return Utils.json_path(cls.json_data, expr)

    # def request(self, method, url, params: dict, json, data):
    #  requests.request(method, url=url, params=params.update({"access_token": Wework.get_app_token()}))
    #   self.verbose(self.json_data)
    #     return self.json_data
    # def post(url, data=None, json=None, **kwargs):
    #     def get(url, params=None, **kwargs):
    @classmethod
    def request_get(cls, url, data, headers):
        r = requests.get(url=url, params=data, headers=headers).json()
        return r

    # def test_run_single_yaml(self):
    #     single_json =