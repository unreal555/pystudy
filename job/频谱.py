# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/31 0031 下午 1:25
# Tool ：PyCharm

import numpy as np
import matplotlib.pyplot as plt


def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range




tmp=np.loadtxt('600.csv',dtype=np.str,delimiter=',')
data=tmp[0:].astype(np.float)


x=data[100000:,0]
y=data[100000:,1]

#
#print(np.max(y))
#print(np.min(y))
#y=np.where(y>0.00001,y,0)
#print(np.max(y))
#print(np.min(y))




yf=np.fft.fft(y)
shift_yf= np.fft.fftshift(yf)
log_yf=np.log(1 + np.abs(yf))

#print(y)
#print(yf)



plt.plot(x,log_yf)

plt.show()

