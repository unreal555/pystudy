#!/bin/py
#   -*-coding:utf-8-*-
'       说明               '
#需要Goopychart,pip install gpcharts
_author_ = 'zl'
import json,time
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['font.family']='sans-serif'


filename="log2018-01-30-22-05-42"
with open("./{}".format(filename),"r",encoding="utf-8") as f:
    dic=json.load(f)
date=[]
load=[]
us=[]
sy=[]
wa=[]
id=[]
a=0
for i in sorted(dic.keys()):
    date.append(time.strftime("%H:%M:%S",time.localtime(float(i))))
    load.append(float((dic[i]['load1'])))
    us.append(float((dic[i]['us'])))
    sy.append(float((dic[i]['sy'])))
    wa.append(float((dic[i]['wa'])))
    id.append(float((dic[i]['id'])))

    a+=1
    if a>1000:
        break
size=a//100


# ymax=round(max((max(us),max(sy),max(wa))))
# print(ymax)
# yticks=list(range(0,ymax,2))
# yticks.append(yticks[-1]+2)
yticks=list(range(0,101,10))

print(yticks)

plt.figure(figsize=(25*size,8))

plt.xticks(range(len(date)),date)    ##x轴是时间时,不能直接plot(date,sy)排序,x轴会重新排序,必须这样处理.
plt.xticks(rotation =315,fontsize=8)
plt.yticks(yticks,fontsize=20)

plt.xlabel('date',fontsize=20)
plt.ylabel("value",fontsize=16)


plt.plot(load,"D-",label=",load")
plt.plot(date,us,"x-",label="us")
plt.plot(sy,"+-",label="sy")
plt.plot(wa,"o-",label="wa")
plt.plot(id,"o-",label="id")

plt.legend()

plt.savefig("a.jpg",bbox_inches = 'tight',transparent=True,pad_inches=0)