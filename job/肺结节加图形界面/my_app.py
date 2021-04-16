# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/3/30 0030 下午 3:23
# Tool ：PyCharm
import sys
from ui import Ui_Form
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import re,os,cv2
import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor

class App(QWidget,Ui_Form):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("原始模型")
        self.setWindowIcon(QIcon('ico.ico'))
        self.toOutput(content='程序初始化中...')
        self.input_view.setAcceptDrops(True)
        self.workfile=''

        self.font=QFont()
        self.font.setPixelSize(100)

        self.toOutput(content='初始化完成，请打开或直接拖入图像...')

        # self.palette_ok=QPalette()
        # self.palette_ok.setColor(QPalette.Base,Qt.green)
        # self.palette_ok.setColor(QPalette.Text, Qt.green)
        # self.palette_ok.setColor(QPalette.Highlight,Qt.green)
        # self.palette_ok.setColor(QPalette.HighlightedText,Qt.green)
        #
        #
        #
        #


    @pyqtSlot()
    def on_button_clicked(self):
        a=self.v_view.size()
        self.button.setText(str(a))

    def name2Wegite(self,name):
        if name:
            return self.findChild(QWidget, name)
        else:
            print('name is empty')

    def dragEnterEvent(self, e:QDragEnterEvent):

        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        txt=e.mimeData().text()
        txt=re.sub('file:[/]+','',txt)
        abspath=os.path.abspath(txt)
        self.workfile=abspath
        self.resizeEvent(QResizeEvent)
        self.toOutput(content='检测到文件输入:{},处理'.format(abspath))

    @pyqtSlot()
    def on_openButton_clicked(self):
        file,type=QFileDialog.getOpenFileName(None,caption='打开',directory='.',filter='*.png *.jpg')
        abspath=os.path.abspath(file)
        self.workfile=abspath
        self.load_pic()
        self.toOutput(content='检测到文件输入:{},处理'.format(abspath))

    def load_pic(self):
        if os.path.isfile(self.workfile):
            try:
                img = cv2.imdecode(np.fromfile(self.workfile, dtype=np.uint8), cv2.IMREAD_COLOR)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
                img_width = img.shape[1]  # 获取图像大小
                img_height = img.shape[0]
                width = self.input_view.width()
                height = self.input_view.height()
                width_scale=width / img_width
                height_scale=height / img_height
                zoomscale = min(width_scale,height_scale )  # 图片放缩尺度
                frame = QImage(img, img_width, img_height, QImage.Format_RGB888)
                pix = QPixmap.fromImage(frame)
                self.source_pic_item = QGraphicsPixmapItem(pix)  # 创建像素图元
                self.source_pic_item.setScale(zoomscale)
                self.source_scene = QGraphicsScene()  # 创建场景
                self.source_scene.addItem(self.source_pic_item)
                self.input_view.setScene(self.source_scene)
                self.input_view.show()
            except Exception as e:
                print(e)

    def startWork(self):
        self.setNormalResult()
        time.sleep(3)
        self.setNoticeResult()

    @pyqtSlot()
    def on_doButton_clicked(self):
        try:
            print(1)
            ThreadPoolExecutor(max_workers=10,).submit(self.startWork)
        except Exception as e:
            print(e)

    def setNormalResult(self):
        print('set normal')
        self.normal_item=QGraphicsTextItem()
        self.normal_item.setPlainText('NORMAL')
        self.normal_item.setDefaultTextColor(Qt.green)
        self.normal_item.setFont(self.font)

        self.normalScene=QGraphicsScene()
        self.normalScene.addItem(self.normal_item)
        self.output_view.setScene(self.normalScene)
        self.output_view.show()

    def setNoticeResult(self):
        print('set notice')
        self.notice_item=QGraphicsTextItem()
        self.notice_item.setPlainText('NOTICE')
        self.notice_item.setDefaultTextColor(Qt.red)
        self.notice_item.setFont(self.font)

        self.noticeScene = QGraphicsScene()
        self.noticeScene.addItem(self.notice_item)
        self.output_view.setScene(self.noticeScene)
        self.output_view.show()

    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.load_pic()

    def toOutput(self,content):
        self.outPut.append('''<html><font-size:10pt">{}</font></html>'''.format(content))
        self.outPut.append('')

    def closeEvent(self, a0: QCloseEvent) -> None:
        if QMessageBox.question(self,'关闭','是否退出程序',QMessageBox.Yes|QMessageBox.No,QMessageBox.No) ==QMessageBox.Yes:
            a0.accept()
        else:
            a0.ignore()


app=QApplication(sys.argv)
window=App()
window.show()
sys.exit(app.exec_())