#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lucifer
# @Time    : 2018/12/2 9:44 AM
# @File    : webprint.py
# @Software: PyCharm
from gevent import monkey

monkey.patch_all()
from gevent.pool import Pool
import re
import sys
import ssl
import whois
import random
import hashlib
import requests
import builtwith

sys.path.append('..')
import subprocess
from urllib.parse import urljoin, urlparse
from pyfancy.pyfancy import pyfancy
from Heaven_Hell.database import db
from .wappalyzer.Wappalyzer import Wappalyzer, WebPage
from .Analysis import judgement
from .Proxy import findProxy
from .cdnwaf import cdnwafidentity
from Backtracking.SatanLogging import mylog
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class explore:
    def __init__(self, url):
        self.url = url
        self.length = 0
        self.header = self.useGetheaders()
        self.proxies = list()

    """
    获取headers
    return: string
    """

    def useGetheaders(self):
        mylog('webprint', True).log.info(pyfancy().green('[+]执行获取headers: {}'.format(self.url)))
        headers = {
            'User-Agent': findProxy().randomUA(),
            'X-Forwarded-For': findProxy().randomXFF()
        }
        try:
            req = requests.get(self.url, headers=headers, timeout=15, verify=False)
            return req.headers
        except Exception as e:
            try:
                req = requests.head(self.url, headers=headers, timeout=15, verify=False)
                return req.headers
            except:
                mylog('webprint').log.critical(pyfancy().red(e))
                return {}

    """
    通用检查CDN
    return: bool
    """

    def useCDNHeader(self):
        mylog('webprint', True).log.info(pyfancy().green('[+]执行通用CDN识别: {}'.format(self.url)))
        try:
            key = False
            cdn_headers = [
                'X-CDN',
                'via',
                'x-cache',
                'x-swift-cachetime',
                'X-Cache-Lookup',
                'X-Via',
                'Via',
                'X-Via-CDN',
                'X-Cdn',
                'X-Cache',
                'CDN-Cache',
                'CDN-Server',
                'X-Cdn-Srv',
                'Cdn',
                'CDN',
                'Cache-Control',
                'X-Cache-Error',
                'X-Upper-Cache',
                "X-Cacheable",
                'X-Cacheable-status',
                'X-Status',
                'X-DNS',
                'X-Proxy',
                'CacheStatus',
                'X-Fastcgi-Cache',
                'X-Backend',
                'X-PingBack',
                'X-Executed-By',
                'X-Front',
                'X-Server',
                'CDN-Node',
                'X-Rack-Cache',
                'X-Request-Id',
                'X-Runtime',
            ]
            for cdn_head in cdn_headers:
                if cdn_head in self.header:
                    key = True
            return key
        except Exception as e:
            mylog('webprint').log.critical(pyfancy().red(e))
        return False

    """
    使用dig检测是否CDN
    return: bool
    """

    def useDig(self):
        mylog('webprint', True).log.info(pyfancy().green('[+]执行dig识别: {}'.format(self.url)))
        judge = judgement(self.url).urlSplit()[1]
        try:
            cmd = ['dig', judge]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()
            content_str = bytes.decode(out).lower()
            return content_str.strip()
        except Exception as e:
            mylog('webprint').log.critical(pyfancy().red(e))
            return 'NULL'

    """
    使用自定义识别CDN和WAF
    return: string
    """

    def myCdnWaf(self):
        key = list()
        mylog('webprint', True).log.info(pyfancy().green('[+]执行自定义CDN/WAF识别: {}'.format(self.url)))
        db = cdnwafidentity().cdnwafdb
        # 一维字典与二维字典的键值比较
        try:
            sdict = self.header
            for skey in sdict:
                for dkey in db:
                    if skey in db[dkey]:
                        if db[dkey][skey] in sdict[skey]:
                            key.append(dkey)
        except Exception as e:
            mylog('webprint').log.critical(pyfancy().red(e))
        key = list(set(key))
        return key

    """
    分析HTTP headers安全性
    return: list
    """

    def hsecscan(self):
        hlist = list()
        mylog('webprint', True).log.info(pyfancy().green('[+]执行headers安全检查: {}'.format(self.url)))
        try:
            headers = str(self.header)
            # secure flag
            if not re.search(r'secure;', headers, re.I):
                hlist.append('[+]Cookie without Secure flag set')
            # httponly flag
            if not re.search(r'httponly;', headers, re.I):
                hlist.append('[+]Cookie without HttpOnly flag set')
            # domain get
            if re.search(r'domain\=\S*', headers, re.I):
                domain = re.findall(r'domain\=(.+?);', headers, re.I)
                if domain:
                    hlist.append('[+]Session Cookie are valid only at Sub/Domain: %s' % domain[0])
            # path get
            if re.search(r'path\=\S*', headers, re.I):
                path = re.findall(r'path\=(.+?);', headers, re.I)
                if path:
                    hlist.append('[+]Session Cookie are valid only on that Path: %s' % path[0])
            # multiple cookie
            if re.search(r'(.+?)\=\S*;', headers, re.I):
                cookie_sessions = re.findall(r'(.+?)\=\S*;', headers, re.I)
                for cs in cookie_sessions:
                    if cs not in ['domain', 'path', 'expires']:
                        hlist.append('[+]Cookie Header contains multiple cookies')
                        break
            # x-xss-protection flag
            if not re.search(r'x-xss-protection', headers, re.I):
                hlist.append('[+]X-XSS-Protection header missing')
            # x-frame-options flag
            if not re.search(r'x-frame-options', headers, re.I):
                hlist.append('[+]Clickjacking: X-Frame-Options header missing')
            # content-type
            if not re.search(r'content-type', headers, re.I):
                hlist.append('[+]Content-Type header missing')
            # strict-transport-security flag
            if not re.search(r'strict-transport-security', headers, re.I):
                hlist.append('[+]Strict-Transport-Security header missing')
            # x-content-type-options flag
            if not re.search(r'x-content-type-options', headers, re.I):
                hlist.append('[+]X-Content-Type-Options header missing')
            # content-security-policy flag
            if not re.search(r'content-security-policy', headers, re.I):
                hlist.append('[+]Content-Security-Policy header missing')
            # x-permitted-cross-domain-policies
            if not re.search(r'x-permitted-cross-domain-policies', headers, re.I):
                hlist.append('[+]X-Permitted-Cross-Domain-Policies header missing')
            # referrer-policy
            if not re.search(r'referrer-policy', headers, re.I):
                hlist.append('[+]Referrer-Policy header missing')

        except Exception as e:
            mylog('webprint').log.critical(pyfancy().red(e))
        return hlist

    """
    使用Wappalyzer识别web指纹
    return: string
    """

    def useWappalyzer(self):
        out = ''
        mylog('webprint', True).log.info(pyfancy().green('[+]执行Wappalyzer识别目标指纹: {}'.format(self.url)))
        try:
            wappalyzer = Wappalyzer.latest()
            webpage = WebPage.new_from_url(self.url)
            webprints = wappalyzer.analyze(webpage)
            if len(webprints) > 0:
                return webprints
            else:
                return {}
        except Exception as e:
            mylog('webprint').log.critical(pyfancy().red(e))
        return out

    """
    使用Python库builtwith识别前端服务
    return: dict
    """

    def useBuiltwith(self):
        # 全局取消SSL证书验证
        ssl._create_default_https_context = ssl._create_unverified_context
        mylog('webprint', True).log.info(pyfancy().green('[+]执行builtwith识别前端组件: {}'.format(self.url)))
        res = builtwith.builtwith(self.url)
        return res

    """
    使用系统命令whatweb识别后端服务
    return: string
    """

    def useWhatweb(self):
        out = ''
        mylog('webprint', True).log.info(pyfancy().green('[+]执行whatweb识别后端组件: {}'.format(self.url)))
        try:
            cmd = ['whatweb', '-a', '3', '--color=never', self.url]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()
            out = bytes.decode(out)
        except Exception as e:
            mylog('webprint').log.critical(pyfancy().red(e))
        return out

    """
    使用whois识别网站注册信息
    return: string
    """

    def useWhois(self):
        mylog('webprint', True).log.info(pyfancy().green('[+]执行whois检查注册信息: {}'.format(self.url)))
        judge = judgement(self.url).urlSplit()[1]
        try:
            domain_reg = whois.whois(judge)
            return domain_reg
        except Exception as e:
            mylog('webprint').log.critical(pyfancy().red(e))
            return {}

    """
    获取远程静态文件md5
    return: string
    """

    def getchecksum(self, prefix):
        headers = {
            'User-Agent': findProxy().randomUA()
        }
        req = requests.get(urljoin(self.url, prefix), headers=headers, timeout=20, verify=False)
        md5sum = hashlib.md5(req.content).hexdigest()
        return md5sum

    """
    判断404页面
    return: bool
    """

    def check404(self, url):
        try:
            req = requests.head(urljoin(url, '534f3c824a9d63a84df8e87f9516857c'), timeout=20, verify=False)
            if req.status_code == 404:
                return True
            else:
                return False
        except:
            pass

    """
    获取404页面字节数
    return: integer
    """

    def get404length(self, url):
        try:
            req = requests.get(urljoin(url, '534f3c824a9d63a84df8e87f9516857c'), timeout=20, verify=False)
            self.length = len(req.text)
        except:
            pass

    """
    正则匹配cms关键字
    return: bool
    """

    def pregmatch(self, prefix, keyword):
        headers = {
            'User-Agent': findProxy().randomUA()
        }
        try:
            req = requests.get(urljoin(self.url, prefix), headers=headers, allow_redirects=True, timeout=20,
                               verify=False)
            match = re.search(keyword, bytes.decode(req.content, encoding='utf-8'), re.IGNORECASE)
            try:
                if match:
                    return True
                else:
                    return False
            except:
                return False
        except:
            return False

    """
    不使用代理发送head请求探测路径是否存在
    return: string
    """

    def sendrequesthead(self, url):
        headers = {
            'User-Agent': findProxy().randomUA(),
            'X-Forwarded-For': findProxy().randomXFF(),
        }
        try:
            req = requests.head(url, headers=headers, timeout=20, verify=False)
            if req.status_code == 200:
                return url
        except Exception as e:
            mylog('webprint').log.critical(pyfancy().red(e))

    """
    不使用代理发送get请求探测路径是否存在
    return: string
    """

    def sendrequestget(self, url):
        headers = {
            'User-Agent': findProxy().randomUA(),
            'X-Forwarded-For': findProxy().randomXFF(),
        }
        try:
            req = requests.get(url, headers=headers, timeout=20, verify=False)
            if req.status_code == 200:
                if len(req.text) == self.length or len(req.text) - 32 == self.length:
                    pass
                else:
                    return url
        except Exception as e:
            mylog('webprint').log.critical(pyfancy().red(e))

    """
    使用代理发送head请求探测路径是否存在
    return: string
    """

    def sendproxyrequesthead(self, url):
        headers = {
            'User-Agent': findProxy().randomUA(),
            'X-Forwarded-For': findProxy().randomXFF(),
        }
        proxies = {
            'http': 'http://{}'.format(random.choice(self.proxies))
        }
        try:
            req = requests.head(url, proxies=proxies, headers=headers, timeout=20, verify=False)
            if req.status_code == 200:
                return url
        except Exception as e:
            mylog('webprint').log.critical(pyfancy().red(e))

    """
     使用代理发送get请求探测路径是否存在
     return: string
     """

    def sendproxyrequestget(self, url):
        headers = {
            'User-Agent': findProxy().randomUA(),
            'X-Forwarded-For': findProxy().randomXFF(),
        }
        proxies = {
            'http': 'http://{}'.format(random.choice(self.proxies))
        }
        try:
            req = requests.get(url, proxies=proxies, headers=headers, timeout=20, verify=False)
            if req.status_code == 200:
                return url
        except Exception as e:
            mylog('webprint').log.critical(pyfancy().red(e))

    """
    使用内建CMS识别技术
    return: list
    """

    def useCmsprint(self, proxy):
        mylog('webprint', True).log.info(pyfancy().green('[+]执行cms识别通用系统信息: {}'.format(self.url)))
        urls = list()
        prefix_urls = list()
        cmsname = list()
        """
        提取静态文件md5方式
        """
        sql = "SELECT staticurl FROM cmsprint"
        for item in db().execute(sql):
            prefix_urls.append(item['staticurl'])
        # 去除空元素和重复元素
        prefix_urls = list(set(filter(None, prefix_urls)))
        # 组合url
        for item in prefix_urls:
            urls.append(self.url + item)
        # 设置并发协程
        pool = Pool(30)
        if proxy:
            proxyclass = findProxy()
            proxyclass.search()
            proxyclass.connectest(self.url)
            self.proxies = proxyclass.proxylist
            if self.check404(self.url):
                checksumlist = list(set(filter(None, pool.map(self.sendproxyrequesthead, urls))))
            else:
                self.get404length(self.url)
                checksumlist = list(set(filter(None, pool.map(self.sendproxyrequestget, urls))))
        else:
            if self.check404(self.url):
                checksumlist = list(set(filter(None, pool.map(self.sendrequesthead, urls))))
            else:
                self.get404length(self.url)
                checksumlist = list(set(filter(None, pool.map(self.sendrequestget, urls))))

        if checksumlist:
            # 重新置空
            prefix_urls = []
            for item in checksumlist:
                prefix_urls.append(urlparse(item)[2])
            cms_set = db().execute('SELECT cmsname, staticurl, checksum FROM cmsprint WHERE staticurl!=""')
            for text in prefix_urls:
                md5sum = self.getchecksum(text)
                for item in cms_set:
                    if md5sum in item['checksum']:
                        cmsname.append(item['cmsname'])
                        mylog('cmsprint').log.debug(
                            pyfancy().blue('匹配到cms: {0} {1}'.format(item['cmsname'], item['checksum'])))

        """
        搜索页面关键字方式
        """
        urls = []
        prefix_urls = []
        sql = "SELECT homeurl FROM cmsprint"
        for item in db().execute(sql):
            prefix_urls.append(item['homeurl'])
        # 去除空元素和重复元素
        prefix_urls = list(set(filter(None, prefix_urls)))
        # 组合url
        for item in prefix_urls:
            urls.append(self.url + item)
        pool = Pool(30)
        if proxy:
            if self.check404(self.url):
                preglist = list(set(filter(None, pool.map(self.sendproxyrequesthead, urls))))
            else:
                self.get404length(self.url)
                preglist = list(set(filter(None, pool.map(self.sendproxyrequestget, urls))))
        else:
            if self.check404(self.url):
                preglist = list(set(filter(None, pool.map(self.sendrequesthead, urls))))
            else:
                self.get404length(self.url)
                preglist = list(set(filter(None, pool.map(self.sendrequestget, urls))))

        if preglist:
            # 重新置空
            prefix_urls = []
            for item in preglist:
                prefix_urls.append(urlparse(item)[2])
            cms_set = db().execute('SELECT cmsname, homeurl, keyword FROM cmsprint WHERE homeurl!=""')
            for text in prefix_urls:
                for item in cms_set:
                    if item['homeurl'] in text:
                        if self.pregmatch(text, item['keyword']):
                            cmsname.append(item['cmsname'])
                            mylog('cmsprint').log.debug(pyfancy().blue(
                                '匹配到cms: {0} {1} {2}'.format(item['cmsname'], item['homeurl'], item['keyword'])))

        # 去重cmsname
        cmsname = list(set(cmsname))
        return cmsname
'''
a = explore('http://www.apache.org')
print(a.useWappalyzer())
'''
