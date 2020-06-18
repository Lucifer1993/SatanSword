#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lucifer
# @Time    : 2019-03-29 00:14
# @File    : dirbrute.py
# @Software: PyCharm
from gevent import monkey;monkey.patch_all()
from gevent.pool import Pool
import gevent
import os
import sys
sys.path.append('..')
import requests
from conf.termcolor import cprint
from pyfancy.pyfancy import pyfancy
from Backtracking.SatanLogging import mylog
from Evil_Eye.Proxy import findProxy
from conf.config import GlobalConf

class dirsearch:
    def __init__(self, url):
        self.url = url
        self.length = 0
        self.count = 0
        self.webpath = list()
        self._403 = ['/.hta', '/.ht_wsr.txt', '/.htaccess-local', '/.htaccess-dev',
                     '/.htaccess.bak1', '/.htaccess.old', '/.htaccess.inc', '/.htaccess.orig',
                     '/.htaccess.save', '/.htaccess.bak', '/.htaccess', '/.htaccess/',
                     '/.htaccessOLD2', '/.htaccessBAK', '/.htaccess.sample', '/.htaccess_extra',
                     '/.htaccess_orig', '/.htaccess_sc', '/.htgroup', '/.htpasswd', '/.htpasswd.bak',
                     '/.htaccess~', '/.htpasswd.inc', '/.htaccess.txt', '/.htpasswds', '/.htpasswrd',
                     '/.htaccessOLD', '/.htusers', '/.htpasswd-old', '/.htpasswd_test','/.htpasswd/',
                     '/.htaccess-marco']

    """
    判断head请求是否支持
    return: boolean
    """
    def check404(self):
        headers = {
            'User-Agent':findProxy().randomUA()
        }
        notfound = self.url + '/c2adf6ecc220f2711801d6e466340183'
        req = requests.head(notfound, headers=headers, verify=False, timeout=10)
        if req.status_code == 404:
            return True
        else:
            return False

    """
    获取404页面字节数
    return: integer
    """
    def get404length(self):
        headers = {
            'User-Agent': findProxy().randomUA()
        }
        try:
            notfound = self.url + '/c2adf6ecc220f2711801d6e466340183'
            req = requests.get(notfound, headers=headers, verify=False, timeout=10)
            self.length = len(req.text)
        except:
            pass

    """
    发送head请求不返回length
    """
    def sendrequestshead(self, url):
        headers = {
            'User-Agent':findProxy().randomUA()
        }
        targeturl = self.url + url
        self.count += 1
        #cprint("[*] 加载")
        cprint('#Process: {}\t[{:.2%}]{}\r'.format(targeturl,(self.count/9739), ' '*(len(targeturl)-90)), 'yellow', attrs=['bold'], end='', flush=True)
        sys.stdout.flush()
        try:
            req = requests.head(targeturl, headers=headers, verify=False, timeout=10, allow_redirects=False)
            if req.status_code != 404 and req.status_code != 400 and req.status_code != 412 and req.status_code != 403:
                if url in self._403 and req.status_code == 403:
                    pass
                else:
                    tmpdict = {'url':targeturl, 'status_code':req.status_code}
                    mylog('webpath', True).log.info(pyfancy().green('[+]发现web路径: {0}'.format(str(tmpdict))))
                    self.webpath.append(tmpdict)
        except:
            pass
        gevent.sleep(0)

    """
    发送get请求返回length
    """
    def sendrequestsget(self, url):
        headers = {
            'User-Agent':findProxy().randomUA()
        }
        targeturl = self.url + url
        try:
            req = requests.get(targeturl, headers=headers, verify=False, timeout=10, allow_redirects=False)
            if len(req.text) == self.length or len(req.text) - 32 == self.length:
                pass
            else:
                if req.status_code != 404 and req.status_code != 400 and req.status_code != 412 and req.status_code != 403:
                    if url in self._403 and req.status_code == 403:
                        pass
                    else:
                        tmpdict = {'url':targeturl, 'status_code':req.status_code, 'length':len(req.text)}
                        mylog('webpath', True).log.info(pyfancy().green('[+]发现web路径: {0}'.format(str(tmpdict))))
                        self.webpath.append(tmpdict)
        except:
            pass
        gevent.sleep(0)

    """
    执行路径爆破
    """
    def run(self):
        crackpasswords = list()
        crackdict = os.path.join(GlobalConf().progpath['location'], 'Endless_Sword/crackdict/webpath.dic')
        with open(crackdict) as f:
            for line in f.readlines():
                line = line.strip()
                crackpasswords.append(line)
        pool = Pool(30)
        if self.check404():
            threads = [pool.spawn(self.sendrequestshead, item) for item in crackpasswords]
            gevent.joinall(threads)
        else:
            threads = [pool.spawn(self.sendrequestsget, item) for item in crackpasswords]
            gevent.joinall(threads)


