import tkinter
from point import Point
from line import *
from circle import *
import turtle
import Teapot
from OpenGL import GLUT

from tkinter import colorchooser

from collections import deque

CURVE = 1
LINE_BRESENHAM = 2
LINE_DDA = 3
LINE_MID = 4
CIRCLE_MID = 5
CIRCLE_BRESENHAM = 6
ELLIPSE_BRESENHAM = 7
POLYGON = 8
ERASE = 20
global busy
busy = False


app = tkinter.Tk()
app.title('画板')
app.attributes("-alpha", 0.9)  # 设置窗体透明度0-1之间

# 绘制多边形时储存的状态，选择的点的位置，和生成的点的图像元素
clickpoints = deque(maxlen=1000)
temppoints = deque(maxlen=100)
global now_item
global pre_point
now_item=None
pre_point=None

# 控制是否允许画图的变量，1：允许，0：不允许
is_draw = tkinter.IntVar(value=0)
# 控制画图类型的变量，1：曲线，2：直线，3：矩形，4：文本，5：橡皮
mode = tkinter.IntVar(value=1)
# 记录鼠标位置的变量
point_start = Point(tkinter.IntVar(value=0), tkinter.IntVar(value=0))
# 前景色
lineColor = 'red'
fillColor = 'green'
backColor = '#bcbcbc'

canvas = tkinter.Canvas(app, width=800, height=600)
canvas.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.NONE)
turtleCv = turtle.TurtleScreen(canvas)
turtleCv.setworldcoordinates(0, -800, 600, 0)

canvas['bg'] = backColor

canvas.create_text(400, 300,  # 使用create_text方法在坐标（302，77）处绘制文字
                   font="Times 100 italic bold",
                   text=''  # 所绘制文字的内容
                   , fill='LightGrey')  # 所绘制文字的颜色为灰色


# 画传入的点集 temp为True时，在move中会删除
def create_point(points, fill=lineColor, temp=False):
    if points is not None:
        for p in points:
            x, y = p.x, p.y
            if temp:
                canvas.create_oval(x, y, x, y, outline=fill, fill=fill, tag='temp')
            else:
                canvas.create_oval(x, y, x, y, outline=fill, fill=fill)


# 鼠标左键单击，允许画图
def on_left_button_down(event):
    is_draw.set(1)
    point_start.set(event.x, event.y)


canvas.bind('<Button-1>', on_left_button_down)
# 记录最后绘制图形的id
lastDraw = 0


# 按住鼠标左键移动，画图
def on_left_button_move(event):
    global pre_point
    global now_item
    if is_draw.get() == 0:
        return

    if mode.get() == CURVE:
        # 使用当前选择的前景色绘制曲线
        canvas.create_line(point_start.x, point_start.y, event.x, event.y, fill=lineColor)
        point_start.set(event.x, event.y)
    elif mode.get() == LINE_BRESENHAM:
        # 绘制直线，先删除刚刚画过的直线，再画一条新的直线
        try:
            canvas.delete('temp')
        except Exception as e:
            pass
        points = bresenham_line(point_start, Point(event.x, event.y))
        create_point(points, fill=lineColor, temp=True)

    elif mode.get() == LINE_DDA:
        # 绘制直线，先删除刚刚画过的直线，再画一条新的直线
        try:
            canvas.delete('temp')
        except Exception as e:
            pass
        points = dda_line(point_start, Point(event.x, event.y))
        create_point(points, fill=lineColor, temp=True)

    elif mode.get() == LINE_MID:
        # 绘制直线，先删除刚刚画过的直线，再画一条新的直线
        try:
            canvas.delete('temp')
        except Exception as e:
            pass
        points = mid_line(point_start, Point(event.x, event.y))
        create_point(points, fill=lineColor, temp=True)

    elif mode.get() == CIRCLE_MID:
        # 绘制圆形，先删除刚刚画过的圆形，再画一个新的圆形
        # global lastDraw
        try:
            canvas.delete('temp')
        except Exception as e:
            pass
        points = mid_circle(point_start, Point(event.x, event.y))
        create_point(points, fill=lineColor, temp=True)

    elif mode.get() == CIRCLE_BRESENHAM:
        # 绘制圆形，先删除刚刚画过的圆形，再画一个新的圆形
        # global lastDraw
        try:
            canvas.delete('temp')
        except Exception as e:
            pass
        points = bresenham_circle(point_start, Point(event.x, event.y))
        create_point(points, fill=lineColor, temp=True)

    elif mode.get() == ELLIPSE_BRESENHAM:
        # 绘制圆形，先删除刚刚画过的圆形，再画一个新的圆形
        # global lastDraw
        try:
            canvas.delete('temp')
        except Exception as e:
            pass
        points = bresenham_ellipse(point_start, Point(event.x, event.y))
        create_point(points, fill=lineColor, temp=True)

    elif mode.get() == ERASE:
        # 橡皮，使用背景色填充10*10的矩形区域
        canvas.create_rectangle(event.x - 5, event.y - 5, event.x + 5, event.y + 5,
                                outline=backColor, fill=backColor)

    elif mode.get() == POLYGON:
        #处理多边形拖动
        now_item=canvas.find_closest(event.x,event.y)[0]  #返回最靠近鼠标位置的图形元素
        if  pre_point==None:
            pre_point=[event.x,event.y]

        if pre_point!=None:
            canvas.tag_raise(now_item)
            canvas.move(now_item,event.x-pre_point[0],event.y-pre_point[-1])  #移动靠近鼠标位置的图形元素
            pre_point = [event.x, event.y]


