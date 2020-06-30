from snownlp import SnowNLP
import pandas as pd

db=pd.read_csv(r'C:\Users\Administrator\Desktop\地王.csv',encoding='utf-8')
print(db)
dup=db.drop_duplicates(subset=['title'],keep='first')
dup['senti']=None



for index,row in dup.iterrows():
    text=row['title']
    s=SnowNLP(text).sentiments
    row['senti']=s.sentiments



print(dup)
dup.to_csv('./text.csv',index=False,encoding='gb18030')