import requests


class Wework():
    corpid = "wwb4823013fcc98751"
    userid = "hggd"
    departmentid = "1"
    tagid = "1"
    agentid = "1000002"
    agentsecret = "lx6okafzuZkxdnjjB3htWd9BXmdfIB8KD7HmzFDO9NA"
    contactsecret = "KR9G1O65OD2eG1FMCBa5WP4Qiq9LET8GN9louUwSeas"
    access_token_contact = None
    access_token_app = None

    @classmethod
    def get_contact_token(cls):
        if cls.access_token_contact is None:
            url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            r = requests.get(url, params={"corpid": cls.corpid, "corpsecret": cls.contactsecret}).json()
            # print(r)
            # cls.verbose(r)
            Wework.access_token_contact = r["access_token"]

        return Wework.access_token_contact

    @classmethod
    def get_app_token(cls):
        if cls.access_token_app is None:
            url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            r = requests.get(url, params={"corpid": cls.corpid, "corpsecret": cls.agentsecret}).json()
            # print(r)
            # cls.verbose(r)
            Wework.access_token_app = r["access_token"]

        return Wework.access_token_app
