# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/31 0031 上午 9:00
# Tool ：PyCharm

import os
import qrcode
from PIL import Image


def make_qrcode(content, save_path=None):  #content似乎长度限制为2321,通过len(s.encode())计算

    length=len(content.encode())

    if isinstance(content,str):
        version=length//58+1
        print('字符串长度为{},version设置为{}'.format(length,version))

    qr_code_maker = qrcode.QRCode(version=version,                    #1-40取值,代表容纳信息的多少,
                                  error_correction=qrcode.constants.ERROR_CORRECT_M,
                                  box_size=8,
                                  border=4,
                                  )
    qr_code_maker.add_data(data=content)
    qr_code_maker.make(fit=True)
    img = qr_code_maker.make_image(fill_color="black", back_color="white").convert(
        'RGBA')  # 问题就出在这个地方，如果要生成白底黑码的二维码必须要在这里以RGB的方式指定颜色。

    if save_path:
        dir,filename=os.path.split(save_path)
        if os.path.exists(dir):
            pass
        else:
            os.makedirs(dir)
        img.save(save_path)
        return save_path
    else:
        img.show()  # 中间图不显示


def make_qrcode_with_icon(content, icon_path, save_path=None):

    if not os.path.exists(icon_path):
        raise FileExistsError(icon_path)

    length=len(content.encode())

    if isinstance(content,str):
        version=length//58+1
        print('字符串长度为{},version设置为{}'.format(length,version))

    # First, generate an usual QR Code image
    qr_code_maker = qrcode.QRCode(version=version,
                                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                                  box_size=8,
                                  border=4,
                                  )
    qr_code_maker.add_data(data=content)
    qr_code_maker.make(fit=True)
    qr_code_img = qr_code_maker.make_image(
        fill_color="black", back_color="white").convert('RGBA')

    # Second, load icon image and resize it
    icon_img = Image.open(icon_path)
    code_width, code_height = qr_code_img.size
    icon_img = icon_img.resize(
        (code_width // 4, code_height // 4), Image.ANTIALIAS)

    # Last, add the icon to original QR Code
    qr_code_img.paste(icon_img, (code_width * 3 // 8, code_width * 3 // 8))

    if save_path:
        dir,filename=os.path.split(save_path)
        if os.path.exists(dir):
            pass
        else:
            os.makedirs(dir)
        qr_code_img.save(save_path)  # 保存二维码图片
        return save_path

    else:
        qr_code_img.show()  # 显示二维码图片


if __name__ == '__main__':
    content='''python两种除法区别以及向上向下取整 - 西瓜SAMA - 博客园
2020年2月8日 因为//除法只取结果的整数部分,所以Python还提供一个余数运算,可以得到两个整数相除的余数: 10 % 3 3 另外//除可以看成math库中的floor方法(向下取
python中的除法,取整和求模_咸鱼半条-thon ...
2018年7月10日 2. %求模是基于向下取整除法规则的 3. 四舍五入取整round, 向零取整int, 向下和向上取整函数math.floor, math.ceil 4. //和math.floor在CPython中的不...
CSDN技术社区百度快照
python 实现 ceiling divide 除法向上取整 (或小数向上...
2017年3月6日 要注意的是,在除法运算中,/,只要有一家家家家家家家家家家家家家家家家家家家家边有浮点数这个除法运算就是精确运算。都是整数的话在python2.7中就默认是向下取整,,所以你用math.ceil()函数向上...
CSDN技术社区百度快照
python3.6 取整除法 - 西风的博客 - 博客园的博客 关注- 0 粉丝- 1 +加关注 0 0 « 上一篇: python 取余运算 » 下一篇: python...
博客园百度快照家家家家家家111
Python中取整的几种方法小结_python_脚本之家家家家家家家家家
2017年1月6日 取整的方式则包括向下取整、四舍五入、向上取整等等。下面就来看看在Python中取整的几种方法吧。1、向下取整 向下取整直接用内建的 int() 函数即可:...
脚本之家百度快照整的几种方法小结_pytho家
2017年1月6日 取整的方式则包括向下取整、四舍五的方式6日 取整的方式6日 取整的方式。下面就来看看在Python中取整的几种方法吧。1、向下取整 向下取整直接用内建的 int() 函数即可:...
6日 取整的方式6日 取整的方式6日 取整的方6日 家家家家家家家家取整的方式6日 取整的方式6日 取整的方式6日 取整的方式6日 取整的方式6日 取整的方式6日 取整的方式6日 取整的方式取整的方式6日 取整的方式6日 取整的方式6日 取整的方式6日 取整的方式式6日 取整的方式6日 取整的方式6日 取整的方式6日 取整的方式6日 6日 取整的方式6日 取整的方式6日 取整的方式6日 取整的方式取整的方式6日 取整的方式6日 取整的方式6日 取整的方式
'''
    make_qrcode('''你好,猪头,你是不是傻''','./temp.png')