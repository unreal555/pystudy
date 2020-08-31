# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/8/28 0028 下午 4:57
# Tool ：PyCharm

import os
import  re
import shutil

def get_files(path,*ext,debug=False,content=''):
    all_files=[]
    all_dirs=[]
    result=''
    ext=[str.lower(x) for x in ext]
    
    for basedir,subdirs,files in os.walk(path,topdown=1):
        if len(files)==0:   #空目录直接跳过
            continue

        if debug:print('正在处理目录:{}'.format(basedir))
        all_dirs.append(basedir)

        if 'dir' not in ext:
            for file in files:
                if debug:print(r'当前目录为:  {}，文件为:  {}'.format(basedir,file))
                all_files.append(os.path.join(basedir, file))
                

    if len(ext)==0:
        print('无类型筛选,返回所有文件')
        result=all_files


    if len(ext)==1 and 'dir' in ext:
        print('返回目录')
        result=all_dirs

    if len(ext)>0 and 'dir' not in ext:
        print('返回{}类型的文件'.format(ext))
        result=[x for x in all_files if str.lower(re.split(r'\.',x)[-1]) in ext]


    if len(ext)>1 and 'dir' in ext:
        print('目录和文件,请分开筛选,本次只返回目录')
        result=all_dirs



    if content=='':
        print('无筛选')
        return result

    if isinstance(content,str):
        print('有筛选，str为"{}"：'.format(content))
        
        temp=[]
        for item in result:
            if str.lower(content) in str.lower(item):
                temp.append(item)

            
        return temp

    if isinstance(content,(list,tuple)):
        print('有筛选，list为"{}"：'.format(str(content)))
        temp=[]
        for item in result:
            flag=0
            if isinstance(item,str):
                for key in content:
                    print(key,item)
                    if str.lower(key) in str.lower(item):
                        flag+=1
                    else:
                        break
                    if flag==len(content):
                        temp.append(item)

        return temp



if __name__ == '__main__':

    for i in get_files(r'e:/',content='新',debug=True):
        print(i)

        


