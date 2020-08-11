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
    elif isinstance(info,bytes):
        m = hashlib.md5(info).hexdigest()
        print(m)
        return m
    else:
        print('MD5只接受byte或str类型数据')
        return False

if __name__ == '__main__':
    with open('./pic/heart.jpg','rb') as f:
        file=f.read()
    get_md5(file)
