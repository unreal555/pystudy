# !/bin/py
#   coding=utf-8
#
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver;
import re
import selenium.common.exceptions as exception
import time
import win32con
import win32clipboard  as w
import random

str = '''
    // ==UserScript==
// @namespace         https://www.github.com/Cat7373/
// @name              网页限制解除
// @name:en           Remove web limits
// @name:zh           网页限制解除
// @name:zh-CN        网页限制解除
// @name:zh-TW        網頁限制解除
// @name:ja           ウェブの規制緩和
// @description       通杀大部分网站，可以解除禁止复制、剪切、选择文本、右键菜单的限制。
// @description:en    Pass to kill most of the site, you can lift the restrictions prohibited to copy, cut, select the text, right-click menu.
// @description:zh    通杀大部分网站，可以解除禁止复制、剪切、选择文本、右键菜单的限制。
// @description:zh-CN 通杀大部分网站，可以解除禁止复制、剪切、选择文本、右键菜单的限制。
// @description:zh-TW 通殺大部分網站，可以解除禁止復制、剪切、選擇文本、右鍵菜單的限制。
// @description:ja    サイトのほとんどを殺すために渡し、あなたは、コピー切り取り、テキスト、右クリックメニューを選択することは禁止の制限を解除することができます。
// @homepageURL       https://cat7373.github.io/remove-web-limits/
// @supportURL        https://github.com/Cat7373/remove-web-limits/issues/
// @author            Cat73
// @version           1.3
// @license           LGPLv3
// @compatible        chrome Chrome_46.0.2490.86 + TamperMonkey + 脚本_1.3 测试通过
// @compatible        firefox Firefox_42.0 + GreaseMonkey + 脚本_1.2.1 测试通过
// @compatible        opera Opera_33.0.1990.115 + TamperMonkey + 脚本_1.1.3 测试通过
// @compatible        safari 未测试
// @match             *://*/*
// @grant             none
// @run-at            document-start
// ==/UserScript==
(function() {
  'use strict';
  // 域名规则列表
  var rules = {
    black_rule: {
      name: "black",
      hook_eventNames: "",
      unhook_eventNames: ""
    },
    default_rule: {
      name: "default",
      hook_eventNames: "contextmenu|select|selectstart|copy|cut|dragstart",
      unhook_eventNames: "mousedown|mouseup|keydown|keyup",
      dom0: true,
      hook_addEventListener: true,
      hook_preventDefault: true,
      hook_set_returnValue: true,
      add_css: true
    }
  };
  // 域名列表
  var lists = {
    // 黑名单
    black_list: [
      /.*\.youtube\.com.*/,
      /.*\.wikipedia\.org.*/,
      /mail\.qq\.com.*/,
      /translate\.google\..*/
    ]
  };
  // 要处理的 event 列表
  var hook_eventNames, unhook_eventNames, eventNames;
  // 储存名称
  var storageName = getRandStr('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM', parseInt(Math.random() * 12 + 8));
  // 储存被 Hook 的函数
  var EventTarget_addEventListener = EventTarget.prototype.addEventListener;
  var document_addEventListener = document.addEventListener;
  var Event_preventDefault = Event.prototype.preventDefault;
  // Hook addEventListener proc
  function addEventListener(type, func, useCapture) {
    var _addEventListener = this === document ? document_addEventListener : EventTarget_addEventListener;
    if(hook_eventNames.indexOf(type) >= 0) {
      _addEventListener.apply(this, [type, returnTrue, useCapture]);
    } else if(unhook_eventNames.indexOf(type) >= 0) {
      var funcsName = storageName + type + (useCapture ? 't' : 'f');
      if(this[funcsName] === undefined) {
        this[funcsName] = [];
        _addEventListener.apply(this, [type, useCapture ? unhook_t : unhook_f, useCapture]);
      }
      this[funcsName].push(func);
    } else {
      _addEventListener.apply(this, arguments);
    }
  }
  // 清理循环
  function clearLoop() {
    var elements = getElements();
    for(var i in elements) {
      for(var j in eventNames) {
        var name = 'on' + eventNames[j];
        if(elements[i][name] !== null && elements[i][name] !== onxxx) {
          if(unhook_eventNames.indexOf(eventNames[j]) >= 0) {
            elements[i][storageName + name] = elements[i][name];
            elements[i][name] = onxxx;
          } else {
            elements[i][name] = null;
          }
        }
      }
    }
  }
  // 返回true的函数
  function returnTrue(e) {
    return true;
  }
  function unhook_t(e) {
    return unhook(e, this, storageName + e.type + 't');
  }
  function unhook_f(e) {
    return unhook(e, this, storageName + e.type + 'f');
  }
  function unhook(e, self, funcsName) {
    var list = self[funcsName];
    for(var i in list) {
      list[i](e);
    }
    e.returnValue = true;
    return true;
  }
  function onxxx(e) {
    var name = storageName + 'on' + e.type;
    this[name](e);
    e.returnValue = true;
    return true;
  }
  // 获取随机字符串
  function getRandStr(chs, len) {
    var str = '';
    while(len--) {
      str += chs[parseInt(Math.random() * chs.length)];
    }
    return str;
  }
  // 获取所有元素 包括document
  function getElements() {
    var elements = Array.prototype.slice.call(document.getElementsByTagName('*'));
    elements.push(document);
    return elements;
  }
  // 添加css
  function addStyle(css) {
    var style = document.createElement('style');
    style.innerHTML = css;
    document.head.appendChild(style);
  }
  // 获取目标域名应该使用的规则
  function getRule(url) {
    function testUrl(list, url) {
      for(var i in list) {
        if(list[i].test(url)) {
          return true;
        }
      }
      return false;
    }
    if(testUrl(lists.black_list, url)) {
      return rules.black_rule;
    }
    return rules.default_rule;
  }
  // 初始化
  function init() {
    // 获取当前域名的规则
    var url = window.location.host + window.location.pathname;
    var rule = getRule(url);
    // 设置 event 列表
    hook_eventNames = rule.hook_eventNames.split("|");
    // TODO Allowed to return value
    unhook_eventNames = rule.unhook_eventNames.split("|");
    eventNames = hook_eventNames.concat(unhook_eventNames);
    // 调用清理 DOM0 event 方法的循环
    if(rule.dom0) {
      setInterval(clearLoop, 30 * 1000);
      setTimeout(clearLoop, 2500);
      window.addEventListener('load', clearLoop, true);
      clearLoop();
    }
    // hook addEventListener
    if(rule.hook_addEventListener) {
      EventTarget.prototype.addEventListener = addEventListener;
      document.addEventListener = addEventListener;
    }
    // hook preventDefault
    if(rule.hook_preventDefault) {
      Event.prototype.preventDefault = function() {
        if(eventNames.indexOf(this.type) < 0) {
          Event_preventDefault.apply(this, arguments);
        }
      };
    }
    // Hook set returnValue
    if(rule.hook_set_returnValue) {
      Event.prototype.__defineSetter__('returnValue', function() {
        if(this.returnValue !== true && eventNames.indexOf(this.type) >= 0) {
          this.returnValue = true;
        }
      });
    }
    console.debug('url: ' + url, 'storageName：' + storageName, 'rule: ' + rule.name);
    // 添加CSS
    if(rule.add_css) {
      addStyle('html, * {-webkit-user-select:text!important; -moz-user-select:text!important;}');
    }
  }
  init();
})();
'''
log=1

