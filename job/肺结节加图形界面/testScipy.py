# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 11:11:28 2019

@author: Administrator
"""
from skimage.segmentation import clear_border
from skimage import io,data,filters,feature,color,measure
import matplotlib.pyplot as plt
img=data.camera()
edges1=filters.sobel(img)
edges2=filters.roberts(img)
edges3=filters.scharr(img)
edges4=filters.prewitt(img)
edges5=feature.canny(img);

#plt.imshow(edges,plt.cm.gray)
#plt.imshow(edges2,plt.cm.gray)


#io.imshow(img)
#io.imsave('H:/Python/workspace/camera.jpg',img)
#print(type(img))  #显示类型
#print(img.shape)  #显示尺寸
#print(img.shape[0])  #图片高度
#print(img.shape[1])  #图片宽度
#print(img.shape[2])  #图片通道数
#print(img.size)   #显示总像素个数
#print(img.max())  #最大像素值
#print(img.min())  #最小像素值
#print(img.mean()) #像素平均值
#print(img[0][0])#图像的像素值
#图像像素访问与裁剪
#彩色图像：img[i,j,c] c表示通道数；
#灰度图：gray[i,j]
#rgb2gray将彩色通道图片转换为灰度图，范围在[0,1]
#直方图与均衡化
