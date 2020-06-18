#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lucifer
# @Time    : 2018/12/14 10:06 AM
# @File    : database.py
# @Software: PyCharm

import sys
sys.path.append('..')
import pymysql
from pyfancy.pyfancy import pyfancy
from conf.config import GlobalConf
from Backtracking.SatanLogging import mylog

class db:
    #自定义构造
    def __init__(self, host = GlobalConf().mysqlconf['host'], port = GlobalConf().mysqlconf['port'], user = GlobalConf().mysqlconf['username'], password = GlobalConf().mysqlconf['password']):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.conn = None
        self.cursor = None

    """
    检查数据库是否连接
    return: bool
    """
    def connectdb(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db='SatanSword',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor,
            )
        except Exception as e:
            mylog('database').log.critical('[-]数据库连接失败: {}'.format(e))
            return False
        self.cursor = self.conn.cursor()
        mylog('database').log.info(pyfancy().green('[+]数据库连接成功'))
        return True

    """
    查询返回结果集
    return: dict
    """
    def execute(self, sql, param=None):
        if self.connectdb():
            try:
                if self.conn and self.cursor:
                    self.cursor.execute(sql, param)
                    self.conn.commit()
            except Exception as e:
                mylog('database').log.critical(pyfancy().red('数据库错误: {}'.format(e)))
                # 发生错误时回滚
                self.conn.rollback()
            mylog('database').log.info(pyfancy().green('SQL已执行: {}'.format(sql)))
            data = self.cursor.fetchall()
            self.close()
            return data

    """
    关闭数据库
    return: bool
    """
    def close(self):
        if self.conn and self.cursor:
            self.conn.close()
            self.cursor.close()
        return True