# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/17 0017 下午 2:52
# Tool ：PyCharm

import os

def get_dir_files(path,*ext):
    '''
    :param path: 要分析的路径
    :param ext:   扩展名,逗号分隔的str
    :return:    False 或者文件列表
    '''
    try:
        if os.path.exists(path) and os.path.isdir(path):
            result=[os.path.join(path,x) for x in os.listdir(path)]

            if len(ext)==0:
                print('无类型筛选,返回所有文件')
                for i in result:print(i)
                return result
            if len(ext)>0:
                print('返回{}类型的文件'.format(ext))

                result=[x for x in result if os.path.splitext(x)[1].split('.')[-1] in ext]
                for i in result:print(i)

        else:
            return False
    except Exception as e:
        print('发生错误{}'.format(e))

              
if __name__ == '__main__':
    get_dir_files(r'C:\Users\Administrator\Desktop','txt','xls')