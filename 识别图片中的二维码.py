# -*- coding: utf-8 -*-


import os
from pyzbar.pyzbar import decode
import cv2


"""
图片包含二维码检测
"""
def qrcode_recongnize(file):
    """
    :param filepath: 图片路径
    :param filename: 图片名字
    :return: qrcode 图片包含二维码，unqrcode 图片不包含二维码
    """
    image_type = []
    try:
        # 读取图片
        image = cv2.imread(file)
        # 灰度化
        image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        # 解码二维码
        result = decode(image)

        if len(result)>0:
            print(dir(result[0]))
            rect=result[0].rect
            print(dir(rect))
            print(type(rect))

            image_type.append('qrcode')
            img=cv2.selectROI(image, rect)
            cv2.imshow('11',img)
            cv2.waitKey(0)


        else:
            image_type.append('unqrcode')
    except Exception as e:
        print(e)
        image_type.append('unqrcode')
    return image_type



if __name__ == '__main__':



    file='d://1.png'
    kk=qrcode_recongnize(file)
    print(file,kk)
