from unittest import TestCase
import requests

from api.baseApi import BaseApi
from api.categorys.list2 import List2
from data.readConfig import ReadConfig


class TestList2(TestCase):

    def test_list2(self):
        list2 = List2()
        data2 = {'category': '10'}
        r = list2.list2(data2)
        print(r)


    # def test_list(self):
    #     # list json assert
    #     # assert depart.list(2).['ddd']=222
    #     department = Department()
    #     r = department.list("")
    #     # print(Utils.format(r))
    #     assert r["errcode"] == 0
    #     assert r["department"][0]["name"] == "吉利"
