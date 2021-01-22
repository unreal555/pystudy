import requests
from lxml import etree
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import configparser
from time import  sleep
conf = configparser.ConfigParser()
conf.read(r'config.ini', encoding="utf-8-sig")

Link_code = conf.get('mysql_info', 'Link_code')
Link_code_title=conf.get('mysql_info', 'Link_code_title')
Link_code_content=conf.get('mysql_info', 'Link_code_content')

url=Link_code+Link_code_title+Link_code_content.replace(' ','')

print(Link_code+Link_code_title+Link_code_content.replace(' ',''))

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

def submit_verify(driver):
    Link_code = conf.get('mysql_info', 'Link_code')
    Link_code_title = conf.get('mysql_info', 'Link_code_title')
    Link_code_content = conf.get('mysql_info', 'Link_code_content')
    url = Link_code + Link_code_title + Link_code_content.replace(' ', '')
    driver.get(url)
    select=driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[6]/div/div/span')
    sleep(2)
    select.click()

submit_verify(driver)