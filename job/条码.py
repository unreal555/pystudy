# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/31 0031 下午 1:25
# Tool ：PyCharm

import pandas as pd
import my_make_barcode_tools as barcode
from docx  import Document
from docx.shared import Cm

data=pd.read_excel('./单号.xls')
doc=Document()
for row in data.iterrows():
    info=row[1]['发票号']
    num=int(row[1]['箱数'])
    path=barcode.make_barcode(info,dir='./barcode')

    for i in range(0,num):
        inline_shape = doc.add_picture(path) # 插入图片，并获取形状对象
        inline_shape.height = Cm(2.5)  # 设置图片高度为4cm
        inline_shape.width = Cm(5)  # 设置图片宽度为4cm



    doc.save('result.docx')

    break
