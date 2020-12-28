import re



file='wrong.txt'


reg='http://www.skwen.me/\d+/(\d+)/.*?.html \d+ \d+ 内容可能丢失，重试'

with open(file,'r',encoding='utf-8') as f:
    txt=f.read()

result=re.findall(reg,txt)


print(set(result))
