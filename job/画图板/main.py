import tkinter
from point import Point
from line import *
from circle import *
#from pig import *
from tkinter import colorchooser
import turtle
from collections import deque

CURVE = 1
LINE_BRESENHAM = 2
LINE_DDA = 3
LINE_MID = 4
CIRCLE_MID = 5
CIRCLE_BRESENHAM = 6
ELLIPSE_BRESENHAM = 7
POLYGON=8
ERASE = 20
global busy
busy=False

app = tkinter.Tk()
app.title('画板')

clickpoints=deque(maxlen=1000)
temppoints=deque(maxlen=100)



# 控制是否允许画图的变量，1：允许，0：不允许
is_draw = tkinter.IntVar(value=0)
# 控制画图类型的变量，1：曲线，2：直线，3：矩形，4：文本，5：橡皮
mode = tkinter.IntVar(value=1)
# 记录鼠标位置的变量
point_start = Point(tkinter.IntVar(value=0), tkinter.IntVar(value=0))
# 前景色
foreColor = '#000000'
backColor = '#FFFFFF'



canvas = tkinter.Canvas(app, bg='white', width=800, height=600)
canvas.pack(side=tkinter.LEFT,  expand=tkinter.YES, fill=tkinter.NONE)
turtleCv = turtle.TurtleScreen(canvas)
turtleCv.setworldcoordinates(0, -800, 600, 0)

canvas.create_text(400,300,       # 使用create_text方法在坐标（302，77）处绘制文字
    font="Times 100 italic bold",
   text = ''      # 所绘制文字的内容
   ,fill = 'LightGrey')       # 所绘制文字的颜色为灰色


# 画传入的点集 temp为True时，在move中会删除
def create_point(points, fill="black", temp=False):
    if points is not None:
        for p in points:
            x, y = p.x, p.y
            if temp:
                canvas.create_oval(x, y, x, y, fill=fill, tag='temp')
            else:
                canvas.create_oval(x, y, x, y, fill=fill)
    


# 鼠标左键单击，允许画图
def on_left_button_down(event):
    is_draw.set(1)
    point_start.set(event.x, event.y)


canvas.bind('<Button-1>', on_left_button_down)
# 记录最后绘制图形的id
lastDraw = 0


# 按住鼠标左键移动，画图
def on_left_button_move(event):
    if is_draw.get() == 0:
        return

    if mode.get() == CURVE:
        # 使用当前选择的前景色绘制曲线
        canvas.create_line(point_start.x, point_start.y, event.x, event.y, fill=foreColor)
        point_start.set(event.x, event.y)
    elif mode.get() == LINE_BRESENHAM:
        # 绘制直线，先删除刚刚画过的直线，再画一条新的直线
        try:
            canvas.delete('temp')
        except Exception as e:
            pass
        points = bresenham_line(point_start, Point(event.x, event.y))
        create_point(points, fill=foreColor, temp=True)

    elif mode.get() == LINE_DDA:
        # 绘制直线，先删除刚刚画过的直线，再画一条新的直线
        try:
            canvas.delete('temp')
        except Exception as e:
            pass
        points = dda_line(point_start, Point(event.x, event.y))
        create_point(points, fill=foreColor, temp=True)

    elif mode.get() == LINE_MID:
        # 绘制直线，先删除刚刚画过的直线，再画一条新的直线
        try:
            canvas.delete('temp')
        except Exception as e:
            pass
        points = mid_line(point_start, Point(event.x, event.y))
        create_point(points, fill=foreColor, temp=True)

    elif mode.get() == CIRCLE_MID:
        # 绘制圆形，先删除刚刚画过的圆形，再画一个新的圆形
        # global lastDraw
        try:
            canvas.delete('temp')
        except Exception as e:
            pass
        points = mid_circle(point_start, Point(event.x, event.y))
        create_point(points, fill=foreColor, temp=True)

    elif mode.get() == CIRCLE_BRESENHAM:
        # 绘制圆形，先删除刚刚画过的圆形，再画一个新的圆形
        # global lastDraw
        try:
            canvas.delete('temp')
        except Exception as e:
            pass
        points = bresenham_circle(point_start, Point(event.x, event.y))
        create_point(points, fill=foreColor, temp=True)

    elif mode.get() == ELLIPSE_BRESENHAM:
        # 绘制圆形，先删除刚刚画过的圆形，再画一个新的圆形
        # global lastDraw
        try:
            canvas.delete('temp')
        except Exception as e:
            pass
        points = bresenham_ellipse(point_start, Point(event.x, event.y))
        create_point(points, fill=foreColor, temp=True)

    elif mode.get() == ERASE:
        # 橡皮，使用背景色填充10*10的矩形区域
        canvas.create_rectangle(event.x - 5, event.y - 5, event.x + 5, event.y + 5,
                                outline=backColor, fill=backColor)


