# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 23:07:01 2018
QQ群：476842922（欢迎加群讨论学习
@author: Administrator
"""
import wx
import time
from threading import Thread
import threading
from pubsub import pub
import shu_lian_wang


class MyWork(Thread):
    flag=True

    def __init__(self,parent=None):
        Thread.__init__(self)

    def run(self):
        self.do_work()

    def do_work(self):
        max=100
        count=1
        while True:
            if self.flag==True and count<max:
                time.sleep(1)
                pub.sendMessage("stat", msg=str(count)+'\r\n')
                count+=1
            else:
                time.sleep(1)
                continue

class Frame( wx.Frame ):
    mywork = MyWork()
    response = ""
    title = '图形界面框架模板'    #窗体名称
    size=wx.Size(500,300)    #尺寸
    Button1 = 'start'  # 第一个按钮名字
    Button2 = 'stop'  # 第二个按钮名字
    Button3 = 'Open'

    def __init__( self, parent ):

        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = self.title, pos = wx.DefaultPosition, size = self.size, style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.file_menu_bar = wx.MenuBar()
        self.file_menu = wx.Menu()
        self.open_Item = wx.MenuItem(self.file_menu, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
        self.file_menu.Append( self.open_Item )

        self.file_menu.AppendSeparator()

        self.stop_Item = wx.MenuItem( self.file_menu, wx.ID_ANY, u"stop", wx.EmptyString, wx.ITEM_NORMAL )
        self.file_menu.Append(self.stop_Item)

        self.file_menu_bar.Append( self.file_menu, u"File" )

        self.SetMenuBar( self.file_menu_bar )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.open, id = self.open_Item.GetId() )
        self.Bind( wx.EVT_MENU, self.stop, id = self.stop_Item.GetId() )

        self.bkg = wx.Panel(self)

        self.startButton = wx.Button(self.bkg, label=self.Button1)
        self.startButton.Bind(wx.EVT_BUTTON, self.start)  # 请修改触发事件和调用函数
        self.stopButton = wx.Button(self.bkg, label=self.Button2)
        self.stopButton.Bind(wx.EVT_BUTTON, self.stop)  # 请修改触发事件和调用函数
        self.openButton = wx.Button(self.bkg, label=self.Button3)
        self.openButton.Bind(wx.EVT_BUTTON, self.open)


        self.input = wx.TextCtrl( self.bkg, wx.ID_ANY,  value='c:\OnKeyDetector.log', style=wx.TE_PROCESS_ENTER)
        self.input.SetBackgroundColour('Black')
        self.input.SetForegroundColour('Green')
        self.input.Bind(wx.EVT_TEXT_ENTER, self.start)  # 当输入框检测到回车事件就调用函数start，必须和上面startButton一致

        self.show = wx.TextCtrl(self.bkg, value='', style=wx.TE_MULTILINE | wx.HSCROLL)  # value设置初始显示内容
        self.show.SetBackgroundColour('Black')
        self.show.SetForegroundColour('Green')

        self.SetTransparent(1000)

        self.hbox = wx.BoxSizer()
        self.hbox.Add(self.input, proportion=1, flag=wx.EXPAND)
        self.hbox.Add(self.startButton, proportion=0, flag=wx.LEFT, border=5)
        self.hbox.Add(self.stopButton, proportion=0, flag=wx.LEFT, border=5)
        self.hbox.Add(self.openButton, proportion=0, flag=wx.LEFT, border=5)

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        self.vbox.Add(self.show, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

        self.bkg.SetSizer(self.vbox)

        pub.subscribe(self.Listener_msg, 'stat')
        pub.subscribe(self.Listener_flag, 'flag')

    def __del__( self ):
        pass

    def stop(self, event ):
        print('stop print')
        pub.sendMessage("flag",flag='False'+'\r\n')
        # file=open("temFile.txt",'w')
        # file.write(self.show.GetValue())
        # file.close()

    def open(self, event):
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*"
        dlg = wx.FileDialog(self, "Open XYZ file", wildcard="XYZ files (*.*)|*.*",style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            print(self.filename)
            file=open(self.filename,'r',encoding='gbk')
            self.show.SetValue(file.read())
            self.SetTitle(self.title + '--' + self.filename)
        dlg.Destroy()

    def start(self,event):
        try:
            print('多线程')
            self.mywork.start()
        except RuntimeError as e:
            if self.mywork.flag==False:
                pub.sendMessage('stat', msg='继续' + '\r\n')
                self.mywork.flag=True
            else:
                pub.sendMessage('stat', msg='进程已启动,请勿重复点击'+'\r\n')



        # file=open(self.input.GetValue())  #特别注意，从输入框这么得到的字符串是unicode
        # s=file.read()
        # self.show.SetValue(s)
        # file.close()

    def Listener_msg(self,msg):
        self.show.AppendText(str(msg))

    def Listener_flag(self,flag):
        self.show.AppendText('停止进程\r\n')
        if 'False' in flag:
            self.mywork.flag=False


    def Quit(self,event):  # 菜单项绑定事件
        show.AppendText(">please\n")
        # exit()

    def OnExit(self,event):
        print('1')

def main():
    app = wx.App()
    win =Frame(None)
    win.Show()
    app.MainLoop()



if __name__ == '__main__':
    main()
