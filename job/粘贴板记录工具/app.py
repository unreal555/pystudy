# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/1/25 0025 上午 9:31
# Tool ：PyCharm
from concurrent.futures import ThreadPoolExecutor

from my_tk_drag import drag_window
from my_clipboard_tools import readclip
import os
import time
import tkinter


def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S')

class clip_app(drag_window):

    def __init__(self,size,file='我的记录本.txt'):
        super().__init__(size)
        with open(file,'a',encoding='gbk') as f:
            f.write(get_time()+'\r\n')
        self.file=file
        self.count_label=tkinter.Label(self.root,text='fsdsdgdfgsdfgsdfg')
        self.count_label.pack(side=tkinter.RIGHT, anchor=tkinter.E, expand=tkinter.YES, fill=tkinter.BOTH)
        self.read_clip_loop()

    def read_clip_loop(self):
        def do():
            count=0
            str=''
            while self.is_closing==False:
                result=readclip()
                if result!=False and result!=str:
                    print(result)
                    count+=1
                    str=result
                    with open(self.file, 'a', encoding='gbk') as f:
                        f.write(result+'\r\n')
                time.sleep(1)
        ThreadPoolExecutor().submit(do)


app=clip_app(size=50)
app.root.mainloop()