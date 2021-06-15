# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/6/15 0015 上午 10:11
# Tool ：PyCharm
from OpenGL.GL import *
from OpenGL.GLUT import *
from pyopengltk import OpenGLFrame
import tkinter as tk

class My_3D(OpenGLFrame):

    def initgl(self):
        glutInit()

        mat_specular = [1.0, 1.0, 1.0, 1.0]  # 镜面反射参数
        mat_shininess = [50.0]  # 高光指数
        light_position = [1.0, 1.0, 1.0, 0.0]  # 光源位置
        white_light = [255.0, 1.0, 1.0, 1.0]  # 灯位置(1,1,1), 最后1-开关
        light_model_ambient = [0.2, 0.2, 0.2, 1.0]  # 环境光参数

        glClearColor(0.0, 0.0, 0.0, 0.0)  # 背景色
        glShadeModel(GL_SMOOTH)  # 填充模式

        # 材质属性 material property
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
        glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

        # 灯光设置
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, white_light)  # 散射光属性
        glLightfv(GL_LIGHT0, GL_SPECULAR, white_light)  # 镜面反射光
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, light_model_ambient)

        glEnable(GL_LIGHTING)  # 开关:使用光
        glEnable(GL_LIGHT0)  # 打开0#灯
        glEnable(GL_DEPTH_TEST)  # 打开深度测试


    def show(self):


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glutWireTeapot(0.5)
        glutSolidTeapot(0.5)  # 茶壶绘制
        glRotatef(0.1, 5, 5, 0)  # (角度,x,y,z)
        glFlush()

    def redraw(self,w=800, h=600):
        print(3)
        glViewport(0, 0, w, h)
        # 设置投影参数
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # 正交投影
        if w <= h:
            glOrtho(-1.5, 1.5, -1.5 * h / w, 1.5 * h / w, -10.0, 10.0)
        else:
            glOrtho(-1.5 * w / h, 1.5 * w / h, -1.5, 1.5, -10.0, 10.0)
        # 设置模型参数--几何体参数
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()


app=tk.Tk()
app.title('aaaa')
area=My_3D(app,width=800,height=600)
area.pack()
area.mainloop()
