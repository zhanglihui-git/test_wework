import requests

from api.baseApi import BaseApi
from api.wework import Wework
from data.readConfig import ReadConfig
from utils.Utils import Utils


class List2(BaseApi):

    def list2(self, data):
        read = ReadConfig()
        headers = {'Authorization': read.get_headers('auth')}
        r = BaseApi.request_get(read.get_http('baseurl') + '/hmdm/v1/0/item-categorys/list2', data,
                                headers)
        return r

# def create(self, name, parentid, order):
#     data = {"name": name, "parentid": parentid, "order": order}
#     params = {"access_token": Wework.get_token()}
#
#     self.json_data = requests.post(self.create_url, params=params,
#                                    headers={'content-type': 'application/json;charset=utf-8'},
#                                    json=data, verify=False).json()
#     self.verbose(self.json_data)
#     return self.json_data
#
# def delete(self, id):
#     r = requests.get(self.delete_url, params={"access_token": Wework.get_token(), "id": id}).json()
#     self.verbose(r)
#     return r
#
# def update(self):
#     pass
