with open('d:/a/a.txt','r',encoding='utf-8') as f:
    str=f.readlines()

content=''
for  i in str:
    content=content+i

content=content.replace(' ','').replace('\r','').replace('\n','')
content=content.replace('。」','」。')
content=content.replace('。','。~!@#$')
content=content.replace('」。','。」')
content=content.split('~!@#$')

print(content)