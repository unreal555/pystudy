# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/9/27 0027 下午 2:02
# Tool ：PyCharm

import os
import zipfile
import re
import shutil

def clean_dir(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


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

def my_zip(path,*files,pwd=''):
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

def zipDir(dirpath,outFullName):
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



def do(dir='.'):

    for file in os.listdir(dir):
        abs_work_path=os.path.abspath(dir)
        print(abs_work_path)
        temp_path=os.path.join(abs_work_path,'temp')
        print(temp_path)

        if not os.path.exists(temp_path):
            os.makedirs(temp_path)

        filename, ext = os.path.splitext(file)

        if str.lower(ext) in ['.xlsx']:

            my_un_zip(os.path.join(abs_work_path,file),extract_to=temp_path)

            with open('{}/docProps/core.xml'.format(temp_path),'r',encoding='utf-8') as f:
                xml=f.read()

            temp=re.sub(r'(<dc:creator>).*?(</dc:creator>)',r'\1Administrator\2',xml)
            temp=re.sub(r'(<cp.lastModifiedBy>).*?(</cp.lastModifiedBy>)',r'\1Administrator\2',temp)


            with open('{}/docProps/core.xml'.format(temp_path),'w',encoding='utf-8') as f:

                f.write(temp)

            os.rename(os.path.join(abs_work_path,file),os.path.join(abs_work_path,file)+'.bak')

            zipDir(temp_path,os.path.join(abs_work_path,file))

            clean_dir(temp_path)

            print('处理完成')

