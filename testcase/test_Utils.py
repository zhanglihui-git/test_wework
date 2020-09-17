from unittest import TestCase
import requests

from test_wework.utils.Utils import Utils


class TestUtils(TestCase):
    def test_format(self):
        print(Utils.format({"a": 1, "b": {"c": "xxxx"}}))

    def test_json_path(self):
        r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2").json()
        print(Utils.jsonpath(r, "$..topics[?(@.excellent == 0)]"[0]))
