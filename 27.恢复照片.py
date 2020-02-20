import re,os,shutil
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename
debug=0
move_dict={}
source_dir=()
root=Tk()
logfile=StringVar()
def select_logfile():
    _logfile=askopenfilename()
    logfile.set(_logfile)
    for item in _logfile.readlines():
        if len(item)<2:
            continue
    No, target, source =item.split("\t")[0],*item.split("\t")[1].split("->")
    # print(No,"目标",target,"源头",source)
    No=No[3:]
    source=source[:-1]
    target_path, target_name=os.path.split(target)
    source_path, source_name=os.path.split(source)
    log.insert(1.0,No+source_path+source_name+target_path+target_name+"\n")
    log.update()
    if debug:print(No,source_path,source_name,target_path, target_name)
area1=Frame(root)
area2=Frame(root)
Label(area1, text="选择日志").grid(row=0, column=0)
Entry(area1, textvariable=logfile).grid(row=0, column=1)
Button(area1, text="选择日志文件",command=select_logfile).grid(row=0, column=2)

log=ScrolledText(area2)
log.grid(row=0,column=0)
area1.pack()
area2.pack()





    # for No in  file_dict.keys():
    #     shutil.move(file_dict[No][1],file_dict[No][0])
    #     print(No+"完毕")
root.mainloop()