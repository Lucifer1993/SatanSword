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
            "url": "",
            "weblog": "http://api.ceye.io/v1/records?token=XXXXXXXXXXXXXXXXXXXXXX&type=http",
            "dnslog": "http://api.ceye.io/v1/records?token=XXXXXXXXXXXXXXXXXXXXXX&type=dns",
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
            "url": "",
            "key": "",
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
            "username": "",
            "password": "",
        }
