1  # coding: utf-8
2  # Team : None
3  # Author：zl
4  # Date ：2020/7/1 0001 上午 9:42
5  # Tool ：PyCharm
import pandas as pd
import os
import csv

def write_csv(file_path,item,column_names):
    '''
    :param file_path: 文件的全路径
    :param item:    要写入的元素,字典形式,key为column_names中的字段
    :param column_names:    表头
    :return:
    '''


    if os.path.exists(file_path):
        with open(file_path, 'a', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, column_names)
            writer.writerow(item)
            f.flush()

    else:
        with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
            # 若文件不存在,则创建文件,写入表头和数据,
            #标头在这里传入，作为第一行数据
            writer = csv.DictWriter(f, column_names)
            writer.writeheader()
            writer.writerow(item)
            f.flush()
    print('{} 写入成功'.format(item))
    return True

def csv_dup(source,des=''):

    if os.path.exists(source):
        pass
    else:
        print('源文件{}不存在'.format(source))

    if des=='':
        des=source.split('.csv')[0]+'.去重.csv'


    db=pd.read_csv(source,encoding='utf-8-sig')
    print(db)
    dup=db.drop_duplicates(subset=['title'],keep='first')
    print(dup)
    dup.to_csv(des,index=False,encoding='utf-8-sig')

def dir_csv_dup(path='.'):
    for root, dirnames, filenames in os.walk(path):
        if os.path.exists(os.path.join(root, '去重')):
            pass
        else:
            os.makedirs(os.path.join(root, '去重'))

        for filename in filenames:
            if '.csv' in filename:
                source=os.path.join(root,filename)
                des=os.path.join(root,'去重',filename)
                csv_dup(source,des)
            else:
                print('跳过',filename)
                continue

if __name__=='__main__':
    head=['a','b']
    item={}
    item['a']='sdafdsad'
    item['b']='adadf'
    write_csv('./text.csv',item=item,column_names=head)