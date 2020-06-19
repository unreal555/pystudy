1  # coding: utf-8
2  # Team : None
3  # Author：zl
4  # Date ：2020/6/18 0018 下午 4:56
5  # Tool ：PyCharm

import cv2
import numpy as  np
img=cv2.imread(r'D:/3.jpg',1) #读取图片
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #将图片变为灰度图片
cv2.imshow('1',gray)
cv2.waitKey(0)
kernel=np.ones((2,2),np.uint8) #进行腐蚀膨胀操作

temp=cv2.erode(gray,kernel,iterations=10) #膨胀
cv2.imshow('1',temp)
cv2.waitKey(0)
temp=cv2.dilate(temp,kernel,iterations=10) #腐蚀
cv2.imshow('1',temp)
cv2.waitKey(0)

ret, thresh = cv2.threshold(temp, 120, 255, cv2.THRESH_BINARY) # 阈值处理 二值法
thresh1 = cv2.GaussianBlur(thresh,(3,3),0)# 高斯滤波


temp=cv2.erode(thresh1,kernel,iterations=12) #膨胀
cv2.imshow('1',temp)
cv2.waitKey(0)



ret, thresh = cv2.threshold(temp, 150, 255, cv2.THRESH_BINARY) # 阈值处理 二值法
thresh1 = cv2.GaussianBlur(thresh,(3,3),0)# 高斯滤波
cv2.imshow("1",thresh1)
cv2.waitKey(0)
contours,hirearchy=cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)# 找出连通域
#对连通域面积进行比较
area=[] #建立空数组，放连通域面积
contours1=[]   #建立空数组，放减去最小面积的数
for i in contours:
      # area.append(cv2.contourArea(i))
      # print(area)
     if cv2.contourArea(i)>1:  # 计算面积 去除面积小的 连通域
        contours1.append(i)
print(len(contours1)-1) #计算连通域个数
draw=cv2.drawContours(img,contours1,-1,(0,255,0),1) #描绘连通域
#求连通域重心 以及 在重心坐标点描绘数字
for i,j in zip(contours1,range(len(contours1))):
    M = cv2.moments(i)
    cX=int(M["m10"]/M["m00"])
    cY=int(M["m01"]/M["m00"])
    draw1=cv2.putText(draw, str(j), (cX, cY), 1,1, (255, 0, 0), 1) #在中心坐标点上描绘数字
#展示图片
cv2.imshow("1",draw1)
cv2.waitKey(0)


