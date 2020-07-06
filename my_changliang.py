# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/2 0002 下午 4:12
# Tool ：PyCharm

import string
from zhon.hanzi import punctuation as ZHONG_WEN_BIAO_DIAN
from string import punctuation as YING_WEN_BIAO_DIAN
from string import ascii_lowercase as XIAO_XIE_ZI_MU
from string import ascii_uppercase as DA_XIE_ZI_MU
from string import digits as SHU_ZI
import random

class ChangLiang():
    ZHONG_WEN_ZI_FU_FOR_RE = r'\u4e00-\u9fa5'

    ZHONG_WEN_ZI_FU_FOR_RE = r'\u4e00-\u9fa5'

    YING_WEN_ZI_FU_FOR_RE = 'a-zA-Z0-9'

    USER_AGENT = {
        'chrome': 'chrome''Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
        # chrome
        'firefox': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        # fireFox
        'ie': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'  # IE11
    }

    Proxy = [
        {'http':'','https':''},
        {'http':'https://test:594188@58.59.25.122:1234','https':'https://test:594188@58.59.25.122:1234'},
        {'http':'http://test:594188@58.59.25.123:1234','https':'https://test:594188@58.59.25.123:1234'}
    ]



if __name__ == '__main__':

    Chang=ChangLiang()
    print(Chang.get_proxie())



