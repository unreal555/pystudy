import pandas as pd
import calendar
# pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com pakegename
a=pd.read_csv('./weather.csv','r',skip_blank_lines=True,header=None,delimiter=',',
              names=['date','zuigao','zuidi','tianqi','fengxiang','fengli','zhishu','dengji','des'])

b=a['date'].str.split('-',1,expand=True)
c=pd.concat([b[0],b[1],a['zhishu']],axis=1,names=['a','b','c'])
for i in c.index:
    print(c.iloc[i]['zhishu'])

for i in c.groupby(0):
    print(i)