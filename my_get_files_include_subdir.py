# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/8/28 0028 下午 4:57
# Tool ：PyCharm

import os
import  re

def get_files(path,*ext,debug=False):
    all_files=[]
    all_dirs=[]
    ext=[str.lower(x) for x in ext]
    for basedir,subdirs,files in os.walk(path,topdown=0):
        if len(files)==0:
            continue
        all_dirs.append(basedir)
        for file in files:
            if debug:print(r'当前目录为:  {}，文件为:  {}'.format(basedir,file))
            all_files.append(os.path.join(basedir, file))

    if len(ext)==0:
        print('无类型筛选,返回所有文件')
        return all_files

    if len(ext)>0 and 'dir' not in ext:
        print('返回{}类型的文件'.format(ext))
        result=[x for x in all_files if str.lower(re.split(r'\.',x)[-1]) in ext]
        return result

    if len(ext)>0 and 'dir' in ext:
        print('目录和文件,请分开筛选,本次只返回目录')
        return all_dirs



if __name__ == '__main__':
    print(get_files(r'e:/','jpg',debug=True))