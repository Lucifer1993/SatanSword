#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lucifer
# @Time    : 2018/12/6 2:20 PM
# @File    : Proxy.py
# @Software: PyCharm
from gevent import monkey;monkey.patch_all()
from gevent.pool import Pool
import gevent
import sys
sys.path.append('..')
import random
import requests
from pyfancy.pyfancy import pyfancy
from faker import Factory
from faker.providers import internet
from faker.providers import user_agent
from Backtracking.SatanLogging import mylog
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class findProxy:
    def __init__(self):
        self.proxylist = [
            {}
        ]

    """
    返回随机代理IP
    """
    def randomProxy(self):
        return random.choice(self.proxylist)

    def send_request(self, proxyheader, url):
        try:
            req = requests.get(url, proxies=proxyheader, timeout=8, verify=False)
            if req.ok:
                mylog('proxy', True).log.info(pyfancy().green('有效代理: {}'.format(proxyheader)))
            else:
                self.proxylist.remove(proxyheader)
                mylog('proxy').log.warning(pyfancy().yellow('无效代理: {}'.format(proxyheader)))
        except Exception as e:
            self.proxylist.remove(proxyheader)
            mylog('proxy').log.critical('无效代理: {}  错误原因: {}'.format(proxyheader, e))

    """
    代理连接测试
    """
    def connectest(self, url):
        pool = Pool(10)
        threads = [pool.spawn(self.send_request, proxy, url) for proxy in self.proxylist]
        gevent.joinall(threads)
        if len(self.proxylist) == 0:
            self.proxylist.append({})

    """
    随机X-Forwarded-For头
    return: string
    """
    def randomXFF(self):
        fake = Factory.create()
        fake.add_provider(internet)
        return fake.ipv4_private()

    """
    随机UserAgent头
    return: string
    """
    def randomUA(self):
        fake = Factory.create()
        fake.add_provider(user_agent)
        return fake.user_agent()