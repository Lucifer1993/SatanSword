#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Lucifer
# Date: 2018.11.26

class GlobalConf:
    def __init__(self):
        """
        ceye接口用来探测盲命令执行
        """
        self.ceye = {
            "url": "http://dx3hbm.ceye.io",
            "weblog": "http://api.ceye.io/v1/records?token=c04665a158430a100ed655f9c710e597&type=http",
            "dnslog": "http://api.ceye.io/v1/records?token=c04665a158430a100ed655f9c710e597&type=dns",
        }

        """
        chromuim路径
        """
        self.chromuim = {
            "path": "/Applications/Chromium.app/Contents/MacOS/Chromium",
        }

        """
        检测是否存在重定向
        """
        self.redirect = {
            "url": "http://www.luciferxx.cn",
            "key": "ed6b123aac0a4636797fefa09097974e2133788974b1c9167b11f1affa3543c7",
        }

        """
        SatanSword主工程路径
        """
        self.progpath = {
            "location": "/Users/lucifer/SatanSword",
        }

        """
        MySQL数据库配置
        """
        self.mysqlconf = {
            "host": "127.0.0.1",
            "port": 3306,
            "username": "root",
            "password": "Han19930101",
        }
