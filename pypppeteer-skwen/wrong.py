import re



file='wrong.txt'


reg='http://www.skwen.me/\d+/(\d+)/.*?.html \d+ \d+ 内容可能丢失，重试'

with open(file,'r',encoding='gbk') as f:
    txt=f.read()


result=[int(x) for x in re.findall(reg,txt)]


print(sorted(list(set(result))))
