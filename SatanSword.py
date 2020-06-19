#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Lucifer
# Date: 2018.11.22
from gevent import monkey;

monkey.patch_all()
from gevent.pool import Pool
import gevent
import re
import os
import emoji
import simplejson
import readline
import subprocess
readline.parse_and_bind('tab: complete')
from cmd2 import Cmd
import prettytable as pt
import urllib.parse
from Evil_Eye.Analysis import judgement
from conf.termcolor import cprint
from conf.config import GlobalConf
from Backtracking.SatanLogging import mylog
from pyfancy.pyfancy import pyfancy
from conf.precheck import Envcheck
from Evil_Eye.cdnwaf import cdnwafidentity
from Heaven_Hell.database import db
from http.cookies import SimpleCookie
from Evil_Eye.webprint import explore
from Endless_Sword.dirbrute import dirsearch
from Endless_Sword.cmsexploit import webpocfactory
from Endless_Sword.hostexploit import hostpocfactory
from Soulcontrol.Scheduler import webschedule
from Soulcontrol.Scheduler import hostschedule
from Endless_Sword.sytax_highlight import runhighlighting

class Mainclass:
	def __init__(self):
		pass

	def check(self):
		if Envcheck().modulecheck() is not True:
			cprint('[-]检查Python模块失败!!!', 'red')
			exit(1)
		if Envcheck().commandcheck() is not True:
			cprint('[-]检查命令模块失败!!!', 'red')
			exit(1)
		if Envcheck().apicheck() is not True:
			cprint('[-]检查api模块失败!!!', 'red')
			exit(1)

