# coding: utf-8
# Team : None
# Author：zl
# Date ：2020/6/30 0030 上午 9:02
# Tool ：PyCharm
import sys
import os
import time
import win32api
import win32con
import pickle

def check_ban_quan(hour=24,debug=False):   #思路，在sys.path目录下创建空文件，设置隐藏，只读属性，程序启动检查这三个文件的创建时间，任何
                                # 一个存在，且创建时间超过n小时的，返回真值,参数为允许运行的小时数,默认为24小时
                                 #返回为真，表示未到期，返回false，表示已到期

    if debug:print('程序期限为%s小时'%hour)
    qixian=hour*60*60

    def get_path():
        paths=[]
        for path in sys.path:
            if os.path.isdir(path):
                paths.append(os.path.join(path,'info'))
        if debug:print(paths)
        return paths

    def set_file(paths):
        for path in paths:
            if os.path.exists(path):
                pass
            else:
                try:
                    s=dict(youxiaoqi=qixian,creattime=time.time())
                    if debug:print(s)
                    with open(path,'wb') as f:
                        pickle.dump(s,f)
                    win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_HIDDEN)
                    win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_READONLY)
                except Exception as e:
                    if debug:print(e)

    def check(paths):    #检测文件是不是存在，存在返回创建和运行的时间差，不存在返回0
        for path in paths:

            # print(path)
            if os.path.exists(path):
                # try:
                    with open(path,'rb') as f:
                        s=pickle.load(f)
                        if debug:print(s)
                        youxiaoqi=s['youxiaoqi']
                        lasts=time.time()-s['creattime']       #day:86400    hour:3600
                        if debug: print('有效期',youxiaoqi)
                        if debug:print('已经运行时间',lasts)
                        if debug:print('程序已运行{:.2f}小时,还有{:.2f}小时到期'.format(lasts/60/60,youxiaoqi/60/60-lasts/60/60))
                        return youxiaoqi ,lasts
                #     break
                # except Exception as e:
                #     print(e)
                #     pass
            return False

    paths=get_path()

    result=check(paths)

    if result==False:
        set_file(paths)
        return '已设置有效期'

    youxiaoqi,lasts=result

    if float(lasts)>float(youxiaoqi):
        print('到期,程序退出')
        return False
    else:
        print('程序加载中')
        return True




if __name__=='__main__':
    # print(check_ban_quan(0.09))
    check_ban_quan(10)
