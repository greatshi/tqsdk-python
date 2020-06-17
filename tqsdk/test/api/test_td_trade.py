#!usr/bin/env python3
#-*- coding:utf-8 -*-
"""
@author: yanqiong
@file: test_td_trade.py
@create_on: 2020/6/12
@description: 
"""
import os
import random
import unittest

from tqsdk import TqApi, TqAccount, utils
from tqsdk.test.api.helper import MockInsServer, MockServer


class TestTdTrade(unittest.TestCase):
    """
    实盘账户下，insert_order 各种情况测试
    """

    def setUp(self):
        self.ins = MockInsServer(5000)
        self.mock = MockServer(td_url_character="q7.htfutures.com")
        # self.tq = WebsocketServer(5300)
        self.ins_url_2020_06_16 = "http://127.0.0.1:5000/t/md/symbols/2020-06-16.json"
        self.md_url = "ws://127.0.0.1:5100/"
        self.td_url = "ws://127.0.0.1:5200/"

    def tearDown(self):
        self.ins.close()
        self.mock.close()

    def test_insert_order_fail1(self):
        # 预设服务器端响应
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.mock.run(os.path.join(dir_path, "log_file", "test_insert_order_shfe_anyprice.script"))
        # 测试
        account = TqAccount("H海通期货", "83011119", "sha121212")
        utils.RD = random.Random(4)
        # 测试
        with self.assertRaises(Exception):
            with TqApi(account=account, _ins_url=self.ins_url_2020_06_16, _md_url=self.md_url, _td_url=self.td_url,
                       debug=False) as api:
                order1 = api.insert_order("SHFE.au2012", "BUY", "OPEN", 1)
