﻿# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/8/28 0028 下午 4:57
# Tool ：PyCharm

import os
import  re
from copy import  deepcopy
import pickle

def get_files_dirs_cache(path,debug=False):
    all_files = []
    all_dirs = []
    empty_dirs = []
    cache_file_path=os.path.join(path,'my_file_info.dat')
    print('开始扫描文件夹')

    for basedir, subdirs, files in os.walk(path, topdown=1):
        if debug: print('正在处理目录:{}'.format(basedir))

        all_dirs.append(basedir)

        if len(files) == 0 and len(subdirs) == 0:  # 不包含文件和文件夹的空目录加入空目录列表
            empty_dirs.append(basedir)

        for file in files:
            if debug: print(r'当前目录为:  {}，文件为:  {}'.format(basedir, file))
            all_files.append(os.path.join(basedir, file))
    
    with open(cache_file_path,'wb') as f:
        pickle.dump([all_files,all_dirs,empty_dirs],f)
    return all_files,all_dirs,empty_dirs

def find_empty_dirs(path='.',use_cache=True):
    cache_file_path = os.path.join(path, 'my_file_info.dat')

    if use_cache==False:
        all_files,all_dirs,empty_dirs=get_files_dirs(path)
        with open(cache_file_path,'wb') as f:
            pickle.dump([all_files,all_dirs,empty_dirs],f)

    if use_cache==True:
        if os.path.exists(cache_file_path) and os.path.isfile(cache_file_path) :
            with open(cache_file_path,'rb') as f:
                all_files,all_dirs,empty_dirs=pickle.load(f)
        if not os.path.exists(cache_file_path):
            all_files, all_dirs, empty_dirs = get_files_dirs(path)
            with open(cache_file_path, 'wb') as f:
                pickle.dump([all_files, all_dirs, empty_dirs],f)

    return empty_dirs



def get_paths(path,*ext,debug=False,filter_key='',filter_type='and',use_cache=True):

    cache_file_path=os.path.join(path,'my_file_info.dat')

    if str.lower(filter_type) not in ['and','or'] :
        print('filter_type must be 'and' or 'or'' )
        return False

    all_files=[]
    all_dirs=[]
    empty_dirs=[]
    result=''
    ext=[str.lower(x) for x in ext]


    if use_cache==False:
        all_files,all_dirs,empty_dirs=get_files_dirs(path)
        with open(cache_file_path,'wb') as f:
            pickle.dump([all_files,all_dirs,empty_dirs],f)

    if use_cache==True:
        if os.path.exists(cache_file_path) and os.path.isfile(cache_file_path) :
            with open(cache_file_path,'rb') as f:
                all_files,all_dirs,empty_dirs=pickle.load(f)
        if not os.path.exists(cache_file_path):
            all_files, all_dirs, empty_dirs = get_files_dirs_cache(path)
            with open(cache_file_path, 'wb') as f:
                pickle.dump([all_files, all_dirs, empty_dirs],f)

    print('扫描文件夹结束')

    print('开始分类筛选')


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



    if filter_key=='':
        print('无筛选')
        return result

    if isinstance(filter_key,str):
        print('有筛选，str为"{}"：'.format(filter_key))
        
        temp=[]
        for item in result:
            if str.lower(filter_key) in str.lower(item):
                temp.append(item)
        return temp

    if isinstance(filter_key,(list,tuple)) and filter_type=='and':
        print('有筛选，过滤字段为"{}",过滤类型为and：'.format(str(filter_key)))
        temp=[]
        for item in result:
            flag=0
            if isinstance(item,str):
                for key in filter_key:
                    if debug:print(key,item)
                    if str.lower(key) in str.lower(item):
                        flag+=1
                    else:
                        break
                    if flag==len(filter_key):
                        temp.append(item)
        return temp

    if isinstance(filter_key,(list,tuple)) and filter_type=='or':
        print('有筛选，过滤字段为"{}",过滤类型为or：'.format(str(filter_key)))
        temp=[]
        for item in result:
            if isinstance(item,str):
                for key in filter_key:
                    if debug:print(key,item)
                    if str.lower(key) in str.lower(item):
                        temp.append(item)
        return temp
        # return list(tuple(temp))



def get_base_dir(dirs):
    s=dirs
    t=deepcopy(dirs)
    try:
        for i in s:
            for j in s:
                
                if i in j and len(j)>len(i):
                    t.remove(j)
                else:
                    pass
    except Exception as e:
        get_base_dir(t)
    return list(set(t))

if __name__ == '__main__':



    print(get_paths('c:/','jpg',filter_key='丰',use_cache=True))
