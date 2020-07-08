# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/1 0001 下午 3:41
# Tool ：PyCharm
import wordcloud
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import random
import pickle
import numpy as np

from matplotlib import font_manager


my_font = font_manager.FontProperties(fname='C:/Windows/Fonts/STHUPO.TTF')
my_font.set_size(20)
print(dir(my_font.set_style))


def create_ciyun(count):
    img=plt.imread('./pic/tuoyuan.jpg')
    img=img.astype(np.uint8)

    wc = wordcloud.WordCloud(font_path='C:/Windows/Fonts/STHUPO.TTF',
                             max_words=150,
                             max_font_size=180,
                             min_font_size=5,
                             # background_color="white",
                             mask=img,
                             color_func = random_color_func,
                             width=1180,  # 设置图片的宽度
                             height=764,  # 设置图片的高度
                             margin=2,
                             scale=3  #这个数值越大，产生的图片分辨率越高，字迹越清晰
                             )
    wc.generate_from_frequencies(count)
    plt.imshow(wc)
    plt.axis("off")
    plt.waitforbuttonpress()

def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None,
                      random_state=None):
    h = random.randint(0,360)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random.randint(150,250)) / 255.0)
    return "hsl({}, {}%, {}%)".format(h, s, l)



def get_count(key='rate'):
    db=pd.read_csv('d:/电影.csv',encoding='utf_8_sig')
    print(db.index)
    result=[]
    for index,row in db.iterrows():
        text=str(row[key])


        if '/' in text:
            temp=row[key].split('/')
            for i in  temp:
                result.append(i)
        else:
            result.append(text)

    count=Counter(result)
    print(count)

    return count




    # dup=result.drop_duplicates(subset=['url'],keep='first').reset_index()
    #
    # # result.to_csv('./test.csv',encoding='utf-8')
    # dup.to_csv('./test1.csv',encoding='utf-8')


def drawBar(count):
    xticks = ['A', 'B', 'C', 'D', 'E']  # 每个柱的下标说明
    gradeGroup = {'A': 200, 'B': 250, 'C': 330, 'D': 400, 'E': 500}  # 用于画图的频率数据

    # 创建柱状图
    # 第一个参数为柱的横坐标
    # 第二个参数为柱的高度
    # 参数align为柱的对齐方式，以第一个参数为参考标准
    plt.bar(range(5), [gradeGroup.get(xtick, 0) for xtick in xticks], align='center', yerr=0.000001)

    # 设置柱的文字说明
    # 第一个参数为文字说明的横坐标
    # 第二个参数为文字说明的内容
    plt.xticks(range(5), xticks)

    # 设置横坐标轴的标签说明
    plt.xlabel('Grade')
    # 设置纵坐标轴的标签说明
    plt.ylabel('Frequency')
    # 设置标题
    plt.title('Grades Of Male Students')
    # 绘图
    plt.show()

if __name__=='__main__':
    count=get_count('guojia')
    count={value:key for key,value in count.items()}
    x=sorted(count.keys())
    print(x)
    y=[]
    for key in x:
        y.append(count[key])






    # 设置图形大小
    fig=plt.figure(figsize=(18, 10), dpi=100)






    for a,b in zip(y,x):
        plt.bar(a,b,bottom=0,edgecolor='k',linewidth=2)
        plt.text(a, b , '%4s' % b, ha='center', va='top', fontsize=30,rotation=90,)

    plt.plot(y,x,color="red",linewidth=6,)





    plt.xticks(fontproperties=my_font, rotation=90,)  #fontsize=30
    plt.yticks(fontproperties=my_font)  # barh()绘制横向条形图时，设置的是y轴刻度   ,fontsize=30
    # plt.title("xxxxx",fontproperties=my_font)
    # plt.ylim(0,3500)

    plt.show()
    # # 保存图片
    # # plt.savefig("./movie.png")

    # create_ciyun({value:key for key,value in count.items()})