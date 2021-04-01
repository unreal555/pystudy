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
    

def get_files(path):
    files=[]
    for i in os.listdir(path):
        if str.lower(i)=='md5.txt':
            continue
        file=os.path.join(path,i)
        if os.path.isfile(file) and os.access(file,os.R_OK):
            files.append(i)
    return files


def check_dir_md5(path):
    keyFile=os.path.join(path,'md5.txt')
    print(keyFile)
    if not os.path.exists(keyFile):
        print('没有校验值文件 ，退出')
        return False

    file_md5={}

    print('读取md5.txt')

    with open(keyFile, 'r', encoding='gbk') as f:
        while True:
            item=f.readline()
            if item in  ['\r','\n','\r\n']:
                # print('跳过空行')
                continue
            if not item:
                # print('文件结束')
                break
            # print(item)
            file,md5=item.replace('\r','').replace('\n','').split('\t')
            file_md5[file]={'read':md5}


    for file in get_files(path):
        try:
            print('计算',file,'md5')
            file_md5[file]['calculate'] = get_file_md5(os.path.join(path,file))
        except:
            print(file, 'read error')
            file_md5[file]['calculate'] = 'read error'

    for file in file_md5.keys():

        if len(file_md5[file].keys())==2:
            if file_md5[file]['read']==file_md5[file]['calculate']:
                print(file,'match')
            else:
                print(file,'not match')

        if list(file_md5[file].keys()) == ['read']:
            print('目录中不存在',file)

        if list(file_md5[file].keys()) == ['calculate']:
            print('MD5.txt中不存在文件',file,'但该文件存在于目录中,MD5为',file_md5[file]['calculate'])

    for file in file_md5.keys():
        print(file,file_md5[file])


def create_dir_md5(path):
    keyFile=os.path.join(path,'md5.txt')
    print(keyFile)
    result={}
    for file in get_files(path):
        try:
            result[file] = get_file_md5(os.path.join(path,file))
            print(file,'MD5 is ' ,result[file])
        except:
            print(file, 'read error')
            result[file] = 'read error'
    with open(keyFile,'w',encoding='gbk') as f:
        for file in result:
            print('文件为:',file + '\tMD5值为：' + result[file] + '\r\n')
            f.write(file+'\t'+result[file]+'\r\n')

if __name__ == '__main__':
    # with open('d:\\福昕编辑器破解版.zip','rb') as f:
    #     file=f.read()
    # get_md5(file)
    #
    # a=get_file_md5(file='d:\\福昕编辑器破解版.zip')
    # print(a)
    

    check_dir_md5('D://')
