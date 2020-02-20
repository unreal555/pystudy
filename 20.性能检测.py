#!/bin/py3
#   -*-coding:utf-8-*-

import os,re,time,json
redcolor="\033[1;31;40m"
greencolor="\033[1;32;40m"
normalcolor="\033[0m"
##字段名称
info_name=["rtime","load1","load5","load15","us","sy","ni","id","wa","hi","si","st","Men_total"
    ,"Men_free","Men_used","Men_cache","Swap_total","Swap_free","Swap_used",
           "Swap_avail","top5"]
top5_name=["PID","USER","PR","NI","VIRT","RES","SHR","%CPU","%MEN","TIME","COMMAND"]
##提取load信息的正则
regload="top.*?(\d+:\d+:\d+).*average:.*?(\d+.\d+).*(\d+.\d+).*(\d+.\d+)"
regcpu="(\d+.\d+).*?us.*?(\d+.\d+).*?sy.*?(\d+.\d+).*?ni.*?(\d+.\d+).*?id.*?(\d+.\d+).*?wa.*?(\d+.\d+).*?hi.*?(\d+.\d+).*?si.*?(\d+.\d+).*?st"
regMen="K.*?(\d+).*?,.*?(\d+).*?,.*?(\d+).*?,.*?(\d+).*?buff/cache"
regSwap="K.*?(\d+).*?,.*?(\d+).*?,.*?(\d+).*?(\d+).*?avail.*?"
regTop5=".*?(\d+)\s+(\w+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\w+)\s+(\d+.\d+)" \
        "\s+(\d+.\d+)\s+(\d+:\d+.\d+)\s+(.*)"
##监控历史记录
his={}
##记录多少条记录
count=1000
##每隔多久记录一次,秒
delay=10
##调试开关,0关闭,1打开
debug=1
##输出的日志文件名
filename="log"+time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
##每多少条记录写入磁盘一次
writecount=20


while count>0:
    result=result1=""
    now=time.time()
    info=os.popen('top -b -n 1|head -n 12')
    i=0
    for line in info:
        if i <7:
            result+=line
            i+=1
            continue
        result1+=line

    if debug:print(redcolor,result,normalcolor)

    if debug:print(greencolor,result1,normalcolor)

    if debug:print(redcolor,re.findall(regload,result),re.findall(regcpu,result),re.findall(regMen,result),
                   re.findall(regSwap, result),normalcolor)

    if debug:print(greencolor,re.findall(regTop5,result1))

    info=list(re.findall(regload,result)[0])
    info+=re.findall(regcpu,result)[0]
    info+=re.findall(regMen,result)[0]
    info+=re.findall(regSwap,result)[0]
    info.append(re.findall(regTop5,result1))


    his[now]=dict(zip(info_name,info))
    time.sleep(delay)
    count-=1
    if count%writecount==0:
        with open("./{}".format(filename), "w", encoding="utf-8") as f:
            json.dump(his, f, ensure_ascii=False)




if debug:
    for i in sorted(his.keys()):
        print(his[i])


