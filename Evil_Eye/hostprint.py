#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lucifer
# @Time    : 2018-12-27 21:14
# @File    : hostprint.py
# @Software: PyCharm
from gevent import monkey;monkey.patch_all()
from gevent.pool import Pool
import gevent
import re
import sys
sys.path.append('..')
import importlib
import subprocess
from Backtracking.SatanLogging import mylog
from pyfancy.pyfancy import pyfancy
from Heaven_Hell.database import db

class scanhost:
    def __init__(self, host):
        self.host = host
        self.prints = list()
        self.tport = 0

    """
    使用masscan扫描获取开放TCP端口
    return: list
    """
    def useMasscanTCP(self):
        mylog('hostprint', True).log.info(pyfancy().green('[+]执行masscan TCP端口扫描: {}'.format(self.host)))
        try:
            ports = list()
            cmd = ['masscan', '-sS', '-Pn', '-p21-25,53,80-90,99,110,113,119,121-123,137-139,\
                    170,443-445,456,554,513-514,559,873,888,1080-1099,1200-1212,1234,1243-1255,\
                    1433-1434,1521,2000,2049,2181,2200-2300,2375,2535,3127-3128,3300-3310,3389,\
                    4443-4444,5000-5001,5432,5900-5901,5432,5984,6000,6370-6380,6984,7000-7010,\
                    8000-8200,8443-8449,8880-8900,9000-9001,9043,9080-9100,9200-9210,9300,9668,\
                    9876,9990-10000,10080,11211,12345,16379,18080,20000-20010,22220-23000,26379,\
                    27010-27020,33060,50070', self.host]
            out1, err1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            out2, err2 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            pattern = re.compile('[0-9]+/tcp')
            list1 = re.findall(pattern, bytes.decode(out1))
            list2 = re.findall(pattern, bytes.decode(out2))
            listres = list(set(list1).union(set(list2)))
            for item in listres:
                ports.append(item.replace('/tcp', ''))
            return ports

        except Exception as e:
            mylog('hostprint').log.critical(e)
            return {}

    """
    使用masscan扫描获取开放UDP端口
    return: list
    """
    def useMasscanUDP(self):
        mylog('hostprint', True).log.info(pyfancy().green('[+]执行masscan UDP端口扫描: {}'.format(self.host)))
        try:
            ports = list()
            cmd = ['masscan', '-sS', '-Pn', '-pU:20-25,79,110,123,137-139,161,180,513-514,559,666,999,\
                    1011-1032,1042-1054,1200-1201,1342-1349,2000-2002,3333,6666,26274,26374,26444,26573,\
                    27184,27444,29589,29891,30103,31320-31340,34555,35555', self.host]
            out1, err1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            out2, err2 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            pattern = re.compile('[0-9]+/udp')
            list1 = re.findall(pattern, bytes.decode(out1))
            list2 = re.findall(pattern, bytes.decode(out2))
            listres = list(set(list1).union(set(list2)))
            for item in listres:
                ports.append(item.replace('/udp', ''))
            return ports

        except Exception as e:
            mylog('hostprint').log.critical(e)
            return {}

    """
    使用nmap进行TCP端口服务探测
    return: string
    """
    def useNmapServTCP(self, port):
        mylog('hostprint', True).log.info(pyfancy().green('[+]执行nmap TCP端口服务探测: {0}:{1}'.format(self.host, port)))
        try:
            cmd = ['nmap', '-sV', '-Pn', '--scan-delay', '2',
                   '--host-timeout', '2m', '--version-intensity', '6', self.host, '-p', port]
            out, err = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            service = bytes.decode(out)
            return service
        except Exception as e:
            cmd = ['nmap', '--host-timeout', '1m', self.host, '-p', port]
            out, err = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            service = bytes.decode(out)
            return service

    """
    使用nmap进行UDP端口服务探测
    return: string
    """
    def useNmapServUDP(self, port):
        mylog('hostprint', True).log.info(pyfancy().green('[+]执行nmap UDP端口服务探测: {0}:{1}'.format(self.host, port)))
        try:
            cmd = ['nmap', '-sV', '-Pn', '--scan-delay', '2',
                   '--host-timeout', '2m', '--version-intensity', '6', '-sU', '-pU:{}'.format(port), self.host]
            out, err = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            service = bytes.decode(out)
            return service
        except Exception as e:
            cmd = ['nmap', '--host-timeout', '1m', '-sU', '-pU:{}'.format(port), self.host]
            out, err = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            service = bytes.decode(out)
            return service

    def loadmodule(self):
        requirements = ['socket', 'requests', 're']
        imported_libs = {lib: importlib.import_module(lib) for lib in requirements}
        globals().update(imported_libs)

    def pocexec(self, poccode):
        exec(poccode)
        gevent.sleep(0)

    """
    使用自定义脚本探测服务
    return: list
    """
    def useScript(self, port):
        self.tport = port
        mylog('hostprint', True).log.info(pyfancy().green('[+]执行自定义脚本探测系统服务: {}'.format(self.host)))
        pool = Pool(20)
        servlist = list()
        self.loadmodule()
        poclist = list()
        try:
            sqlstring = 'SELECT servicepoc FROM hostprint'
            res = db().execute(sqlstring)
            for item in res:
                poclist.append(item['servicepoc'])
            threads = [pool.spawn(self.pocexec, item) for item in poclist]
            gevent.joinall(threads)
            for servprint in self.prints:
                if servprint['isService']:
                    servlist.append(servprint)
            print(servlist)

        except Exception as e:
            mylog('hostprint').log.critical(e)

'''
a = scanhost('117.169.117.78')
print(a.useMasscanTCP())
'''
