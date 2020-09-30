# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/9/27 0027 下午 2:02
# Tool ：PyCharm

import os
import zipfile



def my_zip(path, to='.', pwd=''):
    try:

        r = zipfile.is_zipfile(path)
        if r:
            fz = zipfile.ZipFile(path, 'r')
            for file in fz.namelist():
                fz.extract(file, to)
        else:
            print('This is not zip')
            return False

        return True

    except Exception as e:
        print(e)
        return False


my_zip('d:/chrome-win32.zip')

