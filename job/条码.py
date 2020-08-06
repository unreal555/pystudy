# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/31 0031 下午 1:25
# Tool ：PyCharm

import pandas as pd
import my_make_barcode_tools as barcode
import my_make_qrcode_tools as qrcode

from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image as xlsImage
import os

from PIL import Image, ImageDraw, ImageFont

def image_add_text(img_path, text,  text_color=(0, 0, 0), text_size=20):
    img = Image.open(img_path)
    w,h=img.size
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式 这里的SimHei.ttf需要有这个字体
    fontStyle = ImageFont.truetype("./simhei.ttf", text_size, encoding="utf-8")
    # 绘制文本
    draw.text((1, 0.3*h),'发', text_color, font=fontStyle,align='center')
    draw.text((1, 0.4*h), '票', text_color, font=fontStyle,align='center')
    draw.text((1, 0.5*h), '号', text_color, font=fontStyle,align='center')
    draw.text((1, 0.6*h), '：', text_color, font=fontStyle,align='center')
    draw.text((30, h-text_size), text, text_color, font=fontStyle,align='center')

    img.save(img_path)




w=input('输入图片宽度,单位毫米:')
h=input('输入图片高度,单位毫米:')
o=input('输入间隔行宽度,单位毫米:')
data=pd.read_excel('./单号.xls')


wb = Workbook()
sheet = wb.active
sheet.column_dimensions['b'].width = float(o)/7.9#修改列D的列宽

count=0
for row in data.iterrows():
    num=int(row[1]['箱数'])
    count=count+num

print(count)


def get_cell():
    
    for a,b in [[x,y] for y in range(1,1000) for x in ['A','C']]:
        yield a,b

cell=get_cell()
    

for row in data.iterrows():
        info=row[1]['发票号']
        num=int(row[1]['箱数'])
        path=os.path.join('./barcode',info+'.png')
        qrcode.make_qrcode(info,save_path=path)
        image_add_text(img_path=path,text=info)

        for i in range(0,num):

            m,n=next(cell)
            sheet.column_dimensions[m].width = float(w)/7.9#修改列D的列宽


            img = xlsImage(path)
            newsize = (float(w),float(h))
            img.width, img.height = newsize

            sheet.row_dimensions[n].height =   float(h)/1.35   #修改行3的行高

            sheet.add_image(img, '{}{}'.format(m,n) )


            wb.save('result.xlsx')

            if i>1:
                break

      
