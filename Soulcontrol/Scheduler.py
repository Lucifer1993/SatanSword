#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lucifer
# @Time    : 2018/12/1 11:54 PM
# @File    : Scheduler.py
# @Software: PyCharm
from gevent import monkey;monkey.patch_all()
from gevent.pool import Pool
import gevent
import os
import sys
import time
import pymysql
sys.path.append('..')
from Evil_Eye.webprint import explore
from pyfancy.pyfancy import pyfancy
from conf.config import GlobalConf
from urllib.parse import urlparse
from Evil_Eye.Analysis import judgement
from Heaven_Hell.database import db
from Evil_Eye.hostprint import scanhost
from Backtracking.SatanLogging import mylog

"""
web调度类
"""
class webschedule:
    def __init__(self, project, url, cookies):
        self.url = url
        self.project = project
        self.cookies = cookies

    """
    html start函数
    return:string
    """
    def html_start(self):
        return '''
        <html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></meta><title>SatanSword</title><style type="text/css" media="all">
                    html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video {
                        margin: 0;
                        padding: 0;
                        border: 0;
                        font-size: 100%;
                        font: inherit;
                        vertical-align: baseline;
                        -webkit-text-size-adjust: none;
                    }

                    html, body {
                        font-family: 'Helvetica Neue', 'Segoe UI', helvetica, arial, sans-serif;
                        width: 100%;
                        color: #333;
                        font-size: 13px;
                        background: #efefef;
                    }

                    a, a:visited, a:active {
                        color: #0071b9;
                        text-decoration: none;
                    }

                    a:hover {
                        color: #0071b9;
                        text-decoration: underline;
                    }

                    .clear {
                        clear: both;
                        width: 0 !important;
                        height: 0 !important;
                        margin: 0 !important;
                        padding: 0 !important;
                    }

                    table {
                        table-layout: fixed;
                        width: 100%;
                        border-collapse: collapse;
                        border-spacing: 0;
                    }

                    .plugin-row-header {
                        height: 35px;
                        line-height: 35px;
                        background: #f5f5f5;
                        font-size: 12px;
                        border: 1px solid #ddd;
                    }

                    .plugin-row {
                        height: 40px;
                        border: 1px solid #ddd;
                    }

                    .plugin-row td {
                        padding: 10px 0;
                        line-height: 20px;
                    }

                    .table-wrapper.details,
                    .table-wrapper.see-also {
                        margin: 0 0 20px 0;
                    }

                    .table-wrapper.details > table > tbody > tr > td {
                        padding: 5px 0;
                    }

                    .button {
                        display: block;
                        float: left;
                        line-height: 30px;
                        background: #eee;
                        border-radius: 3px;
                        cursor: pointer;
                        padding: 0 15px;
                    }

                    .button:hover {
                        background: #ccc;
                    }

                    .expand {
                        display: block;
                        float:right;
                        font-size: 12px;
                        color: #0071b9;
                        cursor: pointer;
                        font-weight: normal;
                        line-height: 20px;
                        margin: 0 0 0 10px;
                    }

                    .expand:hover {
                        text-decoration: underline;
                    }

                    .expand-spacer {
                        display: block;
                        float:right;
                        font-size: 12px;
                        font-weight: normal;
                        line-height: 20px;
                        margin: 0 0 0 10px;
                    }

                    .details-header {
                        font-size: 14px;
                        font-weight: bold;
                        padding: 0 0 5px 0;
                        margin: 0 0 5px 0;
                        border-bottom: 1px dotted #ccc;
                    }

                    .offline {
                        background-image: -webkit-repeating-linear-gradient(135deg, transparent, transparent 5px, rgba(255, 255, 255, .2) 5px, rgba(255, 255, 255, .2) 10px) !important;
                        background-image: repeating-linear-gradient(135deg, transparent, transparent 5px, rgba(255, 255, 255, .2) 5px, rgba(255, 255, 255, .2) 10px) !important;
                    }

                    .acas-header {
                        padding: 0 10px;
                    }

                    .acas-header,
                    .acas-footer > h1 {
                        color: #fff;
                        font-weight: bold;
                        font-size: 15px;
                        text-align: center;
                    }
                </style><script type="text/javascript">
                        var toggle = function (id) {
                            var div = document.getElementById(id);
                            var button = document.getElementById(id + '-show');

                            if (!div || !button) {
                                return;
                            }

                            if (div.style.display === '' || div.style.display === 'block') {
                                button.style.display = 'block';
                                div.style.display = 'none';
                                return;
                            }

                            button.style.display = 'none';
                            div.style.display = 'block';
                        };

                        var toggleAll = function (hide) {
                            if (document.querySelectorAll('div.section-wrapper').length) {
                                toggleAllSection(hide);
                                return;
                            }
                            
                            var divs = document.querySelectorAll('div.table-wrapper');

                            for (var i = 0, il = divs.length; i < il; i++) {
                                var id = divs[i].getAttribute('id');
                                var div = document.getElementById(id);
                                var button = document.getElementById(id + '-show');

                                if (div && button) {
                                    if (hide) {
                                        button.style.display = 'block';
                                        div.style.display = 'none';
                                        continue;
                                    }

                                    button.style.display = 'none';
                                    div.style.display = 'block';
                                }
                            }
                        };

                        var toggleSection = function (id) {
                            var div = document.getElementById(id);
                            var toggleText = document.getElementById(id.split('-')[0] + '-toggletext');

                            if (!div) {
                                return;
                            }

                            if (div.style.display !== 'none') {
                                toggleText.innerText = '+';
                                div.style.display = 'none';
                                return;
                            }

                            toggleText.innerText = '-';
                            div.style.display = 'block';
                        };

                        var toggleAllSection = function (hide) {
                            var divs = document.querySelectorAll('div.section-wrapper');

                            for (var i = 0, il = divs.length; i < il; i++) {
                                var id = divs[i].getAttribute('id');
                                var div = document.getElementById(id);
                                var toggleText = document.getElementById(id.split('-')[0] + '-toggletext');

                                if (div) {
                                    if (hide) {
                                        toggleText.innerText = '+';
                                        div.style.display = 'none';
                                        continue;
                                    }

                                    toggleText.innerText = '-';
                                    div.style.display = 'block';
                                }
                            }
                        };
                        </script></head><body><div style="width: 1024px; box-sizing: border-box; margin: 0 auto; background: #fff; padding: 0 20px 20px 20px; border-top: #263746 solid 3px; box-shadow: 0 2px 10px rgba(0, 0, 0, .2); margin-bottom: 20px; border-radius: 0 0 3px 3px;"><header style="width: 100%; border-bottom: 1px dotted #ccc; padding: 20px 0; margin: 0 0 20px 0;"><div style="float: left;"><h2 style="color: #999; text-align: right">SatanSword Report</h2></div><div class="clear"></div></header><div class="clear"></div><div class="clear"></div>
<div xmlns="" id="idp140317528712984" style="display: block;" class="table-wrapper ">
<table cellpadding="0" cellspacing="0">
        '''

    """
    html end函数
    return:string
    """
    def html_end(self):
        return '''
            </body></html>
        '''

    """
    webinfo模板生成函数
    return: string
    """
    def webinfo_template(self, funcname, result):
        return '''
        <div class="details-header">{0}<div class="clear"></div>
        </div>
        <div style="line-height: 20px; padding: 0 0 20px 0;">{1}<div class="clear"></div>
        </div>
        '''.format(funcname, result)

    def webinfo_header(self):
        return '''
            <div xmlns="" id="idp140317528730696" style="box-sizing: border-box; width: 100%; margin: 0 0 10px 0; padding: 5px 10px; background: #fdc431; font-weight: bold; font-size: 14px; line-height: 20px; color: #fff;" class="" onclick="toggleSection('idp140317528730696-container');" onmouseover="this.style.cursor='pointer'">WEB信息收集<div id="idp140317528730696-toggletext" style="float: right; text-align: center; width: 8px;">
                -
            </div>
        </div>
        <div xmlns="" id="idp140317528730696-container" style="margin: 0 0 45px 0;" class="section-wrapper">
        '''

    """
    web基础信息收集函数
    """
    def runexplore(self, url):
        mylog('webprint', True).log.info(pyfancy().green('[+]执行web信息收集: {}'.format(url)))
        runApp = explore(url)
        cdnheader = runApp.useCDNHeader()
        dig = runApp.useDig()
        getheaders = runApp.header
        whois = runApp.useWhois()
        builtwith = runApp.useBuiltwith()
        mycdn = runApp.myCdnWaf()
        wappalyzer = runApp.useWappalyzer()
        whatweb = runApp.useWhatweb()
        hsec = runApp.hsecscan()
        '''网页版模板
        webinfo_html = '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}'.format(
                                            self.html_start(),
                                            self.webinfo_header(),
                                            self.webinfo_template('通用CDN检测', cdnheader),
                                            self.webinfo_template('Dig CDN', dig),
                                            self.webinfo_template('Get Headers', getheaders),
                                            self.webinfo_template('Whois', whois),
                                            self.webinfo_template('builtwith', builtwith),
                                            self.webinfo_template('CDN/WAF Detect', mycdn),
                                            self.webinfo_template('Wappalyzer', wappalyzer),
                                            self.webinfo_template('Whatweb', whatweb),
                                            self.webinfo_template('headers sec', hsec),
                                            self.html_end())
        dirpath = os.path.join(GlobalConf().progpath['location'], 'Heaven_Hell/webrecon')
        if not os.path.isdir(dirpath):
            os.makedirs(dirpath)
        filename = '{0}_{1}.html'.format(urlparse(url)[1], time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time())))
        pathname = os.path.join(dirpath, filename)
        with open(pathname, 'w') as f:
            f.write(webinfo_html)
        mylog('webprint', True).log.info(pyfancy().light_cyan('[+]web信息写入文件: {}'.format(pathname)))
        '''

        #数据库归并
        iprecon = judgement(self.url).iplocation()
        sqlstr = 'INSERT INTO webrecon (Project, URL, cdnheader, Dig, Headers, Whois, Builtwith, Mycdn, wappalyzer, Whatweb, Hsec, Iprecon) VALUE ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}", "{7}", "{8}", "{9}", "{10}", "{11}")'.format(self.project, self.url, cdnheader, dig, pymysql.escape_string(str(getheaders)), pymysql.escape_string(str(whois)), pymysql.escape_string(str(builtwith)), pymysql.escape_string(str(mycdn)), pymysql.escape_string(str(wappalyzer)), pymysql.escape_string(str(whatweb)), pymysql.escape_string(str(hsec)), pymysql.escape_string(str(iprecon)))
        db().execute(sqlstr)
        mylog('webprint', True).log.info(pyfancy().green('[*]结束web信息收集: {}'.format(url)))

