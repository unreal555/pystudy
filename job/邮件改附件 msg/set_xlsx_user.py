# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/4/6 0006 上午 10:10
# Tool ：PyCharm

import os
from openpyxl  import load_workbook
import shutil


def do(file):
    tmp,ext=os.path.splitext(file)
    if str.lower(ext) in ['.xlsx']:

        print(file)
        xlsx = load_workbook(file)
        print(xlsx.properties.creator,xlsx.properties.lastModifiedBy)

        if xlsx.properties.creator in ['openpyxl','']:
            xlsx.properties.creator=''
        else:
            xlsx.properties.creator = 'Administrator'

        if xlsx.properties.lastModifiedBy=='':
            xlsx.properties.lastModifiedBy = ''
        else:
            xlsx.properties.lastModifiedBy='Administrator'

        print(xlsx.properties.creator, xlsx.properties.lastModifiedBy)
        xlsx.save(file)
        xlsx.close()

