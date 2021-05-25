# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/5/19 0019 上午 8:40
# Tool ：PyCharm

import sys,os
import cv2
import numpy as np
from PyQt5.QtWidgets import QDialog,QApplication,QGraphicsView,QGraphicsPixmapItem,QGraphicsScene
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent,QCloseEvent,QImage,QPixmap,QWheelEvent


class MyPicDialog(QDialog):
    
    def __init__(self,imgpath=None,zoomscale=1,opacity=0.8,background='#EAEAEF'):
        super(QDialog, self).__init__()
        self.zoomscale=zoomscale
        self.opacity=opacity
        self.background=background
        
        self.img=None
        self.imageWidth=None
        self.imageHeight=None
        self.pix=None
        self.picItem=None
        self.picScene=None
        
        self.lastMouseP=None

        self.grabMouse()
        
        self.outputView = QGraphicsView(self)
        self.outputView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.outputView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.outputView.wheelEvent=self.wheelEvent
        
        if imgpath==None:
            print('None')
            self.closeEvent(QCloseEvent)
        else:
            self.showImage(imgpath=imgpath)
            
        self.stayOnTop()
        self.frameLessWindow()
    
    def showImage(self,imgpath):
        if os.path.isfile(imgpath):
            try:
                self.img = cv2.imdecode(np.fromfile(imgpath, dtype=np.uint8), cv2.IMREAD_COLOR)
                self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)  # 转换图像通道
                self.imageWidth = self.img.shape[1]  # 获取图像大小
                self.imageHeight = self.img.shape[0]
                self.frame = QImage(self.img, self.imageWidth, self.imageHeight, QImage.Format_RGB888)
                self.pix = QPixmap.fromImage(self.frame)
                self.picItem = QGraphicsPixmapItem(self.pix)  # 创建像素图元
                self.picScene = QGraphicsScene()  # 创建场景
                self.picScene.addItem(self.picItem)
                self.outputView.setScene(self.picScene)
                self.outputView.show()
                self.setupUi()
                self.zoomWin()
            except Exception as e:
                self.hide()
        else:
            self.hide()
            
    def setupUi(self,background=None,opacity=None):
        if not background==None:
            self.background=background
        if not opacity==None:
            self.opacity=opacity
        self.setStyleSheet("background-color: rgb{};".format(self.background))
        self.setWindowOpacity(self.opacity)

    def zoomWin(self):
        newSize=(self.imageWidth*self.zoomscale, self.imageHeight*self.zoomscale)
        self.outputView.resize(*newSize)
        self.resize(*newSize)
        self.picItem.setScale(self.zoomscale)

    def stayOnTop(self,f=True):
        self.setWindowFlag(Qt.WindowStaysOnTopHint,f)
        
    def frameLessWindow(self,f=True):
        self.setWindowFlag(Qt.FramelessWindowHint, f)

    def mouseDoubleClickEvent(self, a0: QMouseEvent) -> None:
        self.hide()

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        self.lastMouseP=(a0.globalPos().x(),a0.globalPos().y())
    
    def wheelEvent(self, a0: QWheelEvent) -> None:
        value=float(a0.angleDelta().y()/1200)
        if not (self.zoomscale<0.2 and value<0):
            self.zoomscale+=value
            self.zoomWin()
    
    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        preX,preY=self.lastMouseP
        nowX,nowY=(a0.globalPos().x(),a0.globalPos().y())
        x,y=self.geometry().x(),self.geometry().y()
        self.move(x+(nowX-preX),y+(nowY-preY))
        self.lastMouseP=(a0.globalPos().x(),a0.globalPos().y())
    
    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        pass
    
    def closeEvent(self, a0: QCloseEvent) -> None:
        self.destroy()
        sys.exit(self)
        
    # def __del__(self):
    #     self.destroy()
    #     sys.exit(self)
        
        
        
if __name__ == '__main__':

    app=QApplication(sys.argv)
    dl=MyPicDialog(imgpath=r'D:\PyCharm2019.3.1\pystudy\pic\2.jpg')
    dl.exec()
    sys.exit(app.exec_())