# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/17 0017 下午 2:52
# Tool ：PyCharm

import os

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
                print('无类型筛选,返回所有文件')
                print(result)
                return result

            if ext[0]=='''dir''':
                dirs=[]
                print('返回目录')
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
    for i in get_dirs_files_list(r'G:\20200819','dir'):
        days={}
        for x in get_dirs_files_list(i):
            days[int(x[-8:-1])]=[x,*get_dirs_files_list(x)]
        print(days)


