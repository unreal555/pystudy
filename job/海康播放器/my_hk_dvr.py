# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/10/12 0012 下午 4:09
# Tool ：PyCharm


import os
import ctypes
from ctypes import *

class NET_DVR_PREVIEWINFO(ctypes.Structure):
    _fields_ = [
        # 通道号，目前设备模拟通道号从1开始，数字通道的起始通道号通过
        # NET_DVR_GetDVRConfig(配置命令NET_DVR_GET_IPPARACFG_V40)获取（dwStartDChan）
        ('lChannel', c_long),
        # 码流类型：0-主码流，1-子码流，2-三码流，3-虚拟码流，以此类推
        ('dwStreamType', c_ulong),
        # 连接方式：0-TCP方式，1-UDP方式，2-多播方式，3-RTP方式，4-RTP/RTSP，5-RTP/HTTP,6-HRUDP（可靠传输）
        ('dwLinkMode', c_ulong),
        # 播放窗口的句柄，为NULL表示不解码显示
        ('hPlayWnd', c_void_p),
        # 0-非阻塞取流，1- 阻塞取流
        # 若设为不阻塞，表示发起与设备的连接就认为连接成功，如果发生码流接收失败、播放失败等
        # 情况以预览异常的方式通知上层。在循环播放的时候可以减短停顿的时间，与NET_DVR_RealPlay
        # 处理一致。
        # 若设为阻塞，表示直到播放操作完成才返回成功与否，网络异常时SDK内部connect失败将会有5s
        # 的超时才能够返回，不适合于轮询取流操作。
        ('bBlocked', c_bool),
        # 是否启用录像回传： 0-不启用录像回传，1-启用录像回传。ANR断网补录功能，
        # 客户端和设备之间网络异常恢复之后自动将前端数据同步过来，需要设备支持。
        ('bPassbackRecord', c_bool),
        # 延迟预览模式：0-正常预览，1-延迟预览
        ('byPreviewMode', c_byte),
        # 流ID，为字母、数字和"_"的组合，IChannel为0xffffffff时启用此参数
        ('byStreamID', c_byte * 32),
        # 应用层取流协议：0-私有协议，1-RTSP协议。
        # 主子码流支持的取流协议通过登录返回结构参数NET_DVR_DEVICEINFO_V30的byMainProto、bySubProto值得知。
        # 设备同时支持私协议和RTSP协议时，该参数才有效，默认使用私有协议，可选RTSP协议。
        ('byProtoType', c_byte),
        # 保留，置为0
        ('byRes1', c_byte),
        # 码流数据编解码类型：0-通用编码数据，1-热成像探测器产生的原始数据
        # （温度数据的加密信息，通过去加密运算，将原始数据算出真实的温度值）
        ('byVideoCodingType', c_byte),
        # 播放库播放缓冲区最大缓冲帧数，取值范围：1、6（默认，自适应播放模式）   15:置0时默认为1
        ('dwDisplayBufNum', c_ulong),
        # 保留，置为0
        ('byRes', c_byte * 216),
    ]

class NET_DVR_DEVICEINFO_V30(ctypes.Structure):
    _fields_ = [
        ("sSerialNumber", c_byte * 48),  # 序列号
        ("byAlarmInPortNum", c_byte),  # 模拟报警输入个数
        ("byAlarmOutPortNum", c_byte),  # 模拟报警输出个数
        ("byDiskNum", c_byte),  # 硬盘个数
        ("byDVRType", c_byte),  # 设备类型，详见下文列表
        ("byChanNum", c_byte),
        ("byStartChan", c_byte),
        ("byAudioChanNum", c_byte),  # 设备语音对讲通道数
        ("byIPChanNum", c_byte),
        ("byZeroChanNum", c_byte),  # 零通道编码个数
        ("byMainProto", c_byte),  # 主码流传输协议类型：
        ("bySubProto", c_byte),  # 字码流传输协议类型：
        ("bySupport", c_byte),
        ("bySupport1", c_byte),
        ("bySupport2", c_byte),
        ("wDevType", c_uint16),  # 设备型号，详见下文列表
        ("bySupport3", c_byte),
        ("byMultiStreamProto", c_byte),
        ("byStartDChan", c_byte),  # 起始数字通道号，0表示无数字通道，比如DVR或IPC
        ("byStartDTalkChan", c_byte),
        ("byHighDChanNum", c_byte),  # 数字通道个数，高8位
        ("bySupport4", c_byte),
        ("byLanguageType", c_byte),
        ("byVoiceInChanNum", c_byte),  # 音频输入通道数
        ("byStartVoiceInChanNo", c_byte),  # 音频输入起始通道号，0表示无效
        ("bySupport5", c_byte),
        ("bySupport6", c_byte),
        ("byMirrorChanNum", c_byte),  # 镜像通道个数，录播主机中用于表示导播通道
        ("wStartMirrorChanNo", c_uint16),
        ("bySupport7", c_byte),
        ("byRes2", c_byte)]  # 保留，置为0

class NET_DVR_DEVICEINFO_V40(Structure):
    _fields_ = [
        # struDeviceV30结构体中包括接口体，我们只需要额外定义一下该子结构体即可
        ("struDeviceV30", NET_DVR_DEVICEINFO_V30),
        ("bySupportLock", c_byte),  # 设备是否支持锁定功能，bySupportLock为1时，dwSurplusLockTime和byRetryLoginTime有效
        ("byRetryLoginTime", c_byte),
        ("byPasswordLevel", c_byte),
        ("byProxyType", c_byte),
        ("dwSurplusLockTime", c_ulong),
        ("byCharEncodeType", c_byte),
        ("bySupportDev5", c_byte),
        ("bySupport", c_byte),
        ("byLoginMode", c_byte),
        ("dwOEMCode", c_ulong),
        ("iResidualValidity", c_int),
        ("byResidualValidity", c_byte),
        ("bySingleStartDTalkChan", c_byte),
        ("bySingleDTalkChanNums", c_byte),
        ("byPassWordResetLevel", c_byte),
        ("bySupportStreamEncrypt", c_byte),
        ("byMarketType", c_byte),
        ("byRes2", c_byte * 253),
    ]

class NET_DVR_USER_LOGIN_INFO(Structure):
    _fields_ = [
        ("sDeviceAddress", c_char * 129),
        ("byUseTransport", c_byte),
        ("wPort", c_uint16),
        ("sUserName", c_char * 64),
        ("sPassword", c_char * 64),
        ("bUseAsynLogin", c_int),
        ("byProxyType", c_byte),
        ("byUseUTCTime", c_byte),
        ("byLoginMode", c_byte),
        ("byHttps", c_byte),
        ("iProxyID", c_long),
        ("byVerifyMode", c_byte),
        ("byRes3", c_byte * 120)
    ]

class HK_DVR():
    lib_path='./hk_dll'
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
            print("登录成功，用户ID：" + str(lUserID),'注意海康设备登陆,返回-1为失败,大于等于零值都为成功')
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
            return 'shibai'
        else:
            print("预览成功")
            return m_lRealHandle

    def Stop_Play_Cam(self,lRealHandle):
        lRealHandle=int(lRealHandle)
        result=self.CallCpp('NET_DVR_StopRealPlay',c_long(lRealHandle))
        print(result)
        return result


    def GetServerInfo(self):
        info=str('HAIKANG:'+self.sDVRIP)+':'+str(self.sUserName)+':'+str(self.sDVRPort)
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







