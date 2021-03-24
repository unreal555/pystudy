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
    files=os.listdir(path)
    try:
        files.remove(str.lower('md5.txt'))
    except ValueError:
        print('没有md5.txt文件')

    return files

def check_dir_md5(path='.'):
    keyFile=os.path.join('.','md5.txt')
    if not os.path.exists(os.path.exists(keyFile)):
        print('没有校验值文件 ，退出')
        return False

    file_md5={}

    with open(keyFile, 'r', encoding='gbk') as f:
        while True:
            item=f.readline()
            if not item:
                break
            file,md5=item
            file_md5[file]=md5

    files=get_files(path)
    for file in files:
        value=get_file_md5(file)
        for item in file_md5:
            if file in item and value in item:
                print(file,'is checked pass by ',value)

def set_dir_md5(path='.'):
    keyFile=os.path.join(path,'md5.txt')
    result={}
    for file in get_files(path):
        result[file] = get_file_md5(os.path.join(path,file))
    with open(keyFile,'w',encoding='gbk') as f:
        for file in result:
            print(keyFile,file + '\t' + result[file] + '\r')
            f.write(file+'\t\t\t\t'+result[file]+'\r')

if __name__ == '__main__':
    # with open('d:\\福昕编辑器破解版.zip','rb') as f:
    #     file=f.read()
    # get_md5(file)
    #
    # a=get_file_md5(file='d:\\福昕编辑器破解版.zip')
    # print(a)
    set_dir_md5('./pic')