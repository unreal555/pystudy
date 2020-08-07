# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/31 0031 下午 1:25
# Tool ：PyCharm

import pandas as pd
from openpyxl import Workbook
from openpyxl.drawing.image import Image as xlsImage
import os
from PIL import Image, ImageDraw, ImageFont
import qrcode


'''
根据conent生成二维码,保存在save_path路径
'''
def make_qrcode(content, save_path=None):  #content似乎长度限制为2321

    length=len(content.encode())       #判断信息长度   
    
    if isinstance(content,str):        #判断信息是否为字符串,是的话根据字符串长度决定二维码版本
        version=length//58+1
        print('字符串长度为{},version设置为{}'.format(length,version))


    dir,filename=os.path.split(save_path)       #拆分储存文件的目录和文件名
    
    if not os.path.exists(dir):    #如果目录不存在,创建目录
        os.makedirs(dir)


    qr_code_maker = qrcode.QRCode(version=version,                    #调用qrcode包,1-40取值,版本代表容纳信息的多少,
                                  error_correction=qrcode.constants.ERROR_CORRECT_M,
                                  box_size=8,
                                  border=4,
                                  )
    qr_code_maker.add_data(data=content)#在二维码中写入信息
    qr_code_maker.make(fit=True)
    img = qr_code_maker.make_image(fill_color="black", back_color="white").convert('RGBA')# 如果要生成白底黑码的二维码必须要在这里以RGB的方式指定颜色。

    
    if save_path:  #储存二维码到save_path
        img.save(save_path)


'''
写入附加信息
'''
def image_add_text(img_path, text,  text_color=(0, 0, 0), text_size=20):     
    img = Image.open(img_path)   #打开图像文件
    w,h=img.size   #读取图像的宽,高
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式 这里的SimHei.ttf需要有这个字体
    fontStyle = ImageFont.truetype("./simhei.ttf", text_size, encoding="utf-8")
    # 绘制文本

    #竖排写入四个字符
    draw.text((1, 0.35*h),'发', text_color, font=fontStyle,align='center')
    draw.text((1, 0.45*h), '票', text_color, font=fontStyle,align='center')
    draw.text((1, 0.55*h), '号', text_color, font=fontStyle,align='center')
    draw.text((1, 0.65*h), '：', text_color, font=fontStyle,align='center')


    #根据二维码图片宽度,均匀将text传递来的字符写入二维码图片
    liubai=20
    for i in range(0,len(text)):
        x=(w-liubai*2)/len(text)*i+liubai
        y=h-text_size
        draw.text((x,y ), text[i], text_color, font=fontStyle,align='center')

    img.save(img_path)




w=input('输入图片宽度,单位毫米:')
h=input('输入图片高度,单位毫米:')
s=input('输入行间距,单位毫米:')
o=input('输入空白列宽度,单位毫米:')


#读取execl表数据到data
data=pd.read_excel('./单号.xls')

#创建execl对象
wb = Workbook()
#激活sheet1
sheet = wb.active
#分别写入表AC列的宽度
sheet.column_dimensions['A'].width = float(o)/7.9
sheet.column_dimensions['C'].width = float(o)/7.9


#用于生成需要写入二维码图片的单元格位置b1,d1  b2,d3 依次类推
def get_cell():

    for a,b in [[x,y] for y in range(1,1000) for x in ['B','D']]:
        
        yield a,b
        
#创建单元格位置生成器
cell=get_cell()

#针对execl中的每一行开始调用函数
for row in data.iterrows():
        info=row[1]['发票号']     #读取发票号码
        num=int(row[1]['箱数']) #读取箱数
        path=os.path.join('./barcode',info+'.png')  #根据发票号,生成二维码图片保存路径
        make_qrcode(info,save_path=path)       #调用函数,生成二维码
        image_add_text(img_path=path,text=info)      #调用函数,给二维码图片添加附加信息

        for i in range(0,num):

            m,n=next(cell)                #获得单元格xy坐标
            sheet.column_dimensions[m].width = float(w)/7.9 #修改单元格列宽


            img = xlsImage(path)                   #  根据输入图片长宽参数,修改图片尺寸以适应单元格
            newsize = (float(w),float(h))
            img.width, img.height = newsize

            sheet.row_dimensions[n].height =   float(h)/1.3+float(s)   #修改单元格行高

            sheet.add_image(img, '{}{}'.format(m,n) )     #将图片插入到单元格


            wb.save('result.xlsx')   #保存execl文件





