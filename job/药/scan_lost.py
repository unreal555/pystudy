import re


with open('./log.txt',encoding='utf-8') as f:
    lines=f.readlines()

keys=[]
lost=[]
for i in lines:
    if i=='':
        continue
    else:
        temp=re.findall(r'''# # #.*?\['(\d+)'\] # # #''',i)
        if len(temp)==1:
            keys.append(int(temp[0]))
keys=sorted(keys)
print(keys)

for i in range(keys[-1],0,-1):


    if i not in keys:
        lost.append(i)



print(lost)