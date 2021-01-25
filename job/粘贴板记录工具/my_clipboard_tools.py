# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/1/25 0025 上午 8:54
# Tool ：PyCharm

import win32con
import win32clipboard  as w

def readclip():
    str=''
    count=3
    while True :
        try:
            w.OpenClipboard()
            str =w.GetClipboardData(win32con.CF_UNICODETEXT)
            w.CloseClipboard()
            return str
        except Exception as e:
            count-=1
            if count==0:
                print('剪切板读取错误，退出',e)
                w.CloseClipboard()
                return False

def write_clip(str):
    str=str
    count = 3
    while True:
        try:
            w.OpenClipboard()
            w.SetClipboardData(win32con.CF_UNICODETEXT, str)
            w.CloseClipboard()
            return True
        except Exception as  e:
            count -= 1
            if count == 0:
                print('剪切板写入取错误，退出',e)
                w.CloseClipboard()
                return False


if __name__ == '__main__':
    print(readclip())

