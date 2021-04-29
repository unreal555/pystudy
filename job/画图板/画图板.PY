from  tkinter import *
import tkinter
import os
from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import *
from concurrent.futures import ThreadPoolExecutor
from collections import deque

import turtle



class DRAWPANEL():


    def __del__(self):
        pass

    def openfile(self):

        file =  askopenfilename()
        temp,ext=os.path.splitext(file)
        print(file)


    def cvMouseDown(self,event):
        x=event.x
        y=event.y
        print('down',x,y)
        self.startX=event.x
        self.startY=event.y
        self.clickspos.append((x,y))
        print(self.clickspos)

    def cvMouseMove(self,event):
        nowX = event.x
        nowY = event.y
        self.cv.delete(self.lastItem)
        
        if self.action=='line':
            self.lastItem=self.drawLine(self.startX,self.startY,nowX,nowY)
        if self.action=='rectangle':
            self.lastItem=self.drawRectangle(self.startX,self.startY,nowX,nowY)
        if self.action=='oval':
            self.lastItem=self.drawOval(self.startX,self.startY,nowX,nowY)
            
    def cvMouseUp(self,event):
        x = event.x
        y = event.y
        print('release', x, y)
        self.Items.append(self.lastItem)
        self.lastItem=''
        print(self.Items)

    def __init__(self):
        self.root = Tk()
        self.root.title('画图板')
        self.root['bg'] = '#bcbcbc'
        # self.root.attributes("-alpha", 0.9)
        # self.root.geometry("1024x600")

        self.linecolor='red'
        self.fillcolor='yellow'
        
        self.action='line'
        
        self.clickspos=deque(maxlen=20)
        
        self.startX=0
        self.startY=0
        
        self.finishX=0
        self.finishY=0
        
        self.lastItem=''
        
        self.Items=[]

        self.colorPanelArea=tkinter.Frame(self.root, bd=2, relief="sunken",height=10)
        self.downArea=tkinter.Frame(self.root, bd=2, relief="sunken",height=10)
        self.colorPanelArea.pack(side=tkinter.TOP, anchor=tkinter.S, expand=tkinter.NO, fill=tkinter.BOTH)
        self.downArea.pack(side=tkinter.BOTTOM, anchor=tkinter.S, expand=tkinter.YES, fill=tkinter.BOTH)
        
        self.drawArea=tkinter.Frame(self.downArea, bd=2, relief="sunken",height=10)
        self.toolsArea=tkinter.Frame(self.downArea, bd=2, relief="sunken",height=10)
        self.drawArea.pack(side=tkinter.RIGHT,  expand=tkinter.YES, fill=tkinter.BOTH)
        self.toolsArea.pack(side=tkinter.LEFT,  expand=tkinter.NO, fill=tkinter.Y)

        self.chooseLineColorButton=tkinter.Button(self.colorPanelArea,text='选择线条颜色',bg=self.linecolor)
        self.chooseLineColorButton.pack(side=tkinter.LEFT,  expand=tkinter.NO, fill=tkinter.X)
        self.chooseLineColorButton.bind("<ButtonPress-1>",self.setLineColor)
        
        self.chooseFillColorButton=tkinter.Button(self.colorPanelArea,text='选择填充颜色',bg=self.fillcolor)
        self.chooseFillColorButton.pack(side=tkinter.LEFT,  expand=tkinter.NO, fill=tkinter.X)
        self.chooseFillColorButton.bind("<ButtonPress-1>", self.setFillColor)
        
        self.drawLineButton=tkinter.Button(self.toolsArea,text='线')
        self.drawLineButton.pack(side=tkinter.TOP,  expand=tkinter.NO, fill=tkinter.X)
        self.drawLineButton.bind('<ButtonPress-1>',self.setAction)
        
        self.drawRectangleButton=tkinter.Button(self.toolsArea,text='矩形')
        self.drawRectangleButton.pack(side=tkinter.TOP,  expand=tkinter.NO, fill=tkinter.X)
        self.drawRectangleButton.bind('<ButtonPress-1>',self.setAction)



        self.drawOvalButton=tkinter.Button(self.toolsArea,text='圆形')
        self.drawOvalButton.pack(side=tkinter.TOP,  expand=tkinter.NO, fill=tkinter.X)
        self.drawOvalButton.bind('<ButtonPress-1>',self.setAction)
        
        self.drawPeiQiButton=tkinter.Button(self.toolsArea,text='佩奇',command=self.drawPeiQi)
        self.drawPeiQiButton.pack(side=tkinter.TOP,  expand=tkinter.NO, fill=tkinter.X)

        self.cleanCanvsButton=tkinter.Button(self.toolsArea,text='清空',command=(lambda x=ALL: self.cv.delete(x)))
        self.cleanCanvsButton.pack(side=tkinter.TOP, expand=tkinter.NO, fill=tkinter.X)

        self.cv=tkinter.Canvas(self.drawArea,width=800,height=600)
        self.cv.pack(side=tkinter.LEFT,  expand=tkinter.YES, fill=tkinter.NONE)
        print(self.cv.winfo_screenheight(),self.cv.winfo_screenmmwidth())
        self.turtleCv = turtle.TurtleScreen(self.cv)
        self.turtleCv.setworldcoordinates(0,-800,600,0)

        self.cv.bind('<ButtonPress-1>',self.cvMouseDown)
        self.cv.bind('<B1-Motion> ',self.cvMouseMove)
        self.cv.bind('<ButtonRelease-1>',self.cvMouseUp)


    def drawRectangle(self,x,y,x1,y1):

        item=self.cv.create_rectangle(x,y,x1,y1,fill=self.fillcolor)
        return item

    def drawLine(self,x,y,x1,y1):
        print(x,y,x1,y1)
        item=self.cv.create_line(x,y,x1,y1,fill=self.linecolor)
        return item
    
    def drawOval(self,x,y,x1,y1):
        return self.cv.create_oval(x,y,x1,y1,fill=self.fillcolor)
    
    def setAction(self,event):
        if event.widget['text']=='线':
            self.action='line'
        if event.widget['text']=='矩形':
            self.action='rectangle'
        if event.widget['text']=='圆形':
            self.action='oval'


    def setLineColor(self,event):
        def do():
            temp, self.linecolor = askcolor()
            self.chooseLineColorButton['bg'] = self.linecolor
    
        pool = ThreadPoolExecutor(max_workers=1)
        pool.submit(do)


    def setFillColor(self,event):
        def do():
            temp,self.fillcolor=askcolor()
            self.chooseFillColorButton['bg']=self.fillcolor
        pool = ThreadPoolExecutor(max_workers=1)
        pool.submit(do)
    
    def drawPeiQi(self):
        t = turtle.RawTurtle(self.turtleCv)
        t.pensize(4)
        t.hideturtle()
        t.color((1, 0.6, 0.75), "pink")
        # t.setup(840, 500)
        t.speed(100)

        # 鼻子
        t.pu()
        t.goto(170,-250)
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
        t.color(0.62,0.32 , 0.18)
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
        t.goto(170,-250)
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
        t.color((0.94,0.5,0.5))
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

