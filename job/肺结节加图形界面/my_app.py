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

class App(QWidget,Ui_Form):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("原始模型")
        self.setWindowIcon(QIcon('ico.ico'))
        self.input_view.setAcceptDrops(True)
        self.workfile=''

    @pyqtSlot()
    def on_button_clicked(self):
        a=self.v_view.size()
        self.button.setText(str(a))

    def dragEnterEvent(self, e):
        print(e.mimeData().hasText())
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        txt=e.mimeData().text()
        txt=re.sub('file:[/]+','',txt)
        abspath=os.path.abspath(txt)
        print(abspath)
        self.workfile=abspath
        self.resizeEvent(QResizeEvent)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        if os.path.isfile(self.workfile):
            print('show')
            try:
                img = cv2.imread(self.workfile)  # 读取图像
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
                img_width = img.shape[1]  # 获取图像大小
                img_height = img.shape[0]
                width = self.input_view.width()
                height = self.input_view.height()
                zoomscale = min(width / img_width, height / img_height)  # 图片放缩尺度
                frame = QImage(img, img_width, img_height, QImage.Format_RGB888)
                pix = QPixmap.fromImage(frame)
                self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
                scene = QGraphicsScene()  # 创建场景
                scene.addItem(self.item)
                self.input_view.setScene(scene)
                self.input_view.show()
                self.item.setScale(zoomscale)

            except Exception as e:
                print(e)

    def closeEvent(self, a0: QCloseEvent) -> None:
        if QMessageBox.question(self,'关闭','是否退出程序',QMessageBox.Yes|QMessageBox.No,QMessageBox.No) ==QMessageBox.Yes:
            a0.accept()
        else:
            a0.ignore()


app=QApplication(sys.argv)
window=App()
window.show()
sys.exit(app.exec_())