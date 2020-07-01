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


def create_ciyun(count):
    img=plt.imread('./pic/heart.jpg')
    img=img.astype(np.uint8)

    wc = wordcloud.WordCloud(font_path='C:/Windows/Fonts/STHUPO.TTF',
                             max_words=100,
                             max_font_size=180,
                             min_font_size=5,
                             # background_color="white",
                             mask=img,
                             # color_func = random_color_func,
                             width=1180,  # 设置图片的宽度
                             height=764,  # 设置图片的高度
                             margin=2,
                             scale=10  #这个数值越大，产生的图片分辨率越高，字迹越清晰
                             )
    wc.generate_from_frequencies(count)
    plt.imshow(wc)
    plt.axis("off")
    plt.waitforbuttonpress()

def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None,
                      random_state=None):
    h = random.randint(0,100)
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
    count=get_count('rate')

    x=sorted(count.keys())
    y=[]
    for key in x:
        y.append(count[key])

    print(x)
    print(y)

    #
    #
    #
    # # 设置图形大小
    # plt.figure(figsize=(18, 10), dpi=100)
    #
    #
    # for i in range(0,len(x)):
    #     plt.bar(x[i],y[i])
    # # 绘制条形图
    # # plt.bar(range(len(x)), y, width=0.3)  # width表示条形粗细
    # # 绘制条形图 （横向条形图）
    # # plt.barh(range(len(x)), y, height=0.3, color="orange")  # 横向条形图中height表示条形粗细
    #
    # # 设置x轴刻度
    # plt.xticks(fontproperties=my_font, rotation=45)
    # plt.yticks(fontproperties=my_font)  # barh()绘制横向条形图时，设置的是y轴刻度
    # plt.show()
    # # 保存图片
    # # plt.savefig("./movie.png")

    create_ciyun(count)