import snownlp
import jieba

juzi=u'司机视觉错乱看错红绿灯 午夜撞车致对方车头撞烂'

s=snownlp.SnowNLP(juzi)

print(s.words)
print(s.sentiments)

s=jieba.cut(juzi)

for i in s:

    print(i)

# for num in range(10,100000):
#     for j in range(2,num):
#         if num%j==0:
#             print(num,"因数",num//j,j)
#             continue
#     else:
#         print(num,"szs")
