# -*- coding:utf-8 -*-
"""
@author: zyd
@file: search.py
@time: 2020-01-26 10:05
@desc: 
"""
import configparser
import csv
import random
import time
import os
import re
import traceback
from datetime import datetime, timedelta, date
import uuid

import netifaces
import requests
from lxml import etree
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from data_sql import MySql
from send_email import send_qq


def valid_date(timestr):
    nowTime_str = datetime.now().strftime('%Y-%m-%d')
    # mktime参数为struc_time,将日期转化为秒，
    e_time = time.mktime(time.strptime(nowTime_str, "%Y-%m-%d"))
    # print(e_time)
    try:
        s_time = time.mktime(time.strptime(timestr, '%Y-%m-%d'))
        # print(s_time)
        # 日期转化为int比较
        diff = int(s_time) - int(e_time)
        # print(diff)
        if diff >= 0:
            is_true = True
            # print('True')
            return is_true
        else:
            is_true = False
            # self.show_data.emit('测试版本已不能试用！！！')
            # print('测试版本已不能试用！！！')
            print('False')
            return is_true
    except Exception as e:
        print(e)
        return 0


class SeleniumTest(object):
    """用来测试selenium相关脚本"""

    def __init__(self, is_true, wait_time):
        self.valid_list = list()  # 有效连接列表用来判断去重
        self.no_valid_list = list()  # 有效连接列表用来判断去重
        with open('duplicate_database.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            self.data_list = [i[0].strip('\ufeff') for i in reader]
        self.__options = webdriver.ChromeOptions()
        self.__options.add_argument('--dns-prefetch-disable')
        # self.__options.add_argument('--disable-gpu')  # 规避bug
        # self.__options.add_argument('--user-agent={}'.format(ua()))
        # self.__options.add_argument('--headless')
        self.__options.add_argument('--window-size=1920,1080')
        # self.__options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        self.__options.add_argument('--no-sandbox')
        self.__options.add_argument('--disable-gpu')
        self.__options.add_argument('--disable-dev-shm-usage')
        if is_image == '否':
            self.__options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
            self.pref = {'profile.managed_default_content_settings.images': 2}
            self.__options.add_experimental_option('prefs', self.pref)
            # self.__options.add_experimental_option('excludeSwitches', ['enable-automation'])

        '''在cmd里输入chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"'''
        # __options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # d = DesiredCapabilities.CHROME
        # d['loggingPrefs'] = {'performance': 'ALL'}
        # driver = webdriver.Chrome(options=__options, desired_capabilities=d)

        # 启用本地浏览器信息
        # self.__options.add_argument(r"user-data-dir=C:\Users\dell\AppData\Local\Google\Chrome\User Data")
        # self.driver = webdriver.Chrome("chromedriver", 0, self.__options)

        # 过检测
        # self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        #     "source": """
        #            Object.defineProperty(navigator, 'webdriver', {
        #              get: () => undefined
        #            })
        #          """
        # })

        self.driver = webdriver.Chrome(chrome_options=self.__options)
        self.driver.set_page_load_timeout(int(wait_time))
        # self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20, 0.5)

    @staticmethod
    def is_end_page(content):
        """
        判断是否是最后一页
        :return:
        """
        if '下一页' in content:
            return False
        else:
            print('进入循环前等待:', date_waittime_start, '~', date_waittime_stop, '秒', time.strftime("%Y/%m/%d %H:%M:%S"))
            time.sleep(random.randint(int(date_waittime_start),int(date_waittime_stop)))
            print('循环等待已完成，继续抓取页面...', time.strftime("%Y/%m/%d %H:%M:%S"))
            return True

    @staticmethod
    def is_contain_num(data):
        regex = re.compile('\d+', re.S)
        num_list = regex.findall(data)
        if len(num_list) > 0:
            return True

        else:
            return False


    def extract_data(self, page_source, search_url):
        """从搜索结果中提取数据"""
        # print(page_source)
        # sys.exit()
        elem = etree.HTML(page_source)
        print('开始提取内容!!!!')
        captcha_div = elem.xpath('//div[@id="recaptcha"]/@data-sitekey')
        captcha_s = elem.xpath('//div[@id="recaptcha"]/@data-s')
        if len(captcha_div) > 0:
            sitekey = captcha_div[0]
            sites = captcha_s[0]
            if is_verify == '1':
                print('date验证码出现!!!', sitekey, sites)
                self.deal_captcha(search_url, sitekey, sites)
            if is_email:
                send_qq(email_user, email_pwd, to_email, "出现谷歌验证码，请即时处理", subject)
                print('-----已暂停程序并邮件提醒-----', time.strftime("%Y/%m/%d %H:%M:%S"))
                input('人机验证完毕后,单击此处>>并按回车(Enter):')
                print('继续启动程序...', time.strftime("%Y/%m/%d %H:%M:%S"))
            self.submit_verify_failure()

        # 搜索结果和广告列表
        # info_list = elem.xpath('//div[@id="rso"]/div|//div[@id="tadsb"]/div')
        info_list = elem.xpath('//div[@id="rso"]/div')
        for info in info_list:
            title = info.xpath('.//h3/span/text()')
            title = ''.join(title)
            link = info.xpath('.//h3/parent::a/@href')
            link = ''.join(link)
            domain_url = info.xpath('.//h3/following-sibling::div/cite/text()')
            domain_url = ''.join(domain_url)
            if len(title) == 0:
                title = info.xpath('.//div[@role="heading"]/span/text()')
                title = ''.join(title)
                link = info.xpath('.//div[@role="heading"]/following-sibling::div[1]/span[2]/span/text()')
                link = ''.join(link)
                domain_url = info.xpath('.//div[@role="heading"]/following-sibling::div[1]/span[2]/span/text()')
                domain_url = ''.join(domain_url).strip('https://').strip('http://')
            # 判断手动库
            if domain_url in self.data_list:
                print('已存在duplicate库里')
                continue
            # 判断有效库和无效库
            if domain_url in self.valid_list:
                # 1个域名只爬取1个有效链接
                continue
            if self.no_valid_list.count(domain_url) >= 5:
                # 5个无效链接
                continue
            print([title, link, domain_url])
            if not link:
                continue
            js_script = """window.open("%s");""" % link
            try:
                self.driver.execute_script(js_script)
                print('开始切换到最后一个窗口')
                self.driver.switch_to.window(self.driver.window_handles[-1])
            # except TimeoutException:
            except:
                print('启动停止!!!')
                print('启动停止切换到最后一个窗口')
                self.driver.switch_to.window(self.driver.window_handles[-1])
                time.sleep(1)
                self.driver.execute_script('window.stop ? window.stop() : document.execCommand("Stop");')
            # time.sleep(2)
            # print('开始切换到最后一个窗口')
            # self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(2)
            try:
                print('等待页面加载完成，并提取数据', time.strftime("%Y/%m/%d %H:%M:%S"))
                self.get_detail(self.driver.page_source, domain_url, link, title)
                self.driver.close()
                time.sleep(1)
                self.driver.switch_to.window(self.driver.window_handles[-1])
            except:
                print('开始进入异常处理', time.strftime("%Y/%m/%d %H:%M:%S"))
                time.sleep(6)
                self.get_detail(self.driver.page_source, domain_url, link, title)
                self.driver.close()
                time.sleep(1)
                self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_detail(self, detail_resp, domain_url, link, title):
        elem = etree.HTML(detail_resp)
        # 判断是否出现验证码
        captcha_div = elem.xpath('//div[@id="recaptcha"]/@data-sitekey')
        captcha_s = elem.xpath('//div[@id="recaptcha"]/@data-s')
        if len(captcha_div) > 0:
            sitekey = captcha_div[0]
            sites = captcha_s[0]
            if is_verify == '1':
                print('page验证码出现!!!', sitekey, sites)
                self.deal_captcha(link, sitekey, sites)
            if is_email:
                send_qq(email_user, email_pwd, to_email, "出现谷歌验证码，请即时处理", subject)
                print('-----已暂停程序并邮件提醒-----', time.strftime("%Y/%m/%d %H:%M:%S"))
                input('人机验证完毕后,单击此处>>并按回车(Enter):')
                print('继续启动程序...', time.strftime("%Y/%m/%d %H:%M:%S"))
            self.submit_verify_failure()

        all = []
        all_text_list = elem.xpath(
            '//div|//strong|//span|//a|//li|//p|//h1|//h2|//h3|//h4|//h5|//h6|//b|//i|//em|//small|//big|//sup|//sub|//ins|//textarea')
        for t in all_text_list:
            text = t.xpath('normalize-space(./text())')
            all_text = ''.join(text)
            regex = re.compile(r'\r| |\t|\n|\\s*', re.S)  # 先清洗内容空格等
            regex1 = re.compile(r'<.+?>|{|}|:|"', re.S)  # 替换html标签为空格
            regex2 = re.compile(r'\s+', re.S)  # 将多个空格替换成一个空格
            ss = regex.sub('', str(all_text))
            s1 = regex1.sub(' ', ss)
            clean_data = regex2.sub(' ', s1)
            if clean_data:
                all.append(clean_data)
        end_text = ' '.join(all)

        price_list = elem.xpath('(//*[contains(@*, "price")]|//*[contains(@*, "money")])//text()')
        # print('价格提取:', price_list)
        price_list1 = [i.replace('\n', '').replace('\t', '').replace('\r', '').replace('\xa0', '') for i in price_list
                       if SeleniumTest.is_contain_num(i)]
        print('价格列表:', price_list1)
        if len(price_list1) > 0:
            if not os.path.exists('valid_image'):
                os.makedirs('valid_image')
            # image_name = str(time.strftime("%Y-%m-%d %H:%M:%S-%f", time.localtime())).replace(':', '-')
            image_name = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S-%f")).replace(':', '-')
            image_path = 'valid_image\\' + image_name + '.png'
            print('valid_image:', image_path)
            self.driver.save_screenshot(image_path)
            print('valid_image保存图片成功')
            # 有效页面 存入有效链接库
            price_info_list = price_list1[:3]
            price = '|'.join(price_info_list).replace('\n', '')
            if '.' in domain_url:
                info_list = [domain_url, link, title, price, image_path, end_text]
                if not os.path.exists('valid.csv'):
                    head_list = ['域名', '链接', '标题', '金额', '截图', '所有文本']
                    with open('valid.csv', 'a+', encoding='utf-8-sig', newline='') as file:
                        writer = csv.writer(file, dialect='excel')
                        writer.writerow(head_list)
                with open('valid.csv', 'a+', encoding='utf-8-sig', newline='') as file:
                    writer = csv.writer(file, dialect='excel')
                    writer.writerow(info_list)
                print('valid:', [domain_url, link, title, price, image_path])
                self.valid_list.append(domain_url)
        else:
            if not os.path.exists('no_valid_image'):
                os.makedirs('no_valid_image')
            # image_name = str(time.strftime("%Y-%m-%d %H:%M:%S-%f", time.localtime())).replace(':', '-')
            image_name = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S-%f")).replace(':', '-')
            image_path = 'no_valid_image\\' + image_name + '.png'
            print('no_valid_image:', image_path)
            self.driver.save_screenshot(image_path)
            print('no_valid_image保存图片成功')
            info_list = [domain_url, link, title, '', image_path, end_text]
            if '.' in domain_url:
                # 无效页面 存入无效连接库
                if not os.path.exists('no_valid.csv'):
                    head_list = ['域名', '链接', '标题', '金额', '截图', '所有文本']
                    with open('no_valid.csv', 'a+', encoding='utf-8-sig', newline='') as file:
                        writer = csv.writer(file, dialect='excel')
                        writer.writerow(head_list)
                with open('no_valid.csv', 'a+', encoding='utf-8-sig', newline='') as file:
                    writer = csv.writer(file, dialect='excel')
                    writer.writerow(info_list)
                print('no_valid_list:', [domain_url, link, title, '', image_path])
                self.no_valid_list.append(link)

    def get_data(self, keyword, date_time,new_max_date):
        """请求页面"""
        for page in range(30):
            print('页面切换防人机验证延时:', page_waittime_start, '~', page_waittime_stop, '秒', time.strftime("%Y/%m/%d %H:%M:%S"))
            time.sleep(random.randint(int(page_waittime_start), int(page_waittime_stop)))
            print(page)
            search_url = "https://www.google.com/search?q={}&source=lnt&tbs=cdr:1,cd_min:{},cd_max:{}&tbm=&start={}"
            search_url = search_url.format(keyword, date_time, new_max_date, page * 10)
            try:
                self.driver.get(search_url)
            except TimeoutException:
                self.driver.execute_script('window.stop ? window.stop() : document.execCommand("Stop");')
            # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(random.uniform(4, 5))
            if SeleniumTest.is_end_page(self.driver.page_source) and '系统检测到您的计算机' not in self.driver.page_source:
                print('下一页判断')
                break
            try:
                self.extract_data(self.driver.page_source, search_url)
            except Exception as e:
                print(e)
                traceback.print_exc()
                time.sleep(random.uniform(4, 6))
                pass

    def deal_captcha(self, search_url, sitekey, sites):
        """
        处理谷歌验证码
        key：注意这里的 KEY 换成你自己的 API KEY
        method：直接赋值 userrecaptcha
        googlekey：复制的 sitekey
        pageurl：当前 URL
        json：直接赋值 1，代表返回 JSON 格式
        :return:
        """
        key = '6d82ee52fa6ea'
        verify_url = self.driver.current_url
        print('==========================开始处理验证码============================')
        captcha_api = (
            key, sitekey, verify_url, sites)
        print('captcha_api:', captcha_api)
        response = requests.get(captcha_api)
        print(response.json())
        request_id = response.json().get('request', '')
        if request_id:
            new_url = 'hmat(key, request_id)
            resp = requests.get(new_url)
            end_value = resp.json().get('request', '')
            print('end_value:', end_value)
            # if end_value == 'CAPCHA_NOT_READY':
            for i in range(int(count)):
                # captcha_api = '}'.format(
                #     key, sitekey, verify_url, sites)
                # print('captcha_api:', captcha_api)
                # response = requests.get(captcha_api)
                # print(response.json())
                # request_id = response.json().get('request', '')
                # if request_id:
                #     new_url = 'https://2captcha.com/res.php?key={}&action=get&id={}&json=1'.format(key, request_id)
                resp = requests.get(new_url)
                end_value = resp.json().get('request', '')
                print('end_value2:', end_value)
                if end_value != 'CAPCHA_NOT_READY':
                    break
                    # time.sleep(8)
            de_js = """document.getElementById("g-recaptcha-response").style='width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px;'"""  # document.getElementById("g-recaptcha-response").style.display ='block';
            self.driver.execute_script(de_js)
            time.sleep(random.uniform(1, 2))
            js_code = 'document.getElementById("g-recaptcha-response").innerHTML="";'.format(end_value)
            self.driver.execute_script(js_code)
            time.sleep(random.uniform(1, 2))
            submit_js = """document.querySelector("#captcha-form").submit()"""
            self.driver.execute_script(submit_js)
            print('验证完毕!!!')
        else:
            print("没有获取到requestsId!!!")

    def submit_verify_failure(self):
        '''
        出现人机验证时向网站提交信息
        '''

        conf = configparser.ConfigParser()
        conf.read(r'config.ini', encoding="utf-8-sig")
        #    读取配置文件

        Link_code = conf.get('mysql_info', 'Link_code')
        Link_code_title = conf.get('mysql_info', 'Link_code_title')
        Link_code_content = conf.get('mysql_info', 'Link_code_content')
        #    读取配置中的三个LINK参数

        n = 0
        #   设置失败重试计数
        try:
            url = (Link_code + Link_code_title + Link_code_content).replace(' ', '')
            # 拼接URL
            self.driver.get(url)
            # 提交URL
            select = self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[6]/div/div/span')
            # 定位提交按钮位置
            time.sleep(1)
            select.click()
            # 点击提交按钮
            return True
        except Exception as e:
            print('提交人际验证失败信息时错误，原因为{}'.format(e))
            if n < 3:
                n += 1
            else:
                return False


def get_mac_address():
    node = uuid.getnode()
    mac = uuid.UUID(int=node).hex[-12:]
    return mac

if __name__ == "__main__":
    """
    https://www.google.com/search?q=cashmere&tbs=qdr:h6
    https://www.google.com/search?q=cashmere&source=lnt&tbs=cdr:1,cd_min:10/14/2020,cd_max:10/14/2020&tbm=
    """
    my = MySql()
    routingNicName = get_mac_address()
    sql_select = "select * from t_cl_goole_info WHERE info='{}'".format(routingNicName)
    result = my.select_sql(sql_select)
    print(result)
    # date_time = '10/14/2020'
    # st = SeleniumTest()
    # st.get_data()
    conf = configparser.ConfigParser()
    conf.read(r'config.ini', encoding="utf-8-sig")
    if len(result) > 0:
        today = date.today()
        is_true = valid_date("2021-12-04") and valid_date(result[0][2])
        if is_true:
            # is_verify = input('是否开启自动验证1=是,0=否:')
            # is_email = input('是否发送email,空值=否,填写email=是:')
            # if is_email:
            #     email_user = input('发送的邮箱:')
            #     email_pwd = input('发送的邮箱授权码:')
            #     to_email = is_email
            # count = input('打码重复次数:')
            # is_image = input('页面是否打开图片(输入是或否):')
            # wait_time = input('页面加载等待时间:')

            # begin_time = input('输入日期(例:2020-11-06)后按回车:')
            # day_num = input('输入执行天数:')
            # key = input('输入关键词:')

            # conf = configparser.ConfigParser()
            # conf.read(r'config.ini', encoding="utf-8-sig")
            is_verify = conf.get('mysql_info', 'is_verify')
            is_email = conf.get('mysql_info', 'is_email')
            email_user = conf.get('mysql_info', 'email_user')
            email_pwd = conf.get('mysql_info', 'email_pwd')
            count = conf.get('mysql_info', 'count')
            is_image = conf.get('mysql_info', 'is_image')
            wait_time = conf.get('mysql_info', 'wait_time')
            begin_time = conf.get('mysql_info', 'begin_time')
            day_num = conf.get('mysql_info', 'day_num')
            key = conf.get('mysql_info', 'key')
            subject = conf.get('mysql_info', 'subject')
            day_section = conf.get('mysql_info', 'day_section')

            page_waittime_start = conf.get('mysql_info', 'page_waittime_start')
            page_waittime_stop = conf.get('mysql_info', 'page_waittime_stop')
            date_waittime_start = conf.get('mysql_info', 'date_waittime_start')
            date_waittime_stop = conf.get('mysql_info', 'date_waittime_stop')

            if is_email:
                to_email = is_email
            print([is_verify, is_email, email_user, email_pwd, count, is_image, wait_time, , day_num])

            st = SeleniumTest(is_true, wait_time)
            new_date = ""
            for _day in range(1, int(day_num)):
                today = datetime.strptime(begin_time, '')
                if new_date == "":
                    current_time = today + timedelta(days=+0)
                    current_date = str(current_time).split()[0]
                    date_list = current_date.split('-')
                    new_date = date_list[1] + '/' + date_list[2] + '/' + date_list[0]
                    _daymax = int(_day) * int(day_section)
                else:
                    _daymax_P = int(_daymax) + 1
                    current_time = today + timedelta(days=+_daymax_P)
                    current_date = str(current_time).split()[0]
                    date_list = current_date.split('-')
                    new_date2 = date_list[1] + '/' + date_list[2] + '/' + date_list[0]
                    new_date = new_date2
                    _daymax = int(_day) * int(day_section) + 1

                new_date2 = date_list[1] + '/' + date_list[2] + '/' + date_list[0]
                new_max_date = new_date2
                print('抓取日期:', new_date, new_max_date)  # 10/14/2020
                st.get_data(key, new_date,new_max_date)

        else:
            print('测试到期!!!')
    else:
        print('该机器不能使用')
        print('机器码:', routingNicName)
        jiqi_is_email = conf.get('mysql_info', 'jiqi_is_email')
        jiqi_email_user = conf.get('mysql_info', 'jiqi_email_user')
        jiqi_email_pwd = conf.get('mysql_info', 'jiqi_email_pwd')
        subject = conf.get('mysql_info', 'subject')
        send_qq(jiqi_email_user, jiqi_email_pwd, jiqi_is_email, routingNicName, subject)
        time.sleep(200)