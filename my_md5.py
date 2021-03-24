# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/3/24  上午 9:54
# Tool ：PyCharm

import hashlib
import os

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

def get_file_md5(file, block_size=64 * 1024):
    with open(file, 'rb') as f:
        md5 = hashlib.md5()
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
        retmd5 = md5.hexdigest()
        return retmd5

def get_files(path='.'):
    files=os.listdir()
    try:
        files.remove(str.lower('md5.txt'))
    except ValueError:
        print('没有md5.txt文件')
    return files

# def set_md5(path='.'):
#     files=get_files(path)
#     for file in files:
#         with open()


# def check_md5(file):


if __name__ == '__main__':
    with open('./pic/heart.jpg','rb') as f:
        file=f.read()
    get_md5(file)
    a=get_file_md5(file='./pic/heart.jpg')
    print(a)