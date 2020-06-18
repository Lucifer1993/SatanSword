#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lucifer
# @Time    : 2018/12/1 6:38 PM
# @File    : Analysis.py
# @Software: PyCharm

import re
import os
import sys
import socket
import requests
import datetime
sys.path.append('..')
from conf.config import GlobalConf
from bs4 import BeautifulSoup
import geoip2.database as ipdb
from urllib.parse import urlparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class judgement:
    def __init__(self, url):
        self.url = url

    """
    判断url中是否包含IP
    return: bool
    """
    def isIp(self):
        pattern = r'\d+.\d+.\d+.\d+'
        m = re.search(pattern, self.url)
        if m:
            return True
        else:
            return False

    """
    提取url中的IP
    return: ip
    """
    def extractIp(self):
        pattern = r'\d+.\d+.\d+.\d+'
        m = re.search(pattern, self.url)
        if m:
            return m.group()

    """
    url分解
    return: ParseResult class
    """
    def urlSplit(self):
        splitres = urlparse(self.url)
        return splitres

    """
    判断url属于内网还是外网,外网返回True
    return: bool
    """
    def interOrouter(self):
        useProxy = GlobalConf().high_hide_agent
        proxies = {
            'http':'http://{0}:{1}'.format(useProxy['url'], useProxy['port'])
        }
        try:
            req = requests.get(self.url, proxies=proxies, verify=False, timeout=20)
            #回收req object
            del req
            return True
        except:
            return False

    """
    获取当前时间戳函数
    return: string
    """
    def getNow(self):
        timeNow = '[{0}]'.format(datetime.datetime.now().strftime('%m-%d %H:%M:%S'))
        return timeNow

    """
    域名转IP函数
    return: string
    """
    def domain2ip(self):
        try:
            domain = self.urlSplit()[1]
            ip = socket.gethostbyname(domain)
            return ip
        except:
            return '0.0.0.0'

    """
    IP地址定位
    return dict
    """
    def iplocation(self):
        try:
            if self.isIp():
                IP = self.extractIp()
            else:
                IP = self.domain2ip()
            dbpath = os.path.join(GlobalConf().progpath['location'], 'Heaven_Hell/GeoLite2-City.mmdb')
            reader = ipdb.Reader(dbpath)
            locate = reader.city(IP)
            return locate

        except:
            return dict()

    """
    获取位置
    return list
    """
    def find_last(self, string, str):
        positions = []
        last_position = -1
        while True:
            position = string.find(str, last_position + 1)
            if position == -1: break
            last_position = position
            positions.append(position)
        return positions

    """
    处理url
    return string
    """
    def process_url(self, URL, re_URL):
        black_url = ["javascript:"]  # Add some keyword for filter url.
        URL_raw = urlparse(URL)
        ab_URL = URL_raw.netloc
        host_URL = URL_raw.scheme
        if re_URL[0:2] == "//":
            result = host_URL + ":" + re_URL
        elif re_URL[0:4] == "http":
            result = re_URL
        elif re_URL[0:2] != "//" and re_URL not in black_url:
            if re_URL[0:1] == "/":
                result = host_URL + "://" + ab_URL + re_URL
            else:
                if re_URL[0:1] == ".":
                    if re_URL[0:2] == "..":
                        result = host_URL + "://" + ab_URL + re_URL[2:]
                    else:
                        result = host_URL + "://" + ab_URL + re_URL[1:]
                else:
                    result = host_URL + "://" + ab_URL + "/" + re_URL
        else:
            result = URL
        return result

    """
    获取源码页
    return string
    """
    def Extract_html(self, URL):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}
        try:
            re = requests.get(URL, headers=header, timeout=10, verify=False)
            raw = re.content.decode("utf-8", "ignore")
            return raw
        except:
            return None

    """
    提取URL
    return list
    """
    def extract_URL(self, JS):
        pattern_raw = r"""
              (?:"|')                               # Start newline delimiter
              (
                ((?:[a-zA-Z]{1,10}://|//)           # Match a scheme [a-Z]*1-10 or //
                [^"'/]{1,}\.                        # Match a domainname (any character + dot)
                [a-zA-Z]{2,}[^"']{0,})              # The domainextension and/or path
                |
                ((?:/|\.\./|\./)                    # Start with /,../,./
                [^"'><,;| *()(%%$^/\\\[\]]          # Next character can't be...
                [^"'><,;|()]{1,})                   # Rest of the characters can't be
                |
                ([a-zA-Z0-9_\-/]{1,}/               # Relative endpoint with /
                [a-zA-Z0-9_\-/]{1,}                 # Resource name
                \.(?:[a-zA-Z]{1,4}|action)          # Rest + extension (length 1-4 or action)
                (?:[\?|/][^"|']{0,}|))              # ? mark with parameters
                |
                ([a-zA-Z0-9_\-]{1,}                 # filename
                \.(?:php|asp|aspx|jsp|json|
                     action|html|js|txt|xml)             # . + extension
                (?:\?[^"|']{0,}|))                  # ? mark with parameters
              )
              (?:"|')                               # End newline delimiter
            """
        pattern = re.compile(pattern_raw, re.VERBOSE)
        result = re.finditer(pattern, str(JS))
        if result == None:
            return None
        js_url = []
        for match in result:
            if match.group() not in js_url:
                js_url.append(match.group().strip('"').strip("'"))
        return js_url

    """
    JS提取子域名信息
    return list
    """
    def find_by_url(self, js=False):
        if js == False:
            try:
                html_raw = self.Extract_html(self.url)
                html = BeautifulSoup(html_raw, "html.parser")
                html_scripts = html.findAll("script")
                script_array = {}
                script_temp = ""
                for html_script in html_scripts:
                    script_src = html_script.get("src")
                    if script_src == None:
                        script_temp += html_script.get_text() + "\n"
                    else:
                        purl = self.process_url(self.url, script_src)
                        script_array[purl] = self.Extract_html(purl)
                script_array[self.url] = script_temp
                allurls = []
                for script in script_array:
                    # print(script)
                    temp_urls = self.extract_URL(script_array[script])
                    if len(temp_urls) == 0: continue
                    for temp_url in temp_urls:
                        allurls.append(self.process_url(script, temp_url))
                result = []
                for singerurl in allurls:
                    url_raw = urlparse(self.url)
                    domain = url_raw.netloc
                    positions = self.find_last(domain, ".")
                    miandomain = domain
                    if len(positions) > 1: miandomain = domain[positions[-2] + 1:]
                    # print(miandomain)
                    suburl = urlparse(singerurl)
                    subdomain = suburl.netloc
                    # print(singerurl)
                    if miandomain in subdomain or subdomain.strip() == "":
                        if singerurl.strip() not in result:
                            result.append(singerurl)
                return result
            except:
                pass

        else:
            temp_urls = self.extract_URL(self.Extract_html(self.url))
            if len(temp_urls) == 0: return None
            result = []
            for temp_url in temp_urls:
                if temp_url not in result:
                    result.append(temp_url)
            return result

    """
    获取子域名
    return list
    """
    def find_subdomain(self, urls, mainurl):
        url_raw = urlparse(mainurl)
        domain = url_raw.netloc
        miandomain = domain
        positions = self.find_last(domain, ".")
        if len(positions) > 1: miandomain = domain[positions[-2] + 1:]
        subdomains = []
        for url in urls:
            suburl = urlparse(url)
            subdomain = suburl.netloc
            # print(subdomain)
            if subdomain.strip() == "": continue
            if miandomain in subdomain:
                if subdomain not in subdomains:
                    subdomains.append(subdomain)
        return subdomains

    """
    返回结果
    return list
    """
    def giveresult(self, urls, domian):
        if urls == None:
            return None
        content_url = ""
        for url in urls:
            content_url += url + "\n"
        subdomains = self.find_subdomain(urls, domian)
        return subdomains
