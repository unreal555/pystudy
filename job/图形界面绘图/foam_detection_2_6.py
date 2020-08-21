# coding: utf-8
# Team : BSH LCDFR
# Author：XuChao, Shi,zhaolong
# Date ：2020/8/12 0027 上午 11:36
# Tool ：Anacoda Spider


import wx
import time
import matplotlib.pyplot as plt


class Frame(wx.Frame):
    title = 'foam detection tool'  # 窗体名称
    size = wx.Size(920, 100)  # 尺寸
    Button1 = '选择'  # 第一个按钮名字
    Button2 = '开始'  # 第一个按钮名字
    filename = r'C:\Users\Administrator\Desktop\data.txt'

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=self.title, pos=wx.DefaultPosition, size=self.size,
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.bkg = wx.Panel(self)

        self.SelectButton = wx.Button(self.bkg, label=self.Button1)
        self.SelectButton.Bind(wx.EVT_BUTTON, self.select)  # 请修改触发事件和调用函数

        self.StartButton = wx.Button(self.bkg, label=self.Button2)
        self.StartButton.Bind(wx.EVT_BUTTON, self.start)  # 请修改触发事件和调用函数

        self.input_file = wx.TextCtrl(self.bkg, wx.ID_ANY, value=self.filename, style=wx.TE_PROCESS_ENTER)
        self.input_file.SetBackgroundColour('Black')
        self.input_file.SetForegroundColour('Green')
        self.input_file.Bind(wx.EVT_TEXT_ENTER, self.start)  # 当输入框检测到回车事件就调用函数start，必须和上面startButton一致

        self.text_a = wx.StaticText(self.bkg, -1, "pressure interval time",
                (100, 10))

        self.input_a = wx.TextCtrl(self.bkg, wx.ID_ANY, value='', style=wx.TE_PROCESS_ENTER)
        self.input_a.SetBackgroundColour('Black')
        self.input_a.SetForegroundColour('Green')
        self.input_a.Bind(wx.EVT_TEXT_ENTER, self.start)  # 当输入框检测到回车事件就调用函数start，必须和上面startButton一致

        self.text_b = wx.StaticText(self.bkg, -1, "moving average",
                                    (110, 10))

        self.input_b = wx.TextCtrl(self.bkg, wx.ID_ANY, value='', style=wx.TE_PROCESS_ENTER)
        self.input_b.SetBackgroundColour('Black')
        self.input_b.SetForegroundColour('Green')
        self.input_b.Bind(wx.EVT_TEXT_ENTER, self.start)  # 当输入框检测到回车事件就调用函数start，必须和上面startButton一致

        self.text_c = wx.StaticText(self.bkg, -1, "Pressure delta time",
                                    (110, 10))
        self.input_c = wx.TextCtrl(self.bkg, wx.ID_ANY, value='', style=wx.TE_PROCESS_ENTER)
        self.input_c.SetBackgroundColour('Black')
        self.input_c.SetForegroundColour('Green')
        self.input_c.Bind(wx.EVT_TEXT_ENTER, self.start)  # 当输入框检测到回车事件就调用函数start，必须和上面startButton一致

        self.text_d = wx.StaticText(self.bkg, -1, "foam delta",
                                    (100, 10))
        self.input_d = wx.TextCtrl(self.bkg, wx.ID_ANY, value='', style=wx.TE_PROCESS_ENTER)
        self.input_d.SetBackgroundColour('Black')
        self.input_d.SetForegroundColour('Green')
        self.input_d.Bind(wx.EVT_TEXT_ENTER, self.start)  # 当输入框检测到回车事件就调用函数start，必须和上面startButton一致

        self.SetTransparent(1000)

        self.hbox = wx.BoxSizer()
        self.hbox.Add(self.input_file, proportion=1, flag=wx.EXPAND)
        self.hbox.Add(self.SelectButton, proportion=0, flag=wx.LEFT, border=1)

        self.bbox = wx.BoxSizer()
        self.bbox.Add(self.text_a, proportion=1, flag=wx.EXPAND)
        self.bbox.Add(self.input_a, proportion=1, flag=wx.EXPAND)
        self.bbox.Add(self.text_b, proportion=1, flag=wx.EXPAND)
        self.bbox.Add(self.input_b, proportion=1, flag=wx.EXPAND)
        self.bbox.Add(self.text_c, proportion=1, flag=wx.EXPAND)
        self.bbox.Add(self.input_c, proportion=1, flag=wx.EXPAND)
        self.bbox.Add(self.text_d, proportion=1, flag=wx.EXPAND)
        self.bbox.Add(self.input_d, proportion=1, flag=wx.EXPAND)
        self.bbox.Add(self.StartButton, proportion=0, flag=wx.LEFT, border=1)

        self.vbox = wx.BoxSizer(wx.VERTICAL)

        self.vbox.Add(self.hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        self.vbox.Add(self.bbox, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

        self.bkg.SetSizer(self.vbox)

    def __del__(self):

        pass

    def select(self, event):
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*"
        dlg = wx.FileDialog(self, "open file", wildcard="files (*.*)|*.*", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.input_file.SetValue(self.filename)
        dlg.Destroy()

    def start(self, event):
        result = []
        if self.filename and self.input_a and self.input_b and self.input_c and self.input_d:
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = f.readlines()
                a = int(self.input_a.Value)
                b = int(self.input_b.Value)
                c = int(self.input_c.Value)
                f = int(c/a)
                d = float(self.input_d.Value)
                count = 0
                dic = {}

                for x in data:
                    tmp = x.split(" ")
                    tmp1 = str(tmp[0])
                    tmp2 = str(tmp[1]).replace("\n", "")
                    dic[int(tmp1)] = float(tmp2)
                    count += 1
                i = 0
                j = 0
                while i < count:
                    tmp = i
                    i += 1
                    num = dic[tmp]
                    j = 0
                    while j < b:
                        j += 1
                        tmp += a
                        if (tmp < count):
                            num += dic[tmp]
                    num = num * 1.0 / b
                    result.append(num)

               # 获取 第 k+f 个 平均值 与 第 k 个平均值的差值
                k=0
                #t=0
                #f2=open('\\naawfs01\data\PLC-DE\10_LCDF\0200-Projects\06-Siena\Siena_working_folders\05 - Test planning\14.4_process and features\Foam\Foam treatment while washing\FSD21_data analysis new foam detection washing\foam analysis result.txt','r+')
                while ((k+f)<len(result)):
                    avg = result[k+f]-result[k]
                    if (avg >= d):
                        break
                        #t=t+1
                        #m = '\n'+str(k)+' '+str(result[k])	#确定写入参数
                        #f2.write(m) #写入参数至txt  
                    k=k+1
                #f2.close()
                
            except Exception as e:
                dlg = wx.MessageDialog(None, str(e), u"错误,请检查输入参数", wx.OK)
                dlg.ShowModal()
            self.draw(result)
            
            #数据分析结束后，弹出结果对话窗口
            if (avg >= d):
                dlg = wx.MessageDialog(None, r"P_ist 数据在{}处存在高泡事件".format(k), u"P_ist数据显示存在高泡",wx.OK)
            else:
                dlg = wx.MessageDialog(None, r"P_ist 数据存在{}次高泡事件".format(0), u"P_ist数据显示不存在高泡",wx.OK)
            dlg.ShowModal()

    def draw(self, data):
        fig = plt.figure(figsize=(18, 10), dpi=100)
        plt.plot(data)
        plt.show()

def main():
    app = wx.App()
    win = Frame(None)
    win.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()



