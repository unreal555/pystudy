# -*- coding: cp936 -*-
#����������Ҫ����һ����ʹ�ã�ʹ�÷������Ǹ���ע���Զ��������ʽ
#ע�Ȿ�����Ƴ��ĵ��Ű��Ѿ��̶�
"""-----------------------------------------------------------------"""
#���������������¼�����Ҫʹ�õ���ģ��
import wx
#�����޸ĵ����� ���������

#��������
title='Application'#������Ķ�����������
size=(410,335)#�������ڳߴ磨�����ߣ�
Button1='Open'#��һ����ť����
Button2='Save'#�ڶ�����ť����

def load(event):
    file=open(input1.GetValue())  #�ر�ע�⣬���������ô�õ����ַ�����unicode
    show.SetValue(file.read())
    file.close()

def save(event):
    file=open(input1,GetValue(),'w')
    file.write(show.GetValue())
    file.close()

def Quit(event):#�˵�����¼�
    show.AppendText(">please\n")
    exit()

app=wx.App()
win=wx.Frame(None,title=title,size=size)
win.SetPosition((450,150))#���ô��ڴ򿪺�����Ļ��λ��

menubar = wx.MenuBar()
##���￪ʼ����һ��
filemenu = wx.Menu()
###���￪ʼ����һ���˵�����������һ��
qmi = wx.MenuItem(filemenu,2, "Quit")#�޸�����
omi=wx.MenuItem(filemenu,1,'Open')


filemenu.Append(omi)
filemenu.AppendSeparator()
filemenu.Append(qmi)


menubar.Append(filemenu, "File")#�޸�����

win.SetMenuBar(menubar)
#��id=1������¼�
win.Bind(wx.EVT_MENU, Quit, id=2) #�޸Ĵ����¼��͵��ú�����ע��Quit���ֳ��˺���������Բ��ܳ������κεط�

bkg=wx.Panel(win)



loadButton=wx.Button(bkg,label=Button1)
loadButton.Bind(wx.EVT_BUTTON,load)            #���޸Ĵ����¼��͵��ú���
saveButton=wx.Button(bkg,label=Button2)
saveButton.Bind(wx.EVT_BUTTON,save)          #���޸Ĵ����¼��͵��ú���

input1 = wx.TextCtrl(bkg,style=wx.TE_PROCESS_ENTER)
input1.Bind(wx.EVT_TEXT_ENTER,load)#��������⵽�س��¼��͵��ú���load�����������loadButtonһ��
show=wx.TextCtrl(bkg,value='',style=wx.TE_MULTILINE | wx.HSCROLL)#value���ó�ʼ��ʾ����

#����
hbox=wx.BoxSizer()
hbox.Add(input1,proportion=1,flag=wx.EXPAND)
hbox.Add(loadButton,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND | wx.ALL,border=5)
vbox.Add(show,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,border=5)

bkg.SetSizer(vbox)

win.Show()

app.MainLoop()