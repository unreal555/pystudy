# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/8/28 0028 下午 4:57
# Tool ：PyCharm

import os
import  re

def get_files(path,*ext,debug=False):
    all=[]
    ext=[str.lower(x) for x in ext]
    for basedir,subdirs,files in os.walk(path,topdown=0):
        if len(files)==0:
            continue
        for file in files:
            if debug:print(r'当前目录为:  {}，文件为:  {}'.format(basedir,file))
            all.append(os.path.join(basedir, file))

    if len(ext)==0:
        print('返回所有文件')
        return all

    if len(ext)>0:
        result=[x for x in all if str.lower(re.split(r'\.',x)[-1]) in ext]
        return result

if __name__ == '__main__':
    print(get_files(r'e:/','Jpg','zip',debug=True))