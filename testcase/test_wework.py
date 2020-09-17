from unittest import TestCase

from test_wework.api.wework import Wework


class TestWework(TestCase):
    def test_get_token(self):
        wework = Wework()
        token = wework.get_token()
        assert token is not None

        token = wework.get_token()
        assert token is not None

        token = wework.get_token()
        assert token is not None
