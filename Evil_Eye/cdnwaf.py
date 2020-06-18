#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lucifer
# @Time    : 2018/12/10 7:58 AM
# @File    : cdnwaf.py.py
# @Software: PyCharm

class cdnwafidentity:
    def __init__(self):
        self.cdnwafdb = {
            "360waf": {
                "Server": "360wzws",
                "X-Powered-By": "360",
                "X-Powered-By-360WZB": "wangzhan.360.cn",
                "X-Safe-Firewall:": "zhuji.360.cn",
                "X-Powered-By-ANYU": "",
                "X-Powered-By-WZWS": "",
            },
            "360waf1": {
                "Server": "WWW Server",
            },
            "qianxin": {
                "Server": "qianxin-waf",
                "WZWS-RAY": "",
            },
            "YxlinkWAF(安恒)": {
                "Server": "YxlinkWAF",
            },
            "Topsec": {
                "Server": "Topsec",
            },
            "bfe": {
                "Server": "bfe/",
            },
            "anquanbao": {
                "Server": "ASERVER",
                "X-Powered-By-Anquanbao": "MISS",
            },
            "BigIP": {
                "Set-Cookie": "BIGipServer",
                "Server": "BigIP",
            },
            "BigIP2": {
                "Set-Cookie": "LastMRH_Session",
            },
            "BinarySEC": {
                "x-binarysec-cache": "i",
                "X-BinarySEC-Via": "com",
            },
            "BlockDoS": {
                "Server": "BlockDOS",
            },
            "CloudFlare": {
                "Server": "cloudflare",
                "Set-Cookie": "__cfduid",
                "CF-RAY": "",
            },
            "BaiduYun": {
                "Server": "yunjiasu",
            },
            "CloudFront": {
                "Server": "cloudfront",
                "X-Cache": "cloudfront",
            },
            "Comodo": {
                "Server": "Comodo",
            },
            "IBM-DataPower": {
                "X-Backside-Transport": "",
            },
            "dotDefender": {
                "X-dotDefender-denied": "1",
            },
            "Incapsula": {
                "X-CDN": "Incapsula",
                "X-Iinfo": "",
                "X-Iejgwucgyu": "1",
                "incap_ses": "",
                "visid_incap": "",
            },
            "Zenedge": {
                "Server": "ZENEDGE",
                "X-Cdn": "Zenedge",
                "X-Zen-Fury": "",
            },
            "OVHcdn": {
                "X-CDN-Pop": "",
                "X-CDN-Geo": "",
                "X-CDN-Pop-IP": "137.74",
            },
            "Jiasule": {
                "Set-Cookie": "jsluid",
                "X-Via-JSL": "",
                "X-Cache": "bypass",
            },
            "KSYUN": {
                "Server": "KSYUN",
            },
            "Akamai": {
                "Server": "AkamaiGHost",
            },
            "NetContinuum": {
                "Cneonction": "close",
                "nnCoection": "close",
                "Set-Cookie": "citrix_ns_id",
            },
            "ModSecurity": {
                "Server": "ModSecurity",
            },
            "ModSecurity2": {
                "Server": "modsecurity",
            },
            "LiteSpeed": {
                "Server": "LiteSpeed",
            },
            "Netscaler": {
                "Cneonction": "close",
                "nnCoection": "close",
                "Set-Cookie": "citrix_ns_id",
            },
            "NewDefend": {
                "Server": "NewDefend",
                "Set-Cookie": "NEWNDSESS",
            },
            "NSFOCUS": {
                "Server": "NSFOCUS",
                "Set-Cookie": "secure",
                "Location": "requireLogin",
            },
            "Safe3": {
                "Server": "Safe3",
                "X-Powered-By": "Safe3WAF",
            },
            "Safedog": {
                "X-Powered-By": "WAF/2.0",
                "Set-Cookie": "safedog",
                "Server": "Safedog"
            },
            "SonicWALL": {
                "Server": "SonicWALL",
            },
            "Stingray": {
                "Server": "Stingray",
            },
            "Sucuri": {
                "Server": "Sucuri",
                "X-Sucuri-ID": "",
                "X-Sucuri-Cache": "MISS",
                "X-Sucuri-Block": "",
            },
            "USPsec": {
                "Server": "Secure Entry Server",
            },
            "Varnish": {
                "Server": "Varnish",
                "Via": "varnish",
                "X-Varnish": "",
                "X-Served-By": "varnish",
                "X-Haste-Cfg": "varnish",
                "X-Varnish-Hits": "",
                "X-Varnish-Cache": "",
                "X-Varnish-Key": "",
                "X-prefetch": "",
            },
            "Wallarm": {
                "Server": "nginx-wallarm",
            },
            "QRATOR": {
                "Server": "QRATOR",
            },
            "WebKnight": {
                "Server": "WebKnight",
            },
            "YUNDUN": {
                "Server": "YUNDUN",
                "X-Cache": "YUNDUN",
                "Set-Cookie": "yd_cookie",
            },
            "yundun": {
                "Set-Cookie": "yundun_404=",
            },
            "Aliyun": {
                "Set-Cookie": "yunqi",
                "Location": "aliyun",
                "Ali-Swift-Global-Savetime": "",
                "Via": "kunlun",
            },
            "Yunsuo": {
                "Set-Cookie": "yunsuo_session_verify",
            },
            "Edgecast": {
                "Server": "ECD (",
            },
            "Edgecast2": {
                "Server": "ECS (",
            },
            "Limelight": {
                "Server": "WowzaStreamingEngine",
                "Access-Control-Expose-Headers": "Server",
            },
            "NetDNA": {
                "Server": "NetDNA",
            },
            "KeyCDN": {
                "Server": "keycdn",
            },
            "Cachefly": {
                "CacheFly-Control": "max-age",
            },
            "Azure": {
                "Server": "Windows-Azure-Blob",
                "x-ms-request-id": "",
            },
            "VoxCDN": {
                "Server": "VoxCAST",
            },
            "Aegins": {
                "Server": "Aegins",
            },
            "BitGravity": {
                "Server": "bit_asic",
            },
            "HuaweiYun": {
                "Server": "NWSs",
            },
            "FastCache": {
                "Server": "fastCache",
            },
            "NGENIX": {
                "X-NGENIX-Cache", "",
            },
            "ChinaCache": {
                "Powered-By-ChinaCache": "MISS",
                "FlexiCache-Error": "ERR_ACCESS_DENIED",
                "Server": "FC",
            },
            "Azion": {
                "Server": "azion",
            },
            "MNCDN": {
                "Server": "MNCDN",
                "x-edge-location": "TR",
                "X-MServer": "",
            },
            "nyiftw": {
                "X-Delivered-By": "NYI FTW",
                "X-FTW-STATUS": "",
                "X-FTW-Transport": "",
                "X-Powered-By": "NYI FTW",
            },
            "ReSRC.it": {
                "Server": "ReSRC",
                "ReSRC-AppServer": "ReSRC",
                "ReSRC-AppHost": "resrc.it",
            },
            "lswcdn": {
                "Server": "leasewebcdn",
                "CDN-Server-Status": "Leaseweb",
                "CDN-Cache-Hit": "",
            },
            "Caspowa": {
                "Server": "Caspowa",
                "Accelerated-By": "Caspowa",
            },
            "Aryaka": {
                "Server": "Aryaka",
                "X-Ar-Debug": "",
            },
            "squixa": {
                "Server": "Squixa",
            },
            "BisonGrid": {
                "X-Powered-By": "Bison Grid",
            },
            "GoCache": {
                "Server": "gocache",
            },
            "HiberniaCDN": {
                "Server": "hiberniacdn",
                "X-HiberniaCDN": "cached=",
            },
            "UnicornCDN": {
                "Server": "UnicornCDN",
            },
            "OptimalCDN": {
                "Server": "Optimal",
            },
            "Roast.io": {
                "Server": "Roast.io",
            },
            "Airee": {
                "Server": "Airee",
            },
            "Instart": {
                "Server": "instart",
                "X-Instart-Request-ID": "",
            },
            "Highwinds": {
                "X-HW": "15",
            },
            "SurgeCDN": {
                "Server": "SurgeCDN",
            },
            "Google_sffe": {
                "Server": "sffe",
            },
            "Google_gws": {
                "Server": "gws",
            },
            "Google_GSE": {
                "Server": "GSE",
            },
            "Google_Golfe2": {
                "Server": "Golfe2",
            },
            "Google": {
                "Via": "google",
                "Server": "Google",
                "__xwaf_id": "",
            },
            "ChinaNetCenter": {
                "X-Cache": "51cdn",
            },
            "section.io": {
                "section-io-id": "",
            },
            "Squid": {
                "Server": "squid",
                "X-Squid-Error": "ERR_INVALID_URL",
                "Via": "squid",
            },
            "finecms": {
                "Set-Cookie": "finecms_b1bf4_ci_session",
            },
            "ThinkPHP": {
                "X-Powered-By": "ThinkPHP",
            },
            "Drupal": {
                "X-Drupal-Cache": "",
                "X-Drupal-Dynamic-Cache": "",
                "X-Generator": "Drupal",
            },
            "Confluence": {
                "X-Confluence-Request-Time": "",
            },
            "CodeIgnitor": {
                "Set-Cookie": "ci_session",
                "X-Codeignitor-Environment": "",
            },
            "GlassFish": {
                "Server": "GlassFish Server",
                "X-Powered-By": "GlassFish Server",
            },
            "Four-Faith": {
                "Server": "httpd_four-faith",
            },
            "Kangle": {
                "Server": "kangle",
            },
            "PHP-Language": {
                "X-Powered-By": "PHP",
                "Set-Cookie": "PHPSSIONID",
            },
            "JSP-Language": {
                "Set-Cookie": "JSESSIONID",
                "X-Powered-By": "JSP",
            },
            "ASP-Language": {
                "Set-Cookie": "ASPSESSION",
            },
            "ASP.NET-Language": {
                "Server": "ASP.NET",
                "Set-Cookie": "ASP.NET_SessionId",
                "X-AspNet-Version": "",
                "X-AspNetMvc-Version": "",
                "X-Powered-By": "ASP.NET",
            },
            "WordPress": {
                "WP-Super-Cache": "supercache",
                "X-Redirect-By": "WordPress",
                "X-Pingback": "xmlrpc.php",
            },
            "Zabbix": {
                "Set-Cookie": "zbx_sessionid",
            },
            "Winmail": {
                "Set-Cookie": "magicwinmail",
            },
            "Outlook": {
                "X-OWA-Version": "",
            },
            "SquirrelMail": {
                "Set-Cookie": "SQMSESSID",
            },
            "zimbra": {
                "Set-Cookie": "ZM_TEST",
            },
            "IlohaMail": {
                "Set-Cookie": "IMAIL_TEST_COOKIE",
                "SESS_KEY": "",
            },
            "mailbase": {
                "Set-Cookie": "mb_",
            },
            "Jboss": {
                "X-Powered-By": "JBoss",
                "Server": "JBoss",
            },
            "HFS": {
                "Server": "HFS",
                "Set-Cookie": "HFS_SID",
            },
            "2wire": {
                "Server": "2wire",
                "WWW-Authenticate": "2wire",
            },
            "Asmax": {
                "WWW-Authenticate": "Asmax",
            },
            "Asus": {
                "WWW-Authenticate": "Asus",
            },
            "D-Link-DCS": {
                "WWW-Authenticate": "DCS-",
            },
            "D-Link-DIR": {
                "Server": "DIR-",
            },
            "Linksys": {
                "WWW-Authenticate": "Basic realm=\"RT-",
            },
            "Netcore": {
                "WWW-Authenticate": "NETCORE",
            },
            "Netgear": {
                "WWW-Authenticate": "NETGEAR",
            },
            "Thomson": {
                "WWW-Authenticate": "Thomson",
            },
            "Tplink": {
                "WWW-Authenticate": "TP-LINK",
            },
            "Zte": {
                "Server": "ZTE corp",
                "Set-Cookie": "_TESTCOOKIESUPPORT",
            },
            "H3C": {
                "Server": "H3C-Miniware-Webs",
                "WWW-Authenticate": "h3c",
            },
            "Huawei": {
                "WWW-Authenticate": "huawei",
            },
            "HuaweiGateway": {
                "WWW-Authenticate": "HuaweiHomeGateway",
            },
            "Hikvision": {
                "Server": "Hikvision-Webs",
            },
            "Hikvision-DVRDVS": {
                "Server": "DVRDVS-Webs",
            },
            "Hikvision-DNVRS": {
                "Server": "DNVRS-Webs",
            },
            "Hikvision-App": {
                "Server": "App-webs",
            },
            "CCTV": {
                "Server": "JAWS",
            },
            "aeSecure": {
                "Protected-by": "aesecure",
            },
            "Airlock": {
                "Set-Cookie": "AL_SESS-S",
            },
            "Airlock2": {
                "Set-Cookie": "AL_LB",
            },
            "Barracuda": {
                "Server": "Barracuda",
                "Set-Cookie": "barra_counter_session",
                "Location": "barracuda",
            },
            "ACE-XML-Gateway": {
                "Server": "ACE XML Gateway",
            },
            "Distil": {
                "x-distil-cs": "MISS",
            },
            "DOSarrest": {
                "Server": "DOSarrest",
                "X-DIS-Request-ID": "",
            },
            "FortiWeb": {
                "Set-Cookie": "FORTIWAFSID",
            },
            "Hyperguard": {
                "Set-Cookie": "ODSESSION",
            },
            "Knownsec": {
                "X-CDN-Edge": "",
                "Set-Cookie": "__cdnuid_h",
            },
            "NAXSI": {
                "X-Data-Origin": "naxsi",
            },
            "NAXSI2": {
                "X-Data-Origin": "rate-limiter",
            },
            "Newdefend": {
                "Server": "Newdefend",
            },
            "Profense": {
                "Server": "Profense",
                "Set-Cookie": "plbsid",
            },
            "AppWall": {
                "X-SL-CompState": "",
            },
            "Reblaze": {
                "Server": "Reblaze",
                "Set-Cookie": "rbzid",
            },
            "Tencent": {
                "Server": "TCW",
            },
            "TrafficShield": {
                "Server": "TrafficShield",
            },
            "WatchGuard": {
                "Server": "WatchGuard",
                "www-authenticate": "WatchGuard",
            },
            "宝塔": {
                "Set-Cookie": "BT_PANEL_6",
            },
            "D盾": {
                "Set-Cookie": "_D_SID",
            },
            "D盾2": {
                "Set-Cookie": "_d_id",
            },
            "SDWAF": {
                "Set-Cookie": "sdwaf-test-item",
                "X-Powered-By": "SDWAF",
            },
            "WDCP": {
                "Set-Cookie": "wdcpsessionID",
            },
            "WTS": {
                "Server": "wts",
            },
            "VPSSIM": {
                "X-Powered-By": "VPSSIM",
            },
            "wafcloud": {
                "Server": "wafcloud",
            },
            "蓝盾BLUEDON": {
                "Server": "BDWAF",
            },
            "南昌邦腾CDN": {
                "Location": "lhzl61",
            },
            "Denyall": {
                "Set-Cookie": "sessioncookie",
            },
            "hyperguard": {
                "Set-Cookie": "ODSESSION",
            },
            "ISAserver": {
                "Via": "ISASERVER",
                "WWW-Authenticate": "isaserver",
            },
            "URLscan": {
                "Rejected-By-UrlScan": "",
            },
            "Nginx": {
                "Server": "nginx",
                "X-Rocket-Nginx-File": "",
                "X-Rocket-Nginx-Bypass": "",
                "X-Rocket-Nginx-Reason": "",
                "X-Backend-Server": "nginx",
            },
            "Apache": {
                "Server": "Apache",
            },
            "Microsoft-IIS": {
                "Server": "Microsoft-IIS",
                "X-AspNetMvc-Version": "",
                "X-AspNet-Version": "",
                "X-MS-InvokeApp": "",
            },
            "openresty": {
                "Server": "openresty",
            },
            "AmazonS3": {
                "Server": "AmazonS3",
                "x-amz-version-id": "",
                "X-Amz-Cf-Pop": "",
                "X-Amz-Cf-Id": "",
            },
            "Apache-Traffic-Server": {
                "Server": "ATS",
                "X-INKT-SITE": "",
                "X-INKT-URI": "",
            },
            "淘宝Tengine": {
                "Server": "Tengine",
            },
            "Cowboy": {
                "Server": "Cowboy",
            },
            "Flywheel": {
                "X-FW-Server": "Flywheel",
                "Server": "Flywheel",
                "X-FW-Hash": "",
                "X-FW-Serve": "",
                "X-FW-Static": "",
                "X-FW-Type": "",
            },
            "IdeaWebServer": {
                "Server": "IdeaWebServer",
            },
            "Microsoft-HTTPAPI": {
                "Server": "Microsoft-HTTPAPI",
            },
            "DPS": {
                "Server": "DPS",
                "Set-Cookie": "dps_site_id",
            },
            "Netlify": {
                "Server": "Netlify",
                "X-NF-Request-ID": "",
            },
            "ghs": {
                "Server": "ghs",
            },
            "Kestrel": {
                "Server": "Kestrel",
            },
            "aruba-proxy": {
                "Server": "aruba-proxy",
            },
            "Jino.ru": {
                "Server": "Jino.ru/mod_pizza",
            },
            "lighttpd": {
                "Server": "lighttpd",
            },
            "gunicorn": {
                "Server": "gunicorn",
            },
            "EHTTP": {
                "Server": "eHTTP",
            },
            "PWS": {
                "Server": "PWS",
            },
            "Pagely-Gateway": {
                "Server": "Pagely Gateway",
            },
            "CDK-Websites": {
                "Server": "CDK-Websites",
            },
            "Jetty": {
                "Server": "Jetty",
            },
            "ngjit": {
                "Server": "ngjit",
            },
            "Zope": {
                "Server": "Zope",
            },
            "BWS": {
                "Server": "BWS",
            },
            "DCSaaS": {
                "X-Powered-By": "DCSaaS",
                "Server": "DCSaaS",
            },
            "PowerBoost": {
                "Server": "PowerBoost",
                "Set-Cookie": "o2switch-PowerBoost-Protect",
            },
            "AtyponWS": {
                "Server": "AtyponWS",
            },
            "ArvanCloud": {
                "Server": "ArvanCloud",
            },
            "Starlet": {
                "Server": "Starlet",
                "X-Framework": "JP",
            },
            "nxfps": {
                "Server": "nxfps",
            },
            "TServer": {
                "Server": "TServer",
            },
            "Caddy": {
                "Server": "Caddy",
            },
            "WEBrick": {
                "Server": "WEBrick",
            },
            "awselb": {
                "Server": "awselb",
            },
            "shield": {
                "Server": "shield",
            },
            "Router-Webserver": {
                "Server": "Router Webserver",
            },
            "Lotus-Domino": {
                "Server": "Lotus-Domino",
            },
            "gocache": {
                "Server": "gocache",
            },
            "Pagely-ARES": {
                "Server": "Pagely-ARES",
                "X-Gateway-Cache-Key": "",
                "X-Gateway-Cache-Status": "",
                "X-Gateway-Skip-Cache": "",
            },
            "MageStack-MagentoOS": {
                "Server": "MageStack-MagentoOS",
            },
            "myracloud": {
                "Server": "myracloud",
            },
            "IBM_HTTP_Server": {
                "Server": "IBM_HTTP_Server",
            },
            "Sun-ONE-Web-Server": {
                "Server": "Sun-ONE-Web-Server",
            },
            "Boa": {
                "Server": "Boa",
                "X-Mercku-API-Version": "",
            },
            "wts": {
                "Server": "wts",
                "X-Cache": "WTS",
            },
            "Squeegit": {
                "Server": "Squeegit",
                "Set-Cookie": "REFERRER",
            },
            "Oracle-Application-Server": {
                "Server": "Oracle-Application-Server",
            },
            "Oracle-HTTP-Server": {
                "Server": "Oracle-HTTP-Server",
            },
            "ws-httpd": {
                "Server": "ws-httpd",
            },
            "SSWS": {
                "Server": "SSWS",
            },
            "Resin": {
                "Server": "Resin",
            },
            "ECAcc": {
                "Server": "ECAcc",
            },
            "WSGIServer": {
                "Server": "WSGIServer",
            },
            "Xavante": {
                "Server": "Xavante",
            },
            "api-gateway": {
                "Server": "api-gateway",
                "X-App-Name": "Pro2-Renderer",
            },
            "NWSs": {
                "Server": "NWSs",
            },
            "envoy": {
                "Server": "envoy",
            },
            "Toofun": {
                "Server": "Toofun",
                "Set-Cookie": "ads_cnt",
            },
            "UploadServer": {
                "Server": "UploadServer",
                "X-GUploader-UploadID": "",
            },
            "Oracle-iPlanet": {
                "Server": "iPlanet",
            },
            "WisePanel": {
                "Server": "WisePanel",
            },
            "Beaver": {
                "Server": "Beaver",
            },
            "BlueServer": {
                "Server": "BlueServer",
            },
            "Now": {
                "x-now-trace": "",
                "x-now-id": "",
                "server": "now",
            },
            "Express": {
                "Server": "express",
                "X-Powered-By": "Express",
            },
            "ESF": {
                "Server": "ESF",
            },
            "Mopro": {
                "Server": "Mopro",
                "X-Via": "web-mopro",
                "X-Redirected-By": "Mopro WebUIKit",
            },
            "UD-Webspace": {
                "Server": "UD Webspace",
            },
            "NGUARDX": {
                "Server": "NGUARDX",
            },
            "Apptegy": {
                "Server": "Apptegy",
            },
            "httpv2": {
                "Server": "httpv2",
                "P3P": "CAO PSA CONi OTR",
            },
            "Tornado": {
                "Server": "TornadoServer",
            },
            "marco": {
                "Server": "marco",
            },
            "Thin": {
                "Server": "thin",
            },
            "gwt": {
                "Server": "gwt",
            },
            "awex": {
                "Server": "awex",
            },
            "WildFly": {
                "Server": "WildFly",
            },
            "Undertow": {
                "Server": "undertow",
                "X-Powered-By": "Undertow",
            },
            "JSP3": {
                "Server": "JSP3",
            },
            "sffe": {
                "Server": "sffe",
            },
            "fasterize": {
                "Server": "fasterize",
            },
            "kibana": {
                "kbn-name": "kibana",
                "kbn-version": "",
                "kbn-xpack-sig": "",
                "Kbn-Name": "kibana",
                "location": "kibana",
                "Kbn-Xpack-Sig": "",
            },
            "nghttpx": {
                "Server": "nghttpx",
                "Via": "nghttpx",
            },
            "Perl-Dancer": {
                "Server": "Perl Dancer",
                "X-Powered-By": "Perl Dancer",
                "Chimera-API-Server": "",
            },
            "VARITI": {
                "X-VARITI-CCR": "",
                "X-Variti-Ccr": "",
            },
            "RadfaWS": {
                "Server": "RadfaWS",
            },
            "akka-http": {
                "Server": "akka-http",
            },
            "Scutum": {
                "Server": "Scutum",
            },
            "Footprint-Distributor": {
                "Server": "Footprint Distributor",
            },
            "marrakesh": {
                "Server": "marrakesh",
            },
            "WebLogic": {
                "Server": "WebLogic",
            },
            "FBS": {
                "Server": "fbs",
                "set-cookie": "spcsrf",
            },
            "AASAAM": {
                "Server": "AASAAM",
            },
            "AASAAM2": {
                "Server": "Aasaam",
            },
            "Pepyaka": {
                "Server": "Pepyaka",
                "X-Seen-By": "",
                "X-Wix-Request-Id": "",
            },
            "Web-r": {
                "Server": "Web r",
            },
            "MI": {
                "Server": "MI",
                "Via": "1.1 mi",
                "MI-Cache-Age": "",
                "MI-Cache": "",
                "Mi-Api": "",
            },
            "ZGS": {
                "Server": "ZGS",
            },
            "Dreamlab": {
                "Server": "Dreamlab",
            },
            "CDN77-Turbo": {
                "Server": "CDN77-Turbo",
            },
            "NWS_SP": {
                "Server": "NWS_SP",
                "X-NWS-LOG-UUID": "",
            },
            "DNSME-HTTP-Redirection": {
                "Server": "DNSME HTTP Redirection",
            },
            "Airee-Cloud": {
                "Server": "Airee/Cloud",
                "X-Airee-Node": "",
                "X-Airee-Id": "",
            },
            "Python-Werkzeug": {
                "Server": "Werkzeug",
            },
            "Python-Flask": {
                "Server": "Flask",
            },
            "CM4all": {
                "Server": "CM4all",
            },
            "DataDome": {
                "Server": "DataDome",
                "X-DataDomeResponse": "",
                "Set-Cookie": "datadome",
                "X-DataDome": "",
                "X-DataDome-CID": "",
            },
            "EdgePrism": {
                "Server": "EdgePrism",
            },
            "WowzaStreamingEngine": {
                "Server": "WowzaStreamingEngine",
            },
            "Tomahawk-Ultra": {
                "Server": "Tomahawk Ultra",
            },
            "OMCnet": {
                "Server": "OMCnet",
                "X-Processed-By": "omc.net",
            },
            "Zeus": {
                "Server": "Zeus",
                "WWW-Authenticate": "Zeus",
            },
            "imio": {
                "Server": "imio",
            },
            "Virb <3's You!": {
                "Server": "Virb <3's You",
                "X-Powered-By": "1virb1",
            },
            "Skipper": {
                "Server": "Skipper",
            },
            "greywizard": {
                "Server": "greywizard",
                "GW-Server": "greywizard",
            },
            "IA-Web-Server": {
                "Server": "IA Web Server",
            },
            "waitress": {
                "Server": "waitress",
            },
            "PowerBoutique": {
                "Server": "PowerBoutique",
                "X-PwB-Node": "",
            },
            "CHO": {
                "Server": "CHO",
            },
            "Global Webserver": {
                "Server": "Global Webserver",
                "X-Powered-By": "Fastcommerce",
                "bios": "",
            },
            "SingularCDN": {
                "Server": "SingularCDN",
            },
            "PORTFOLIOBOX": {
                "Server": "PORTFOLIOBOX",
                "X-Served-By": "portfoliobox",
                "App": "SaleSite",
                "App-SaleSite-Updated": "",
            },
            "PORTFOLIOBOX2": {
                "App": "Route",
            },
            "PCX/No-Cache": {
                "Server": "PCX/No-Cache",
            },
            "0W/0.8e": {
                "Server": "0w/0.8e",
            },
            "NWS_TCloud_S1": {
                "Server": "NWS_TCloud_S1",
            },
            "micro_httpd": {
                "Server": "micro_httpd",
            },
            "CoreyeCDN": {
                "Server": "CoreyeCDN",
                "Via": "coreye_cdn",
                "Set-Cookie": "CoreyeCDN",
            },
            "KIABI": {
                "Server": "KIABI",
            },
            "KIABI2": {
                "Set-Cookie": "MRHSession",
            },
            "Ruby-WEBrick": {
                "Server": "WEBrick",
            },
            "InGaia": {
                "Server": "InGaia",
                "Stack": "InGaia",
                "X-Powered-By": "InGaia",
            },
            "Consultix": {
                "Server": "Consultix",
                "X-Powered-By": "Consultix",
            },
            "DnionOS": {
                "Server": "DnionOS",
                "Server-Info": "DnionATS",
            },
            "YouTube-Frontend": {
                "Server": "YouTube Frontend",
            },
            "Mastodon": {
                "Server": "Mastodon",
                "Set-Cookie": "_mastodon_session",
                "Location": "mastodon",
            },
            "zeroserver": {
                "Server": "zeroserver",
            },
            "WIFEO": {
                "Server": "WIFEO",
                "Set-Cookie": "statcountalamargefr26",
            },
            "WPX-CLOUD/KAN01": {
                "Server": "WPX CLOUD/KAN01",
                "X-Edge-Location": "WPX CLOUD/KAN01",
            },
            "GRM - pd": {
                "Server": "GRM - pd",
                "X-Pram": "GRMVAL",
            },
            "NOYB": {
                "Server": "NOYB",
            },
            "Plesk主机管理软件linux": {
                "X-Powered-By": "PleskLin",
            },
            "Plesk主机管理软件windows": {
                "X-Powered-By": "PleskWin",
            },
            "By-drsrv.com": {
                "Server": "drsrv.com",
            },
            "esky-edge": {
                "Server": "esky-edge",
            },
            "sopws": {
                "Server": "sopws",
            },
            "kindred-loadbalancer": {
                "Server": "kindred-loadbalancer",
                "X-DD-Host": "",
            },
            "Firewall": {
                "Server": "Firewall",
            },
            "Odiso": {
                "Server": "Odiso",
            },
            "JAS-BHV3": {
                "Server": "JAS BHV3",
                "Set-Cookie": "targetPath_b2c",
            },
            "JAS-BHV3-2": {
                "Set-Cookie": "ASID=.",
            },
            "Pro-Managed": {
                "Server": "Pro-Managed",
            },
            "UNIX-SERVER": {
                "Server": "UNIX-SERVER",
            },
            "BasisCore": {
                "Server": "BasisCore",
            },
            "Anaxa-LLC": {
                "Server": "Anaxa LLC",
            },
            "elb": {
                "Server": "elb",
            },
            "AWSALB": {
                "Server": "AWSALB",
                "Set-Cookie": "AWSALB",
            },
            "Yoncu-Bilisim-Cozumleri": {
                "Server": "Yoncu Bilisim Cozumleri",
                "Yoncu-Errno": "",
            },
            "Cherokee": {
                "Server": "Cherokee",
                "WWW-Authenticate": "proliphixrealm",
            },
            "Warp": {
                "Server": "Warp",
            },
            "SAP": {
                "Server": "SAP",
                "sap-system": "",
                "sap-client": "",
            },
            "AkamaiNetStorage": {
                "Server": "AkamaiNetStorage",
                "X-Akamai-Transformed": "",
            },
            "My-web-server": {
                "Server": "My web server",
            },
            "AL_TEST": {
                "Server": "AL_TEST",
            },
            "Dot-Enterprise": {
                "Server": "Dot Enterprise",
                "X-Powered-By": "Dot Enterprise",
            },
            "lpgenerator.ru": {
                "Server": "lpgenerator.ru",
            },
            "bytex": {
                "Server": "bytex",
            },
            "http-server": {
                "Server": "http server",
            },
            "LoadBalancer": {
                "Server": "LoadBalancer",
                "X-Proxy-Request-Received": "",
                "X-Proxy-Request-Routed": "",
                "X-Proxy-Request-Forwarded": "",
                "X-Proxy-Response-Received": "",
            },
            "NodeJS": {
                "Server": "NodeJS",
            },
            "funeralOne-F1Connect": {
                "Server": "funeralOne-F1Connect",
                "X-StackifyID": ""
            },
            "suduserver": {
                "Server": "suduserver",
            },
            "UCMS": {
                "X-Powered-By": "UCMS",
            },
            "NewCloud-V": {
                "Server": "NewCloud-V",
                "X-NewCloud-V-Cache": "",
                "X-Backend-TTL": "",
                "X-Type": "Dynamic URI",
            },
            "Haste": {
                "Server": "Haste",
                "X-Haste-Node": "",
                "X-Haste-Cache": "",
                "X-Haste-Cfg": "haste",
            },
            "Sun-Java-System-Web-Server": {
                "Server": "Sun-Java-System-Web-Server",
            },
            "Python-PasteWSGIServer": {
                "Server": "PasteWSGIServer",
            },
            "IITP-Server": {
                "Server": "IITP Server",
            },
            "Mikrotik": {
                "Server": "Mikrotik",
            },
            "WT_11.13": {
                "Server": "WT_11.13",
            },
            "SCICUBE_LIMITED": {
                "Server": "SCICUBE_LIMITED",
            },
            "Magento": {
                "X-Server": "Magento",
            },
            "Magento2": {
                "X-Server": "magento",
            },
            "SecurityCore": {
                "Server": "SecurityCore",
                "X-Software-Info": "Plataforma CORE",
                "Request-Context": "appId=",
            },
            "WiziServer": {
                "Server": "WiziServer",
            },
            "IF_WAF": {
                "Server": "IF_WAF",
            },
            "Server24.it": {
                "Server": "Server24.it",
                "X-Powered-By": "Incubatec",
            },
            "acwebconnecting": {
                "Server": "acwebconnecting",
                "Set-Cookie": "xlove_id_affi",
            },
            "OpenCms": {
                "Server": "OpenCms",
            },
            "Caddy2": {
                "Server": "SITE123secure",
            },
            "roxen": {
                "Server": "roxen",
            },
            "roxen2": {
                "Server": "Roxen",
            },
            "Python-CherryPy": {
                "Server": "CherryPy",
            },
            "(null)": {
                "Server": "(null)",
                "X-Server": "(null)",
            },
            "ngx_openresty": {
                "Server": "ngx_openresty",
            },
            "Internet": {
                "Server": "Internet",
            },
            "Visualsoft": {
                "Server": "Visualsoft",
            },
            "Eplica": {
                "Server": "Eplica",
                "Powered-By": "Eplica",
                "Set-Cookie": "eplicaWebVisitor",
            },
            "MyServer": {
                "Server": "MyServer",
            },
            "wswaf": {
                "Server": "wswaf",
            },
            "WPThing": {
                "Server": "WPThing",
                "X-Cache-Why": "",
            },
            "Perl-Mojolicious": {
                "Server": "Mojolicious",
                "X-Powered-By": "Mojolicious",
                "Set-Cookie": "mojolicious",
            },
            "Squiz": {
                "Server": "Squiz",
                "Set-Cookie": "SQ_SYSTEM_SESSION",
                "X-Cache": "squiz",
                "X-Cache-Lookup": "squiz",
            },
            "HyperFilter": {
                "Server": "HYPERFILTER",
                "DDOS": "HyperFilter",
                "HF-Wall": "",
            },
            "Nitro": {
                "Server": "Nitro",
            },
            "ejuniper": {
                "Server": "www.ejuniper.com",
            },
            "iNetweek": {
                "Server": "iNetweek",
            },
            "NetNames": {
                "Server": "NetNames",
            },
            "FireShield": {
                "X-Server-Powered-By": "FireShield",
            },
            "nunya": {
                "Server": "nunya",
            },
            "DataPalm": {
                "Server": "DataPalm",
            },
            "IMU": {
                "Server": "IMU",
                "Set-Cookie": "phx_ssl_redi",
            },
            "blizhost": {
                "Server": "blizhost",
            },
            "Carrot": {
                "Server": "Carrot",
            },
            "OpenBSD-httpd": {
                "Server": "OpenBSD httpd",
            },
            "iCore": {
                "Server": "iCore Proxy",
            },
            "Fly.io": {
                "Server": "Fly.io",
                "Set-Cookie": "fly_cid",
                "Fly-Request-Id": "",
                "fly-request-id": "",
            },
            "VWebServer": {
                "Server": "VWebServer",
            },
            "Binford": {
                "Server": "Binford",
            },
            "Ninja": {
                "Server": "Ninja",
            },
            "Ninja2": {
                "Server": "ninja wasp",
            },
            "Thrive": {
                "Server": "Thrive",
                "Set-Cookie": "THRIVE_SESS",
            },
            "III-100": {
                "Server": "III 100",
                "Set-Cookie": "III_SESSION_ID",
            },
            "w3pcloud": {
                "Server": "w3pcloud",
            },
            "GNU-Terry-Pratchett": {
                "X-Clacks-Overhead": "GNU Terry Pratchett",
            },
            "domain-redirector": {
                "Server": "domain-redirector",
            },
            "AOLserver": {
                "Server": "AOLserver",
            },
            "aolserver": {
                "Server": "aolserver",
            },
            "Increo-Ninja": {
                "Server": "Increo Ninja",
            },
            "Custom/1.0 UPnP/1.0 Proc/Ver": {
                "Server": "Custom/1.0 UPnP/1.0 Proc/Ver",
                "ST": "upnp:rootdevice",
                "USN": "uuid:",
            },
            "Shop-Application.com": {
                "Server": "Shop-Application.com",
                "X-Page-Speed": "Shop-Application.com",
            },
            "CarlosSantana": {
                "Server": "CarlosSantana",
            },
            "SiteW-Webserver": {
                "Server": "SiteW Webserver",
                "Set-Cookie": "_sw_session",
            },
            "SGW": {
                "Server": "SGW",
            },
            "cisco-IOS": {
                "Server": "cisco-IOS",
                "WWW-Authenticate": "level_15 or view_access",
            },
            "Barista": {
                "Server": "Barista",
            },
            "Barista2": {
                "Server": "barista",
            },
            "Luffy": {
                "Server": "Luffy",
            },
            "Luffy2": {
                "Server": "luffy",
            },
            "Destinet": {
                "Server": "Destinet",
            },
            "thttpd": {
                "Server": "thttpd",
            },
            "Sparkred": {
                "Server": "Sparkred",
                "X-Powered-By": "Sparkred",
            },
            "Bitrix24.Sites": {
                "Server": "Bitrix24.Sites",
                "X-Powered-Cms": "Bitrix24.Sites",
            },
            "nws": {
                "Server": "nws",
            },
            "Mongrel": {
                "Server": "Mongrel",
                "Set-Cookie": "_admin_session_id",
            },
            "TIN-AppServer": {
                "Server": "TIN-AppServer",
            },
            "Cacti": {
                "Set-Cookie": "Cacti=",
                "CactiEZ": "www.cactiez.com",
            },
            "WebSEAL": {
                "Server": "WebSEAL",
            },
            "kisa": {
                "Server": "kisa",
                "Serverstatus": "Backtracking",
            },
            "Dustin-LB": {
                "Server": "Dustin LB",
            },
            "Hiawatha": {
                "Server": "Hiawatha",
            },
            "NWS_TCloud_S2": {
                "Server": "NWS_TCloud_S2",
            },
            "Optimal-CDN": {
                "Server": "Optimal CDN",
            },
            "Piolink-Switch": {
                "Server": "Piolink Switch",
            },
            "Dimofinf": {
                "Server": "Dimofinf",
                "Set-Cookie": "awtsessionhash",
            },
            "SPDCDN": {
                "Server": "SPDCDN",
                "Set-Cookie": "spdcdn_sc",
                "X-SPDCDN-Cache-Key": "",
                "X-SPDCDN-Device": "",
                "X-SPDCDN-Cache-Status": "",
            },
            "RVA": {
                "Server": "RVA",
            },
            "webkaos": {
                "Server": "webkaos",
            },
            "h2o": {
                "Server": "h2o",
            },
            "Zamba-Vccorp": {
                "Server": "Zamba Vccorp",
            },
            "Exsitee": {
                "Server": "Exsitee",
                "Set-Cookie": "symfony=",
            },
            "Magnetpro": {
                "Server": "Magnetpro",
                "Set-Cookie": "_CH_SID=",
            },
            "i-Motor": {
                "Server": "i-Motor",
            },
            "Pantheon": {
                "Server": "Pantheon",
                "X-pantheon-fun-reason": "",
                "X-pantheon-fun-extended": "",
                "X-Pantheon-Site": "",
                "X-Pantheon-Environment": "",
                "X-Pantheon-Styx-Hostname": "",
            },
            "Groupon": {
                "Server": "Groupon",
            },
            "LinQhost-HPW": {
                "Server": "LinQhost HPW",
            },
            "xServers": {
                "Server": "xServers",
            },
            "dweb": {
                "Server": "dweb",
                "DB-Nickname": "VTJGc2",
                "X-DB-NAR": "",
            },
            "tsa_k": {
                "Server": "tsa_k",
            },
            "laravel": {
                "xxx-server": "laravel",
                "Set-Cookie": "laravel_session",
            },
            "BelugaCDN": {
                "Server": "BelugaCDN",
                "X-Beluga-Cache-Status": "",
                "X-Beluga-Node": "",
                "X-Beluga-Record": "",
                "X-Beluga-Response-Time": "",
                "X-Beluga-Status": "",
                "X-Beluga-Trace": "",
                "X-Beluga-Response-Time-X": "",
            },
            "Universe": {
                "Server": "Universe",
            },
            "astrazeneca.com": {
                "Server": "astrazeneca.com",
            },
            "VietNamHost": {
                "Server": "VietNamHost",
                "X-Cache-Status": "DYNAMIC-",
            },
            "Mapfre": {
                "Server": "Mapfre",
                "X-Powered-By": "MAPFRE",
            },
            "Mapfre2": {
                "Server": "MAPFRE",
            },
            "Microsoft-SharePoint": {
                "MicrosoftSharePointTeamServices": "",
                "X-SharePointHealthScore": "",
            },
            "Coding-Pages": {
                "Server": "Coding Pages",
            },
            "Skynet": {
                "Server": "Skynet",
            },
            "SkyNet": {
                "Server": "SkyNet",
            },
            "SKYNET": {
                "Server": "SKYNET",
            },
            "Palo_Alto_Software": {
                "Server": "Palo_Alto_Software",
            },
            "Leadpages": {
                "Server": "Leadpages",
            },
            "Toluna": {
                "Server": "Toluna",
                "X-Banner": "Toluna",
            },
            "DROP-TABLE": {
                "Server": "DROP TABLE",
            },
            "ONTRAport": {
                "Server": "ONTRAport",
            },
            "Endouble": {
                "Server": "Endouble",
            },
            "Beon-x-Fast": {
                "Server": "Beon-x-Fast",
            },
            "Mutu-Nerim": {
                "Server": "Mutu-Nerim",
            },
            "Blogcu": {
                "Server": "Blogcu",
                "Set-Cookie": "nosplashad",
            },
            "Tallink": {
                "Server": "Tallink",
                "X-Sw-Bes": "",
            },
            "Oracle-Traffic-Director": {
                "Server": "Oracle-Traffic-Director",
                "Proxy-agent": "Oracle-Traffic-Director",
            },
            "AliyunOSS": {
                "Server": "AliyunOSS",
                "x-oss-request-id": "",
                "x-oss-server-time": "",
            },
            "Hippo/AppServ": {
                "Server": "Hippo/AppServ",
                "Set-Cookie": "BACKEND=",
            },
            "Parallax": {
                "Server": "Parallax",
                "Set-Cookie": "SnapshotMedia",
            },
            "UltraDNS": {
                "Server": "UltraDNS",
            },
            "Consisto": {
                "Server": "Consisto",
            },
            "xws": {
                "Server": "xws",
                "Set-Cookie": "xwsID=",
                "X-XWS-Performance": "",
            },
            "cloud-shield": {
                "Server": "cloud-shield",
            },
            "ZeroPark-Traffic": {
                "Server": "ZeroPark-Traffic",
            },
            "DHL": {
                "Server": "DHL",
            },
            "HIDDEN": {
                "Server": "HIDDEN",
            },
            "Hidden": {
                "Server": "Hidden",
            },
            "hidden": {
                "Server": "hidden",
            },
            "Twitter": {
                "Server": "tsa_",
                "x-connection-hash": "",
                "Set-Cookie": "_twitter_sess",
            },
            "FCR-PROXY": {
                "Server": "FCR PROXY",
                "X-FCR-Cache": "",
            },
            "abfrl-server": {
                "Server": "abfrl-server",
            },
            "GH61": {
                "Server": "GH61",
            },
            "aws": {
                "Server": "aws",
                "X-Server": "AWS",
            },
            "Netrix": {
                "Server": "Netrix",
                "X-Netrix-ID": "",
                "X-Powered-By": "NetiyiAntiDDOS",
            },
            "Straightsell": {
                "Server": "Straightsell",
                "Location": "straightsell",
            },
            "STEPHANIE": {
                "Server": "STEPHANIE",
                "Set-Cookie": "ECOMMARKER=",
            },
            "24h.com.vn": {
                "Server": "24h.com.vn",
                "Location": "24h.com.vn",
            },
            "TW": {
                "Server": "Managed by TW",
            },
            "www.buildabazaar.com": {
                "Server": "www.buildabazaar.com",
                "X-Debug-Serve": "",
            },
            "idealoAppServer": {
                "Server": "idealoAppServer",
                "Set-Cookie": "SSLB=1",
            },
            "IdealoAppServer": {
                "Server": "IdealoAppServer",
            },
            "SWB": {
                "Server": "SWB",
                "Set-Cookie": "wcm=1",
            },
            "Winho-CDN": {
                "Server": "Winho-CDN",
            },
            "ElUniversal": {
                "Server": "ElUniversal",
            },
            "csw": {
                "Server": "csw",
            },
            "CSW": {
                "Server": "CSW",
            },
            "1111": {
                "Server": "1111",
                "Set-Cookie": "agentfrom1111",
            },
            "North-Dakota": {
                "Server": "North Dakota",
            },
            "betPawa": {
                "Server": "betPawa",
            },
            "WISECART": {
                "Server": "WISECART",
            },
            "Transunion": {
                "Server": "Transunion",
            },
            "Carbase": {
                "Server": "Carbase",
                "X-App": "Carbase.com",
                "X-Server": "Carbase",
                "X-Employment": "carbase",
            },
            "EvoWebBase": {
                "Server": "EvoWebBase",
                "Set-Cookie": "websidretailmgr",
            },
            "anycast.io": {
                "Server": "anycast.io",
            },
            "京东WebServer": {
                "Server": "JengineD",
            },
            "京东WebServer2": {
                "Server": "JDWS",
            },
            "京东WebServer3": {
                "Server": "jfe",
            },
            "ProApps": {
                "Server": "ProApps",
            },
            "Roundcube-Webmail": {
                "Set-Cookie": "roundcube_sessid",
            },
            "BunnyCDN": {
                "Server": "BunnyCDN",
                "CDN-PullZone": "",
                "CDN-Uid": "",
                "CDN-RequestCountryCode": "",
                "CDN-EdgeStorageId": "",
                "CDN-CachedAt": "",
            },
            "Norauto-Int": {
                "Server": "Norauto Int",
            },
            "PRX1-FORUM": {
                "Server": "PRX1 FORUM",
            },
            "KWS": {
                "Server": "KWS-",
            },
            "Webmercs": {
                "Server": "Webmercs",
            },
            "Clara-ASAP": {
                "Server": "Clara-ASAP",
            },
            "e-pixler": {
                "Server": "e-pixler",
                "HA-Status": "Master",
            },
            "EOS": {
                "Server": "EOS",
            },
            "Tomcat": {
                "Server": "Tomcat",
            },
            "haproxy": {
                "Server": "haproxy",
            },
            "cvg": {
                "Server": "cvg",
            },
            "KCDN": {
                "Server": "KCDN",
                "X-Cdn-Srv": "",
            },
            "Doubleknot": {
                "Server": "Doubleknot",
                "p3p": "www.doubleknot.com",
            },
            "Saashr": {
                "Server": "Saashr",
            },
            "NWS": {
                "Server": "NWS",
                "X-Nws-Log-Uuid": "",
                "X-Nws-Uuid-Verify": "",
                "X-Daa-Tunnel": "",
                "X-NWS-LOG-UUID": "",
            },
            "MyShop": {
                "Server": "MyShop",
            },
            "proxypipe": {
                "Server": "proxypipe",
            },
            "DWS": {
                "Server": "DWS",
            },
            "Hello-World": {
                "Server": "Hello World",
                "X-POWERED-BY": "hello world",
            },
            "Altavoz": {
                "Server": "Altavoz",
            },
            "nginy": {
                "Server": "nginy",
                "X-Nginy-Latency": "",
                "X-Nginy-Cache": "",
                "X-Nginy-Upstream-Code": "",
            },
            "TrianCDN": {
                "Server": "TrianCDN",
            },
            "VCCloud": {
                "Server": "VCCloud",
                "X-Cache": "VCCloud",
            },
            "BekkerHTTPd": {
                "Server": "BekkerHTTPd",
            },
            "Webscale": {
                "Server": "Webscale",
                "Set-Cookie": "lagrange_session",
            },
            "Redirector": {
                "Server": "Redirector",
            },
            "template51": {
                "Server": "template51",
                "Backend": "templates_newlaw_director",
            },
            "SupplyFrame-SRE": {
                "Server": "SupplyFrame",
                "X-Powered-By": "SupplyFrame",
            },
            "RDS-WebServer": {
                "Server": "RDS-WebServer",
            },
            "web/server/14": {
                "Server": "web/server/14",
            },
            "WMT": {
                "Server": "WMT",
                "X-Powered-by": "WMT",
            },
            "Secured-Gateway": {
                "Server": "Secured Gateway",
            },
            "JDR": {
                "Server": "JDR",
            },
            "ADEOWS": {
                "Server": "ADEOWS",
            },
            "ServerHttp": {
                "Server": "ServerHttp",
            },
            "MKCL-Server": {
                "Server": "MKCL Server",
            },
            "BorderMARA": {
                "Server": "BorderMARA",
            },
            "ESWeb": {
                "Server": "ESWeb",
            },
            "CareerBuilder": {
                "Server": "CareerBuilder",
                "Location": "careerbuilder",
            },
            "CDNFly": {
                "Server": "CDNFly",
            },
            "VPZ": {
                "Server": "VPZ",
            },
            "CXLWS": {
                "Server": "CXLWS",
            },
            "MochiWeb": {
                "Server": "MochiWeb",
            },
            "Trademotion": {
                "Server": "Trademotion",
            },
            "WS-CDN": {
                "Server": "WS CDN Server",
            },
            "WS-web-server": {
                "Server": "WS-web-server",
            },
            "Taleo-Web-Server": {
                "Server": "Taleo Web Server",
            },
            "MisraG": {
                "Server": "MisraG",
            },
            "NHN": {
                "Server": "NHN",
            },
            "SCAPRCMS07": {
                "Server": "SCAPRCMS07",
            },
            "Gerenciado-por-StoreHosting.com.br": {
                "Server": "Gerenciado por StoreHosting.com.br",
            },
            "Python-Rocket": {
                "Server": "Rocket",
            },
            "Python-web2py": {
                "X-Powered-By": "web2py",
                "Set-Cookie": "session_id_welcome",
            },
            "Flex": {
                "Server": "Flex",
            },
            "LoveCrafts": {
                "Server": "LoveCrafts",
                "X-LC-Sid": "",
                "X-LC-Rid": "",
            },
            "Jedi-Knight": {
                "Server": "Jedi Knight",
                "Set-Cookie": "jkeditinghub_data",
            },
            "4D": {
                "Server": "4D/",
            },
            "PAC": {
                "Server": "PAC",
            },
            "pac": {
                "Host": "pac1-cor.hybridcloudspan.com",
            },
            "Unspecified": {
                "SERVER": "Unspecified",
                "Server": "Unspecified",
            },
            "unspecified": {
                "Server": "unspecified",
            },
            "SCANA": {
                "Server": "SCANA",
                "SCANA-SSL-Version": "",
                "SCANA-SSL-Bits": "",
                "SCANA-SSL-Cipher": "",
            },
            "gogogadgeto-server": {
                "Server": "gogogadgeto-server",
            },
            "WorldShield": {
                "Server": "WorldShield",
            },
            "VIE-Portal-NG": {
                "Server": "VIE Portal NG",
                "X-Powered-By": "VIEPortalNG",
                "X-Correlation-ID": "VIE Portal NG",
                "X-Cache": "VIE Portal NG",
                "Set-Cookie": ".VIEPortal-SessionId",
            },
            "w3": {
                "Server": "w3/",
            },
            "CommuniGatePro": {
                "Server": "CommuniGatePro",
                "Location": "Master/MainAdmin",
            },
            "Private-Server": {
                "Server": "Private Server",
            },
            "App-Server": {
                "Server": "App-Server",
            },
            "cl-http": {
                "Server": "cl-http",
            },
            "CL-HTTP": {
                "Server": "CL-HTTP",
            },
            "Servlet": {
                "X-Powered-By": "Servlet",
            },
            "Play! Framework": {
                "Server": "Play! Framework",
                "Set-Cookie": "PLAY_SESSION",
            },
            "My-httpd-server": {
                "Server": "My httpd server",
            },
            "Digitalproserver": {
                "Server": "Digitalproserver",
            },
            "Inspopocom31": {
                "X-Server": "Inspopocom31",
            },
            "sepehr-proxy": {
                "Server": "sepehr-proxy",
            },
            "QWS": {
                "Server": "QWS",
                "QY-H-M": "",
            },
            "Glaucorm2": {
                "Server": "Glaucorm2",
            },
            "NaviServer": {
                "Server": "NaviServer",
            },
            "mine": {
                "Server": "mine",
            },
            "Mobile-Sales-Suite": {
                "Server": "Mobile Sales Suite",
            },
            "SWS": {
                "Server": "SWS",
            },
            "Secret": {
                "Server": "Secret",
            },
            "Hello-from-Server!": {
                "Server": "Hello from Server!",
            },
            "Jedi-business": {
                "Server": "Jedi business",
            },
            "FantasticWebServer": {
                "Server": "FantasticWebServer",
                "Location": "fantasticservices",
            },
            "ebay": {
                "Server": "ebay server",
                "X-EBAY-C-REQUEST-ID": "",
                "Set-Cookie": "ebay=",
            },
            "GMZLG": {
                "Server": "GMZLG",
            },
            "SentinelKeysServer": {
                "Server": "SentinelKeysServer",
            },
            "Viator-Secure": {
                "Server": "Viator Secure",
                "Set-Cookie": "x-viator-tapersistentcookie",
            },
            "Abyss": {
                "Server": "Abyss",
            },
            "quarxConnect.de": {
                "Server": "quarxConnect.de",
            },
            "PUMO-NETWORK": {
                "Server": "PUMO NETWORK",
            },
            "PCA": {
                "Server": "PCA",
            },
            "OPTIC": {
                "Server": "OPTIC",
            },
            "WRL-Cloud-Hosting": {
                "Server": "WRL-Cloud-Hosting",
                "X-Server-ID": "RabblerousingRhonda",
                "X-Load-Balancer": "JollyJeff",
            },
            "IndiaWeb": {
                "Server": "IndiaWeb",
            },
            "SSL-API-GATEWAY": {
                "Server": "SSL-API-GATEWAY",
                "X-IN-APIGATEWAY": "",
                "X-IN-APIGATEWAYSSL": "",
            },
            "Interlatin": {
                "Server": "Interlatin",
                "X-Powered-By": "Interlatin",
            },
            "hws": {
                "Server": "hws",
            },
            "HWS": {
                "Server": "HWS",
            },
            "Macro": {
                "Server": "Macro",
            },
            "XO.webservant": {
                "Server": "XO.webservant",
            },
            "FooServer": {
                "Server": "FooServer",
            },
            "NY1": {
                "Server": "NY1",
            },
            "SS&C": {
                "Server": "SS&C",
                "X-Powered-By": "SS&C",
            },
            "SS": {
                "Server": "SS",
            },
            "Indy": {
                "Server": "Indy",
            },
            "Douran-webserver": {
                "Server": "Douran",
                "Set-Cookie": "DouranPortal",
            },
            "Intsig-webserver": {
                "Server": "Intsig",
            },
            "eqmod_httpd": {
                "Server": "eqmod_httpd",
            },
            "ha113": {
                "Server": "ha113",
            },
            "C-007-1": {
                "Server": "C-007-1",
            },
            "BLB": {
                "Server": "BLB/",
            },
            "Proxy-Custome-Build": {
                "Server": "Proxy Custome Build",
            },
            "VDC": {
                "Server": "VDC",
            },
            "OurLounge": {
                "Server": "OurLounge",
                "Location": "ourlounge",
            },
            "LQG": {
                "Server": "LQG",
            },
            "AIX": {
                "Server": "AIX",
            },
            "TR-privateCloud": {
                "Server": "TR-privateCloud",
            },
            "BenQ-B2C": {
                "Server": "BenQ B2C",
            },
            "lighty": {
                "Server": "lighty",
            },
            "Web_Server": {
                "Server": "Web_Server",
            },
            "domecloud": {
                "Server": "domecloud",
            },
            "DomeCloud": {
                "Server": "DomeCloud",
                "X-DomeCloud-Cache": "",
                "X-DomeCloud-APP": "",
            },
            "WebRock": {
                "Server": "WebRock",
            },
            "BAY-WS": {
                "Server": "BAY-WS",
            },
            "Python-TwistedWeb": {
                "Server": "TwistedWeb",
                "Set-Cookie": "TWISTED_SESSION",
            },
            "Fotuto": {
                "Server": "Fotuto",
            },
            "HI": {
                "Server": "HI",
            },
            "CentralApp": {
                "Server": "CentralApp",
            },
            "PRD-FrontEnd": {
                "Server": "PRD FrontEnd",
            },
            "Primenets": {
                "Server": "Primenets",
            },
            "fastCache": {
                "Server": "fastCache",
            },
            "_waflopenresty": {
                "Server": "_waflopenresty",
            },
            "IDN-Server-System": {
                "Server": "IDN Server System",
            },
            "eBuyNow": {
                "Server": "eBuyNow",
                "Location": "ebuynow.com",
            },
            "TRD-Engine": {
                "Server": "TRD-Engine",
            },
            "nlappsrvr": {
                "Server": "nlappsrvr",
            },
            "Yaws": {
                "Server": "Yaws",
            },
            "WebtoB": {
                "Server": "WebtoB",
            },
            "CV": {
                "Server": "CV",
            },
            "mw1267.eqiad.wmnet": {
                "Server": "mw1267.eqiad.wmnet",
            },
            "RaidenHTTPD": {
                "Server": "RaidenHTTPD",
            },
            "TT-WS-WP": {
                "Server": "TT-WS-WP",
            },
            "Payara": {
                "Server": "Payara",
                "X-Powered-By": "Payara",
            },
            "bean": {
                "Server": "bean",
            },
            "Box-of-bolts": {
                "Server": "Box of bolts",
            },
            "WebServer.YanJ": {
                "Server": "WebServer.YanJ",
            },
            "Netscape-Enterprise": {
                "Server": "Netscape-Enterprise",
            },
            "Tui-Web": {
                "Server": "Tui Web",
            },
            "Netscape-iPlanet": {
                "Server": "Netscape-iPlanet",
            },
            "MSX-Turbo": {
                "Server": "MSX Turbo",
            },
            "Vodacom": {
                "Server": "Vodacom",
            },
            "App-webs": {
                "Server": "App-webs",
            },
            "KPN": {
                "Server": "KPN",
            },
            "SecureServer": {
                "Server": "SecureServer",
            },
            "Carbonmade": {
                "Server": "Carbonmade",
                "Location": "carbonmade",
            },
            "Soro": {
                "Server": "Soro",
                "X-Soro": "",
            },
            "ASPA-WAF": {
                "Server": "ASPA-WAF",
                "ASPA-Cache-Status": "",
            },
            "ASPAWAF": {
                "Server": "ASPAWAF",
            },
            "INT/Cache": {
                "Server": "INT/Cache",
            },
            "Tencent-Server-Web(Node.JS)": {
                "Server": "TSW/",
                "X-Powered-By": "TSW/",
            },
            "mini_httpd": {
                "Server": "mini_httpd",
            },
            "ZHUHAI": {
                "Server": "ZHUHAI",
            },
            "CERN-httpd": {
                "Server": "CERN httpd",
            },
            "Monkey": {
                "Server": "Monkey",
            },
            "MVCR": {
                "Server": "MVCR",
            },
            "Charles": {
                "Server": "Charles",
                "Via": "Charles",
                "X-Cache": "Charles",
            },
            "WP-Optimize": {
                "Server": "WP Optimize",
                "X-Powered-By": "WP Optimize",
            },
            "Difference": {
                "Server": "Difference",
            },
            "GCMS": {
                "Server": "GCMS",
            },
            "gcms": {
                "Server": "gcms",
            },
            "Comarch": {
                "Server": "Comarch",
            },
            "dvs.engine": {
                "Server": "dvs.engine",
            },
            "MIFE": {
                "Server": "MIFE",
                "X-Cacheable": "MI-STATIC",
            },
            "REDACTED": {
                "Server": "REDACTED",
            },
            "Radnet": {
                "Server": "Radnet",
            },
            "RadNet": {
                "Server": "RadNet",
            },
            "Linux/2.x UPnP/1.0 Avtech": {
                "Server": "Linux/2.x UPnP/1.0 Avtech",
            },
            "fs4host.com": {
                "Server": "fs4host.com",
            },
            "ARMIN/Server": {
                "Server": "ARMIN/Server",
            },
            "slardar": {
                "Server": "slardar",
            },
            "Nothing": {
                "Server": "Nothing",
            },
            "Spiral": {
                "Generator": "Spiral",
                "Set-Cookie": "spiral-localization",
            },
            "TFE": {
                "Server": "TFE",
            },
            "METRO-L3-Switch": {
                "Server": "METRO-L3-Switch",
            },
            "WonderHowTo": {
                "Server": "WonderHowTo",
                "Location": "wonderhowto",
            },
            "Nacho-WebServer": {
                "Server": "Nacho",
            },
            "AJ-Bell": {
                "Server": "AJ Bell",
            },
            "BitBalloon": {
                "Server": "BitBalloon",
            },
            "TUHUND": {
                "Server": "TUHUND",
                "Location": "tuhund",
            },
            "trx": {
                "Server": "trx",
            },
            "CPA-SERVER": {
                "Server": "CPA SERVER",
            },
            "Everscale": {
                "Server": "Everscale",
            },
            "rackcorp": {
                "Server": "rackcorp",
            },
            "Generic": {
                "Server": "Generic",
            },
            "securesauce": {
                "Server": "securesauce",
                "Set-Cookie": "cookie-encrypt",
            },
            "Hanbiro-Server-Centre": {
                "Server": "Hanbiro Server Centre",
            },
            "IPL": {
                "Server": "IPL/",
            },
            "NotAvailable": {
                "Server": "NotAvailable",
            },
            "GoIServer": {
                "Server": "GoIServer",
            },
            "Big-Server": {
                "Server": "Big Server",
            },
            "Your-Own-Server": {
                "Server": "Your Own Server",
            },
            "DSF": {
                "Server": "DSF",
            },
            "SCS-193.12": {
                "Server": "193.12",
            },
            "NE-webserver": {
                "Server": "NE webserver",
            },
            "SMQ": {
                "Server": "SMQ",
            },
            "Phenom": {
                "Server": "Phenom",
            },
            "EDE-Cloud": {
                "Server": "EDE Cloud",
                "Composed-By": "EDE Software",
                "X-Served-By": "EDE Software",
            },
            "Cirrus-CDN": {
                "Server": "Cirrus CDN",
            },
            "Grid/LoopSecure": {
                "Server": "Grid/LoopSecure",
                "X-Cacheable": "beresp.status",
            },
            "Vinahost": {
                "Server": "Vinahost",
                "X-Powered-By": "VinaHost",
            },
            "uPressPowerEdge": {
                "Server": "uPressPowerEdge",
            },
            "AppDrag-WebFront": {
                "Server": "AppDrag WebFront",
            },
            "Quaggans": {
                "Server": "Quaggans",
            },
            "VZW": {
                "Server": "VZW",
                "X-Powered-By": "VZW",
                "Set-cookie": ".vzw.com",
            },
            "SWM-Webserver": {
                "Server": "SWM Webserver",
            },
            "Pennsylvania": {
                "Server": "Pennsylvania",
            },
            "mthyz": {
                "Server": "mthyz",
            },
            "HFServer": {
                "Server": "HFServer",
            },
            "Oscar": {
                "Server": "Oscar",
                "X-Cdn-Origin": "CF_live",
            },
            "mystery": {
                "Server": "mystery",
                "Set-Cookie": "xomgappctx",
                "X-Omg-Tr-Av": "",
            },
            "Retif": {
                "Server": "Retif",
            },
            "Atlassian-Proxy": {
                "Server": "Atlassian Proxy",
            },
            "Userver": {
                "Server": "Userver",
            },
            "Mediacdn": {
                "Server": "Mediacdn",
            },
            "Tesco-webserver": {
                "Server": "Tesco",
            },
            "ZebuServer": {
                "Server": "ZebuServer",
            },
            "template243": {
                "Server": "template243",
                "Backend": "templates_newlaw_director",
            },
            "Irontec": {
                "Server": "Irontec",
            },
            "EnGenius_Router": {
                "Server": "EnGenius_Router",
            },
            "TANDBERG": {
                "Server": "TANDBERG",
            },
            "Ladesk-SIP-Proxy": {
                "Server": "Ladesk SIP Proxy",
            },
            "陌陌科技momo": {
                "Server": "momo",
                "Via": "momo.com",
            },
            "nikee2": {
                "Server": "nikee2",
            },
            "Undisclosed": {
                "Server": "Undisclosed",
            },
            "Webservices": {
                "Server": "Webservices",
            },
            "WebServices": {
                "Server": "WebServices",
                "x-rdn-server": "webservices",
            },
            "pirate": {
                "Server": "pirate",
            },
            "Refine": {
                "Server": "Refine",
            },
            "CISW": {
                "Server": "CISW",
            },
            "ITS": {
                "Server": "ITS",
                "X-Server": "WT7",
            },
            "100hub.com": {
                "Server": "100hub.com",
                "X-Powered-By": "100hub.com",
            },
            "August-Chat-System": {
                "Server": "August Chat System",
            },
            "nfront": {
                "Server": "nfront",
            },
            "IIS7": {
                "Server": "IIS7",
            },
            "iis7": {
                "Server": "iis7",
            },
            "KM-Galileo": {
                "Server": "KM Galileo",
            },
            "websdr": {
                "Server": "websdr",
            },
            "Dom-Cdn": {
                "Server": "Dom Cdn",
            },
            "Jeus-WebContainer": {
                "Server": "Jeus WebContainer",
            },
            "meuhost": {
                "Server": "meuhost",
                "Location": "meuhost.net",
            },
            "NWS_Oversea_AP": {
                "Server": "NWS_Oversea_AP",
            },
            "Voracio/Platform": {
                "Server": "Voracio/Platform",
            },
            "Sparkol-webserver": {
                "Server": "Sparkol",
            },
            "aerobiletf103": {
                "Server": "aerobiletf103",
            },
            "STP": {
                "Server": "STP/",
            },
            "Flagged": {
                "Server": "Flagged",
                "X-Powered-By": "Flagged",
            },
            "AnNyung": {
                "Server": "AnNyung",
            },
            "dms": {
                "Server": "dms",
            },
            "DMS": {
                "Server": "DMS",
            },
            "YServer": {
                "Server": "YServer",
            },
            "Yottaa": {
                "X-Yottaa-Metrics": "",
                "X-Yottaa-FW": "",
            },
            "ServaxNet": {
                "Server": "ServaxNet",
            },
            "NetScaler": {
                "Server": "NetScaler",
                "Set-Cookie": "NSC_",
            },
            "LTMP": {
                "Server": "LTMP",
            },
            "OracleDB": {
                "Server": "Oracle XML DB/Oracle Database",
            },
            "jpServer": {
                "Server": "jpServer",
            },
            "PhoneMore.com": {
                "Server": "PhoneMore.com",
            },
            "ASMP-AAA-Proxy": {
                "Server": "ASMP-AAA-Proxy",
            },
            "styx": {
                "Server": "styx",
                "X-Server": "styx",
            },
            "HulbeeWebServer": {
                "Server": "HulbeeWebServer",
                "X-Hostname-Hulbee": "",
            },
            "Win007": {
                "Server": "Win007",
            },
            "None-of-your-business": {
                "Server": "None of your business",
            },
            "Netdirekt": {
                "Server": "Netdirekt",
            },
            "CCAcc": {
                "Server": "CCAcc",
            },
            "InfoTip-Server": {
                "Server": "InfoTip-Server",
            },
            "PlantUML": {
                "Server": "PlantUML",
            },
            "Patreon": {
                "X-Patreon": "patreon",
            },
            "uServ": {
                "Server": "uServ",
            },
            "idi-httpd": {
                "Server": "idi-httpd",
            },
            "qServer": {
                "qServer": "sipXecs",
            },
            "comsenz": {
                "Server": "comsenz",
            },
            "KosWEB": {
                "Server": "KosWEB",
            },
            "mod_antiloris": {
                "Server": "mod_antiloris",
            },
            "Wabadoo": {
                "Server": "Wabadoo",
            },
            "MarkLogic": {
                "Server": "MarkLogic",
            },
            "CloudHTTPd": {
                "Server": "CloudHTTPd",
            },
            "DrunkenElefant": {
                "Server": "DrunkenElefant",
            },
            "esx": {
                "Server": "esx",
            },
            "Python-BaseHTTP": {
                "Server": "BaseHTTP",
            },
            "WebBox": {
                "Server": "WebBox",
            },
            "Moringa": {
                "Server": "Moringa",
            },
            "WLW": {
                "Server": "WLW-",
            },
            "NIRS": {
                "Server": "NIRS",
            },
            "Telking": {
                "Server": "Telking",
            },
            "Vesemir": {
                "Server": "Vesemir",
            },
            "WebOTX_Web_Server": {
                "Server": "WebOTX_Web_Server",
            },
            "OFE": {
                "Server": "OFE",
            },
            "ndns": {
                "Server": "ndns",
            },
            "Beast": {
                "Server": "Beast",
            },
            "nada": {
                "Server": "nada",
            },
            "NADA": {
                "Server": "NADA",
            },
            "IronPlanet": {
                "Server": "IronPlanet",
            },
            "inter@CEMI": {
                "Server": "inter@CEMI",
            },
            "AVN": {
                "Server": "AVN",
            },
            "Servidor": {
                "Server": "Servidor",
            },
            "TI-Brothers": {
                "X-Powered-By": "TI-Brothers",
            },
            "Abreu": {
                "Server": "Abreu",
            },
            "SAP-NetWeaver": {
                "Server": "SAP NetWeaver",
            },
            "Archive-Host": {
                "Server": "Archive-Host",
            },
            "Skye": {
                "Server": "Skye",
                "User-Agent": "Skye",
            },
            "BW-HTTP-Server": {
                "Server": "BW HTTP Server",
            },
            "Vyom": {
                "Server": "Vyom",
            },
            "Ygg-Webserver": {
                "Server": "Ygg Webserver",
            },
            "quizzclub_server": {
                "Server": "quizzclub_server",
            },
            "FreeOSHTTP": {
                "Server": "FreeOSHTTP",
            },
            "DSA": {
                "Server": "DSA",
            },
            "SchoolCloudSystems": {
                "Server": "SchoolCloudSystems",
            },
            "HayoolaServe": {
                "Server": "HayoolaServe",
            },
            "Columbus": {
                "Server": "Columbus",
                "X-Powered-By": "svgcolumbus.com",
                "Title": "data-driven digital",
            },
            "Alliance": {
                "Server": "Alliance",
            },
            "Foo": {
                "Server": "Foo",
            },
            "SiiN-Server": {
                "Server": "SiiN Server",
            },
            "HOTELPLANNER.COM": {
                "Server": "HOTELPLANNER.COM",
                "Location": "hotelplanner.com",
            },
            "netius": {
                "Server": "netius",
                "Via": "netius",
            },
            "IntareS-HACL": {
                "Server": "IntareS-HACL",
            },
            "WebSphere": {
                "Server": "WebSphere",
            },
            "MHRS9": {
                "Server": "MHRS9",
            },
            "Co-op": {
                "Server": "Co-op",
                "X-Powered-By": "Co-op",
            },
            "cat-factory": {
                "Server": "cat factory",
            },
            "CWS": {
                "Server": "CWS",
            },
            "reichelt-Webservice": {
                "Server": "reichelt Webservice",
                "Location": "reichelt",
            },
            "mod_security": {
                "Server": "mod_security",
            },
            "WebHare": {
                "Server": "WebHare",
            },
            "QTWS": {
                "Server": "QTWS",
            },
            "convesio": {
                "Server": "convesio",
            },
            "Kigo": {
                "Server": "Kigo",
            },
            "DAE-SSDP-Server": {
                "Server": "DAE SSDP Server",
            },
            "uvicorn": {
                "Server": "uvicorn",
                "x-enes-version": "",
            },
            "greenchu": {
                "Server": "greenchu",
            },
            "Security-Filter": {
                "Server": "Security Filter",
            },
            "Tableau": {
                "Server": "Tableau",
                "X-Tableau": "",
            },
            "MonexBoom": {
                "Server": "MonexBoom",
            },
            "Wedge": {
                "Server": "Wedge",
            },
            "Groupe-LDLC.com": {
                "Server": "Groupe-LDLC.com",
            },
            "GROUPE-LDLC": {
                "Server": "GROUPE LDLC",
            },
            "mtgxh": {
                "Server": "mtgxh",
            },
            "IPoAC": {
                "Server": "IPoAC",
                "XID-Deliver": "",
            },
            "Iteris": {
                "Server": "Iteris",
            },
            "vodafone.pt": {
                "Server": "vodafone.pt",
                "Set-Cookie": "ObSSOCookie",
            },
            "Paranoid": {
                "Server": "Paranoid",
            },
            "phpBB": {
                "Set-Cookie": "phpbb3",
            },
            "redir-httpd": {
                "Server": "redir-httpd",
            },
            "Netinternet": {
                "Server": "Netinternet",
            },
            "TDA": {
                "Server": "TDA",
                "Set-Cookie": "NSC_",
            },
            "CDNSpeed": {
                "Server": "CDNSpeed",
            },
            "cache.opcja.pl": {
                "Server": "cache.opcja.pl",
            },
            "FLP-Web": {
                "Server": "FLP Web",
                "Location": "flp.de",
            },
            "JCB": {
                "Server": "JCB",
                "Set-Cookie": "SC_ANALYTICS_GLOBAL_COOKIE",
                "X-Powered-By": "JCB",
            },
            "Snap": {
                "Server": "Snap",
            },
            "Z-World-Rabbit": {
                "Server": "Z-World Rabbit",
            },
            "UK": {
                "Server": "UK",
            },
            "urmom": {
                "Server": "urmom",
            },
            "UrMom": {
                "Server": "UrMom",
            },
            "CFS-0215": {
                "Server": "CFS 0215",
            },
            "cache02": {
                "Server": "cache02",
            },
            "TiMMiT": {
                "Server": "TiMMiT",
            },
            "Together-Cloud": {
                "Server": "Together Cloud",
            },
            "wrp101": {
                "Server": "wrp101",
            },
            "KNOTIA-TECH": {
                "Server": "KNOTIA-TECH",
            },
            "Sustainability-Victoria": {
                "Server": "Sustainability",
            },
            "meinheld": {
                "Server": "meinheld",
            },
            "NCOL": {
                "Server": "NCOL",
            },
            "TTserver": {
                "Server": "TTserver",
            },
            "U-NEXT": {
                "Server": "U-NEXT",
            },
            "Aliantic": {
                "Server": "Aliantic",
            },
            "Infoclimat": {
                "Server": "Infoclimat",
                "Location": "infoclimat",
                "X-Powered-By": "Infoclimat",
            },
            "RMBHJMS": {
                "Server": "RMBHJMS",
            },
            "durable": {
                "Server": "durable",
            },
            "WebCelerate": {
                "Server": "WebCelerate",
                "Via": "WebCelerate",
                "X-Webcelerate": "",
            },
            "FileSolutions": {
                "Server": "FileSolutions",
            },
            "Jumeirah-Security-Servers": {
                "Server": "Jumeirah",
                "X-Powered-By": "Jumeirah",
            },
            "DNSPod": {
                "Server": "DNSPod",
            },
            "Rabbit": {
                "Server": "Rabbit",
            },
            "MF2": {
                "Server": "MF2",
            },
            "Livemaster": {
                "Server": "Livemaster",
            },
            "snooserv": {
                "Server": "snooserv",
            },
            "http-kit": {
                "Server": "http-kit",
            },
            "am/2": {
                "Server": "am/2",
            },
            "METRO": {
                "Server": "METRO",
            },
            "Strategi": {
                "Server": "Strategi",
            },
            "cws": {
                "Server": "cws",
            },
            "VA_System": {
                "Server": "VA_System",
            },
            "Hunchentoot": {
                "Server": "Hunchentoot",
                "Set-Cookie": "hunchentoot-session",
            },
            "Mono-HTTPAPI": {
                "Server": "Mono-HTTPAPI",
                "X-ApplicationVersion": "",
            },
            "Power-Sockets": {
                "Server": "Power-Sockets",
            },
            "Moodle": {
                "Server": "Moodle",
                "X-Powered-By": "Moodle",
                "Set-Cookie": "MoodleSession",
            },
            "noal.org.il": {
                "Server": "noal.org.il",
            },
            "CCTV_WebServer": {
                "Server": "CCTV_WebServer",
            },
            "schuh-bamberg": {
                "X-Backend-Server": "schuh-bamberg",
            },
            "Darwin": {
                "Server": "Darwin",
            },
            "Instituto-Metodista": {
                "Server": "Instituto Metodista",
            },
            "monobank": {
                "Server": "monobank",
            },
            "UGC": {
                "Server": "UGC",
            },
            "mszs2": {
                "Server": "mszs2",
                "X-Powered-By": "mszx2",
            },
            "LoudClear-webserver": {
                "Server": "LoudClear",
            },
            "VitalityServer": {
                "Server": "VitalityServer",
                "Set-Cookie": "ruc-session-id",
            },
            "MyFRITZ": {
                "Server": "MyFRITZ",
            },
            "JuanniuX": {
                "Server": "JuanniuX",
            },
            "Vetorial.net": {
                "Server": "Vetorial.net",
            },
            "365GCD": {
                "Server": "365GCD",
            },
            "UoL-WebServer": {
                "Server": "UoL Web Server",
            },
            "Knstat": {
                "Server": "Knstat",
            },
            "tarena": {
                "Server": "tarena",
            },
            "PEN-PEN": {
                "Server": "PEN PEN",
            },
            "My_Server": {
                "Server": "My_Server",
            },
            "x-speed": {
                "Server": "x-speed",
            },
            "Lasso": {
                "Server": "Lasso",
            },
            "unknownX": {
                "Server": "unknownX",
            },
            "Sarenet-webserver": {
                "Server": "Sarenet",
            },
            "Miginiz": {
                "Server": "Miginiz",
            },
            "www.lexisnexis.com": {
                "Server": "www.lexisnexis.com",
                "Set-Cookie": "LNMEGASITE=",
            },
            "塞班Symbian": {
                "Server": "Symbian",
            },
            "Tibus": {
                "Server": "Tibus",
            },
            "Honeywell": {
                "Server": "Honeywell",
            },
            "Altair": {
                "Server": "Altair",
            },
            "FCR-MEDIA": {
                "Server": "FCR MEDIA",
            },
            "elektronik": {
                "Server": "elektronik",
            },
            "F5": {
                "Server": "F5",
            },
            "Nagix": {
                "Server": "Nagix",
            },
            "nxweb": {
                "Server": "nxweb",
            },
            "NxWEB": {
                "Server": "NxWEB",
            },
            "litb-webserver": {
                "Server": "litb-webserver",
                "Set-Cookie": "first_visit_time",
            },
            "Teamie": {
                "Server": "Teamie",
                "X-Teamie-Server": "",
                "X-Server-Name": "server-main",
                "Access-Control-Allow-Headers": "X-Teamie-Api-Version",
            },
            "ecstatic": {
                "Server": "ecstatic",
            },
            "NWS_Qcloud_Oversea_Static_Mid": {
                "Server": "NWS_Qcloud_Oversea_Static_Mid",
            },
            "Sansun-Calakci": {
                "Server": "Sansun Calakci",
            },
            "FWS": {
                "Server": "FWS",
            },
            "Reshift-Digital": {
                "Server": "Reshift Digital",
            },
            "BizMaC.Cloud": {
                "Server": "BizMaC.Cloud",
                "X-Powered-By": "BizMaC.CMS",
            },
            "CloudRambo": {
                "Server": "CloudRambo",
                "Server-Info": "CloudRamb",
                "X-Powered-By": "CloudRamb",
                "X-Page-Speed": "CloudRamb",
            },
            "EngineX": {
                "Server": "Engine X",
            },
            "Engine-X": {
                "Server": "Engine-X",
            },
            "Next-Gen": {
                "Server": "Next-Gen",
            },
            "DZ-HTTP": {
                "Server": "DZ-HTTP",
            },
            "Weyes-Web": {
                "Server": "Weyes-Web",
            },
            "ustream": {
                "Server": "ustream",
                "X-BackendOrigin": "",
            },
            "tizra": {
                "Server": "tizra",
            },
            "WooyaServer": {
                "Server": "WooyaServer",
            },
            "Tips": {
                "Server": "Tips",
            },
            "DT-54": {
                "Server": "DT-54",
            },
            "callr": {
                "Server": "callr",
            },
            "www.rb.cz": {
                "Server": "www.rb.cz",
            },
            "BSF-Online-Services": {
                "Server": "BSF Online Services",
            },
            "Blue-sky-Server": {
                "Server": "Blue-sky-Server",
            },
            "TBS": {
                "Server": "TBS/",
            },
            "sdn": {
                "Server": "sdn/",
            },
            "wedeploy/hosting": {
                "Server": "wedeploy/hosting",
            },
            "APIP": {
                "Server": "APIP",
            },
            "Dolce & Gabbana": {
                "Server": "Dolce & Gabbana",
            },
            "Schnapps": {
                "Server": "Schnapps",
            },
            "x-web": {
                "Server": "x-web",
            },
            "X-Web": {
                "Server": "X-Web",
            },
            "kHTTPd": {
                "Server": "kHTTPd",
            },
            "UBG-HTTPServer": {
                "Server": "UBG HTTP Server",
            },
            "iptoX-GmbH": {
                "Server": "iptoX GmbH",
            },
            "Server-LNAMP": {
                "Server": "Server LNAMP",
            },
            "Ikano-webserver": {
                "Server": "Ikano",
            },
            "BlueStripe.PVN": {
                "Set-Cookie": "BlueStripe.PVN",
            },
            "roiback-ha-server": {
                "Server": "roiback-ha-server",
            },
            "RCMP": {
                "Server": "RCMP",
                "X-Powered-By": "RCMP",
            },
            "ASPENCORE": {
                "Server": "ASPENCORE",
            },
            "WMaker/Prod": {
                "Server": "WMaker/Prod",
            },
            "PayuMoney": {
                "Server": "PayuMoney",
            },
            "Gupshup-Webserver": {
                "Server": "Gupshup-Webserver",
            },
            "Minion": {
                "Server": "Minion",
            },
            "RWS": {
                "Server": "RWS",
            },
            "Rws": {
                "Server": "Rws",
            },
            "rws": {
                "Server": "rws",
            },
            "Hualv-FES": {
                "Server": "Hualv FES",
            },
            "PlipPlop": {
                "Server": "PlipPlop",
            },
            "Clickky": {
                "Server": "Clickky",
            },
            "GES": {
                "Server": "GES",
            },
            "Ben_Kenobi": {
                "Server": "Ben_Kenobi",
            },
            "No-Probing": {
                "Server": "No Probing",
                "X-Powered-By": "No Probing",
            },
            "Podbean-CDN": {
                "Server": "Podbean",
            },
            "FODWWW": {
                "Server": "FODWWW",
            },
            "LS-Secure-webserver": {
                "Server": "LS Secure",
            },
            "Nimbu.io": {
                "Server": "Nimbu.io",
            },
            "OVIT": {
                "Server": "OVIT",
            },
            "fasthttp": {
                "Server": "fasthttp",
            },
            "Appache": {
                "Server": "Appache",
            },
            "WestLotto": {
                "Server": "WestLotto",
                "Set-Cookie": "cZFx",
            },
            "TRS": {
                "Server": "TRS",
            },
            "Duo": {
                "Server": "Duo/",
            },
            "nCore": {
                "Server": "nCore",
                "Location": "ncore.cc",
            },
            "cpasWS": {
                "Server": "cpasWS",
            },
            "ZX2C4-webserver": {
                "Server": "ZX2C4",
            },
            "GreyCDN-Tengine": {
                "Server": "GreyCDN-Tengine",
            },
            "WT_11.12": {
                "Server": "WT_11.12",
            },
            "Triptych": {
                "Server": "Triptych",
            },
            "b4f": {
                "Server": "b4f",
            },
            "Glaucome2": {
                "Server": "Glaucome2",
            },
            "BlueIris": {
                "Server": "BlueIris",
            },
            "Innova": {
                "Server": "Innova",
                "X-Powered-By": "Innova",
                "X-AspNetMvc-Version": "Innova",
                "X-AspNet-Version": "Innova",
            },
            "LWS1.1": {
                "Server": "LWS1.1",
            },
            "SAP_acz": {
                "Server": "SAP_acz",
            },
            "gatejs": {
                "Server": "gatejs",
                "Via": "gatejs",
            },
            "RapidLogic": {
                "Server": "RapidLogic",
            },
            "iws": {
                "Server": "iws",
            },
            "IWS": {
                "Server": "IWS",
            },
            "IPRAGAZ-webserver": {
                "Server": "IPRAGAZ",
            },
            "Mynet": {
                "Server": "Mynet",
                "X-Powered-By": "Mynet",
            },
            "TUIfly.com": {
                "Server": "TUIfly.com",
            },
            "BSE-LTD": {
                "Server": "BSE LTD",
            },
            "SDX-Router": {
                "Server": "SDX Router",
            },
            "Nastooh": {
                "Server": "Nastooh",
            },
            "CamembertServer": {
                "Server": "CamembertServer",
            },
            "InSite": {
                "Server": "InSite",
                "X-Powered-By": "InSite",
            },
            "Prometheus": {
                "Server": "Prometheus",
                "Pre-Cognitive-Push": "",
                "Quantum-Flux-Capacity": "",
            },
            "ibweb203": {
                "Server": "ibweb203",
            },
            "SNP-PROXY": {
                "Server": "SNP PROXY",
            },
            "VilaWeb": {
                "Server": "VilaWeb",
            },
            "HCM": {
                "Server": "HCM",
            },
            "Concealed": {
                "Server": "Concealed",
            },
            "ADV-HTTPD": {
                "Server": "ADV-HTTPD",
            },
            "JIO": {
                "Server": "JIO",
            },
            "Bura-webserver": {
                "Server": "Bura Web Server",
            },
            "xShieldx": {
                "X-Powered-By": "xShieldx",
            },
            "EWA-CDN": {
                "Server": "EWA CDN",
            },
            "SB-Ranger": {
                "Server": "SB Ranger",
            },
            "Lemonhead": {
                "X-bCube-Filmed-By": "Lemonhead",
                "X-Bcube-Generated-By": "Lemonhead",
            },
            "ParsOnline": {
                "Server": "ParsOnline",
            },
            "Vanguard": {
                "Server": "Vanguard",
            },
            "kong": {
                "Server": "kong/",
            },
            "s8-api-server": {
                "Server": "s8-api-server",
            },
            "NURSING": {
                "Server": "NURSING",
            },
            "UNIQA": {
                "Server": "UNIQA",
            },
            "Uniqa": {
                "Server": "Uniqa",
            },
            "Showrand": {
                "Server": "Showrand",
            },
            "OOS": {
                "Server": "OOS",
            },
            "M-W": {
                "Server": "M-W",
                "X-Powered-By": "Port Eighty Hosting",
            },
            "iSpot": {
                "Server": "iSpot",
            },
            "msg": {
                "Server": "msg",
            },
            "MSG": {
                "Server": "MSG",
            },
            "CaravanWebServer": {
                "Server": "CaravanWebServer",
            },
            "Edistrict-webserver": {
                "Server": "Edistrict",
            },
            "MasterWS": {
                "Server": "MasterWS",
            },
            "bq": {
                "Server": "bq",
            },
            "BoC": {
                "Server": "BoC",
            },
            "0W/0.8d": {
                "Server": "0W/0.8d",
            },
            "SaiGonPixelServer": {
                "Server": "SaiGonPixelServer",
                "Set-Cookie": "_culture=",
            },
            "LiteWeb": {
                "Server": "LiteWeb",
            },
            "RZ-WIKA": {
                "Server": "RZ WIKA",
            },
            "Cray": {
                "Server": "Cray",
            },
            "follow-webserver": {
                "Server": "follow-webserver",
            },
            "NProxy": {
                "Server": "NProxy",
            },
            "skistar.com": {
                "Server": "skistar.com",
            },
            "MuaBanNhanh": {
                "Server": "MuaBanNhanh",
            },
            "adf_http_server": {
                "Server": "adf_http_server",
            },
            "PoudreVerte": {
                "Server": "PoudreVerte",
            },
            "Gabia": {
                "Server": "Gabia",
            },
            "gabia": {
                "Server": "gabia",
                "Set-Cookie": "gasession=",
            },
            "awlb": {
                "Server": "awlb",
            },
            "Mediawill": {
                "Server": "Mediawill",
            },
            "lapis": {
                "Server": "lapis",
            },
            "链家Lianjia": {
                "Server": "Lianjia",
                "Set-Cookie": "lianjia_ssid",
            },
            "fastmirror": {
                "Server": "fastmirror",
            },
            "Rondtarin": {
                "Server": "Rondtarin",
            },
            "USIL-HTTPD": {
                "Server": "USIL HTTPD",
            },
            "supreme": {
                "Server": "supreme",
            },
            "CPWS": {
                "Server": "CPWS",
            },
            "Linux": {
                "Server": "Linux",
            },
            "gomenyan": {
                "Server": "gomenyan",
                "XXX-Admin": "",
            },
            "websvr": {
                "Server": "websvr",
            },
            "UEA-App-Server": {
                "Server": "UEA App Server",
                "UEAID": "",
            },
            "MYPANEL": {
                "Server": "MYPANEL",
            },
            "_lzx_": {
                "Server": "_lzx_",
            },
            "Changed": {
                "Server": "Changed",
            },
            "Webser": {
                "Server": "Webser",
            },
            "cloudwall": {
                "Server": "cloudwall",
                "X-CloudWall": "",
            },
            "SysDSI": {
                "Server": "SysDSI",
            },
            "Microseven": {
                "Server": "Microseven",
            },
            "MICROSEVEN": {
                "Server": "MICROSEVEN",
            },
            "Cheetah-webserver": {
                "Server": "Cheetah",
            },
            "WSO2-Carbon-Server": {
                "Server": "WSO2 Carbon",
            },
            "IBM-Mobile-Connect": {
                "Server": "IBM Mobile Connect",
            },
            "IBM-IMM2": {
                "Server": "IBM IMM2",
            },
            "Infermedica": {
                "Server": "Infermedica",
            },
            "TQServer": {
                "Server": "TQServer",
            },
            "ngx-flair": {
                "Server": "ngx-flair",
            },
            "KirchenWS_6.1.2": {
                "Server": "KirchenWS_6.1.2",
            },
            "SPECTRE": {
                "Server": "SPECTRE",
            },
            "Reed-Exhibitions": {
                "Server": "Reed Exhibitions",
            },
            "MGAME_SERVER": {
                "Server": "MGAME_SERVER",
            },
            "TNPDS-webserver": {
                "Server": "TNPDS",
            },
            "Molly-and-John": {
                "Server": "Molly and John",
            },
            "PlusPowered": {
                "Server": "PlusPowered",
                "X-Powered-By": "PlusPowered",
            },
            "muscope": {
                "Server": "muscope",
            },
            "Grayskull": {
                "X-Powered-By": "Grayskull",
            },
            "HuaweiCloudWAF": {
                "Server": "CloudWAF",
            },
            "Adwise": {
                "Server": "Adwise",
                "Author": "Adwise",
            },
            "Jagermeister": {
                "Server": "Jagermeister",
            },
            "ArtaServer": {
                "Server": "ArtaServer",
            },
            "AdaptiveServerAnywhere": {
                "Server": "AdaptiveServerAnywhere",
            },
            "DaubK": {
                "Server": "DaubK",
            },
            "RusEngine": {
                "Server": "RusEngine",
            },
            "Ravian": {
                "Server": "Ravian",
                "X-AspNet-Version": "Ravian",
                "X-Powered-By": "Ravian",
                "X-AspNetMvc-Version": "Ravian",
            },
            "StackBlitz": {
                "Server": "StackBlitz",
            },
            "Hotcores": {
                "Server": "Hotcores",
            },
            "WCSFlare": {
                "Server": "WCSFlare",
            },
            "FIATPRESS2": {
                "Server": "FIATPRESS2",
            },
            "86f0-Kucci": {
                "Server": "86f0 Kucci",
            },
            "Smarthouse-Lightspeed": {
                "Server": "Smarthouse Lightspeed",
            },
            "ECHELON": {
                "Server": "ECHELON",
            },
            "PCX/Cache": {
                "Server": "PCX/Cache",
            },
            "guess-which": {
                "Server": "guess which",
            },
            "VellanceBlast": {
                "Server": "VellanceBlast",
                "Via": "VellanceBlast",
            },
            "PAweb": {
                "Server": "PAweb",
            },
            "DesignInc": {
                "Server": "DesignInc",
            },
            "uewaf": {
                "Server": "uewaf",
            },
            "安全宝aserver": {
                "Server": "aserver",
            },
            "安全宝Aserver": {
                "Server": "Aserver",
            },
            "MWS": {
                "Server": "MWS/",
            },
            "movieextras": {
                "Server": "movieextras",
            },
            "AngryDog": {
                "Server": "AngryDog",
            },
            "SolwaysCuba": {
                "Server": "SolwaysCuba",
            },
            "Steel-and-Mines": {
                "Server": "Steel and Mines",
            },
            "GMN/RedPort": {
                "Server": "GMN/RedPort",
            },
            "medPass": {
                "Server": "medPass",
                "X-Powered-By": "medPass",
                "Set-Cookie": "medpassSessionId",
                "Location": "medpass",
            },
            "unset": {
                "Server": "unset",
                "X-Powered-By": "unset",
            },
            "ninja": {
                "Server": "ninja_session",
            },
            "Showhaber": {
                "Server": "Showhaber",
            },
            "cPSistem": {
                "Server": "cPSistem",
                "Application-Version": "cPSistem",
            },
            "Deutsche-Sporthochschule-Koeln": {
                "Server": "Deutsche Sporthochschule Koeln",
            },
            "ttas": {
                "Server": "ttas/",
            },
            "BSWS": {
                "Server": "BSWS",
            },
            "Melexis": {
                "Server": "Melexis",
            },
            "Alpes-One-Service": {
                "Server": "Alpes One Service",
                "X-Powered-By": "DevOps Scherney Schwalbe",
            },
            "heaveniphone.com": {
                "Server": "heaveniphone.com",
            },
            "TVPlayer": {
                "Server": "TVPlayer",
            },
            "OfficeDepotWebServer": {
                "Server": "OfficeDepotWebServer",
            },
            "Merus-Magic": {
                "Server": "Merus Magic",
                "Lots": "of Coffee",
            },
            "Kebab-Enterprise-Server": {
                "Server": "Kebab",
                "X-Tried-To-Kebabify": "",
                "X-Kebabable": "",
                "X-Kebab": "",
            },
            "wenjoys": {
                "Server": "wenjoys",
            },
            "teddy": {
                "Server": "teddy",
            },
            "Teddy": {
                "Server": "Teddy",
            },
            "llLUL-WWW": {
                "Server": "llLUL-WWW",
            },
            "Nexgate": {
                "Server": "Nexgate",
            },
            "NHP": {
                "Server": "NHP",
            },
            "Penny": {
                "Server": "Penny",
            },
            "phpMyAdmin": {
                "Set-Cookie": "phpMyAdmin",
            },
            "cernercentral_home1": {
                "Server": "cernercentral_home1",
            },
            "Mohammad-Luqman-Server": {
                "Server": "Mohammad-Luqman-Server",
            },
            "Healthx/Healthx": {
                "Server": "Healthx/Healthx",
            },
            "va1": {
                "Server": "va1",
            },
            "mw1262.eqiad.wmnet": {
                "Server": "mw1262.eqiad.wmnet",
            },
            "pingodoce": {
                "Server": "pingodoce",
                "Location": "pingodoce",
            },
            "fi.ai": {
                "Server": "fi.ai",
            },
            "Yoobi": {
                "Server": "Yoobi",
            },
            "Rapidbaz": {
                "Server": "Rapidbaz",
                "X-Powered-By": "Rapidbaz",
            },
            "Web_Server_4D": {
                "Server": "Web_Server_4D",
            },
            "Milchschaum": {
                "Server": "Milchschaum",
            },
            "www.imyfone.com": {
                "Server": "www.imyfone.com",
            },
            "mwave": {
                "Server": "mwave",
                "Set-Cookie": "MWAVE_SESSION",
            },
            "MoneyTips": {
                "Server": "MoneyTips",
                "Link": "www.moneytips.com",
            },
            "ngnix": {
                "Server": "ngnix",
            },
            "F5aaS": {
                "Server": "F5aaS",
            },
            "uca.edu": {
                "Server": "uca.edu",
            },
            "preisdeWeb": {
                "Server": "preisdeWeb",
            },
            "1MG-Server": {
                "Server": "1MG-Server",
            },
            "Sportsmans": {
                "Server": "Sportsmans",
            },
            "B-007-1": {
                "Server": "B-007-1",
            },
            "AGMB-Web-Server": {
                "Server": "AGMB Web Server",
            },
            "Daemon": {
                "Server": "Daemon",
            },
            "Rumpus": {
                "Server": "Rumpus",
            },
            "GR-HTTPD": {
                "Server": "GR-HTTPD",
            },
            "XMAIL.NET": {
                "Server": "XMAIL.NET",
                "Location": "www.xmail.net",
            },
            "Autostrade": {
                "Server": "Autostrade",
            },
            "KSIDC": {
                "Server": "KSIDC",
            },
            "PU": {
                "Server": "PU",
            },
            "ISS-Autoscope": {
                "Server": "ISS Autoscope",
            },
            "Heptu-webserver": {
                "Server": "Heptu",
            },
            "JRun": {
                "Server": "JRun",
            },
            "Jenkins": {
                "X-Jenkins": "",
                "X-Jenkins-Session": "",
                "X-You-Are-In-Group-Disabled": "JENKINS",
                "X-Jenkins-CLI-Port": "",
                "X-Jenkins-CLI2-Port": "",

            },
            "swr-in": {
                "Server": "swr-in",
            },
            "SWR Webservice": {
                "Server": "SWR Webservice",
            },
            "GrupoSura": {
                "Server": "GrupoSura",
            },
            "Linktrails": {
                "Server": "Linktrails",
            },
            "IV-Web-Server": {
                "Server": "IV Web Server",
            },
            "mw1264.eqiad.wmnet": {
                "Server": "mw1264.eqiad.wmnet",
            },
            "CSM-Tools": {
                "Server": "CSM-Tools",
            },
            "CSM": {
                "Server": "CSM",
            },
            "csm": {
                "Server": "csm",
            },
            "Nasturcjan": {
                "Server": "Nasturcjan",
                "X-Powered-By": "Nasturcjan",
            },
            "mfcu": {
                "Server": "mfcu",
            },
            "HMWS-webserver": {
                "Server": "HMWS",
            },
            "Jeeves": {
                "Server": "Jeeves",
            },
            "109809809809": {
                "Server": "109809809809",
            },
            "Iris": {
                "Server": "Iris",
            },
            "iris": {
                "Server": "iris",
            },
            "IRIS": {
                "Server": "IRIS",
            },
            "DogsNow": {
                "Server": "DogsNow",
            },
            "BoxerEngine": {
                "Server": "BoxerEngine",
            },
            "webserver": {
                "Server": "webserver",
            },
            "Wakanda": {
                "Server": "Wakanda",
            },
            "Weaveability": {
                "Server": "Weaveability",
            },
            "PRAGYAWARE": {
                "Server": "PRAGYAWARE",
            },
            "THECHEAT": {
                "Server": "THECHEAT",
            },
            "X-Ada": {
                "Server": "X-Ada/",
            },
            "pchome": {
                "Server": "pchome",
            },
            "leasewebcdn": {
                "Server": "leasewebcdn",
            },
            "kali": {
                "Server": "kali",
            },
            "unicorns": {
                "Server": "unicorns",
            },
            "homeppl.com": {
                "Server": "homeppl.com",
            },
            "corporateaffiliations.com": {
                "Server": "corporateaffiliations.com",
            },
            "Redfish": {
                "Server": "Redfish",
            },
            "BSrapture": {
                "Server": "BSrapture",
            },
            "Prism-WSHOST": {
                "Server": "Prism WSHOST",
            },
            "Tapzo": {
                "Server": "Tapzo",
            },
            "PJNServer": {
                "Server": "PJNServer",
            },
            "ColdStorage_Server": {
                "Server": "ColdStorage_Server",
            },
            "TCG": {
                "Server": "TCG",
            },
            "TORC-mailserver": {
                "Server": "TORC Mail",
            },
            "wigsbuy-NY": {
                "Server": "wigsbuy-NY",
            },
            "MFU": {
                "Server": "MFU",
            },
            "TNWS": {
                "Server": "TNWS",
            },
            "ServelWS": {
                "Server": "ServelWS",
                "X-Powered-By": "Servel",
            },
            "NashaLife": {
                "Server": "NashaLife",
            },
            "auctollo.net": {
                "Server": "auctollo.net",
            },
            "EZproxy": {
                "Server": "EZproxy",
            },
            "QuickLaunchv4": {
                "Server": "QuickLaunchv4",
            },
            "Virtuous-Reviews-webserver": {
                "Server": "Virtuous Reviews",
                "Set-Cookie": "_VirtuousReviews",
            },
            "GFF": {
                "Server": "GFF/",
            },
            "Lua": {
                "Server": "lua-httpd",
                "X-Powered-By": "Lua",
            },
            "AHBV_HTTP_Server_by_iaksit": {
                "Server": "AHBV_HTTP_Server_by_iaksit",
            },
            "off": {
                "Server": "off",
            },
            "inbox.lt": {
                "Server": "inbox.lt",
            },
            "inbox.lv": {
                "Server": "inbox.lv",
            },
            "Spacelink": {
                "Server": "Spacelink",
                "Location": "spacelink",
            },
            "MangaBox": {
                "Server": "MangaBox",
            },
            "Stream-Market-Web-Server": {
                "Server": "Stream Market",
            },
            "PALSS": {
                "Server": "PALSS",
            },
            "Not-allowed": {
                "Server": "Not-allowed",
            },
            "BIDWARE": {
                "Server": "BIDWARE",
                "X-Powered-By": "BIDWARE",
            },
            "MessageXchange": {
                "Server": "MessageXchange",
                "Location": "messagexchange",
            },
            "iLang-Server": {
                "Server": "iLang Server",
            },
            "OracleAS": {
                "Server": "OracleAS",
            },
            "Danoshop-Server": {
                "Server": "Danoshop",
            },
            "NFM-LTM-Server": {
                "Server": "NFM-LTM-Server",
            },
            "vload.expert": {
                "Server": "vload.expert",
            },
            "Kaazing Gateway": {
                "Server": "Kaazing",
            },
            "Oracle9iAS": {
                "Server": "Oracle9iAS",
            },
            "Draper-Esprit": {
                "Server": "Draper Esprit",
            },
            "multinet": {
                "Server": "multinet",
            },
            "sinergia": {
                "Server": "sinergia",
            },
            "sclws": {
                "Server": "sclws",
            },
            "SCLWS": {
                "Server": "SCLWS",
            },
            "Present": {
                "Server": "Present",
            },
            "SmartWebServer": {
                "Server": "SmartWebServer",
            },
            "OurServer": {
                "Server": "OurServer",
            },
            "cloudleft": {
                "Server": "cloudleft",
            },
            "QiaoNaoCDN": {
                "Server": "QiaoNaoCDN",
            },
            "5lux_server": {
                "Server": "5lux_server",
            },
            "Acturis-webserver": {
                "Server": "Acturis",
                "Set-Cookie": "Acturis.ASPXSESSION",
            },
            "ZomatoBook": {
                "Server": "ZomatoBook",
                "X-Powered-By": "ZomatoBook",
                "X-ZB-TransactionId": "",
                "X-ZB-ServerTime": "",
                "Location": "zomatobook",
            },
            "ZWS": {
                "Server": "ZWS/",
            },
            "Corelan-webserver": {
                "Server": "Corelan",
            },
            "www.cnb.com": {
                "Server": "www.cnb.com",
            },
            "Exeter-College": {
                "Server": "Exeter College",
            },
            "WCA-System": {
                "Server": "WCA System",
            },
            "LDLC.com": {
                "Server": "LDLC.com",
            },
            "Daniel15-Web": {
                "Server": "Daniel15-Web",
            },
            "7sobh": {
                "Server": "7sobh",
                "Location": "7sobh.com",
            },
            "CM": {
                "Server": "CM",
            },
            "Ahnlab": {
                "Server": "Ahnlab",
                "Location": "ahnlab.com",
            },
            "ConferiumWebServer": {
                "Server": "ConferiumWebServer",
            },
            "civetweb": {
                "Server": "civetweb",
            },
            "Selency": {
                "Server": "Selency",
                "X-Powered-By": "Selency",
            },
            "figi_Server": {
                "Server": "figi_Server",
            },
            "hakase": {
                "Server": "hakase",
            },
            "JNP-HTTPD": {
                "Server": "JNP-HTTPD",
            },
            "151.35": {
                "Server": "151.35",
            },
            "Aeria-Games": {
                "Server": "Aeria Games",
            },
            "boss": {
                "Server": "boss/",
            },
            "Lucy-HTTPd": {
                "Server": "Lucy-HTTPd",
            },
            "BageIO": {
                "Server": "BageIO",
            },
            "TranscribeMe": {
                "Server": "TranscribeMe",
            },
            "API-GATEWAYSSL": {
                "Server": "API-GATEWAYSSL",
            },
            "AmigoServ.CoM": {
                "Server": "AmigoServ.CoM",
            },
            "wongnai": {
                "Server": "wongnai",
            },
            "Docker": {
                "Docker-Distribution-Api-Version": "",
            },
            "Allibo": {
                "Server": "Allibo",
            },
            "ardu1n0-uhttpd": {
                "Server": "ardu1n0-uhttpd",
            },
            "Joker.com-HTTP-Parking-Server": {
                "Server": "Joker.com HTTP Parking Server",
            },
            "wisekey": {
                "Server": "wisekey",
            },
            "www.info01.it": {
                "Server": "www.info01.it",
            },
            "aerishttpd": {
                "Server": "aerishttpd",
            },
            "Destiny": {
                "Server": "Destiny",
                "X-Powered-By": "Follett School Solutions",
            },
            "KSOWS": {
                "Server": "KSOWS",
            },
            "IcodiaWebmelHttpd": {
                "Server": "IcodiaWebmelHttpd",
            },
            "WebSTAR": {
                "Server": "WebSTAR",
            },
            "UHS": {
                "Server": "UHS",
            },
            "Gramex": {
                "Server": "Gramex",
            },
            "Epic-Dental": {
                "Server": "Epic Dental",
            },
            "DNVRS-Webs": {
                "Server": "DNVRS-Webs",
            },
            "Courcasa": {
                "Server": "Courcasa",
                "X-Powered-By": "Courcasa",
                "Location": "courcasa",
            },
            "ViecLam24h-HTTP2": {
                "Server": "ViecLam24h-HTTP2",
            },
            "wikittpd": {
                "Server": "wikittpd",
            },
            "icreate": {
                "Server": "icreate",
            },
            "Hoqool.NET": {
                "Server": "Hoqool.NET",
            },
            "WP-Dedicated": {
                "Server": "WP Dedicated",
            },
            "stern-freunde": {
                "Server": "stern-freunde",
            },
            "7eleven": {
                "Server": "7eleven",
            },
            "NinjaCat-Hybrid": {
                "Server": "NinjaCat Hybrid",
            },
            "LeapFILE": {
                "Server": "LeapFILE",
            },
            "QS": {
                "Server": "QS",
            },
            "QibuCloud": {
                "Server": "QibuCloud",
            },
            "IISShield": {
                "Server": "IISShield",
            },
            "Toaster": {
                "Server": "Toaster",
            },
            "Zebu-IO": {
                "Server": "Zebu IO",
            },
            "TBO": {
                "Server": "TBO",
            },
            "CIWebServer": {
                "Server": "CIWebServer",
            },
            "AspectWorks": {
                "Server": "AspectWorks",
                "Set-Cookie": "aspectworks",
                "Location": "aspectworks",
            },
            "ETWS": {
                "Server": "ETWS",
            },
            "NJ": {
                "Server": "NJ",
            },
            "billogram.com": {
                "Server": "billogram.com",
            },
            "IMC-Web-Server": {
                "Server": "IMC Web Server",
            },
            "The-Job-Auction": {
                "Server": "The-Job-Auction",
            },
            "ngp": {
                "Server": "ngp",
            },
            "RealMedia": {
                "Server": "RealMedia",
                "RealChallenge1": "",
            },
            "Helix-Mobile-Server": {
                "Server": "Helix Mobile Server",
            },
            "AKL-MDR-A1": {
                "Server": "AKL-MDR-A1",
            },
            "EZBill": {
                "Server": "EZBill",
            },
            "ServiceNow": {
                "Server": "ServiceNow",
            },
            "theonering": {
                "Server": "theonering",
            },
            "cutelyst": {
                "Server": "cutelyst",
                "X-Cutelyst": "",
            },
            "tws": {
                "Server": "tws",
            },
            "Powered-by-steam": {
                "Server": "Powered by steam",
            },
            "nope": {
                "Server": "nope",
            },
            "Nope": {
                "Server": "Nope",
            },
            "INVESTREE": {
                "Server": "INVESTREE",
            },
            "phodal": {
                "Server": "phodal",
            },
            "Ufficiostile": {
                "Server": "Ufficiostile",
            },
            "TVSquared": {
                "Server": "TVSquared",
            },
            "VG-WEB.21": {
                "Server": "VG-WEB.21",
            },
            "vssc": {
                "Server": "vssc",
            },
            "!!! TMB !!!": {
                "Server": "!!! TMB !!!",
                "X-Powered-By": "!!! TMB !!!",
            },
            "gzidc": {
                "Server": "gzidc",
            },
            "GZIDC": {
                "Server": "GZIDC",
            },
            "awh": {
                "Server": "awh",
            },
            "Namviet": {
                "Server": "Namviet",
            },
            "Interactor": {
                "Server": "Interactor",
            },
            "SoftFluent-SSB": {
                "Server": "SoftFluent-SSB",
            },
            "Happstack": {
                "Server": "Happstack",
            },
            "Vico-Group": {
                "Server": "Vico Group",
            },
            "Your_New_Server_Name": {
                "Server": "Your_New_Server_Name",
            },
            "EasternKun": {
                "Server": "EasternKun",
            },
            "smsticket.cz": {
                "Server": "smsticket.cz",
            },
            "doc88": {
                "Server": "doc88",
            },
            "enercity": {
                "Server": "enercity",
                "X-POWERED-BY": "enercity",
            },
            "sina-webserver": {
                "Server": "WeiBo",
            },
            "Sina-webserver": {
                "Server": "Sina",
                "SINA-LB": "",
                "SINA-TS": "",
            },
            "edge-esnssl": {
                "Server": "edge-esnssl",
            },
        }
