import json
import requests
from functools import partial


import tkinter as tk
from tkinter import *



def main():
    root = tk.Tk()
    root.geometry('200x300')

    frame=tk.Frame(root, bd=0, relief="sunken")

    workers={1:{'name':'张三','checked':''},2:{'name':'李四','checked':''},3:{'name':'王五','checked':''}}

    
    def checked_button_click():
        for id in workers:
            if workers[id]['checked'].get()==1:
                print(id,workers[id]['name'],'is checked')
            else:
                print(id,workers[id]['name'],'is not checked')
        print('\n')


    for id in workers:

        name=workers[id]['name']        
        
        v = IntVar()

        Checkbutton(master=root, variable=v, text=name, height=2, width=10, anchor=W).pack()

        v.set(1)

        workers[id]['checked']=v

    Button(master=root, text="选好了",command=checked_button_click).pack()


    mainloop()
if __name__ == '__main__':
    main()