canvas.bind('<B1-Motion>', on_left_button_move)


def init_bind(self):
        self.cv.bind('<Motion>', self.mouse_move)
        self.cv.bind("<ButtonPress-1>", self.StartMove)  # 监听左键按下操作响应函数
        self.cv.bind("<ButtonRelease-1>", self.StopMove)  # 监听左键松开操作响应函数
        self.cv.bind("<B1-Motion>", self.OnMotion)  # 监听鼠标移动操作响应函数


#绘制多边形
def drawPolygon(event):
    if mode.get() != POLYGON:
        return
    try:
        for x, y in clickpoints:
            if x in range(event.x - 8, event.x + 8) and y in range(event.y - 8, event.y + 8):
                print('封闭')
                for item in temppoints:
                    canvas.delete(item)
                canvas.create_polygon(*clickpoints, outline=lineColor, fill=fillColor)
                clearPolygonState()
                return
    except Exception as e:
        print(e)
        clearPolygonState()
        return

    clickpoints.append((event.x, event.y))
    temppoints.append(canvas.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3, outline='red', fill='red'))


canvas.bind('<Double-Button-1>', drawPolygon)


# 鼠标左键抬起，结束画图
def on_left_button_up(event):
    global now_item
    global pre_point
    if mode.get() == LINE_BRESENHAM:
        # 绘制直线
        points = bresenham_line(point_start, Point(event.x, event.y))
        create_point(points, lineColor)

    elif mode.get() == LINE_DDA:
        points = dda_line(point_start, Point(event.x, event.y))
        create_point(points, lineColor)

    elif mode.get() == LINE_MID:
        points = mid_line(point_start, Point(event.x, event.y))
        create_point(points, lineColor)

    elif mode.get() == CIRCLE_MID:
        # 绘制圆形
        points = mid_circle(point_start, Point(event.x, event.y))
        create_point(points, lineColor)

    elif mode.get() == CIRCLE_BRESENHAM:
        # 绘制圆形
        points = bresenham_circle(point_start, Point(event.x, event.y))
        create_point(points, lineColor)

    elif mode.get() == ELLIPSE_BRESENHAM:
        # 绘制圆形
        points = bresenham_ellipse(point_start, Point(event.x, event.y))
        create_point(points, lineColor)

    #处理多边形拖动
    elif mode.get() == POLYGON:

        global pre_point
        pre_point=None

    is_draw.set(0)


canvas.bind('<ButtonRelease-1>', on_left_button_up)


# 创建菜单


def clearPolygonState():
    temppoints.clear()
    clickpoints.clear()


def clear():
    for item in canvas.find_all():
        canvas.delete(item)

def select_erase():
    mode.set(ERASE)


def drawCurve():
    mode.set(CURVE)
    print(mode.get())


def select_line_bresenham():
    mode.set(LINE_BRESENHAM)


def select_line_dda():
    mode.set(LINE_DDA)


def select_line_mid():
    mode.set(LINE_MID)


def select_circle_mid():
    mode.set(CIRCLE_MID)


def select_circle_bresenham():
    mode.set(CIRCLE_BRESENHAM)


def select_polygon():
    print('set polygon')
    mode.set(POLYGON)


def select_ellipse_bresenham():
    mode.set(ELLIPSE_BRESENHAM)


# 选择线条颜色
def chooseLineColor():
    global lineColor
    lineColor = colorchooser.askcolor()[1]


# 选择填充颜色
def chooseFillColor():
    global fillColor
    fillColor = colorchooser.askcolor()[1]


# 选择绘图板底色
def chooseBackColor():
    pass
    # global backColor
    # backColor = colorchooser.askcolor()[1]
    # canvas['bg']=backColor

def start():
    app.destroy()
    Teapot.start()


menubar = tkinter.Menu(app)



# 在顶级菜单实例下创建子菜单实例

menu3 = tkinter.Menu(menubar, tearoff=0)
for each, command in zip(['绘图线条颜色', '多边形填充颜色'], [chooseLineColor, chooseFillColor]):
    menu3.add_command(label=each, command=command)
menubar.add_cascade(label='颜色', menu=menu3)
#顶级菜单
#menubar.add_command(label='曲线', command=drawCurve)
# 在顶级菜单实例下创建子菜单实例
menu1 = tkinter.Menu(menubar, tearoff=0)
for each, command in zip(['DDA画直线', '中点画直线', 'line_bresenham画直线'],
                     [select_line_dda, select_line_mid, select_line_bresenham]):
    menu1.add_command(label=each, command=command)
menubar.add_cascade(label='直线', menu=menu1)
# 在顶级菜单实例下创建子菜单实例
menu2 = tkinter.Menu(menubar, tearoff=0)
for each, command in zip(['中点画圆', 'bresenham画圆'],
                         [select_circle_mid, select_circle_bresenham]):
    menu2.add_command(label=each, command=command)
menubar.add_cascade(label='圆', menu=menu2)
# 顶级菜单
menubar.add_command(label='椭圆', command=select_ellipse_bresenham)


# 顶级菜单
menubar.add_command(label='多边形', command=select_polygon)
# 顶级菜单
#menubar.add_command(label='橡皮擦', command=select_erase)
# 顶级菜单
menubar.add_command(label='清除', command=clear)

menubar.add_command(label='3D', command=start)

# 顶级菜单实例应用到大窗口中
app['menu'] = menubar
canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
app.mainloop()