app=DRAWPANEL()
app.root.mainloop()




#
# <ButtonPress-n>     <Button-n>      <n>                         鼠标按钮n被按下，n为1左键，2中键，3右键
# <ButtonRelease-n>                                               鼠标按钮n被松开
# <Double-Button-n>                                               鼠标按钮n被双击
# <Triple-Button-n>                                               鼠标按钮n被三击
# <Motion>                                                        鼠标被按下，同时，鼠标发生移动
# <Bn-Motion>                                                     鼠标按钮n被按下，同时，鼠标发生移动
# <Enter>                                                         鼠标进入
# <Leave>                                                         鼠标离开
# <MouseWheel>                                                    鼠标滚轮滚动
# <Button-1>  鼠标左键
# <Button-2>   鼠标中间键（滚轮）
# <Button-3>  鼠标右键
# <Double-Button-1>   双击鼠标左键
# <Double-Button-3>   双击鼠标右键
# <Triple-Button-1>   三击鼠标左键
# <Triple-Button-3>   三击鼠标右键

'''
from tkinter import *
import math as m

root = Tk()

w = Canvas(root, width=200, height=100, background='red')
w.pack()

center_x = 100
center_y = 50
r = 50

points = [
    #左上点
    center_x - int(r*m.sin(2 * m.pi/5)),
    center_y - int(r*m.cos(2 * m.pi/5)),
    #右上点
    center_x + int(r*m.sin(2 * m.pi/5)),
    center_y - int(r*m.cos(2 * m.pi/5)),
    #左下点
    center_x - int(r*m.sin(m.pi/5)),
    center_y + int(r*m.cos(m.pi/5)),
    #顶点
    center_x,
    center_y - r,
    #右下点
    center_x + int(r*m.sin(m.pi/5)),
    center_y + int(r*m.cos(m.pi/5))
    ]

w.create_polygon(points, outline='green', fill='black')'''

