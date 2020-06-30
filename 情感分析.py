from snownlp import SnowNLP
import pandas as pd
import os

path='d:/dir'


def dup(source,des):
    if not os.path.exists(os.path.join(root,'去重')):
        os.makedirs(os.path.join(root,'去重'))
    db=pd.read_csv(source,encoding='utf-8')
    print(db)
    dup=db.drop_duplicates(subset=['title'],keep='first')
    print(dup)
    dup.to_csv(des,index=False,encoding='gb18030')



for root, dirnames, filenames in os.walk(path):
    for filename in filenames:
        source=os.path.join(root,filename)
        des=os.path.join(root,'去重',filename)
        dup(source,des)


#
#
# for index,row in dup.iterrows():
#     text=row['title']
#     s=SnowNLP(text).sentiments
#     row['senti']=s.sentiments


