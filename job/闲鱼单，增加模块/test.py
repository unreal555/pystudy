import requests
from lxml import etree
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import configparser
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()
options.add_argument('--dns-prefetch-disable')
# options.add_argument('--disable-gpu')  # 规避bug
# options.add_argument('--user-agent={}'.format(ua()))
# options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
# options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
driver=webdriver.Chrome(options=options)

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

    n=0
    #   设置失败重试计数
    try:
        handle=self.driver.current_window_handle
        url = (Link_code + Link_code_title + Link_code_content).replace(' ', '')
        #拼接URL

        self.driver.get(url)
        select=self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[6]/div/div/span')
        #定位提交按钮位置

        time.sleep(1)
        select.click()
        time.sleep(1)
        #点击提交按钮

        for h in self.driver.window_handles:
            if h!=handle:
                self.driver.switch_to.window(h)
                self.driver.close()
        self.driver.switch_to.window(handle)
        #清理无用页面

        return True
    except Exception as e:
        print('提交人际验证失败信息时错误，原因为{}'.format(e))
        if n<3:
            n+=1
        else:
            return False



submit_verify_failure(driver)