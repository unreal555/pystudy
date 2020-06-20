# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 23:07:01 2018
QQ群：476842922（欢迎加群讨论学习
@author: Administrator
"""
import wx

class MyFrame2 ( wx.Frame ):

    response = ""

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar3 = wx.MenuBar( 0 )
        self.m_menu6 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu6.Append( self.m_menuItem3 )

        self.m_menuItem4 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu6.Append( self.m_menuItem4 )

        self.m_menubar3.Append( self.m_menu6, u"File" )

        self.SetMenuBar( self.m_menubar3 )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,600 ), 0)
        self.m_textCtrl2.SetBackgroundColour('Black')
        self.m_textCtrl2.SetForegroundColour('Green')
        self.SetTransparent(200)
        bSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.open, id = self.m_menuItem3.GetId() )
        self.Bind( wx.EVT_MENU, self.save, id = self.m_menuItem4.GetId() )

    def __del__( self ):
        pass

    def save( self, event ):
        file=open("temFile.txt",'w')
        file.write(self.m_textCtrl2.GetValue())
        file.close()

    def open(self, event):
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*"
        dlg = wx.FileDialog(self, "Open XYZ file", wildcard="XYZ files (*.*)|*.*",style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.ReadFile()
            self.SetTitle(self.title + '--' + self.filename)
        dlg.Destroy()


def main():
    app = wx.App()
    ex = MyFrame2(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
