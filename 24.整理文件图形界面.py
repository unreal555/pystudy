#!/bin/py
#   -*-coding:utf-8-*-

from tkinter import *
from tkinter.filedialog import askdirectory
import os, time, shutil, re, tkinter.messagebox, PIL.Image

root = Tk()
root.title("整理照片")
#不使用StringVar,选择的结果不会在图形界面上回显
SetSourceDir = StringVar()
#必须先定义窗口,才能定义StringVar
SetTargetDir = StringVar()
log = os.path.join(".", "移动日志" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".txt")


def checkinput():
    if SetSourceDir.get() == '':
        tkinter.messagebox.showinfo("源目录错误", "请输入要整理的目录")
        return None

    SourceDir = os.path.normpath(SetSourceDir.get())
    if (not os.path.exists(SourceDir)) and (not os.path.isdir(SourceDir)):
        tkinter.messagebox.showinfo("源目录错误", "{}不是目录,或者目录不存在,请重新输入".format(SourceDir))
        return None

    if SetTargetDir.get() == '':
        tkinter.messagebox.showinfo("目标目录错误", "请输入移动到那个目录,建议不要保存在源目录下")
        return None

    TargetDir = os.path.normpath(SetTargetDir.get())
    if (not os.path.exists(TargetDir)) and (not os.path.isdir(TargetDir)):
        tkinter.messagebox.showinfo("目标目录错误", "{}不是目录,或者目录不存在,请重新输入".format(SourceDir))
        return None

    if SourceDir == TargetDir:
        tkinter.messagebox.showinfo("目标目录错误", "源目录和目的目录相同,请更换目的目录")
        return None

    # print("检查结果",SourceDir,TargetDir)
    return SourceDir, TargetDir


# noinspection PyProtectedMember
def getpictime(path):
    print("getctime", path)
    ctime = ""
    info = {}
    try:
        im = PIL.Image.open(path, "r")
        info = im._getexif()
        print("info", info)
    except:
        print("read wrong")
        pass

#如果不存在exif信息,则返回文件的创建时间
    if info == {}:
        return time.strftime("%Y:%m:%d %H:%M:%S", time.localtime(float(os.path.getctime(path))))
    if 0X9003 in info.keys():  #0X9003是照片拍摄时间
        ctime = info[0X9003]
        return ctime
    if 0X9004 in info.keys():  #0X9003是照片存入时间
        ctime = info[0X9004]
        return ctime
    if 0X132 in info.keys():  #0X132是修改时间
        ctime = info[0X132]
        return ctime
    #如果存在exif信息,但exif中的时间信息不存在,返回照片的创建时间
    if ctime == "":
        return time.strftime("%Y:%m:%d %H:%M:%S", time.localtime(float(os.path.getctime(path))))


def changename(path):
    rem = re.search(r"\(\d+\).jpg", path)
    if rem != None:
        path = path[:0 - len(rem.group())] + "(" + str(int((re.findall("\d+", rem.group()))[0]) + 1) + ")" + ".jpg"
    else:
        path = path[:-4] + "{}".format("(1)") + ".jpg"

    print(path)

    if os.path.exists(path):

        return (changename(path))

    else:
        return path


def visitdir(SourceDir, TargetDir):
    WorkPath=''
    for name in os.listdir(SourceDir):

        # 拼接成当年目标的完整路径
        WorkPath = os.path.join(SourceDir, name)
        print("workpath", WorkPath)
        #判断当前目标是不是存储结果的目录,避免重复递归该目录
        if WorkPath == TargetDir:
            print("当前目录{}是结果目录,跳过".format(SourceDir))
            continue
        #判断当前目标是文件夹还是子目录,如果是目录,递归调用函数
        if os.path.isdir(WorkPath):
            print(WorkPath, "是文件夹")
            visitdir(WorkPath, TargetDir)
        #不是目录,读取文件信息,根据文件时间放入相应的目标目录
        else:
            filename, extension = os.path.splitext(name)  #将读取到的name分解成文件名和扩展名
            print("源文件", WorkPath, "源文件目录", SourceDir, "源文件名", filename, "源文件扩展名", extension)
            if extension == '.jpg' or extension == ".jpeg":
                #调用函数获得照片的时间信息
                tempCtime = getpictime(WorkPath)
                print(tempCtime)
                cdate, ctime = (tempCtime.replace(":", "-")).split(" ")
                cmonth = cdate[:-3]
                print(cmonth)
                TargetPath = os.path.join(TargetDir, cmonth)
                TargetBaseName = os.path.join(cdate + "." + ctime + ".jpg")
                TargetFullPath = os.path.join(TargetPath, TargetBaseName)

                if not os.path.exists(TargetPath):
                    print("目标文件夹不存在")
                    os.mkdir(TargetPath)

                if os.path.exists(TargetFullPath):
                    TargetFullPath = changename(TargetFullPath)

                print(WorkPath, "------>", TargetFullPath)
                shutil.move(WorkPath, TargetFullPath)
                with open(log, "a", encoding="utf-8") as f:
                    f.write(SourceDir + "\t\t\t" + TargetFullPath + "\r\n")

    print("目录\"{}\"处理完毕".format(WorkPath))



def main():
    temp = checkinput()
    print(temp)

    if temp:
        visitdir(*temp)
    else:
        return


def selectsetsourcedir():
    SetSourceDir_ = askdirectory()
    SetSourceDir.set(SetSourceDir_)


def selectTargetdir():
    SetTargetDir_ = askdirectory()
    SetTargetDir.set(SetTargetDir_)


Label(root, text="源目录").grid(row=0, column=0)
Entry(root, textvariable=SetSourceDir).grid(row=0, column=1)
Button(root, text="选择源目录", command=selectsetsourcedir).grid(row=0, column=2)  #注意注意,command后的函数不能加括号,否则直接执行

Label(root, text="目标目录").grid(row=1, column=0)
Entry(root, textvariable=SetTargetDir).grid(row=1, column=1)
Button(root, text="选择目标目录", command=selectTargetdir).grid(row=1, column=2)  #注意注意,command后的函数不能加括号,否则直接执行

Button(root, text="开始", command=main).grid(row=3, column=2)  #注意注意,command后的函数不能加括号,否则直接执行

root.mainloop()
