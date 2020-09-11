# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/9/11 0011 上午 11:58
# Tool ：PyCharm

import psutil

def check_process(processname):
    result=[]
    try:
        pids= psutil.pids()
        for pid in pids:
            if str.lower(processname) in str.lower(psutil.Process(pid).name()) :
                result.append((pid,psutil.Process(pid).name()))
    except Exception as e:
        print(e)
    return result