canvas.bind('<B1-Motion>', on_left_button_move)



def drawPolygon(event):

    if mode.get()!=POLYGON:
        return
    
    for x,y in clickpoints:
        if x in range(event.x-5,event.x+5) and y in range(event.y-5,event.y+5):
            print('封闭')
            for item in temppoints:
                canvas.delete(item)

            

            canvas.create_polygon(*clickpoints,outline=foreColor,fill=backColor)

            clearPolygonState()


    clickpoints.append((event.x,event.y))
    temppoints.append(canvas.create_oval(event.x-2,event.y-2,event.x+2,event.y+2,outline='#000000'))
    


canvas.bind('<Double-Button-1>',drawPolygon)


# 鼠标左键抬起，结束画图
def on_left_button_up(event):
    if mode.get() == LINE_BRESENHAM:
        # 绘制直线
        points = bresenham_line(point_start, Point(event.x, event.y))
        create_point(points, foreColor)

    elif mode.get() == LINE_DDA:
        points = dda_line(point_start, Point(event.x, event.y))
        create_point(points, foreColor)

    elif mode.get() == LINE_MID:
        points = mid_line(point_start, Point(event.x, event.y))
        create_point(points, foreColor)

    elif mode.get() == CIRCLE_MID:
        # 绘制圆形
        points = mid_circle(point_start, Point(event.x, event.y))
        create_point(points, foreColor)

    elif mode.get() == CIRCLE_BRESENHAM:
        # 绘制圆形
        points = bresenham_circle(point_start, Point(event.x, event.y))
        create_point(points, foreColor)

    elif mode.get() == ELLIPSE_BRESENHAM:
        # 绘制圆形
        points = bresenham_ellipse(point_start, Point(event.x, event.y))
        create_point(points, foreColor)

    #elif mode.get() == select_pig:

        #points = bresenham_ellipse(point_start, Point(event.x, event.y))
        #create_point(points, foreColor)
    is_draw.set(0)


canvas.bind('<ButtonRelease-1>', on_left_button_up)
# 创建菜单



def clearPolygonState():
    temppoints.clear()
    clickpoints.clear()

def clear():
    for item in canvas.find_all():
        canvas.delete(item)
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
# 选择前景色
def chooseForeColor():
    global foreColor
    foreColor = colorchooser.askcolor()[1]
# 选择背景色
def chooseBackColor():
    global backColor
    backColor = colorchooser.askcolor()[1]
# 橡皮
def select_erase():
    mode.set(ERASE)


