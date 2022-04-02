# SatanSword
***红队综合渗透框架***

[![python](https://img.shields.io/badge/python-3.x-blue.svg?logo=python&labelColor=yellow)](https://www.python.org/downloads/)
[![platform](https://img.shields.io/badge/platform-osx%2Flinux-green.svg)](https://github.com/Lucifer1993/SatanSword/)
[![Github Stars](https://img.shields.io/github/stars/Lucifer1993/SatanSword)](https://github.com/Lucifer1993/SatanSword) 
[![GitHub forks](https://img.shields.io/github/forks/Lucifer1993/SatanSword)](https://github.com/Lucifer1993/SatanSword)
![license](https://img.shields.io/badge/License-GPL--3.0-yellow.svg)
![release](https://img.shields.io/badge/Release-v0.1-orange.svg)


### >>>Docker使用(同时集成了AngelSword)
- 1.拉取镜像 docker pull fuckuanywhere/satansword
- 2.执行命令 docker run -ti fuckuanywhere/satansword /bin/bash -c "service mysql start && python3 /root/SatanSword/SatanSword.py"

### >>>功能描述
- web指纹识别，集成whatweb及wappalyzer所有指纹及自己收集的web服务器指纹1839条+cms指纹1936条。

- 漏洞PoC检测，提供360+PoC检测脚本内置在数据库中，同时支持漏洞查询和代码查看及一键批量检测功能。

- 批量web信息和端口信息查询，web信息包括headers，whois，dig，CDN检测，指纹检测，IP位置检测。端口扫描使用masscan+nmap探测常用端口指纹服务。

- 路径扫描，集成dirsearch的路径字典，通过GET和HEAD两种方法实现。

- 批量JS查找子域名，参考某大佬写的脚本直接拿过来改了一下，后面会贴上地址链接。

- 协程支持。

- 使用google headless，更精准的XSS检测。

- 完整的日志回溯。

### >>>环境设置
- **安装python3+模块+系统命令+配置api文件**

 ![image](https://github.com/Lucifer1993/SatanSword/raw/master/img/checkenv.png)
**修改conf/config.py，在对应的参数中填入自己辅助接口的信息**
 ![image](https://github.com/Lucifer1993/SatanSword/raw/master/img/config.png)

- **新建mysql数据库名“SatanSword”，导入Heaven_Hell/backuptables路径下面的所有SQL文件**

- **保证下载的chromedriver和chromium版本一致**
 ![image](https://github.com/Lucifer1993/SatanSword/raw/master/img/chromedriver.png)

### >>>使用说明

- **设置或取消线程数、cookies**
 ![image](https://github.com/Lucifer1993/SatanSword/raw/master/img/use1.png)

- **对多个目标执行多个POC**
 ![image](https://github.com/Lucifer1993/SatanSword/raw/master/img/use2.png)

- **所有成功和失败的利用都会写入数据库和日志文件**
![image](https://github.com/Lucifer1993/SatanSword/raw/master/img/use3.png)

- **CMS指纹识别**
![image](https://github.com/Lucifer1993/SatanSword/raw/master/img/use4.png)

- **web和ip信息识别，sniper用于单一IP或URL，批量请使用bomber，结果自动保存到数据库中**
![image](https://github.com/Lucifer1993/SatanSword/raw/master/img/use5.png)

- **JS文件批量检索子域名**
![image](https://github.com/Lucifer1993/SatanSword/raw/master/img/use6.png)

### >>>感谢如下优秀开源项目

## https://github.com/nmap/nmap

## https://github.com/robertdavidgraham/masscan

## https://github.com/knownsec/pocsuite3

## https://github.com/Threezh1/JSFinder

## https://github.com/urbanadventurer/WhatWeb

## https://github.com/chorsley/python-Wappalyzer

### >>>特别说明

***1.本项目中的所有PoC代码全部转移到 https://github.com/Lucifer1993/PoCHub ，提供json和sql两种文件格式。***

***2.请遵守《中华人民共和国网络安全法》，禁止将代码用于未授权测试及破坏行为。***
