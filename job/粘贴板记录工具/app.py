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
import base64
from my_img import little_png



def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S')

class clip_app(drag_window):

    def __init__(self,size,file='我的记录本.txt'):
        super().__init__(size)

        self.text_back_png = os.path.join(self.temp_dir, 'little.png')

        with open(self.text_back_png, 'wb') as f:
            f.write(base64.b64decode(little_png))

        self.little_img = tkinter.PhotoImage('little.png')
        self.file=file
        self.text_back=tkinter.PhotoImage(file=self.text_back_png)   #必须带file，否则无效
        self.read_clip_loop()

    def read_clip_loop(self):
        def do():
            count=0
            str=readclip()
            while self.is_closing==False:
                result=readclip()
                print(result)
                print(result!=False )
                print(result!=str)
                if (result!=False) and (result!=str):
                    count+=1
                    str=result
                    try:
                        with open(self.file, 'a', encoding='utf-8') as f:
                            f.write(result+'\r\n')
                    except Exception as e:
                        raise e
                    print(count, result)
                    self.info_label['image']=self.text_back
                    self.info_label['text'] = '%s' % count
                    time.sleep(1)
                else:
                    time.sleep(1)
                    continue

        ThreadPoolExecutor().submit(do)

    def __del__(self):
        super().__del__()



app=clip_app(size=50)
app.root.mainloop()