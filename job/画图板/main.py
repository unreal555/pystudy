import tkinter
from point import Point
from line import *
from circle import *
#from pig import *
from tkinter import colorchooser
from PIL import Image
CURVE = 1
LINE_BRESENHAM = 2
LINE_DDA = 3
LINE_MID = 4

CIRCLE_MID = 5
CIRCLE_BRESENHAM = 6
ELLIPSE_BRESENHAM = 7
ERASE = 20

app = tkinter.Tk()
app.title('画板')
app['width'] = 800
app['height'] = 600
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
                canvas.create_oval(x, y, x, y, fill='red', tag='temp')
            else:
                canvas.create_oval(x, y, x, y, fill='red')


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
menubar = tkinter.Menu(app)


# 添加菜单，清除
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
menubar.add_command(label='橡皮擦', command=select_erase)
#顶级菜单
menubar.add_command(label='pig', command=drawCurve)

#顶级菜单
menubar.add_command(label='清除', command=clear)

#顶级菜单实例应用到大窗口中
app['menu']=menubar
canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
app.mainloop()
