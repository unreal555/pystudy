import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageEnhance

import cv2
import numpy as np

img = cv2.imread('d:/1.png')
cv2.imshow('11',img)
cv2.waitKey(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

result_detection = None
count_experiments = 10
transform = None
qrcode = cv2.QRCodeDetector()


result_detection, transform, straight_qrcode = qrcode.detectAndDecode(img_gray)

if result_detection:
    print('result', result_detection)

# img = Image.open(image)
#
# #img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度
#
# #img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化
#
# #img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度
#
# #img = img.convert('L')#灰度化
#
# img.show()
#
# barcodes = pyzbar.decode(img)
#
# for barcode in barcodes:
#     barcodeData = barcode.data.decode("utf-8")
#     print(barcodeData)

