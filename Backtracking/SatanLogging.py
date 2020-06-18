#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lucifer
# @Time    : 2018/12/3 1:03 AM
# @File    : SatanLogging.py
# @Software: PyCharm

import os
import sys
sys.path.append('..')
import logbook
from conf.config import GlobalConf
from logbook.more import ColorizedStderrHandler
from logbook import Logger,StreamHandler, FileHandler,TimedRotatingFileHandler

class mylog:
    def __init__(self, logname, toscreen=False):
        # 设置日志名称
        self.logname = logname
        self.toscreen = toscreen
        # 设置日志目录
        self.LOG_DIR = self.setpath()
        # 设置本地时间
        logbook.set_datetime_format("local")
        # 设置终端输出格式
        self.log_standard = ColorizedStderrHandler(bubble=True)
        self.log_standard.formatter = self.logformat
        # 设置文件输出格式
        self.log_file = TimedRotatingFileHandler(
            os.path.join(self.LOG_DIR, '{}.log'.format(self.logname)), date_format='%Y-%m-%d', bubble=True, encoding='utf-8')
        self.log_file.formatter = self.logformat
        # 执行log记录
        self.log = Logger("SatanLogging")
        self.logrun()

    """
    日志存储函数
    """
    def setpath(self):
        logpath = os.path.join(GlobalConf().progpath['location'], 'Backtracking/log')
        if not os.path.exists(logpath):
            os.makedirs(logpath)
        return logpath

    """
    格式化日志函数
    """
    def logformat(self, record, handler):
        log = "[{date}] [{level}] [{filename}] [{func_name}] [{lineno}] {msg}".format(
            # 日志时间
            date=record.time,
            # 日志等级
            level=record.level_name,
            # 文件名
            filename=os.path.split(record.filename)[-1],
            # 函数名
            func_name=record.func_name,
            # 行号
            lineno=record.lineno,
            # 日志内容
            msg=record.message
        )
        return log

    """
    生成日志函数
    """
    def logrun(self):
        self.log.handlers = []
        self.log.handlers.append(self.log_file)
        # 如果为True将日志打到屏幕
        if self.toscreen:
            self.log.handlers.append(self.log_standard)
