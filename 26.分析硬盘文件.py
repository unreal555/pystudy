#!/bin/py
#   -*-coding:utf-8-*-
import os
import tkinter
import _thread
from tkinter.filedialog import askdirectory
from tkinter import *



root=Tk()
root.title("分析文件")
ent_dir=StringVar()
file_dict={}


def select_ent_dir():
    _ent_dir = askdirectory()
    ent_dir.set(_ent_dir)

def creat_file_dict(dir):
    try:
        for name in os.listdir(dir):
            full=os.path.join(dir,name)
            if os.path.isdir(full):
                creat_file_dict(full)
            else:
                if os.path.isfile(full):

                    basename,extension=os.path.splitext(name)
                    print(full,basename,extension)
                    if (extension not in file_dict.keys()):
                        file_dict[extension]={"count":1,"path":[]}
                        file_dict[extension]["path"].append(full)
                    else:
                        file_dict[extension]["count"]+=1
                        file_dict[extension]["path"].append(full)
    except:
        pass


    for name in file_dict:
        print (name,file_dict[name]["count"])
        for path in file_dict[name]["path"]:
            print(path)
            file_dict[name]["path"].remove(path)






def main():
    if ent_dir.get()!="":
        try:
            _thread.start_new_thread(creat_file_dict,(ent_dir.get(),))
        except:
            print("adkfaldjkadf")





Label(root, text="目录").grid(row=0, column=0)
Entry(root, textvariable=ent_dir).grid(row=0, column=1)
Button(root, text="选择源目录", command=select_ent_dir).grid(row=0, column=2)  #注意注意,command后的函数不能加括号,否则直接执行

Button(root,text="开始",command=main).grid(row=1,column=2)


root.mainloop()