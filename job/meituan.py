# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/29 0029 下午 4:19
# Tool ：PyCharm

import my_html_tools

url='https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=019a7b8df6d14b289618.1595383015.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fwww.meituan.com%2Fmeishi%2F163559578%2F&riskLevel=1&optimusCode=10&id=163559578&userId=&offset=90&pageSize=30&sortType=1'
              
page=my_html_tools.my_request(url)
print(page)