# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/31 0031 下午 1:25
# Tool ：PyCharm

import pandas as pd
import my_make_barcode_tools as barcode
import my_make_qrcode_tools as qrcode

from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image
import os




w=input('输入图片宽度,单位毫米:')
h=input('输入图片高度,单位毫米:')

data=pd.read_excel('./单号.xls')


wb = Workbook()
sheet = wb.active


count=0
for row in data.iterrows():
    num=int(row[1]['箱数'])
    count=count+num

print(count)


def get_cell():
    
    for a,b in [[x,y] for y in range(1,1000) for x in ['A','B']]:
        yield a,b

cell=get_cell()
    

m='A'
n=1
for row in data.iterrows():
        info=row[1]['发票号']
        num=int(row[1]['箱数'])
        path=os.path.join('./barcode',info+'.png')
        qrcode.make_qrcode(info,save_path=path)

        for i in range(0,num):

            m,n=next(cell)
            sheet.column_dimensions[m].width = float(w)/7.9#修改列D的列宽
            
                 
            img = Image(path)
            newsize = (float(w),float(h))
            img.width, img.height = newsize
                
            sheet.row_dimensions[n].height =   float(h)/1.38   #修改行3的行高

            sheet.add_image(img, '{}{}'.format(m,n) )
            
           
            wb.save('result.xlsx')


            
      
