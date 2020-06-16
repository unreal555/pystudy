# -*- coding: utf-8 -*-

from pyzbar.pyzbar import decode
import cv2
import pic_exchange
import os
temp_dir_path=os.getenv('temp')
print(temp_dir_path)
import mytools

"""
图片包含二维码检测
"""
def qrcode_detected(path):

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
                clip=image[top:top+height,left:left+width]

                # cv2.imshow('qrcode',clip)
                # cv2.waitKey(0)
                qr_path=temp_dir_path+mytools.get_random_str(8)+'.png'
                cv2.imwrite(qr_path,clip)
                str=pic_exchange.pic_to_base64(qr_path)
                print(info,str)
                os.remove(qr_path)

                qr[s]=[info,str]

            print(qr)

        else:
            print('1未检测出二维码')
            return 0
    except Exception as e:
        print(e)
        print('2未检测出二维码')
        return 0







    return qr



if __name__ == '__main__':
    path = 'd:/1.png'

    qrcode_detected(path)
    


