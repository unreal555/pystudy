# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/17 0017 下午 2:52
# Tool ：PyCharm

import os
import shutil
import re

def get_dirs_files_list(path,*ext):
    '''
    :param path: 要分析的路径
    :param ext:   dir或者扩展名,逗号分隔的str
    :return:    False 或者文件列表
    '''
    path=os.path.abspath(path)
    try:
        if os.path.exists(path) and os.path.isdir(path):
            result=[os.path.join(path,x) for x in os.listdir(path)]



            if len(ext)==0:
                print('无类型筛选,返回所有文件目录')
                print(result)
                return result

            if ext[0]=='''dir''':
                dirs=[]
                print('只返回目录')
                for i in result:
                    if os.path.isdir(i):
                        dirs.append(i)
                print(dirs)
                return  dirs


            if len(ext)>0:
                print('返回{}类型的文件'.format(ext))
                result=[x for x in result if os.path.splitext(x)[1].split('.')[-1] in ext]
                print(result)
                return result

        else:
            return False
    except Exception as e:
        print('发生错误{}'.format(e))



if __name__ == '__main__':
    source=r'''X:\自动备份'''
    des=os.path.join(source,'des')

    if not os.path.exists(des):
        os.makedirs(des)

    for zhangtao in get_dirs_files_list(source,'dir'):

        if zhangtao==des:
            continue

        days={}
        for x in get_dirs_files_list(zhangtao):
            days[int(x[-8:])]=[x,*get_dirs_files_list(x,'BA_','Lst')]
        print(days)

        if len(days)==0:
            pass

        if len(days)==1:
            shutil.move(zhangtao, des)

        if len(days)>1:
            for key in sorted(days.keys(),reverse=True):

                if len(days[key])==3:
                    s=days[key][0]
                    d=os.path.join(des,re.findall(r'ZT[0-9]{3,}',days[key][0])[0])

                    if not os.path.exists(d):
                        os.makedirs(d)


                    shutil.move(s,d)
                    break





