# encoding: utf-8
"""
@author: sy_dove
@license: (C) Copyright 2019-2020, Node Supply Chain Manager Corporation Limited.
@contact: sydove08152@gmail.com
@file: yttytt.py
@time: 2019/6/2 23:01
@desc:
"""
import requests
from selenium import webdriver
import time


class getCookie:

    def get_cookie(self):
        # 使用selenium打开网址,然后让用户完成手工登录,再获取cookie
        url = u'http://10.224.221.200/mdm/customer-manage/list'
        # username = u'admin'
        password = 'Admin@123'
        # search_by_name = "username"
        search_by_id = "password"
        login_path = "//*[@id='loginFormAccount']/div[2]/span/button"
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(30)
        driver.find_element_by_name('username').send_keys(u'admin')
        driver.find_element_by_id(search_by_id).send_keys(password)
        driver.find_element_by_xpath(login_path).click()
        driver.implicitly_wait(30)
        driver.refresh()
        c = driver.get_cookies()
        print(c)
        cookies = {}
        # 获取cookie中的name和value,转化成requests可以使用的形式
        for cookie in c:
            cookies[cookie['name']] = cookie['value']

        cookie_token = cookies.get('access_token')
        print(cookie_token)
        driver.quit()
        return cookie_token
