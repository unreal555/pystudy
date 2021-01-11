# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/1/11 0011 上午 8:07
# Tool ：PyCharm

import os
import ctypes
from ctypes import *



class DAHUA_DVR():
    lib_path='./dahua_dll'
    def __init__(self, sDVRIP, sDVRPort, sUserName, sPassword,lib_path=lib_path):

        self.dlls =self.Get_Dlls(lib_path)
        print('生成dll库完毕',self.dlls)
        self.NET_DVR_Init()
        # 用户注册设备
        # c++传递进去的是byte型数据，需要转成byte型传进去，否则会乱码
        sDVRPort=int(sDVRPort)
        self.sDVRIP = bytes(sDVRIP, "ascii")
        self.sUserName = bytes(sUserName, "ascii")
        self.sPassword = bytes(sPassword, "ascii")
        self.sDVRPort=sDVRPort
        self.DeviceInfo = NET_DVR_DEVICEINFO_V30()
        print("DVR参数初始化成功")
        self.lUserID = self.NET_DVR_Login()
        print('DVR初始化完毕,登录状态为:',self.lUserID)

    def Get_Last_Error(self):
        error_code = self.CallCpp("NET_DVR_GetLastError")
        #print('error code', error_code)
        return error_code

    def Get_Dlls(self,lib_path):
        pathss = []
        for root, dirs, files in os.walk(lib_path):
            for file in files:
                if '.dll' in str.lower(file):
                    pathss.append(os.path.join(lib_path, file))
        return pathss

    def CallCpp(self, func_name, *args):
        for HK_dll in self.dlls:
            try:
                lib = ctypes.cdll.LoadLibrary(HK_dll)
                try:
                    value = eval("lib.%s" % func_name)(*args)
                    print('命令为:', func_name, "    参数为:", str(args), " 调用的dll为:" + HK_dll, '  执行结果为:', value)
                    return value
                except:
                    continue
            except:
                print(HK_dll, '库文件载入失败')
                continue
        print("没有找到接口！")
        return False

    def NET_DVR_Init(self):
        init_res = self.CallCpp("NET_DVR_Init")  # SDK初始化
        print(init_res)
        if init_res:
            error_info = self.CallCpp("NET_DVR_GetLastError")
        else:
            error_info = self.CallCpp("NET_DVR_GetLastError")
            print("SDK初始化错误：" + str(error_info))
            return False
        set_overtime = self.CallCpp("NET_DVR_SetConnectTime", 5000, 4)  # 设置超时
        if set_overtime:
            print("设置超时时间成功")
        else:
            error_info = self.CallCpp("NET_DVR_GetLastError")
            print("设置超时错误信息：" + str(error_info))
            return False

        print("SDK初始化成功")
        return True

    def NET_DVR_Login(self):
        sDVRIP = self.sDVRIP
        sDVRPort = self.sDVRPort
        sUserName = self.sUserName
        sPassword = self.sPassword
        lUserID = self.CallCpp("NET_DVR_Login_V30", sDVRIP, sDVRPort, sUserName, sPassword, ctypes.byref(self.DeviceInfo))

        if lUserID == -1:
            error_info = self.CallCpp("NET_DVR_GetLastError")
            print("登录错误信息：" + str(error_info))
            return -1
        else:
            print("登录成功，用户ID：" + str(lUserID))
            return lUserID

    # 预览实现
    def Play_Cam(self,hwnd,channel):
        hwnd=int(hwnd)
        channel=int(channel)
        lpPreviewInfo = NET_DVR_PREVIEWINFO()
        # hPlayWnd需要输入创建图形窗口的handle,没有输入无法实现BMP抓图
        lpPreviewInfo.hPlayWnd = hwnd
        lpPreviewInfo.lChannel = channel
        lpPreviewInfo.dwLinkMode = 0
        lpPreviewInfo.sMultiCastIP = None
        lpPreviewInfo.bBlocked = 1
        lUserID = self.lUserID
        m_lRealHandle = self.CallCpp("NET_DVR_RealPlay_V40", lUserID, ctypes.byref(lpPreviewInfo), None, None)
        if (m_lRealHandle == -1):
            error_info = self.CallCpp("NET_DVR_GetLastError")
            print("预览失败：" + str(error_info))
            return -1
        else:
            print("预览成功")
        return m_lRealHandle

    def Stop_Play_Cam(self,lRealHandle):
        lRealHandle=int(lRealHandle)
        result=self.CallCpp('NET_DVR_StopRealPlay',c_long(lRealHandle))
        print(result)
        return result


    def GetServerInfo(self):
        info=str(self.sDVRIP)+':'+str(self.sUserName)+':'+str(self.sDVRPort)
        print(info)
        return info

    def Rec_Cam(self,lRealHandle,file):

        file=bytes(file,'utf-8')

        file=c_char_p(file)

        self.CallCpp('NET_DVR_SaveRealData', c_long(lRealHandle),file)

        self.Get_Last_Error()


    def Capture_Cam(self,lRealHandle,file):

        file=bytes(file,'utf-8')
        file=c_char_p(file)
        self.CallCpp('NET_DVR_CapturePicture', c_long(lRealHandle),file)
        self.Get_Last_Error()

    def Stop_Rec_Cam(self,lRealHandle,):
        self.CallCpp('NET_DVR_StopSaveRealData', c_long(lRealHandle))
        self.Get_Last_Error()


    def Close(self):
        self.CallCpp('NET_DVR_Logout', self.lUserID)
        self.Get_Last_Error()

        self.CallCpp('NET_DVR_Cleanup', self.lUserID)
        self.Get_Last_Error()

    def check_device_online(self):
        dwCommand=c_double(20005)
        dwCount=c_double(1)
        result=self.CallCpp('NET_DVR_RemoteControl',self.lUserID,20005,'','')
        if result==0:
            return False
        if result==1:
            return True

if __name__ == '__main__':
    import tkinter as tk
    window = tk.Tk()  # 创建窗口
    window.title("this is a test")  # 窗口标题
    window.geometry('500x900')  # 窗口大小，小写字母x
    video = tk.Frame(window, cursor='plus', bd=2, relief="sunken")
    video.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)  # 固定
    video1 = tk.Frame(window, cursor='plus', bd=2, relief="sunken")

    video1.pack(side=tk.TOP, anchor=tk.S, expand=tk.YES, fill=tk.BOTH)  # 固定

    hwnd1 = video.winfo_id()


    server1=HK_DVR( sDVRIP='47.92.89.1', sDVRPort=8001, sUserName='user1', sPassword='abcd1234')

    print(server1.GetServerInfo())
    print(server1.check_device_online())



    window.mainloop()