def init():
    options = webdriver.ChromeOptions()
    options.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    # options.add_argument('--incognito')  # 隐身模式（无痕模式）
    options.add_argument(
        r'--load-extension=C:\kaiojmmceppobhckijngalaceghockfc\2.9.10')
    # options.add_argument(r'----user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default')
    # options.add_argument('--headless')
    Browser = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
    # Browser.minimize_window()
    Browser.set_window_size(1024,768)
    Browser.set_window_position(12000,70)
    Browser.set_page_load_timeout(30)
    Browser.set_script_timeout(30)
    random_wait()
    print(Browser)
    if Browser:
        return Browser
    else:
        print('初始化浏览器错误，程序退出')
        exit()

def set_baolihou_js(str):
    str=str
    count=3
    def do(str):
        str=str
        nonlocal count
        get_page('chrome-extension://fkhcifjengaaiefnnhaaoenbeclmeakd/options/index.html#scripts/_new')
        random_wait()
        Browser.refresh()
        random_wait()
        ActionChains(Browser).send_keys(Keys.PAGE_DOWN).perform()
        random_wait()
        write_clip(str)
        random_wait()
        ActionChains(Browser).send_keys(Keys.CONTROL + 'v').perform()
        random_wait()
        js = 'document.querySelector("body > div > div > div.edit.frame.flex.flex-col.fixed-full > div.flex.flex-wrap.edit-header.mx-1.my-1 > div.flex-auto.flex > div.edit-buttons > button:nth-child(2)").click()'
        Browser.execute_script(js)
        random_wait()
        get_page('chrome-extension://fkhcifjengaaiefnnhaaoenbeclmeakd/options/index.html#scripts/1')
        random_wait()
        get_page('chrome-extension://fkhcifjengaaiefnnhaaoenbeclmeakd/options/index.html#scripts/1')
        random_wait()
        if (Browser.page_source).find('网页限制解除')>-1:
            print('暴力猴脚本已设置')
            count=0
            get_page('chrome-extension://fkhcifjengaaiefnnhaaoenbeclmeakd/options/index.html')
            return
        else:
            count -= 1
            print('重新设置暴力猴 ，还有{}次'.format(count))
    while 1:
        if count>0:
            do(str)
            break
        else:
            print('baolihoushezhishibai,chengxutuichu')
            exit()
    return


