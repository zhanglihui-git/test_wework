import requests

from test_wework.api.BaseApi import BaseApi
from test_wework.api.wework import Wework
from test_wework.utils.Utils import Utils


class Department(BaseApi):
    list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
    create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
    delete_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"

    def list(self, id):
        r = requests.get(self.list_url, params={"access_token": Wework.get_token(), "id": id}).json()
        self.verbose(r)
        return r

    def create(self, name, parentid, order):
        data = {"name": name, "parentid": parentid, "order": order}
        params = {"access_token": Wework.get_token()}

        self.json_data = requests.post(self.create_url, params=params,
                                       headers={'content-type': 'application/json;charset=utf-8'},
                                       json=data, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data

    def delete(self, id):
        r = requests.get(self.delete_url, params={"access_token": Wework.get_token(), "id": id}).json()
        self.verbose(r)
        return r

    def update(self):
        pass