"""
主机调度类
"""
class hostschedule:
    def __init__(self, project, host):
        self.project = project
        self.host = host
        self.hostrecon = scanhost(self.host)

    def routinetcp(self, port):
        service = self.hostrecon.useNmapServTCP(port)
        try:
            sqlstr = 'INSERT INTO hostrecon (Project, Host, Port, Service) VALUE ("{0}", "{1}", "{2}", "{3}")'.format(self.project, self.host, port, pymysql.escape_string(str(service)))
            db().execute(sqlstr)
        except Exception as e:
            mylog('hostprint').log.critical(pyfancy().red(e))

    def routineudp(self, port):
        service = self.hostrecon.useNmapServUDP(port)
        try:
            sqlstr = 'INSERT INTO hostrecon (Project, Host, Port, Service) VALUE ("{0}", "{1}", "{2}", "{3}")'.format(self.project, self.host, port, pymysql.escape_string(str(service)))
            db().execute(sqlstr)
        except Exception as e:
            mylog('hostprint').log.critical(pyfancy().red(e))

    def runexplore(self):
        mylog('hostprint', True).log.info(pyfancy().green('[+]执行host信息收集: {}'.format(self.host)))
        pool = Pool(10)
        tcp_ports_list = self.hostrecon.useMasscanTCP()
        mylog('hostprint', True).log.info(pyfancy().yellow('[+][{0}]{1}'.format(self.host, tcp_ports_list)))
        if len(tcp_ports_list) != 0:
            threads = [pool.spawn(self.routinetcp, item) for item in tcp_ports_list]
            gevent.joinall(threads)
        udp_ports_list = self.hostrecon.useMasscanUDP()
        mylog('hostprint', True).log.info(pyfancy().yellow('[+][{0}]{1}'.format(self.host, udp_ports_list)))
        if len(udp_ports_list) != 0:
            threads = [pool.spawn(self.routineudp, item) for item in udp_ports_list]
            gevent.joinall(threads)
        mylog('hostprint', True).log.info(pyfancy().green('[*]结束host信息收集: {}'.format(self.host)))
