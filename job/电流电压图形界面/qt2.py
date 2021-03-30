# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/3/30 0030 下午 3:23
# Tool ：PyCharm
import sys,os
from ui import Ui_Form
from PyQt5.QtWidgets import QApplication,QWidget,QGraphicsScene
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
import pandas as pd

class Moniter(QWidget,Ui_Form):
    temp_path = os.path.join(os.getenv('temp'), 'p.jpg')
    print(temp_path)
    data = pd.read_excel('./接触电阻数据.xlsx')
    print(data)
    shijian = data['时间/S']
    dianya = data['电压/V']
    dianliu = data['电流/A']
    dianzu = data['电阻/Ω']
    yali = data['压力/N']
    def __init__(self):
        super(Moniter, self).__init__()
        self.setupUi(self)
        self.draw()
        self.showMaximized()



    def draw(self):
        fig, ax = plt.subplots()

        plt.plot(self.shijian, self.dianya)
        plt.xticks(self.shijian)
        plt.ylabel('V', rotation=0)
        plt.xlabel('S')
        plt.savefig(self.temp_path)
        plt.close()
        p_dianya = QPixmap(self.temp_path)
        s_dianya = QGraphicsScene()
        s_dianya.addPixmap(p_dianya)

        plt.plot(self.shijian, self.dianliu)
        plt.xticks(self.shijian)
        plt.ylabel('A', rotation=0)
        plt.xlabel('S')
        plt.savefig(self.temp_path)
        plt.close()
        p_dianliu = QPixmap(self.temp_path)
        s_dianliu = QGraphicsScene()
        s_dianliu.addPixmap(p_dianliu)

        plt.plot(self.shijian, self.dianzu)
        plt.xticks(self.shijian)
        plt.ylabel('Ω', rotation=0)
        plt.xlabel('S')
        plt.savefig(self.temp_path)
        plt.close()
        p_dianzu = QPixmap(self.temp_path)
        s_dianzu = QGraphicsScene()
        s_dianzu.addPixmap(p_dianzu)

        plt.plot(self.shijian, self.yali)
        plt.xticks(self.shijian)
        plt.ylabel('N', rotation=0)
        plt.xlabel('S')
        plt.savefig(self.temp_path)
        plt.close()
        p_yali = QPixmap(self.temp_path)
        s_yali = QGraphicsScene()
        s_yali.addPixmap(p_yali)

        self.v_view.setScene(s_dianya)
        self.a_view.setScene(s_dianliu)
        self.z_view.setScene(s_dianzu)
        self.n_view.setScene(s_yali)


app=QApplication(sys.argv)
window=Moniter()
window.show()
sys.exit(app.exec_())