# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/5/12 0012 上午 11:35
# Tool ：PyCharm

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
              
class MySelectFont(QWidget):
    def  __init__(self):
        super(MySelectFont,self).__init__()
        self.initGui()
    
    def initGui(self):
        self.setWindowTitle('测试 ')
        self.resize(800,600)
        self.layout = QVBoxLayout()
        
        self.fontButton = QPushButton('选择字体')
        self.colorButton= QPushButton('字体颜色')
    
        self.label  = QLabel('测试显示的字体')
        self.label.setAlignment(Qt.AlignCenter)
        
        self.p=QPalette()
        
        
        self.layout.addWidget(self.fontButton)
        self.layout.addWidget(self.colorButton)
        self.layout.addWidget(self.label)
        
        self.fontButton.clicked.connect(self.selectFont)
        self.colorButton.clicked.connect(self.selectColor)
        self.setLayout(self.layout)

    def selectFont(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.label.setFont(font)
    
    def selectColor(self):
        color=QColorDialog.getColor()
        self.p.setColor(QPalette.WindowText,color)
        self.label.setPalette(self.p)

    
                         
            
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MySelectFont()
    win.show()
    sys.exit(app.exec_())