colors = '''
#FFB6C1 LightPink 浅粉红
,#FFC0CB Pink 粉红
,#DC143C Crimson 深红/猩红
,#FFF0F5 LavenderBlush 淡紫红
,#DB7093 PaleVioletRed 弱紫罗兰红
,#FF69B4 HotPink 热情的粉红
,#FF1493 DeepPink 深粉红
,#C71585 MediumVioletRed 中紫罗兰红
,#DA70D6 Orchid 暗紫色/兰花紫
,#D8BFD8 Thistle 蓟色
,#DDA0DD Plum 洋李色/李子紫
,#EE82EE Violet 紫罗兰
,#FF00FF Magenta 洋红/玫瑰红
,#FF00FF Fuchsia 紫红/灯笼海棠
,#8B008B DarkMagenta 深洋红
,#800080 Purple 紫色
,#BA55D3 MediumOrchid 中兰花紫
,#9400D3 DarkViolet 暗紫罗兰
,#9932CC DarkOrchid 暗兰花紫
,#4B0082 Indigo 靛青/紫兰色
,#8A2BE2 BlueViolet 蓝紫罗兰
,#9370DB MediumPurple 中紫色
,#7B68EE MediumSlateBlue 中暗蓝色/中板岩蓝
,#6A5ACD SlateBlue 石蓝色/板岩蓝
,#483D8B DarkSlateBlue 暗灰蓝色/暗板岩蓝
,#E6E6FA Lavender 淡紫色/熏衣草淡紫
,#F8F8FF GhostWhite 幽灵白
,#0000FF Blue 纯蓝
,#0000CD MediumBlue 中蓝色
,#191970 MidnightBlue 午夜蓝
,#00008B DarkBlue 暗蓝色
,#000080 Navy 海军蓝
,#4169E1 RoyalBlue 皇家蓝/宝蓝
,#6495ED CornflowerBlue 矢车菊蓝
,#B0C4DE LightSteelBlue 亮钢蓝
,#778899 LightSlateGray 亮蓝灰/亮石板灰
,#708090 SlateGray 灰石色/石板灰
,#1E90FF DodgerBlue 闪兰色/道奇蓝
,#F0F8FF AliceBlue 爱丽丝蓝
,#4682B4 SteelBlue 钢蓝/铁青
,#87CEFA LightSkyBlue 亮天蓝色
,#87CEEB SkyBlue 天蓝色
,#00BFFF DeepSkyBlue 深天蓝
,#ADD8E6 LightBlue 亮蓝
,#B0E0E6 PowderBlue 粉蓝色/火药青
,#5F9EA0 CadetBlue 军兰色/军服蓝
,#F0FFFF Azure 蔚蓝色
,#E0FFFF LightCyan 淡青色
,#AFEEEE PaleTurquoise 弱绿宝石
,#00FFFF Cyan 青色
,#00FFFF Aqua 浅绿色/水色
,#00CED1 DarkTurquoise 暗绿宝石
,#2F4F4F DarkSlateGray 暗瓦灰色/暗石板灰
,#008B8B DarkCyan 暗青色
,#008080 Teal 水鸭色
,#48D1CC MediumTurquoise 中绿宝石
,#20B2AA LightSeaGreen 浅海洋绿
,#40E0D0 Turquoise 绿宝石
,#7FFFD4 Aquamarine 宝石碧绿
,#66CDAA MediumAquamarine 中宝石碧绿
,#00FA9A MediumSpringGreen 中春绿色
,#F5FFFA MintCream 薄荷奶油
,#00FF7F SpringGreen 春绿色
,#3CB371 MediumSeaGreen 中海洋绿
,#2E8B57 SeaGreen 海洋绿
,#F0FFF0 Honeydew 蜜色/蜜瓜色
,#90EE90 LightGreen 淡绿色
,#98FB98 PaleGreen 弱绿色
,#8FBC8F DarkSeaGreen 暗海洋绿
,#32CD32 LimeGreen 闪光深绿
,#00FF00 Lime 闪光绿
,#228B22 ForestGreen 森林绿
,#008000 Green 纯绿
,#006400 DarkGreen 暗绿色
,#7FFF00 Chartreuse 黄绿色/查特酒绿
,#7CFC00 LawnGreen 草绿色/草坪绿
,#ADFF2F GreenYellow 绿黄色
,#556B2F DarkOliveGreen 暗橄榄绿
,#9ACD32 YellowGreen 黄绿色
,#6B8E23 OliveDrab 橄榄褐色
,#F5F5DC Beige 米色/灰棕色
,#FAFAD2 LightGoldenrodYellow 亮菊黄
,#FFFFF0 Ivory 象牙色
,#FFFFE0 LightYellow 浅黄色
,#FFFF00 Yellow 纯黄
,#808000 Olive 橄榄
,#BDB76B DarkKhaki 暗黄褐色/深卡叽布
,#FFFACD LemonChiffon 柠檬绸
,#EEE8AA PaleGoldenrod 灰菊黄/苍麒麟色
,#F0E68C Khaki 黄褐色/卡叽布
,#FFD700 Gold 金色
,#FFF8DC Cornsilk 玉米丝色
,#DAA520 Goldenrod 金菊黄
,#B8860B DarkGoldenrod 暗金菊黄
,#FFFAF0 FloralWhite 花的白色
,#FDF5E6 OldLace 老花色/旧蕾丝
,#F5DEB3 Wheat 浅黄色/小麦色
,#FFE4B5 Moccasin 鹿皮色/鹿皮靴
,#FFA500 Orange 橙色
,#FFEFD5 PapayaWhip 番木色/番木瓜
,#FFEBCD BlanchedAlmond 白杏色
,#FFDEAD NavajoWhite 纳瓦白/土著白
,#FAEBD7 AntiqueWhite 古董白
,#D2B48C Tan 茶色
,#DEB887 BurlyWood 硬木色
,#FFE4C4 Bisque 陶坯黄
,#FF8C00 DarkOrange 深橙色
,#FAF0E6 Linen 亚麻布
,#CD853F Peru 秘鲁色
,#FFDAB9 PeachPuff 桃肉色
,#F4A460 SandyBrown 沙棕色
,#D2691E Chocolate 巧克力色
,#8B4513 SaddleBrown 重褐色/马鞍棕色
,#FFF5EE Seashell 海贝壳
,#A0522D Sienna 黄土赭色
,#FFA07A LightSalmon 浅鲑鱼肉色
,#FF7F50 Coral 珊瑚
,#FF4500 OrangeRed 橙红色
,#E9967A DarkSalmon 深鲜肉/鲑鱼色
,#FF6347 Tomato 番茄红
,#FFE4E1 MistyRose 浅玫瑰色/薄雾玫瑰
,#FA8072 Salmon 鲜肉/鲑鱼色
,#FFFAFA Snow 雪白色
,#F08080 LightCoral 淡珊瑚色
,#BC8F8F RosyBrown 玫瑰棕色
,#CD5C5C IndianRed 印度红
,#FF0000 Red 纯红
,#A52A2A Brown 棕色
,#B22222 FireBrick 火砖色/耐火砖
,#8B0000 DarkRed 深红色
,#800000 Maroon 栗色
,#FFFFFF White 纯白
,#F5F5F5 WhiteSmoke 白烟
,#DCDCDC Gainsboro 淡灰色
,#D3D3D3 LightGrey 浅灰色
,#C0C0C0 Silver 银灰色
,#A9A9A9 DarkGray 深灰色
,#808080 Gray 灰色
,#696969 DimGray 暗淡灰
,#000000 Black 纯黑'''






