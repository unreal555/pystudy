# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/17 0017 下午 2:52
# Tool ：PyCharm

import os
import re

def get_dirs_files_list(path,*ext,debug=False,full_path=True):
    '''
    :param path: 要分析的路径
    :param ext:   dir或者扩展名,逗号分隔的str
    :param debug:  是否输出
    :param full_path:   默认返回全路径
    :return:    False 或者文件列表
    '''
    
    path=str.lower(path)

    path=os.path.abspath(path)

  
    
    
    try:
        if os.path.exists(path) and os.path.isdir(path):

            temp=[os.path.join(path,x) for x in os.listdir(path)]



            if len(ext)==0:
                print('无类型筛选,返回所有文件')

                if full_path==True:
                    result=temp
                else:
                    result=[]
                    for i in temp:
                        result.append(re.split(r'[\\/]',i)[-1])                                                    
                if debug:print(result)                
                return result


            if ext[0]=='''dir''':
                dirs=[]
                print('返回目录')

                
                for i in temp:
                    
                    if os.path.isdir(i):
                        if full_path==True:
                            dirs.append(i)
                        else:
                            dirs.append(re.split(r'[\\/]',i)[-1])


                        
                if debug:print(dirs)
                return  dirs


            if len(ext)>0:
                print('返回{}类型的文件'.format(ext))
                s=[x for x in temp if str.lower(os.path.splitext(x)[1].split('.')[-1]) in ext]
                files=[]
                if full_path==True:
                    files=s
                else:
                    for i in s:
                        files.append(re.split(r'[\\/]',i)[-1])

                
                if debug:print(files)
                return files

        else:
            return False
    except Exception as e:
        print('发生错误{}'.format(e))



if __name__ == '__main__':
    for i in get_dirs_files_list(r'Z:\job',debug=False,full_path=False):
        print(i)