def readclip():
    str=''
    count=3
    while True :
        try:
            w.OpenClipboard()
            str = w.GetClipboardData(win32con.CF_UNICODETEXT)
            w.CloseClipboard()
            return str
        except:
            count-=1
            if count==0:
                print('剪切板读取错误，退出')
                exit()
            print('读取剪切板错误')

def write_clip(str):
    str=str
    count = 3
    while True:
        try:
            w.OpenClipboard()
            w.SetClipboardData(win32con.CF_UNICODETEXT, str)
            w.CloseClipboard()
            return True
        except:
            count -= 1
            if count == 0:
                print('剪切板写入取错误，退出')
                exit()
            print('写入剪切板错误')

def random_wait():
    time.sleep(random.choice(range(1, 3)))

def get_clip():
    ActionChains(Browser).send_keys(Keys.CONTROL + "a").perform()
    ActionChains(Browser).send_keys(Keys.CONTROL + "a").perform()
    ActionChains(Browser).send_keys(Keys.CONTROL + "a").perform()
    ActionChains(Browser).send_keys(Keys.CONTROL + "a").perform()
    time.sleep(1)
    ActionChains(Browser).send_keys(Keys.CONTROL + 'c').perform()
    ActionChains(Browser).send_keys(Keys.CONTROL + 'c').perform()
    ActionChains(Browser).send_keys(Keys.CONTROL + 'c').perform()
    ActionChains(Browser).send_keys(Keys.CONTROL + 'c').perform()
    str=readclip()
    return str

def get_text(clip):
    global count
    count=count+1
    print(count)
    # print(clip)
    temp = re.findall('上一章下一章>(.*?)【1】', clip, re.S)
    # print(temp)
    result = re.findall('    (.*?)\n', temp[0], re.S)
    print(result)
    str=''
    for i in result:
        str+=i
    # print(str)
    return str

def get_page(url):
    global Browser
    while 1:
        try:
            Browser.get(url)
            time.sleep(5)
            break
        except:
            print(Browser)
            print('{}page open time out,retry '.format(url))
            Browser.close()
            print(Browser)
            Browser=init()
            set_baolihou_js(str)

def get_chapter_content(url):
    url = url
    all=[[],['']]
    get_page(url)
    # time.sleep(10)
    clip = get_clip()
    select=Browser.find_element_by_xpath('/html/body/div[2]/h1')
    chapter_name=select.text
    all[0]=chapter_name
    print('本章第一页下载',url,chapter_name)
    temp = re.findall('【(\d+)】', clip, re.S)
    print(temp)
    urls=[]
    for i in temp:
        urls.append('{}{}{}{}'.format(url[:-5], '_', i, '.html'))
    print(urls,urls[1:])



    while 1:
        clip = get_clip()
        all[1].append(get_text(clip))
        select = Browser.find_element_by_xpath('//*[@id="ChapterView"]/div[2]/div/a[2]')
        next_chapter_url = select.get_attribute('href')
        print('下一章url',next_chapter_url)
        if len(urls)==1:
            print('本章只有一页，下一章url',next_chapter_url)
            return all, next_chapter_url
            break
        for url in urls[1:]:
            print('本章有{}页，开始下载{}'.format(len(urls),url))
            get_page(url)
            # time.sleep(10)
            clip = get_clip()
            all[1].append(get_text(clip))
        print('check')
        select=Browser.find_element_by_xpath('//*[@id="ChapterView"]/div[2]/div/a[2]')
        next_chapter_url=select.get_attribute('href')
        print(next_chapter_url)
        content=''
        for i in all[1]:
            content=content+i
        all.pop()
        content = content.replace('”','」')
        content = content.replace('“','「')
        content = content.replace(' ', '').replace('\r', '').replace('\n', '')
        content = content.replace('。」', '」。')
        content = content.replace('。', '。~!@#$')
        content = content.replace('」。', '。」')
        content = content.split('~!@#$')
        all.append(content)
        return all,next_chapter_url

