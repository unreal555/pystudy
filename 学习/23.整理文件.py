#!/bin/py
#   -*-coding:utf-8-*-

from PIL import Image
import os,time,shutil,re



root="test"
root=os.path.normpath(root)
print("主目录是:",root)

log=os.path.join(root,"整理"+time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())+".txt")


if (not os.path.exists(root)) and (not os.path.isdir(root)):
    print("{}不是目录,或者目录不存在".format(root))
    exit(-1)

ResultDir=os.path.join(root,"result")

if os.path.exists(ResultDir):
    print("储存结果的目录{}已存在,跳过".format(ResultDir))
else:
    os.mkdir(ResultDir)



def getPicTime(path):
    ctime=""
    info={}
    try:
        im = Image.open(path, "r")
        info = im._getexif()
    except:
        print("文件{}读取错误".format(path))

    ##如果不存在exif信息,则返回文件的创建时间
    if info:
        return time.strftime("%Y:%m:%d %H:%M:%S", time.localtime(float(os.path.getctime(path))))
    if 0X9003 in info.keys():  ##0X9003是照片拍摄时间
        ctime = info[0X9003]
        return ctime
    if 0X9004 in info.keys():  ##0X9003是照片存入时间
        ctime = info[0X9004]
        return ctime
    if 0X132 in info.keys():  ##0X132是修改时间
        ctime = info[0X132]
        return ctime
    ##如果存在exif信息,但exif中的时间信息不存在,返回照片的创建时间
    if ctime=="":
        return time.strftime("%Y:%m:%d %H:%M:%S",time.localtime(float(os.path.getctime(path))))


def changeName(path):
    rem=re.search(r"\(\d+\).jpg", path)
    if rem!=None:
        path=path[:0-len(rem.group())]+"("+str(int((re.findall("\d+",rem.group()))[0])+1)+")"+".jpg"
    else:
        path = path[:-4] + "{}".format("(1)") + ".jpg"

    if os.path.exists(path):

        return(changeName(path))

    else:
        return path


def visitDir(path):
    for name in os.listdir(path):

        #拼接成当年目标的完整路径
        SourcePath=os.path.join(path,name)
        
        ##判断当前目标是不是存储结果的目录,避免重复递归该目录
        if SourcePath==ResultDir:
            print("当前目录{}是结果目录,跳过".format(SourcePath))
            continue
        ##判断当前目标是文件夹还是子目录,如果是目录,递归调用函数
        if os.path.isdir(SourcePath):
            print(SourcePath,"是文件夹")
            visitDir(SourcePath)
        ##不是目录,读取文件信息,根据文件时间放入相应的目标目录
        else:
            filename,extension = os.path.splitext(name)   ##将读取到的name分解成文件名和扩展名
            print("源文件",SourcePath,"源文件目录","源文件名","源文件扩展名",filename,extension)
            if extension == '.jpg' or extension==".jpeg":
                ##调用函数获得照片的时间信息
                tempCtime=getPicTime(SourcePath)
                cdate,ctime=(tempCtime.replace(":","-")).split(" ")
                cmonth=cdate[:-3]
                print (cmonth)
                DestDir=os.path.join(ResultDir, cmonth)
                DestBaseName=os.path.join(cdate+"."+ctime+"."+filename+".jpg")
                DestFullPath=os.path.join(DestDir,DestBaseName)

                if not os.path.exists(DestDir):
                    os.mkdir(DestDir)

                if os.path.exists(DestFullPath):
                    DestFullPath=changeName(DestFullPath)
                print(SourcePath,DestFullPath)
                shutil.move(SourcePath,DestFullPath)
                with open(log,"a",encoding="utf-8") as f:
                    f.write(SourcePath+"\t\t\t"+DestFullPath+"\r\n")


visitDir(root)
# print(changeName(r"D:\pycharm-professional-2017.2.4\pystudy\test\result\2018-02-07\15-42-00(1).jpg"))