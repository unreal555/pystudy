# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/4/1 0001 下午 3:24
# Tool ：PyCharm

import re

def calc(i):
    print(i)
    s=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]   #系数
    n2k=['1','0','X','9','8','7','6','5','4','3','2']  #余数转换
    if re.fullmatch('[0-9]{17}',i):
        i=[int(x) for x in list(i)]
    else:
        print('输入有误')
        return False
    n=sum(map(lambda x,y:x*y,i,s))%11
    last_n=n2k[n]
    return last_n

def id15to18(s):
    pass

def check_id(id):
    ''' ^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$'''
    reg18='''^[1-9]\d{5}(18|19|2\d)\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$'''
    reg15='''^[1-9]\d{5}\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{2}$'''

    if not re.fullmatch(reg18,id):
        print('身份证号码有误')
        return False
    i=id[0:17]
    key=id[17]
    if key==calc(i):
        print('match')
    else:
        print('校验码有误')


#calc('37010220080806010')
check_id('370102197901210050')