# play_button=tkinter.Button(control1,text='播放',command=self.play)
# speedup_button=tkinter.Button(control1,text='加速',command=self.play_fast)
# # pause_button=tkinter.Button(control1,text='暂停',command=self.pause)
# onebyone_button=tkinter.Button(control1,text='单帧',command=self.onebyone)
# catchpic_button = tkinter.Button(control1, text='截图', command=self.catchpic)
# stop_button=tkinter.Button(control1,text='停止',command=self.stop)
#
# open_button.grid(row=0, column=0)
# play_button.grid(row=0, column=1)
# speedup_button.grid(row=0, column=2)
# # pause_button.grid(row=0, column=3)
# onebyone_button.grid(row=0, column=4)
# catchpic_button.grid(row=0, column=5)
# stop_button.grid(row=0, column=6)
#
# self.bar=tkinter.Scale(control2, from_=0, to=100, orient=tkinter.HORIZONTAL,showvalue=0,borderwidth=0.01,repeatinterval=0,tickinterval=25,font=('宋体',8),cursor='cross',
#                        sliderlength=13)
#
# self.bar.bind("<ButtonPress-1>",self.mouse_down)
# self.bar.bind("<ButtonRelease-1>",self.mouse_up)
# self.bar.bind('<B1-Motion> ',self.mouse_move)
# self.bar.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)
#
# video.pack(side=tkinter.TOP,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)
# control.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.NO,fill=tkinter.BOTH)
# self.hwnd = video.winfo_id()        #获得视频窗体的句柄