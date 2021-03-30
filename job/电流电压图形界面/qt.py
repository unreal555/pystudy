# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/3/30 0030 上午 9:14
# Tool ：PyCharm

import sys
import os
import pandas as pd
from PyQt5.QtWidgets import  QGraphicsItem,QGraphicsProxyWidget,QLabel,QGridLayout,QVBoxLayout,QGraphicsView,QApplication,QWidget,QMainWindow,QGraphicsScene
from PyQt5.QtGui import QBitmap,QImage,QPixmap
from ui import Ui_Form
import matplotlib.pyplot  as plt



temp_path=os.path.join(os.getenv('temp'),'p.jpg')
print(temp_path)
data = pd.read_excel('./接触电阻数据.xlsx')
print(data)
shijian = data['时间/S']
dianya = data['电压/V']
dianliu = data['电流/A']
dianzu = data['电阻/Ω']
yali = data['压力/N']



def run():
    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_Form()
    ui.setupUi(window)

    fig, ax = plt.subplots()

    plt.plot(shijian, dianya)
    plt.xticks(shijian)
    plt.ylabel('V', rotation=0)
    plt.xlabel('S')
    plt.savefig(temp_path)
    plt.close()
    p_dianya = QPixmap(temp_path)
    s_dianya = QGraphicsScene()
    s_dianya.addPixmap(p_dianya)

    plt.plot(shijian, dianliu)
    plt.xticks(shijian)
    plt.ylabel('A', rotation=0)
    plt.xlabel('S')
    plt.savefig(temp_path)
    plt.close()
    p_dianliu = QPixmap(temp_path)
    s_dianliu = QGraphicsScene()
    s_dianliu.addPixmap(p_dianliu)

    plt.plot(shijian, dianzu)
    plt.xticks(shijian)
    plt.ylabel('Ω', rotation=0)
    plt.xlabel('S')
    plt.savefig(temp_path)
    plt.close()
    p_dianzu = QPixmap(temp_path)
    s_dianzu = QGraphicsScene()
    s_dianzu.addPixmap(p_dianzu)

    plt.plot(shijian, yali)
    plt.xticks(shijian)
    plt.ylabel('N', rotation=0)
    plt.xlabel('S')
    plt.savefig(temp_path)
    plt.close()
    p_yali = QPixmap(temp_path)
    s_yali = QGraphicsScene()
    s_yali.addPixmap(p_yali)

    ui.v_view.setScene(s_dianya)
    ui.a_view.setScene(s_dianliu)
    ui.z_view.setScene(s_dianzu)
    ui.n_view.setScene(s_yali)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()



              
