#!/bin/py
#   -*-coding:utf-8-*-
'       说明               '
_author_ = 'zl'

#!/bin/py
#   -*-coding:utf-8-*-

from tkinter import *
from tkinter.filedialog import askdirectory
import os, time, shutil, re, tkinter.messagebox, PIL.Image

reg_date = r"[1-2]{1}[0-9]{3}:[0-1]{1}[0-9]{1}:[0-3]{1}[0-9]{1}"
reg_time = r" (\d{2}:\d{2}:\d{2})"

RED="\033[1;31;40m"
GREEN="\033[1;32;40m"
NOEMAL="\033[0m"
root = Tk()
root.title("整理照片")
#不使用StringVar,选择的结果不会在图形界面上回显
ent_source_dir = StringVar()
#必须先定义窗口,才能定义StringVar
ent_target_dir = StringVar()
log = os.path.join(".", "移动日志" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".txt")
source_file_list=[]
target_file_dict={}
sourcedir=''
targetdir=''


def checkinput():
    if ent_source_dir.get() == '':
        tkinter.messagebox.showinfo("源目录错误", "请输入要整理的目录")
        return -1,-1

    source = os.path.normpath(ent_source_dir.get())
    if (not os.path.exists(source)) and (not os.path.isdir(source)):
        tkinter.messagebox.showinfo("源目录错误", "{}不是目录,或者目录不存在,请重新输入".format(source))
        return -1,-1

    if ent_target_dir.get() == '':
        tkinter.messagebox.showinfo("目标目录错误", "请输入移动到那个目录,建议不要保存在源目录下")
        return -1,-1

    target = os.path.normpath(ent_target_dir.get())
    if (not os.path.exists(target)) and (not os.path.isdir(target)):
        tkinter.messagebox.showinfo("目标目录错误", "{}不是目录,或者目录不存在,请重新输入".format(source))
        return -1,-1

    if source == target:
        tkinter.messagebox.showinfo("目标目录错误", "源目录和目的目录相同,请更换目的目录")
        return -1,-1

    # print("检查结果",SourceDir,TargetDir)
    return source, target


# noinspection PyProtectedMember
def get_pic_ctime(path):

    print("get_pic_ctime", path)
    cdate=ctime = []
    info = {}
    try:
        im = PIL.Image.open(path, "r")
        info = im._getexif()
        print("info", info)
    except:
        print("read wrong")
        pass

#如果不存在exif信息,则返回文件的创建时间
    if info == {} or info == None:
        return time.strftime("%Y:%m:%d %H:%M:%S", time.localtime(float(os.path.getctime(path))))
#存在有0X9003项但值为空的情况，下面处理这种情况
    if 0X9003 in info.keys():  #0X9003是照片拍摄时间
        cdate = re.findall(reg_date,info[0X9003])
        ctime=re.findall(reg_time,info[0X9003])
        if cdate and ctime:
            return cdate[0]+" "+ctime[0]
        if cdate:
            return cdate[0]+" "+"00:00:00"
        if ctime:
            return "1980:01:01" + " " +ctime[0]

    if 0X9004 in info.keys():  #0X9003是照片存入时间
        cdate = re.findall(reg_date,info[0X9004])
        ctime=re.findall(reg_time,info[0X9004])
        if cdate and ctime:
            return cdate[0]+" "+ctime[0]
        if cdate:
            return cdate[0]+" "+"00:00:00"
        if ctime:
            return "1980:01:01" + " " +ctime[0]

    if 0X132 in info.keys():  #0X132是修改时间
        cdate = re.findall(reg_date,info[0X132])
        ctime=re.findall(reg_time,info[0X132])
        if cdate and ctime:
            return cdate[0]+" "+ctime[0]
        if cdate:
            return cdate[0]+" "+"00:00:00"
        if ctime:
            return "1980:01:01" + " " +ctime[0]
#如果存在exif信息,但exif中的时间信息不存在,返回照片的创建时间
    if ctime==[] and cdate==[]:
        return time.strftime("%Y:%m:%d %H:%M:%S", time.localtime(float(os.path.getctime(path))))


