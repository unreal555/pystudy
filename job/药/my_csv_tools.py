# coding: utf-8
# Team : None
# Author：zl
# Date ：2020/7/1 0001 上午 9:42
# Tool ：PyCharm
import os
import csv

def write_csv(item,file_path='./result.csv',column_names=''):
    '''
    :param file_path: 文件的全路径
    :param item:    要写入的元素,字典形式,key为column_names中的字段
    :param column_names:    表头
    :return:
    '''
    if isinstance(item,list) and column_names=='':
        if not os.path.exists(file_path) or os.path.isfile(file_path):
            with open(file_path, 'a', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(item)
            print('{} 写入成功'.format(item))
            return True


    if isinstance(item,dict) and isinstance(column_names,list):
        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_path, 'a', newline='', encoding='utf-8-sig') as f:
                writer = csv.DictWriter(f, column_names)
                writer.writerow(item)
            print('{} 写入成功'.format(item))

        if not os.path.exists(file_path):
            with open(file_path,'w', newline='', encoding='utf-8-sig') as f:
                # 若文件不存在,则创建文件,写入表头和数据,
                #标头在这里传入，作为第一行数据
                writer = csv.DictWriter(f, column_names)
                writer.writeheader()
                writer.writerow(item)
                f.flush()
        print('{} 写入成功'.format(item))
        return True


if __name__=='__main__':



    a=['a','b','c','d']
    write_csv(a)