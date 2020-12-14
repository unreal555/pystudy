# -*- coding: utf-8 -*-

from pyzbar.pyzbar import decode
import cv2
import my_pic_base64_exchange
import os
import numpy
import base64

'''
图片包含二维码检测
'''

def qrcode_detected(path):
    temp_dir_path = os.getenv('temp')

    try:
        # 读取图片
        image = cv2.imread(path)
        # 灰度化
        image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        # 解码二维码
        result = decode(image)
        print(result)
        qr={}
        if len(result)>0:
            for s in range(0,len(result)):
                print(s)
                i=result[s]
                rect=i.rect
                info=i.data
                top,left,height,width= rect.top,rect.left,rect.height,rect.width

                print(info, top,left,height,width)
                clip=image[top-10:top+height+10,left-10:left+width+10]

                # cv2.imshow('qrcode',clip)
                # cv2.waitKey(0)
                temp=cv2.imencode('.png',clip)[1]
                temp=numpy.array(temp)
                temp = temp.tobytes()

                str ="data:image/png;base64,"+ base64.b64encode(temp).decode()
                qr[s]=[info,str]

        else:
            print('图片中未检测出二维码')
            return False
    except Exception as e:
        print(e)
        print('异常错误，未检测出二维码')
        return False
    return qr



if __name__ == '__main__':
    path = 'd:/1.png'
    print(qrcode_detected(path))




