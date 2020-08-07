# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/8/7 0007 上午 9:54
# Tool ：PyCharm

import hashlib

def get_md5(info):
    if isinstance(info,str):
        m = hashlib.md5(info.encode('utf-8')).hexdigest()
        print(m)
        return m
    if isinstance(info,bytes):
        m = hashlib.md5(info).hexdigest()
        print(m)
        return m
    return False

if __name__ == '__main__':
    with open('./pic/2.jpg','rb') as f:
        file=f.read()
    get_md5(file)