class SatanCmd(Cmd):
	prompt = r'SatanSword{0}=>>> '.format(emoji.emojize(':high_voltage:' * 1))
	"""
	intro = r'''
			  ____        _              ____                       _
			 / ___|  __ _| |_ __ _ _ __ / ___|_      _____  _ __ __| |
			 \___ \ / _` | __/ _` | '_ \\___ \ \ /\ / / _ \| '__/ _` |
			  ___) | (_| | || (_| | | | |___) \ V  V / (_) | | | (_| |
			 |____/ \__,_|\__\__,_|_| |_|____/ \_/\_/ \___/|_|  \__,_|
			'''
	"""

	def __init__(self):
		Cmd.__init__(self)
		self.set_window_title('SatanSword Terminal')
		self.threads = 10
		self.cookies = {}
		self.domains = []

	"""
	sniper针对单一目标进行渗透攻击
	"""

	def do_sniper(self, args):
		if len(str(args)) == 0:
			cprint('[!]命令sniper用法:\n\tsniper [web/host] project target', 'red')
		else:
			type = args.split()[0]
			project = args.split()[1]
			url = args.split()[2]
			if type in r'web':
				try:
					webInstance = webschedule(project, url, self.cookies)
					webInstance.runexplore(url)
				except Exception as e:
					cprint('[!]web调度错误!! 原因: {0}'.format(e))
			elif type in r'host':
				try:
					hostInstence = hostschedule(project, url)
					hostInstence.runexplore()
				except Exception as e:
					cprint('[!]host调度错误!! 原因: {0}'.format(e))
			else:
				cprint('[!]命令sniper用法:\n\tsniper [web/host] project target', 'red')

	"""
	bomber协程For WEB
	"""

	def routineWeb(self, project, url):
		webinstance = webschedule(project, url, {})
		webinstance.runexplore(url)

	"""
	bomber协程For HOST
	"""

	def routineHost(self, project, host):
		hostInstance = hostschedule(project, host)
		hostInstance.runexplore()

	"""
	bomber针对文件列表里的目标批量渗透攻击
	"""

	def do_bomber(self, args):
		if len(str(args)) == 0:
			cprint('[!]命令bomber用法:\n\tbomber [web/host] file', 'red')
		else:
			type = args.split()[0]
			filepath = args.split()[1]
			if type in 'web':
				urlist = []
				if os.path.isfile(filepath):
					with open(filepath) as f:
						for line in f.readlines():
							line = line.strip()
							urlist.append(line)
					project = input('[*]请设置project标签: ')
					process_num = input('[*]请设置进程并发数: ')
					ppool = Pool(int(process_num))
					threads = [ppool.spawn(self.routineWeb, project, url) for url in urlist]
					gevent.joinall(threads)
			elif type in 'host':
				hostlist = []
				if os.path.isfile(filepath):
					with open(filepath) as f:
						for line in f.readlines():
							line = line.strip()
							hostlist.append(line)
					project = input('[*]请设置project标签: ')
					process_num = input('[*]请设置进程并发数: ')
					ppool = Pool(int(process_num))
					threads = [ppool.spawn(self.routineHost, project, host) for host in hostlist]
					gevent.joinall(threads)

			else:
				cprint('[!]不是有效文件!!!', 'red')

	"""
	统计扫描器状态
	"""

	def do_status(self, instance=None):
		tb = pt.PrettyTable()
		tb.field_names = ['实例类型', '实例状态', '实例值']
		database = db()

		# MYSQL状态
		if database.connectdb():
			dbstatus = '已连接'
		else:
			dbstatus = '未连接'
		dbsize = database.execute(
			'SELECT CONCAT(ROUND(SUM(INDEX_LENGTH)+SUM(DATA_LENGTH)/(1024*1024),2),"MB") AS "数据库容量" FROM information_schema.tables WHERE table_schema="SatanSword"')[
			0]
		tb.add_row(['MySQL', dbstatus, dbsize])

		# CMS模块状态
		table_status = \
		database.execute('SELECT table_name FROM information_schema.TABLES WHERE table_name ="cmsprint"')[0]
		if table_status['TABLE_NAME'] == 'cmsprint':
			table_status = '已加载'
		else:
			table_status = '未加载'
		count = database.execute('SELECT COUNT(DISTINCT(cmsname)) AS "cms种类" FROM cmsprint')[0]
		checksum_num = database.execute('SELECT count(*) AS "Md5指纹" FROM cmsprint WHERE checksum !=""')[0]
		keyword_num = database.execute('SELECT count(*) AS "正则指纹" FROM cmsprint WHERE keyword !=""')[0]
		tb.add_row(['CMS指纹识别模块', table_status, dict(**count, **checksum_num, **keyword_num)])

		# CDN/WAF模块状态
		cdnwafdict = cdnwafidentity().cdnwafdb
		cdnwafcount = len(cdnwafdict)
		printcount = 0
		for item in cdnwafdict.values():
			printcount += len(item)
		tb.add_row(['CDN/WAF模块', '已加载', dict(**{"cdn/waf种类": cdnwafcount}, **{"cdn/waf指纹": printcount})])

		# WEB POC模块状态
		table_status = \
		database.execute('SELECT table_name FROM information_schema.TABLES WHERE table_name ="webexploit"')[0]
		if table_status['TABLE_NAME'] == 'webexploit':
			table_status = '已加载'
		else:
			table_status = '未加载'
		poccount = database.execute('SELECT COUNT(DISTINCT(vulname)) AS "可利用poc数" FROM webexploit')[0]
		tb.add_row(['CMS漏洞验证模块', table_status, dict(**poccount)])

		# HOST POC模块状态
		table_status = \
		database.execute('SELECT table_name FROM information_schema.TABLES WHERE table_name ="hostexploit"')[0]
		if table_status['TABLE_NAME'] == 'hostexploit':
			table_status = '已加载'
		else:
			table_status = '未加载'
		poccount = database.execute('SELECT COUNT(DISTINCT(vulname)) AS "可利用poc数" FROM hostexploit')[0]
		expcount = database.execute('SELECT COUNT(DISTINCT(exp)) AS "可利用exp数" FROM hostexploit')[0]
		tb.add_row(['HOST漏洞验证模块', table_status, dict(**poccount, **expcount)])

		cprint(tb, 'yellow')

	"""
	搜索漏洞、POC、文章函数
	"""

	def do_search(self, args):
		if len(str(args)) == 0:
			cprint('[!]命令search用法:\n\tsearch keyword', 'red')
		else:
			database = db()
			keyword = args.split()[0]
			# 查询webexploit和hostexploit做表连接
			sqlstring = 'SELECT vulname, description, level, param FROM (SELECT vulname, description, level, param FROM webexploit WHERE vulname LIKE "%{0}%") AS t1 UNION ALL SELECT vulname, description, level, param FROM (SELECT vulname, description, level, param FROM hostexploit WHERE vulname LIKE "%{1}%") AS t2'.format(
				keyword, keyword)
			search_result = database.execute(sqlstring)
			tb = pt.PrettyTable()
			tb.field_names = ['漏洞名称', '漏洞描述', '漏洞等级', '传递参数']
			for item in search_result:
				tb.add_row([item['vulname'], item['description'], item['level'], item['param']])
			cprint(tb, 'magenta', attrs=['bold'])
			cprint("[+]"+"="*20+"|        搜索到{0}个POC        |".format(len(search_result))+"="*20, "green")

	"""
	查看漏洞POC，文章函数，exploitdb
	"""

	def do_show(self, args):
		if len(str(args)) == 0:
			cprint('[!]命令show用法:\n\tshow [poc] vulname', 'red')
		else:
			database = db()
			type = args.split()[0]
			showname = args.split()[1]
			if type in r'poc':
				sqlstring = 'SELECT poc FROM (SELECT poc FROM webexploit WHERE vulname="{0}") AS t1 UNION ALL SELECT poc FROM (SELECT poc FROM hostexploit WHERE vulname="{1}") AS t2'.format(
					showname, showname)
				show_result = database.execute(sqlstring)
				sourcecode = show_result[0]['poc']
				if sourcecode is None:
					cprint('[!] Wooo! 没有poc代码!!!', 'red')
				else:
					print('\n')
					runhighlighting(sourcecode)
					print('\n')

			elif type in r'vuldb':
				sqlstring = 'SELECT filed FROM exploitdb WHERE id={0}'.format(showname)
				show_result = database.execute(sqlstring)
				exploitcode = show_result[0]['filed']
				print('\n')
				try:
					runhighlighting(exploitcode)
				except:
					runhighlighting('"""\n{0}\n"""'.format(exploitcode))
				print('\n')

			else:
				cprint('[!]命令show用法:\n\tshow [poc/vuldb] vulname', 'red')

	"""
	webexploit多url执行函数
	"""

	def webexecfile(self, target, vulname):
		exploit = webpocfactory(target, self.cookies, self.threads)
		exploit.runpocwithcmsname(vulname)
		gevent.sleep(0)

	"""
	hostexploit多url执行函数
	"""

	def hostexecfile(self, target, vulname):
		host = target.split(':')[0]
		port = target.split(':')[1]
		exploit = hostpocfactory(host, port, self.threads)
		exploit.runpocwithsysname(vulname)
		gevent.sleep(0)

	"""
	webexploit检查漏洞执行结果
	"""

	def webexeccheck(self, url):
		if isinstance(url, list):
			sqlstring = 'SELECT * FROM webvulnlist WHERE isvul="True" AND url in ({})'.format(
				','.join(["'%s'" % x for x in url]))
		else:
			sqlstring = 'SELECT * FROM webvulnlist WHERE isvul="True" AND url="{}"'.format(url)
		show_result = db().execute(sqlstring)
		tb = pt.PrettyTable()
		tb.field_names = ['URL', 'VULNAME', 'VURL', 'ISVUL', 'PAYLOAD', 'PROOF', 'EXCEPTION']
		for item in show_result:
			tb.add_row([item['url'], item['vulname'], item['vulnurl'], item['isvul'], item['payload'], item['proof'],
			            item['exception']])
		cprint(tb, 'red')

	"""
	hostexploit检查漏洞执行结果
	"""

	def hostexeccheck(self, host):
		if isinstance(host, list):
			sqlstring = 'SELECT * FROM hostvulnlist WHERE isvul="True" AND vulnhost in ({})'.format(
				','.join(["'%s'" % x for x in host]))
		else:
			sqlstring = 'SELECT * FROM hostvulnlist WHERE isvul="True" AND vulnhost="{}"'.format(host)
		show_result = db().execute(sqlstring)
		tb = pt.PrettyTable()
		tb.field_names = ['HOST', 'PORT', 'VULNAME', 'ISVUL', 'PAYLOAD', 'PROOF', 'EXCEPTION']
		for item in show_result:
			tb.add_row(
				[item['vulnhost'], item['vulnport'], item['vulnname'], item['isvul'], item['payload'], item['proof'],
				 item['exception']])
		cprint(tb, 'red')

	"""
	漏洞exploit函数
	"""

	def do_exploit(self, args):
		try:
			if len(str(args)) == 0:
				cprint('[!]命令exploit用法:\n\texploit [web/host] vulname target', 'red')
			else:
				type = args.split()[0]
				vulname = args.split()[1]
				target = args.split()[2]
				if type in r'web':
					exploit = webpocfactory(target, self.cookies, self.threads)
					if r'http' in target:
						exploit.runpocwithcmsname(vulname)
						self.webexeccheck(target)
					else:
						explist = list()
						pool = Pool(10)
						with open(target, 'r') as f:
							for targetline in f.readlines():
								explist.append(targetline.strip('\n').strip())
						threads = [pool.spawn(self.webexecfile, item, vulname) for item in explist]
						gevent.joinall(threads)
						self.webexeccheck(explist)

				elif type in r'host':
					if re.match(r'[0-9]+.[0-9]+.[0-9]+.[0-9]+', target):
						host = target.split(':')[0]
						port = target.split(':')[1]
						exploit = hostpocfactory(host, port, self.threads)
						exploit.runpocwithsysname(vulname)
						self.hostexeccheck(host)
					else:
						pool = Pool(10)
						explist = list()
						tmpexplist = list()
						with open(target, 'r') as f:
							for targetline in f.readlines():
								explist.append(targetline.strip('\n').strip())
						threads = [pool.spawn(self.hostexecfile, item, vulname) for item in explist]
						gevent.joinall(threads)
						for item in explist:
							tmpexplist.append(item.split(":")[0])
						self.hostexeccheck(tmpexplist)

				else:
					cprint('[!]命令exploit用法:\n\texploit [web/host] vulname target', 'red')
		except Exception as e:
			print(e)

	"""
	jsfinder routine函数
	"""

	def jsfinder_routine(self, url):
		mylog('webprint', True).log.info(pyfancy().green('[+]搜集目标url: {0}'.format(url)))
		judge = judgement(url)
		subdomain = judge.giveresult(judge.find_by_url(), urllib.parse.urlparse(url)[1])
		print(subdomain)
		self.domains += subdomain
		self.domains = list(set(self.domains))
		gevent.sleep(0)

	"""
	JSFinder
	return list
	"""

	def do_jsfinder(self, args):
		if len(str(args)) == 0:
			cprint('[!]命令jsfinder用法:\n\tjsfinder filename', 'red')
		else:
			try:
				pool = Pool(20)
				urllist = list()
				with open(args, 'r') as fp:
					for line in fp.readlines():
						urllist.append(line.strip('\n').strip())
				threads = [pool.spawn(self.jsfinder_routine, item) for item in urllist]
				gevent.joinall(threads)
				print('[+]JSFinder搜集子域名如下:\n')
				for subdom in self.domains:
					cprint('http://' + subdom, 'green')
				self.domains = []
			except:
				cprint('[!]请载入url文件!!!', 'red')

	"""
	设置和显示全局变量函数
	"""

	def do_config(self, args):
		if len(str(args)) == 0:
			tb = pt.PrettyTable()
			tb.field_names = ['配置名称', '属性值']
			tb.add_row(['threads', self.threads])
			tb.add_row(['cookies', self.cookies])
			cprint(tb, 'yellow')
		else:
			keyname = args.split()[0]
			valuename = args.split()[1]
			if keyname in r'cookies':
				try:
					with open(valuename, 'r') as fp:
						mycookie = SimpleCookie()
						mycookie.load(fp.read())
						self.cookies = {key: morsel.value for key, morsel in mycookie.items()}
				except:
					cprint('[!]请载入cookies文件!!!', 'red')
			if keyname in r'threads':
				self.threads = int(valuename)

	"""
	取消全局设置函数
	return: None
	"""

	def do_unconfig(self, args):
		if len(str(args)) == 0:
			cprint('[!]命令unconfig用法:\n\tunconfig keyname', 'red')
		else:
			if args in "cookies":
				self.cookies = {}
			if args in "threads":
				self.threads = 10

	"""
	cms指纹识别
	return: list
	"""

	def do_whatcms(self, args):
		if len(str(args)) == 0:
			cprint('[!]命令whatcms用法:\n\twhatcms targeturl', 'red')
		else:
			runApp = explore(args.strip())
			print(runApp.useCmsprint(False))

	"""
	web路径爆破
	return: list
	"""

	def do_dirsearch(self, args):
		if len(str(args)) == 0:
			cprint('[!]命令dirsearch用法:\n\tdirsearch targeturl', 'red')
		else:
			runApp = dirsearch(args.strip())
			runApp.run()

	"""
	clear清屏函数
	"""

	def do_clear(self, cl):
		cl = lambda: os.system('clear')
		cl()

	"""
	exit退出函数
	"""

	def do_exit(self, args):
		exit(0)
	"""
	banner函数
	"""

	def do_banner(self, args):
		args = '''
                             /   ))     |\         )               ).
               c--. (\  ( `.    / )  (\   ( `.     ).     ( (
               | |   ))  ) )   ( (   `.`.  ) )    ( (      ) )
               | |  ( ( / _..----.._  ) | ( ( _..----.._  ( (
 ,-.           | |---) V.'-------.. `-. )-/.-' ..------ `--) \._
 | /===========| |  (   |      ) ( ``-.`\/'.-''           (   ) ``-._
 | | / / / / / | |--------------------->  <-------------------------_>=-
 | \===========| |                 ..-'./\.`-..                _,,-'
 `-'           | |-------._------''_.-'----`-._``------_.-----'
               | |         ``----''            ``----''
               | |
               c--`       SatanSword
        '''
		cprint(args, 'magenta', attrs=['bold'])

	"""
	获取版本函数
	"""

	def do_version(self, args):
		args = 'v0.1'
		cprint(args, 'cyan')

if __name__ == '__main__':
	"""
	Satan主类调用
	"""
	SatanMain = Mainclass()
	SatanMain.check()

	"""
	Satan命令行循环
	"""
	appActive = SatanCmd()
	appActive.cmdloop()
