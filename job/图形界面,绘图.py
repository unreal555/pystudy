# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/27 0027 上午 11:36
# Tool ：PyCharm


import wx,os
import matplotlib.pyplot as plt
print(os.path.abspath('.'))


class Frame( wx.Frame ):

    title = 'wx'    #窗体名称
    size=wx.Size(600,150)    #尺寸
    Button1 = '选择'  # 第一个按钮名字
    Button2 = '开始'  # 第一个按钮名字
    filename=r'data.txt'



    def __init__( self, parent ):

        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = self.title, pos = wx.DefaultPosition, size = self.size, style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.bkg = wx.Panel(self)

        self.SelectButton = wx.Button(self.bkg, label=self.Button1)
        self.SelectButton.Bind(wx.EVT_BUTTON, self.select)  # 请修改触发事件和调用函数

        self.StartButton = wx.Button(self.bkg, label=self.Button2)
        self.StartButton.Bind(wx.EVT_BUTTON, self.start)  # 请修改触发事件和调用函数

        self.input_file = wx.TextCtrl( self.bkg, wx.ID_ANY,  value=self.filename, style=wx.TE_PROCESS_ENTER)
        self.input_file.SetBackgroundColour('Black')
        self.input_file.SetForegroundColour('Green')
        self.input_file.Bind(wx.EVT_TEXT_ENTER, self.start)  # 当输入框检测到回车事件就调用函数start，必须和上面startButton一致

        self.input_a = wx.TextCtrl( self.bkg, wx.ID_ANY,  value='A', style=wx.TE_PROCESS_ENTER)
        self.input_a.SetBackgroundColour('Black')
        self.input_a.SetForegroundColour('Green')
        self.input_a.Bind(wx.EVT_TEXT_ENTER, self.start)  # 当输入框检测到回车事件就调用函数start，必须和上面startButton一致

        self.input_b= wx.TextCtrl( self.bkg, wx.ID_ANY,  value='B', style=wx.TE_PROCESS_ENTER)
        self.input_b.SetBackgroundColour('Black')
        self.input_b.SetForegroundColour('Green')
        self.input_b.Bind(wx.EVT_TEXT_ENTER, self.start)  # 当输入框检测到回车事件就调用函数start，必须和上面startButton一致

        self.input_c = wx.TextCtrl( self.bkg, wx.ID_ANY,  value='C', style=wx.TE_PROCESS_ENTER)
        self.input_c.SetBackgroundColour('Black')
        self.input_c.SetForegroundColour('Green')
        self.input_c.Bind(wx.EVT_TEXT_ENTER, self.start)  # 当输入框检测到回车事件就调用函数start，必须和上面startButton一致

        self.input_d = wx.TextCtrl(self.bkg, wx.ID_ANY, value='D', style=wx.TE_PROCESS_ENTER)
        self.input_d.SetBackgroundColour('Black')
        self.input_d.SetForegroundColour('Green')
        self.input_d.Bind(wx.EVT_TEXT_ENTER, self.start)  # 当输入框检测到回车事件就调用函数start，必须和上面startButton一致




        self.SetTransparent(1000)

        self.hbox = wx.BoxSizer()
        self.hbox.Add(self.input_file, proportion=1, flag=wx.EXPAND)
        self.hbox.Add(self.SelectButton, proportion=0, flag=wx.LEFT, border=1)

        self.bbox = wx.BoxSizer()
        self.bbox.Add(self.input_a, proportion=1, flag=wx.EXPAND)
        self.bbox.Add(self.input_b, proportion=1, flag=wx.EXPAND)
        self.bbox.Add(self.input_c, proportion=1, flag=wx.EXPAND)
        self.bbox.Add(self.input_d, proportion=1, flag=wx.EXPAND)
        self.bbox.Add(self.StartButton, proportion=0, flag=wx.LEFT, border=1)



        self.vbox = wx.BoxSizer(wx.VERTICAL)

        self.vbox.Add(self.hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        self.vbox.Add(self.bbox, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)


        self.bkg.SetSizer(self.vbox)



    def __del__( self ):

        pass


    def select(self, event):
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*"
        dlg = wx.FileDialog(self, "open file", wildcard="files (*.*)|*.*",style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.input_file.SetValue(self.filename)
        dlg.Destroy()

    def start(self,event):
        if self.filename and self.input_a and self.input_b and self.input_c and self.input_d:
            try :
                with open(self.filename,'r',encoding='utf-8') as f:
                    data=f.readlines()
                data=[int(x) for x in data]
                a=int(self.input_a.Value)
                b = int(self.input_b.Value)
                c = int(self.input_c.Value)
                d = int(self.input_d.Value)

                dlg = wx.MessageDialog(None,r"读取数据{}行,读取参数abcd分别为{},{},{},{}".format(len(data), a, b, c, d), u"数据获取成功", wx.OK)
                dlg.ShowModal()
            except Exception as e:
                dlg = wx.MessageDialog(None, str(e), u"错误,请检查输入参数", wx.OK)
                dlg.ShowModal()
            if len(data)<1:
                dlg = wx.MessageDialog(None, '数据量错误','', u"数据错误", wx.OK)
                dlg.ShowModal()
            else:
                self.draw(data)



    def draw(self,data):
        fig = plt.figure(figsize=(18, 10))#, dpi=100)
        plt.plot(data)
        plt.show()





def main():
    app = wx.App()
    win =Frame(None)
    win.Show()
    app.MainLoop()



if __name__ == '__main__':
    main()

