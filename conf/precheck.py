#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Lucifer
# Date: 2018.11.22
from shutil import which
from termcolor import cprint
from conf.config import GlobalConf
class Envcheck:
    """
    python依赖库检查函数
    return: bool
    """
    def modulecheck(self):
        success = True
        cprint('[*]执行Python模块检查..', 'blue')
        modlist = [
            'requests', 'bs4', 'builtwith', 'cmd2', 'gnureadline',
            'paramiko', 'pexpect', 'json', 're', 'socket', 'readline',
            'gevent', 'urllib3', 'logbook', 'faker', 'pymongo',
            'pymysql', 'prettytable', 'pyfancy', 'selenium', 'struct',
            'http.cookies', 'click', 'redis',
            'binascii', 'emoji', 'geoip2', 'ssl', 'telnetlib', 'whois',
            'lxml', 'simplejson',
        ]
        for _mod in modlist:
            try:
                importmod =  __import__(_mod)
                cprint('[+]已安装模块: {0}'.format(importmod.__name__), 'green')
            except:
                success = False
                cprint('[-]缺少Python模块: {0}'.format(_mod), 'red')
        return success

    """
    系统命令库检查函数
    return: bool
    """
    def commandcheck(self):
        success = True
        cprint('[*]执行命令模块检查..', 'blue')
        commlist = [
            'nmap', 'whatweb', 'masscan', 'java', 'chromedriver',
        ]
        for _comm in commlist:
            try:
                res = which(_comm)
                if _comm in res:
                    cprint('[+]已安装命令: {0}'.format(_comm), 'green')
            except:
                success = False
                cprint('[-]缺少命令: {0}'.format(_comm), 'red')
        return success

    """
    第三方api接口检查函数
    return: bool
    """
    def apicheck(self):
        success = True
        cprint('[*]执行api模块检查..', 'blue')
        try:
            ceye_conf = GlobalConf().ceye
            if len(ceye_conf['url'])>0:
                cprint('[+]ceye接口已配置', 'green')
            else:
                cprint('[-]ceye接口未配置', 'red')

            chromuim_conf = GlobalConf().chromuim
            if len(chromuim_conf['path'])>0:
                cprint('[+]chromuim路径已配置', 'green')
            else:
                cprint('[-]chromuim路径未配置', 'red')

            redirect_conf = GlobalConf().redirect
            if len(redirect_conf['url'])>0 and len(redirect_conf['key'])>0:
                cprint('[+]重定向接口已配置', 'green')
            else:
                cprint('[-]重定向接口未配置', 'red')

            logpath = GlobalConf().progpath
            if len(logpath['location'])>0:
                cprint('[+]日志存储路径已配置', 'green')
            else:
                cprint('[-]日志存储路径未配置', 'red')

            my = GlobalConf().mysqlconf
            if len(my['host'])>0 and my['port']>0 and len(my['username'])>0 and len(my['password'])>0:
                cprint('[+]MySQL数据库已配置', 'green')
            else:
                cprint('[-]MySQL数据库未配置', 'red')
        except Exception as e:
            print(e)
            success = False
        return success
