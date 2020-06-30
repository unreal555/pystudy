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

def check_ban_quan(hour=24):   #思路，在sys.path目录下创建空文件，设置隐藏，只读属性，程序启动检查这三个文件的创建时间，任何
                                # 一个存在，且创建时间超过n小时的，返回真值,参数为允许运行的小时数,默认为24小时
                                 #返回为真，表示未到期，返回false，表示已到期
    debug=True

    if debug:print('程序期限为%s小时'%hour)
    qixian=hour*60*60

    def get_path():
        paths=[]
        for path in sys.path:
            if os.path.isdir(path):
                paths.append(os.path.join(path,'info.ini'))
        if debug:print(paths)
        return paths

    def creat_file(paths):
        for path in paths:
            if os.path.exists(path):
                pass
            else:
                try:
                    with open(path,'w',encoding='utf-8') as f:
                        f.write(str(time.time()))
                    win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_HIDDEN)
                    win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_READONLY)
                except:
                    pass

    def check(paths):    #检测文件是不是存在，存在返回创建和运行的时间差，不存在返回0
        for path in paths:

            # print(path)
            if os.path.exists(path):
                # try:
                    with open(path,'r',encoding='utf-8') as f:
                        creat_time=f.read()
                        print(creat_time)
                        creat_time=float(creat_time)
                        lasts=time.time()-creat_time#day:86400    hour:3600
                        lasts=int(lasts)
                        if debug:print('程序已运行{:.2f}小时,还有{:.2f}小时到期'.format(lasts/60/60,hour-lasts/60/60))
                        return lasts
                #     break
                # except Exception as e:
                #     print(e)
                #     pass
            return False

    paths=get_path()
    lasts=check(paths)
    if lasts==False:
        creat_file(paths)
    if abs(lasts)>qixian:
        print('到期,程序退出')
        return False
    else:
        print('程序加载中')
        return True

def clean_ban_quan():
    debug=False
    def get_path():
        paths=[]
        for path in sys.path:
            if os.path.isdir(path):
                try:
                    win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_HIDDEN)
                    win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_READONLY)
                    paths.append(os.path.join(path,'info.ini'))
                except Exception as e:
                    if debug:print(e)
        if debug:print(paths)
        return paths

    def clean(paths):
        for path in paths:
            print('REMOVE',path)
            if os.path.isfile(path):
                try:

                    win32api.SetFileAttributes(path, win32con.FILE_ATTRIBUTE_NORMAL)
                    os.remove(path)
                    print('REMOVE',path)
                except:
                    pass

    paths=get_path()
    clean(paths)


if __name__=='__main__':
    # print(check_ban_quan(0.09))
    clean_ban_quan()