def get_start_chapter_url(url):
    get_page(url)
    time.sleep(10)
    select=Browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr/td[1]/a')
    print(select.get_attribute('href'))
    start_chapter_url=select.get_attribute('href')
    select=Browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/h1')
    novel_name=select.text
    print(novel_name)
    return novel_name,start_chapter_url
# try:



def start(url):
    book_url=url
    book=[[],[]]
    book[0],start_chapter_url=get_start_chapter_url(book_url)
    chapter_content,next_chapter_url=get_chapter_content(start_chapter_url)
    book[1].append(chapter_content)
    print(next_chapter_url[-5:])
    while next_chapter_url[-5:]=='.html':

        chapter_content,next_chapter_url=get_chapter_content(next_chapter_url)
        book[1].append(chapter_content)
        # print(book)
    print(all)
    with open('d:/a/{}.txt'.format(book[0]),'w',encoding='utf-8') as f:
        f.write(book[0])
        f.write('\n\r')
        f.write('\n\r')
        f.write('\n\r')
        for chapter in book[1]:
            f.write('\t')
            f.write(chapter[0])
            f.write('\n\r')
        f.write('\n\r')
        f.write('\n\r')
        for chapter in book[1]:
            print(chapter)
            f.write(chapter[0])
            f.write('\n\r')
            for line in chapter[1]:
                line=line.replace(chapter[0].replace(' ',''),'').replace('努力加载中','')
                f.write('    '+line+'\n\r')
            f.write('\n\r')
count=0
Browser = init()
set_baolihou_js(str)
# except:
#     print("初始化出错")
#     Browser.close()
for i in range(23,1000):
    start('http://www.skwen.me/1/{}/'.format(i))

# start('http://www.skwen.me/1/13434/')


# try:
#     'http://skwen.me/2/2107/'
#
#     get_page('chrome://settings/clearBrowserData')
#     random_wait()
#     ActionChains(Browser).send_keys(Keys.ENTER).perform()
#     time.sleep(5)
#     Browser.close()
# except:
#     get_page('chrome://settings/clearBrowserData')
#     random_wait()
#     ActionChains(Browser).send_keys(Keys.ENTER).perform()
#     time.sleep(5)
#     Browser.close()
# chrome_options.add_argument('--headless') # 无头模式
# chrome_options.add_argument('--disable-gpu') # 禁用GPU加速
# chrome_options.add_argument('--start-maximized')#浏览器最大化
# chrome_options.add_argument('--window-size=1280x1024') # 设置浏览器分辨率（窗口大小）
# chrome_options.add_argument('log-level=3')
# #info(default) = 0
# #warning = 1
# #LOG_ERROR = 2
# #LOG_FATAL = 3
#
# chrome_options.add_argument('--user-agent=""') # 设置请求头的User-Agent
# chrome_options.add_argument('--disable-infobars') # 禁用浏览器正在被自动化程序控制的提示
# chrome_options.add_argument('--incognito') # 隐身模式（无痕模式）
# chrome_options.add_argument('--hide-scrollbars') # 隐藏滚动条, 应对一些特殊页面
# chrome_options.add_argument('--disable-javascript') # 禁用javascript
# chrome_options.add_argument('--blink-settings=imagesEnabled=false') # 不加载图片, 提升速度
#
# chrome_options.add_argument('--ignore-certificate-errors') # 禁用扩展插件并实现窗口最大化
# chrome_options.add_argument('–disable-software-rasterizer')
# chrome_options.add_argument('--disable-extensions')
