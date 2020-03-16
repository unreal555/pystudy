s=''':authority: you.ctrip.com
:method: POST
:path: /destinationsite/TTDSecond/SharedView/AsynCommentView
:scheme: https
accept: */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
content-length: 119
content-type: application/x-www-form-urlencoded'''

strs=s\
    .split('\n')
# print(s)
# print(strs)
result={}
for i in strs:
    key,value=i.split(': ')
    # print(key,value)
    result[key]=str(value)

# print(result)

print('{')
for i in result:
    print('\'{}\':\'{}\','.format(i,result[i]))
print('}')