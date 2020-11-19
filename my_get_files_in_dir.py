# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/17 0017 下午 2:52
# Tool ：PyCharm

import os
import re

def get_files(path,*ext,debug=False):

    path=str.lower(path)
    path=os.path.abspath(path)
    ext = [str.lower(x) for x in ext]
    try:
        if os.path.exists(path) and os.path.isdir(path):
            result=[os.path.join(path,x) for x in os.listdir(path)]
            files=[x for x in result if os.path.isfile(x)]
            if len(ext)==0:
                print('无类型筛选,返回所有文件')
                if debug:print(files)
                return files

            if len(ext)>0 :
                print('返回{}类型的文件'.format(ext))
                files=[x for x in files if str.lower(re.split(r'\.',x)[-1]) in ext]
                if debug:print(files)
                return files
        else:
            return False
    except Exception as e:
        print('发生错误{}'.format(e))


if __name__ == '__main__':
    print(get_files(r'c:','sys',''))