def change_name(name,list):
    print(RED,"开始重命名",NORMAL)
    rem = re.search(r"\(\d+\).jpg", name)
    if  not rem == None:
        name = name[:0 - len(rem.group())] + "(" + str(int((re.findall("\d+", rem.group()))[0]) + 1) + ")" + ".jpg"
    else:
        name = name[:-4] + "{}".format("(1)") + ".jpg"

    print(GREEN,name,NORMAL)

    if name in (i[1] for i in list):

        return (change_name(name,list))

    else:
        return name


def create_source_file_list(sourcedir,targetdir):
    workpath=''
    try:
        for name in os.listdir(sourcedir):

            # 拼接成当年目标的完整路径
            workpath = os.path.join(sourcedir, name)
            print("workpath", workpath)
            #判断当前目标是不是存储结果的目录,避免重复递归该目录
            if workpath == targetdir:
                print("当前目录{}是结果目录,跳过".format(sourcedir))
                continue
            #判断当前目标是文件夹还是子目录,如果是目录,递归调用函数
            if os.path.isdir(workpath):
                print(workpath, "是文件夹")
                create_source_file_list(workpath, targetdir)
            #不是目录,读取文件信息,根据文件时间放入相应的目标目录
            else:
                source_file_list.append(workpath)
    except:
        pass
            
def create_target_file_dict(source_file_list): 
    for sourcefile in source_file_list:
        sourcefilepath,sourcefilename=os.path.split(sourcefile)
        sourcebasename, extension = os.path.splitext(sourcefilename)  #将读取到的name分解成文件名和扩展名
        print("源文件",sourcefile, "源文件目录", sourcefilepath, "源文件名", sourcebasename, "源文件扩展名", extension)
        if extension.lower() == '.jpg' or extension.lower() == ".jpeg":
            #调用函数获得照片的时间信息
            tempCtime = get_pic_ctime(sourcefile)
            print(tempCtime)
            cdate, ctime = (tempCtime.replace(":", "-")).split(" ")
            cmonth = cdate[:-3]
            print(cmonth)
            target_path = os.path.join(targetdir, cmonth)
            target_name = os.path.join(cdate + "." + ctime + ".jpg")

            if target_path not in target_file_dict.keys():
                target_file_dict[target_path]=[]

            if target_name not in (i[1] for i in target_file_dict[target_path]):
                target_file_dict[target_path].append([sourcefile,target_name])
            else:
                target_file_dict[target_path].append([sourcefile,change_name(target_name,target_file_dict[target_path])])
    source_file_list.clear()

def move():
    c=0
    for target_path in target_file_dict.keys():
        if not os.path.exists(target_path):
            print("目标文件夹不存在")
            os.mkdir(target_path)
        for source,target_name in target_file_dict[target_path]:
            print(source, "------>", target_path+target_name)
            shutil.move(source, os.path.join(target_path,target_name))

            c += 1
            with open(log, "a", encoding="utf-8") as f:
                f.write("NO.{}\t".format(c)+source + "->" + os.path.join(target_path,target_name) + "\r\n")
    target_file_dict.clear()

    tkinter.messagebox.showinfo("任务完成","{}个图片复制完成，请检查".format(c))



def main():
    global sourcedir,targetdir
    sourcedir,targetdir = checkinput()
    print(sourcedir,targetdir)

    if sourcedir==-1 or targetdir==-1:
        return
        

    create_source_file_list(sourcedir,targetdir)
    create_target_file_dict(source_file_list)
    move()




def select_ent_source_dir():
    ent_source_dir_ = askdirectory()
    ent_source_dir.set(ent_source_dir_)


def select_ent_target_dir():
    ent_target_dir_ = askdirectory()
    ent_target_dir.set(ent_target_dir_)


Label(root, text="源目录").grid(row=0, column=0)
Entry(root, textvariable=ent_source_dir).grid(row=0, column=1)
Button(root, text="选择源目录", command=select_ent_source_dir).grid(row=0, column=2)  #注意注意,command后的函数不能加括号,否则直接执行

Label(root, text="目标目录").grid(row=1, column=0)
Entry(root, textvariable=ent_target_dir).grid(row=1, column=1)
Button(root, text="选择目标目录", command=select_ent_target_dir).grid(row=1, column=2)  #注意注意,command后的函数不能加括号,否则直接执行

Button(root, text="开始", command=main).grid(row=3, column=2)  #注意注意,command后的函数不能加括号,否则直接执行

root.mainloop()
