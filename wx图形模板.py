# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/28 0028 上午 9:49
# Tool ：PyCharm

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 23:07:01 2018
QQ群：476842922（欢迎加群讨论学习
@author: Administrator
"""
import wx

class Frame( wx.Frame ):
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

        self.SetMenuBar(self.file_menu_bar )

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



    def __del__( self ):

        pass


    def stop(self, event ):
        self.show.AppendText('stop click\r\n')
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
        self.show.AppendText('start click\r\n')

        # file=open(self.input.GetValue())  #特别注意，从输入框这么得到的字符串是unicode
        # s=file.read()
        # self.show.SetValue(s)
        # file.close()

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