def drawPeiQi():
    global busy
    if busy == True:
        return
    busy = True
    t = turtle.RawTurtle(turtleCv)
    t.pensize(4)
    t.hideturtle()
    t.color((1, 0.6, 0.75), "pink")
    # t.setup(840, 500)
    t.speed(10)
    
    # 鼻子
    t.pu()
    t.goto(170, -250)
    t.pd()
    t.seth(-30)
    t.begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            t.lt(3)  # 向左转3度
            t.fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            t.lt(3)
            t.fd(a)
    t.end_fill()
    
    t.pu()
    t.seth(90)
    t.fd(25)
    t.seth(0)
    t.fd(10)
    t.pd()
    t.pencolor(1, 0.6, 0.75)
    t.seth(10)
    t.begin_fill()
    t.circle(5)
    t.color(0.62, 0.33, 0.18)
    t.end_fill()
    
    t.pu()
    t.seth(0)
    t.fd(20)
    t.pd()
    t.pencolor(1, 0.6, 0.75)
    t.seth(10)
    t.begin_fill()
    t.circle(5)
    t.color(0.62, 0.32, 0.18)
    t.end_fill()
    
    # 头
    t.color((1, 0.6, 0.75), "pink")
    t.pu()
    t.seth(90)
    t.fd(41)
    t.seth(0)
    t.fd(0)
    t.pd()
    t.begin_fill()
    t.seth(180)
    t.circle(300, -30)
    t.circle(100, -60)
    t.circle(80, -100)
    t.circle(150, -20)
    t.circle(60, -95)
    t.seth(161)
    t.circle(-300, 15)
    t.pu()
    t.goto(170, -250)
    t.pd()
    t.seth(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            t.lt(3)  # 向左转3度
            t.fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            t.lt(3)
            t.fd(a)
    t.end_fill()
    
    # 耳朵
    t.color((1, 0.6, 0.75), "pink")
    t.pu()
    t.seth(90)
    t.fd(-7)
    t.seth(0)
    t.fd(70)
    t.pd()
    t.begin_fill()
    t.seth(100)
    t.circle(-50, 50)
    t.circle(-10, 120)
    t.circle(-50, 54)
    t.end_fill()
    
    t.pu()
    t.seth(90)
    t.fd(-12)
    t.seth(0)
    t.fd(30)
    t.pd()
    t.begin_fill()
    t.seth(100)
    t.circle(-50, 50)
    t.circle(-10, 120)
    t.circle(-50, 56)
    t.end_fill()
    
    # 眼睛
    t.color((1, 0.6, 0.75), "white")
    t.pu()
    t.seth(90)
    t.fd(-20)
    t.seth(0)
    t.fd(-95)
    t.pd()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    
    t.color("black")
    t.pu()
    t.seth(90)
    t.fd(12)
    t.seth(0)
    t.fd(-3)
    t.pd()
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    
    t.color((1, 0.6, 0.75), "white")
    t.pu()
    t.seth(90)
    t.fd(-25)
    t.seth(0)
    t.fd(40)
    t.pd()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    
    t.color("black")
    t.pu()
    t.seth(90)
    t.fd(12)
    t.seth(0)
    t.fd(-3)
    t.pd()
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    
    # 腮
    t.color((1, 0.6, 0.75))
    t.pu()
    t.seth(90)
    t.fd(-95)
    t.seth(0)
    t.fd(65)
    t.pd()
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    
    # 嘴
    t.color(0.94, 0.27, 0.075)
    t.pu()
    t.seth(90)
    t.fd(15)
    t.seth(0)
    t.fd(-100)
    t.pd()
    t.seth(-80)
    t.circle(30, 40)
    t.circle(40, 80)
    
    # 身体
    t.color("red", (1, 0.39, 0.28))
    t.pu()
    t.seth(90)
    t.fd(-20)
    t.seth(0)
    t.fd(-78)
    t.pd()
    t.begin_fill()
    t.seth(-130)
    t.circle(100, 10)
    t.circle(300, 30)
    t.seth(0)
    t.fd(230)
    t.seth(90)
    t.circle(300, 30)
    t.circle(100, 3)
    t.color((1, 0.6, 0.75), (1, 0.39, 0.39))
    t.seth(-135)
    t.circle(-80, 63)
    t.circle(-150, 24)
    t.end_fill()
    
    # 手
    t.color((1, 0.6, 0.75))
    t.pu()
    t.seth(90)
    t.fd(-40)
    t.seth(0)
    t.fd(-27)
    t.pd()
    t.seth(-160)
    t.circle(300, 15)
    t.pu()
    t.seth(90)
    t.fd(15)
    t.seth(0)
    t.fd(0)
    t.pd()
    t.seth(-10)
    t.circle(-20, 90)
    
    t.pu()
    t.seth(90)
    t.fd(30)
    t.seth(0)
    t.fd(237)
    t.pd()
    t.seth(-20)
    t.circle(-300, 15)
    t.pu()
    t.seth(90)
    t.fd(20)
    t.seth(0)
    t.fd(0)
    t.pd()
    t.seth(-170)
    t.circle(20, 90)
    
    # 脚
    t.pensize(10)
    t.color((0.94, 0.5, 0.5))
    t.pu()
    t.seth(90)
    t.fd(-75)
    t.seth(0)
    t.fd(-180)
    t.pd()
    t.seth(-90)
    t.fd(40)
    t.seth(-180)
    t.color("black")
    t.pensize(15)
    t.fd(20)
    
    t.pensize(10)
    t.color((0.94, 0.5, 0.5))
    t.pu()
    t.seth(90)
    t.fd(40)
    t.seth(0)
    t.fd(90)
    t.pd()
    t.seth(-90)
    t.fd(40)
    t.seth(-180)
    t.color("black")
    t.pensize(15)
    t.fd(20)
    
    # 尾巴
    t.pensize(4)
    t.color((1, 0.6, 0.75))
    t.pu()
    t.seth(90)
    t.fd(70)
    t.seth(0)
    t.fd(95)
    t.pd()
    t.seth(0)
    t.circle(70, 20)
    t.circle(10, 330)
    t.circle(70, 30)
    busy = False


def drawXiangRiKui():
    global busy
    if busy == True:
        return
    busy = True
    t = turtle.RawTurtle(turtleCv)
    
    t.speed(10)
    t.hideturtle()
    t.up()
    t.goto(300, -600)
    t.down()
    
    t.color("green", "black")
    t.left(90)
    t.forward(300)
    t.right(90)
    t.color("black", "yellow")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    # t.circle(10)
    
    for i in range(1, 24):
        if t.color() == ("red", "black"):
            t.color("orange", "black")
        elif t.color() == ("red", "black"):
            t.colot("yellow", "black")
        else:
            t.color("red", "black")
        t.left(15)
        t.forward(150)
        t.left(157)
        t.forward(150)
    t.hideturtle()
    busy = False


def drawRose():
    global busy
    if busy == True:
        return
    busy = True
    t = turtle.RawTurtle(turtleCv)
    t.goto(0, 0)
    t.speed(10)
    t.hideturtle()
    t.up()
    t.goto(300, -350)
    t.down()
    
    t.speed(5)
    
    # 设置初始位置
    
    t.penup()
    
    t.left(90)
    
    t.fd(200)
    
    t.pendown()
    
    t.right(90)
    # 花蕊
    
    t.fillcolor("red")
    
    t.begin_fill()
    
    t.circle(10, 180)
    
    t.circle(25, 110)
    
    t.left(50)
    
    t.circle(60, 45)
    
    t.circle(20, 170)
    
    t.right(24)
    
    t.fd(30)
    
    t.left(10)
    
    t.circle(30, 110)
    
    t.fd(20)
    
    t.left(40)
    
    t.circle(90, 70)
    
    t.circle(30, 150)
    
    t.right(30)
    
    t.fd(15)
    
    t.circle(80, 90)
    
    t.left(15)
    
    t.fd(45)
    
    t.right(165)
    
    t.fd(20)
    
    t.left(155)
    
    t.circle(150, 80)
    
    t.left(50)
    
    t.circle(150, 90)
    
    t.end_fill()
    
    # 花瓣1
    
    t.left(150)
    
    t.circle(-90, 70)
    
    t.left(20)
    
    t.circle(75, 105)
    
    t.setheading(60)
    
    t.circle(80, 98)
    
    t.circle(-90, 40)
    
    # 花瓣2
    
    t.left(180)
    
    t.circle(90, 40)
    
    t.circle(-80, 98)
    
    t.setheading(-83)
    
    # 叶子1
    
    t.fd(30)
    
    t.left(90)
    
    t.fd(25)
    
    t.left(45)
    
    t.fillcolor("green")
    
    t.begin_fill()
    
    t.circle(-80, 90)
    
    t.right(90)
    
    t.circle(-80, 90)
    
    t.end_fill()
    
    t.right(135)
    
    t.fd(60)
    
    t.left(180)
    
    t.fd(85)
    
    t.left(90)
    
    t.fd(80)
    
    # 叶子2
    
    t.right(90)
    
    t.right(45)
    
    t.fillcolor("green")
    
    t.begin_fill()
    
    t.circle(80, 90)
    
    t.left(90)
    
    t.circle(80, 90)
    
    t.end_fill()
    
    t.left(135)
    
    t.fd(60)
    
    t.left(180)
    
    t.fd(60)
    
    t.right(90)
    
    t.circle(200, 60)
    busy = False

menubar = tkinter.Menu(app)

#顶级菜单
menubar.add_command(label='曲线', command=drawCurve)
#在顶级菜单实例下创建子菜单实例
menu1 = tkinter.Menu(menubar)
for each,command in zip(['line_bresenham','line_DDA','line_mid'],[select_line_bresenham,select_line_dda,select_line_mid]):
    menu1.add_command(label=each,command=command)
menubar.add_cascade(label='直线',menu=menu1)
#在顶级菜单实例下创建子菜单实例
menu2 = tkinter.Menu(menubar)
for each,command in zip(['circle_mid','circle_bresenham','elipse_bresenham'],[select_circle_mid,select_circle_bresenham,select_ellipse_bresenham]):
    menu2.add_command(label=each,command=command)
menubar.add_cascade(label='圆',menu=menu2)
#在顶级菜单实例下创建子菜单实例
menu3 = tkinter.Menu(menubar)
for each,command in zip(['forefround_color','background_color'],[chooseForeColor,chooseBackColor]):
    menu3.add_command(label=each,command=command)
menubar.add_cascade(label='颜色',menu=menu3)

#顶级菜单
menubar.add_command(label='多边形', command=select_polygon)

menu4=tkinter.Menu(menubar)
menu4.add_command(label='佩奇猪',command=drawPeiQi)
menu4.add_command(label='玫瑰',command=drawRose)
menu4.add_command(label='向日葵',command=drawXiangRiKui)
menubar.add_cascade(label='绘图',menu=menu4)

#顶级菜单
menubar.add_command(label='橡皮擦', command=select_erase)


#顶级菜单
menubar.add_command(label='清除', command=clear)

#顶级菜单实例应用到大窗口中
app['menu']=menubar
canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
app.mainloop()



