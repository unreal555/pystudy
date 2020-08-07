# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/31 0031 上午 11:00
# Tool ：PyCharm

import barcode
import os
import re
[ 'code39', 'ean', 'ean13', 'ean8', 'gs1', 'gtin', 'isbn', 'isbn10', 'isbn13', 'issn', 'jan', 'pzn', 'upc', 'upca' 'code39', 'ean', 'ean13', 'ean8', 'gs1', 'gtin', 'isbn', 'isbn10', 'isbn13', 'issn', 'jan', 'pzn', 'upc', 'upca']

def qu_te_shu_zi_fu(s):
    if isinstance(s, str):
        return re.sub('[\/:*?"<>|]','-',s)
    else:
        print('老兄，给字符串')
        return False


def make_barcode(content, dir=None):

    try:

        if dir==None:
            dir=os.path.join('.')
        
        if not os.path.exists(dir):
            os.makedirs(dir)


        filename=qu_te_shu_zi_fu(content)
        path = os.path.join(dir, filename)

        length=len(content.encode())
        print('信息为{},长度为{}'.format(content,length))

        Code = barcode.get_barcode_class('code39')

        if isinstance(content,str):
            bar=Code(content,barcode.writer.ImageWriter(),add_checksum=False)

            bar.save(path,{'text_distance':2,'format':'PNG'})

        return os.path.abspath(path+'.png')

    except Exception as e:
        print(e)

if __name__ == '__main__':

    a=make_barcode('LLF200730013--14')
    print(a)



'''
#导入模块
import barcode

#获取编码类
Code = barcode.get_barcode_class('code39')        #参数为支持的格式

#获取条形码对象
bar = Code("123456")
"""
Code构造函数有3个参数：Code(code, writer=None, add_checksum=True)
code参数为编码数据，如'123445'等
writer参数默认值为None，此时默认使用barcodr.writer.SVGWriter()，生成的文件为SVG格式。如果想获得PNG、JPEG或BMP图像格式，需要将该参数设置为barcode.writer.ImageWriter()，例如：Code('123456',barcode.writer.ImageWriter(),False)
add_checksum参数默认值为True，生成的条码中会自动加上校验和，如果为False，则不加校验和
"""

#保存条形码文件
bar.save("d:\\barcode")        #此处不需要输入文件后缀
"""
save函数有两个参数：save(filename,options=None)
filename参数为保存文件名，不需要加扩展名，将根据设置自动添加扩展名，由函数返回文件全名。当前面构造函数使用默认writer时，保存为SVG文件，扩展名为.svg。
options参数默认值为None，此时使用默认参数。如果需要修改设置，使用字典传入参数，例如：save("d:\\barcode",{'text': 'ABCD','format':'JPEG'})。可用参数如下：
    'module_width'：默认值0.2，每个条码宽度（？），单位为毫米
    'module_height'：默认值15.0，条码高度，单位为毫米
    'quiet_zone'：默认值6.5，两端空白宽度，单位为毫米
    'font_size'：默认值10，文本字体大小，单位为磅
    'text_distance'：默认值5.0，文本和条码之间的距离，单位为毫米
    'background'：默认值'white'，背景色
    'foreground'：默认值'black'，前景色
    'text'：默认值''，显示文本，默认显示编码，也可以自行设定
    'write_text'：默认值True，是否显示文本，如果为True自动生成text的值，如果为False则不生成（如果此时手工设置了text的值，仍然会显示文本）。
    'center_text'：默认值True，是否居中显示文本
    'format'：默认值'PNG'，保存文件格式，默认为PNG，也可以设为JPEG、BMP等，只在使用ImageWriter时有效。
    'dpi'：默认值300，图片分辨率，，只在使用ImageWriter时有效。
'''
