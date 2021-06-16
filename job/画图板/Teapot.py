# 导入相关库
from OpenGL.GL import *
from OpenGL.GLUT import *


# 初始化OpenGL函数


def init():
    # 材质反光性设置
    mat_specular = [1.0, 1.0, 1.0, 1.0]  # 镜面反射参数
    mat_shininess = [20.0]  # 高光指数
    light_position = [1200, 800.0, 1800.0, 0.0]  # 光源位置
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
    
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(display)
    glutCloseFunc(close)
    glutMouseFunc(mouseclick)

def mouseclick(button,state,x,y):
    print(button,state,x,y)
    if button==2:
        glLightfv(GL_LIGHT0, GL_POSITION, [(x-400)*10, (300-y)*10, 600.0, 1.0])
        
    

def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glutWireTeapot(1)
    # glutSolidTeapot(1)  # 茶壶绘制
    glRotatef(0.01, 0, 1, 0)  # (角度,x,y,z)
    glFlush()


def reshape(w=800, h=600):
    # glViewport(0, 0, w, h)
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

def close():
    glutHideWindow()

    glutDestroyWindow(glutGetWindow())
    
    import main6


def start():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE| GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    print(glutCreateWindow("3D"))

    init()
    glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_GLUTMAINLOOP_RETURNS)
    glutMainLoop()


if __name__ == "__main__":

    start()
