import pandas as pd
import os

def dup(source,des):
    if not os.path.exists(os.path.join(root,'去重')):
        os.makedirs(os.path.join(root,'去重'))
    else:
        print('去重目录已经存在,请移动重命名或删除该文件夹,防止误删')
    db=pd.read_csv(source,encoding='utf-8-sig')
    print(db)
    dup=db.drop_duplicates(subset=['title'],keep='first')
    print(dup)
    dup.to_csv(des,index=False,encoding='utf-8-sig')


def do(path='.'):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if '.csv' in filename:
                source=os.path.join(root,filename)
                des=os.path.join(root,'去重',filename)
                dup(source,des)
            else:
                print('跳过',filename)
                continue


if __name__=='__main__':
    do()