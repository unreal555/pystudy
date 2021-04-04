# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/9/27 0027 下午 2:02
# Tool ：PyCharm

import os
import zipfile



def my_un_zip(path, extract_to='.', pwd=''):
    try:

        if zipfile.is_zipfile(path):
            f= zipfile.ZipFile(path, 'r')
            for file in f.namelist():
                f.extract(file, extract_to)
            return True
        else:
            print('This is not zip')
            return False

    except Exception as e:
        print(e)
        return False

def my_zip_files(path,*files,pwd=''):
    print(path,pwd,files)
    has_done=[]
    if os.path.exists(path):
        print('压缩文件{}已存在,写入此文件'.format(path))
        f=zipfile.ZipFile(path,'a')
        for i in f.filelist:
            has_done.append(i.filename)

    try:
        for file in files:
            name=os.path.split(file)[-1]
            while name in has_done:
                name=''.join([os.path.splitext(name)[0],'-重命名-',os.path.splitext(name)[1]])
            has_done.append(name)
            f.write(file,name, zipfile.ZIP_DEFLATED)
        f.close()
        return True

    except Exception as e:
        print(e)
        return False

def my_zip_dir(dirpath,outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
    for path,dirnames,filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath,'')

        for filename in filenames:
            zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
    zip.close()


my_zip('d:/test.zip','d:/图片文件差异比较.rar','d:/图片文件差异比较.rar','d:/黄猿养殖.txt',pwd='test')

