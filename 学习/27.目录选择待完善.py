#!/usr/bin/env python
# !encoding:utf-8
# !filename:test_filedialog.py
import tkinter.filedialog as filedialog
import os
from tkinter import *



class UI():

    path = ''

    def callback(self):
        self.entry.delete(0, END)  # 清空entry里面的内容
        self.listbox_filename.delete(0, END)
        # 调用filedialog模块的askdirectory()函数去打开文件夹
        if self.path=='':
            path = filedialog.askdirectory()
            self.entry.insert(0, path)  # 将选择好的路径加入到entry里面
            print(path)
            self.getdir(path)
        else:
            self.entry.insert(0, self.path)  # 将选择好的路径加入到entry里面
            print(self.path)
            self.getdir(self.path)


    def getdir(self,path):
        """
        用于获取目录下的文件列表
        """
        print("dangqian",path)
        cf = os.listdir(path)
        for i in cf:
            self.listbox_filename.insert(END, i)

    def select_target(self):
        name=""
        self.listbox_filename.getvar(name)
        print(name)


    def __init__(self):
        if __name__ == "__main__":

            self.root = Tk()
            self.root.title("测试版本")
            self.root.geometry("400x400")
            self.root.rowconfigure(1, weight=1)
            self.root.rowconfigure(2, weight=30)

            self.entry = Entry(self.root, width=60)
            self.entry.grid(sticky=W + N, row=0, column=0, columnspan=4, padx=5, pady=5)

            self.button = Button(self.root, text="选择文件夹", command=self.callback)
            self.button.grid(sticky=W + N, row=1, column=0, padx=5, pady=5)
            # 创建loistbox用来显示所有文件名
            self.listbox_filename = Listbox(self.root,selectmode=BROWSE,width=60)
            self.listbox_filename.grid(row=2, column=0, columnspan=4, rowspan=4,
                                  padx=5, pady=5, sticky=W + E + S + N)
            scb=Scrollbar(self.root)
            scb.grid(row=2, column=3, columnspan=4, rowspan=4,
                                  padx=5, pady=5, sticky=W + E + S + N)

            self.listbox_filename['yscrollcommand'] = scb.set
            scb['command']=self.listbox_filename.yview

            def listbox_click(event):
                print("path", self.path)
                select=os.path.join(self.path,os.path.join(self.listbox_filename.get(self.listbox_filename.curselection())))
                print("select",select)

                print(os.path.isdir(select))
                if os.path.isdir(select):
                    self.path=select
                    self.callback()

            self.listbox_filename.bind('<<ListboxSelect>>',listbox_click)

            self.root.mainloop()

a=UI()
