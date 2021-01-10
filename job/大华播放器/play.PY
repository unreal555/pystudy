from  tkinter import *
from tkinter.messagebox import *
import tkinter 
import ctypes
from ctypes import *
import time
import os
from tkinter.filedialog import askopenfilename


#tkinter.messagebox.showinfo("源目录错误", "{}不是目录,或者目录不存在,请重新输入".format(source))
class myapp():


    dll = ctypes.windll.LoadLibrary('./dhplay.dll')  # 加载动态库为dh

    nPort=None
    # nPort=get_nPort(dll)
    root=Tk()
    hwnd=''
    bar=''

    drag_flag=True

    def get_nPort(self):
        port = c_long()  # 定义视频通道类型
        nPort = c_long(self.dll.PLAY_GetFreePort(byref(port)))  # 调用函数获得视频通道编号
        return nPort

    def __del__(self):
        self.dll.PLAY_Stop(self.nPort)
        self.dll.PLAY_CloseFile(self.nPort)
        self.dll.PLAY_ReleasePort(self.nPort)
        self.nPort=0
        self.bar=0
        self.hwnd=0
        self.drag_flag=0
        self.dll=0
        self.root=0
        del self.bar
        del self.hwnd
        del self.drag_flag
        del self.dll
        del self.root

    def openfile(self):

        file =  askopenfilename()
        temp,ext=os.path.splitext(file)
        print(file)
        if file=='':
            return 0

        if str.lower(ext)!='.dav':
            showinfo('注意','应该为.dav文件')
            return 0
        file=file.encode('gbk')
        file = ctypes.c_char_p(file)  # 转换文件地址为c字符指针类型
        if self.nPort==None:
            self.nPort = self.get_nPort()
        self.dll.PLAY_OpenFile(self.nPort,file)
        self.dll.PLAY_Play(self.nPort, self.hwnd)
        self.dll.PLAY_PlaySound(self.nPort)
        print(self.dll.PLAY_GetLastErrorEx(self.nPort))

    def get_pos(self):

        try:
            full=self.dll.PLAY_GetFileTime(self.nPort)

            past=self.dll.PLAY_GetPlayedTime(self.nPort)

            if full>0 and past>0:
                pos=int(past/full*100)
                return pos

            else:
                return 0


        except Exception as e:
            print(e)
            return 0

    def refresh_data(self):
        # 需要刷新数据的操作
        # 代码...
        pos=self.get_pos()

        if isinstance(pos,int) and self.drag_flag==True:
            self.bar.set(pos)
            # self.value=pos

        self.root.after(10, self.refresh_data )   # 这里的10000单位为毫秒

    def mouse_down(self,event):
        self.drag_flag=False

    def mouse_move(self,event):
        pos=self.bar.get()/100
        print(pos)
        self.dll.PLAY_SetPlayPos(self.nPort, ctypes.c_float(pos))

    def mouse_up(self,event):
        self.drag_flag=True

    def stop(self):

        self.dll.PLAY_Stop(self.nPort)
        self.dll.PLAY_CloseFile(self.nPort)
        self.dll.PLAY_ReleasePort(self.nPort)
        self.nPort=None

    def play(self):
        self.dll.PLAY_Play(self.nPort,self.hwnd)

    def play_fast(self):
        self.dll.PLAY_Fast(self.nPort)

    def pause(self):
        self.dll.PLAY_Pause(self.nPort,ctypes.c_bool(TRUE))

    def onebyone(self):
        self.dll.PLAY_OneByOne(self.nPort)

    def catchpic(self):
        filename=str(time.time())+'.bmp'
        dir=os.path.abspath('.')
        dir=os.path.join(dir,'catch')
        if not os.path.exists(dir):
            os.makedirs(dir)
        path=os.path.join(dir,filename)
        path=path.encode('gbk')
        path=ctypes.c_char_p(path)
        self.dll.PLAY_CatchPic(self.nPort,path)
        print(self.dll.PLAY_GetLastErrorEx(self.nPort))

    def __init__(self):

                                       #定义图形界面
        self.root.title('dhplay')
        self.root['bg'] = '#bcbcbc'
        # self.root.attributes("-alpha", 0.9)

        self.root.geometry("800x600")


        video = tkinter.Frame(self.root,bg='#bcbcbc')             #定义视频播放窗体

        control=tkinter.Frame(self.root)

        control1=tkinter.Frame(control)
        control2=tkinter.Frame(control)

        control1.pack(side=tkinter.LEFT,anchor=tkinter.S,expand=tkinter.NO,fill=tkinter.BOTH)
        control2.pack(side=tkinter.RIGHT,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)


        open_button=tkinter.Button(control1,text='打开',command=self.openfile)

        play_button=tkinter.Button(control1,text='播放',command=self.play)

        speedup_button=tkinter.Button(control1,text='加速',command=self.play_fast)

        # pause_button=tkinter.Button(control1,text='暂停',command=self.pause)

        onebyone_button=tkinter.Button(control1,text='单帧',command=self.onebyone)

        catchpic_button = tkinter.Button(control1, text='截图', command=self.catchpic)

        stop_button=tkinter.Button(control1,text='停止',command=self.stop)



        open_button.grid(row=0, column=0)
        play_button.grid(row=0, column=1)
        speedup_button.grid(row=0, column=2)
        # pause_button.grid(row=0, column=3)
        onebyone_button.grid(row=0, column=4)
        catchpic_button.grid(row=0, column=5)
        stop_button.grid(row=0, column=6)

        self.bar=tkinter.Scale(control2, from_=0, to=100, orient=tkinter.HORIZONTAL,showvalue=0,borderwidth=0.01,repeatinterval=0,tickinterval=25,font=('宋体',8),cursor='cross',
                               sliderlength=13)

        self.bar.bind("<ButtonPress-1>",self.mouse_down)
        self.bar.bind("<ButtonRelease-1>",self.mouse_up)
        self.bar.bind('<B1-Motion> ',self.mouse_move)
        self.bar.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)


        video.pack(side=tkinter.TOP,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)
        control.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.NO,fill=tkinter.BOTH)
        self.hwnd = video.winfo_id()        #获得视频窗体的句柄

        self.refresh_data()

        self.root.mainloop()

app=myapp()




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
