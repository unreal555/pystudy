#!/bin/py
#   -*-coding:utf-8-*-

_author_ = 'zl'


import json,time,os,re
import matplotlib.pyplot as plt
redcolor="\033[1;31;40m"
greencolor="\033[1;32;40m"
normalcolor="\033[0m"
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['font.family']='sans-serif'

def createPic(filename):
    with open("./{}".format(filename), "r", encoding="utf-8") as f:
        print(filename, "loading")
        dic = json.load(f)
        print(filename, "loaded")
    date=[]
    load=[]
    us=[]
    sy=[]
    wa=[]
    id=[]
    recno=0
    for i in sorted(dic.keys()):
        date.append(time.strftime("%H:%M:%S",time.localtime(float(i))))
        load.append(float((dic[i]['load1'])))
        us.append(float((dic[i]['us'])))
        sy.append(float((dic[i]['sy'])))
        wa.append(float((dic[i]['wa'])))
        id.append(float((dic[i]['id'])))
        recno+=1
        if recno>1000:
            break
    size=recno//100

    fig=plt.figure(figsize=(25*size,8))
    ax1=fig.add_subplot(111)
    ax1.set_xticks(range(len(date)),date)   ##把x轴时间坐标序列化,不能直接把date队列作为参数进行绘图,顺序会被打乱
    ax1.set_xlabel("{}".format(filename),fontsize=20)
    plt.xticks(rotation =315)

    ax2=ax1.twinx()



    ax1.set_yticks(range(0,100,10))
    # ax1.set_ylim(0,100)
    ax1.set_ylabel("us,sy,wa,id value",fontsize=16)
    ax1.plot(date,us,"o-",label="us")
    ax1.plot(sy,"o-",label="sy")
    ax1.plot(wa,"o-",label="wa")
    ax1.plot(id,"o-",label="id")

    ax2.set_autoscaley_on(1)
    ax2.set_ylabel("cpu load",fontsize=16)
    ax2.plot(load,"D-",label=",load")



    ax1.legend(loc='upper left')

    ax2.legend(loc='upper right')
    plt.grid(1)
    print("日志{}已发现,开始生成曲线".format(filename))
    plt.savefig("{}.png".format(filename),bbox_inches = 'tight',transparent=True,pad_inches=0)
    print("日志{}的曲线已生成".format(filename))

count=flag=0
for  filename in  os.listdir("./"):
    if len(re.findall("(log\d+-\d+-\d+-\d+-\d+-\d+)$",filename))!=0:
        if os.path.exists("{}.png".format(filename)):
            print("日志{}的曲线已发现,跳过该日志".format(filename))
            flag+=1
            continue
        createPic(filename)
        count+=1


if count==0:
    if flag==0:
        print(redcolor,"日志文件没有找到,程序退出",normalcolor)
    else:
        print(redcolor,"{}个日志的曲线已存在,没有发现新的日志文件,程序退出".format(flag),normalcolor)
else:
    if flag==0:
        print(redcolor,"{}张曲线生成,程序退出".format(count),normalcolor)
    else:
        print(redcolor,"{}张曲线生成,{}个日志曲线已存在,程序退出".format(count,flag),normalcolor)

