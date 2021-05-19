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
    
    def __init__(self,imgpath=None):
        super(QDialog, self).__init__()
        self.zoomscale=1
        self.opacity=0.8
        self.background='#EAEAEF'
        
        self.imageWidth=-1
        self.imageHeight=-1
        
        self.lastMouseP=''
        
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.grabMouse()
        
        self.outputView = QGraphicsView(self)
        self.outputView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.outputView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFocus()

        if imgpath==None:
            print('None')
            self.closeEvent(QCloseEvent)
            
        if os.path.isfile(imgpath):
            try:
                self.img = cv2.imdecode(np.fromfile(imgpath, dtype=np.uint8), cv2.IMREAD_COLOR)
                self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)  # 转换图像通道
                self.imageWidth = self.img.shape[1]  # 获取图像大小
                self.imageHeight = self.img.shape[0]
            except Exception as e:
                self.closeEvent(QCloseEvent)
                
        self.frame = QImage(self.img, self.imageWidth, self.imageHeight, QImage.Format_RGB888)
        self.pix = QPixmap.fromImage(self.frame)
        self.picItem = QGraphicsPixmapItem(self.pix)  # 创建像素图元
        self.picScene = QGraphicsScene()  # 创建场景
        self.picScene.addItem(self.picItem)
        self.outputView.setScene(self.picScene)
        self.outputView.show()
        self.setupUi()
        self.zoomWin()
            
    def setupUi(self):
        self.setStyleSheet("background-color: rgb{};".format(self.background))
        self.setWindowOpacity(self.opacity)

    def zoomWin(self):
        print(self.imageWidth*self.zoomscale, self.imageHeight*self.zoomscale)
        print(self.picScene.sceneRect())
        self.picItem.setScale(self.zoomscale)
        self.outputView.resize(self.imageWidth*self.zoomscale, self.imageHeight*self.zoomscale)
        self.resize(self.imageWidth*self.zoomscale, self.imageHeight*self.zoomscale)

        

    def mouseDoubleClickEvent(self, a0: QMouseEvent) -> None:
        self.closeEvent(QCloseEvent)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        self.lastMouseP=(a0.globalPos().x(),a0.globalPos().y())
        print(self.lastMouseP)
    
    def wheelEvent(self, a0: QWheelEvent) -> None:
        value=float(a0.angleDelta().y()/1200)
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
        
if __name__ == '__main__':

    app=QApplication(sys.argv)
    dl=MyPicDialog(imgpath=r'C:\Users\Administrator\Desktop\样本\有1 (7).png')
    dl.exec()
    sys.exit(dl)