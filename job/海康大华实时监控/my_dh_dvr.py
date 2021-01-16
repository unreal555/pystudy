# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2021/1/11 0011 上午 8:07
# Tool ：PyCharm

import os
from ctypes import *
from NetSDK.NetSDK import NetClient
from NetSDK.SDK_Callback import fDisConnect, fHaveReConnect, fDecCBFun, fRealDataCallBackEx2
from NetSDK.SDK_Enum import SDK_RealPlayType, EM_LOGIN_SPAC_CAP_TYPE, EM_REALDATA_FLAG, EM_DEV_CFG_TYPE
from NetSDK.SDK_Struct import C_LLONG, NET_TIME, sys_platform, NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY, \
	NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY, PLAY_FRAME_INFO


class DAHUA_DVR():
	lib_path = './dahua_dll'

	def __init__(self, sDVRIP, sDVRPort, sUserName, sPassword, lib_path=lib_path):

		self.sDVRIP = sDVRIP
		self.sDVRPort = sDVRPort
		self.sUserName = sUserName
		self.sPassword = sPassword

		self.lUserID = 0
		self.m_DisConnectCallBack = fDisConnect(self.DisConnectCallBack)
		self.m_ReConnectCallBack = fHaveReConnect(self.ReConnectCallBack)

		# 获取NetSDK对象并初始化
		self.sdk = NetClient()
		self.sdk.InitEx(self.m_DisConnectCallBack)
		self.sdk.SetAutoReconnect(self.m_ReConnectCallBack)

		self.stuInParam = NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY()
		self.stuInParam.dwSize = sizeof(NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY)
		self.stuInParam.szIP = sDVRIP.encode()
		self.stuInParam.nPort = int(sDVRPort)
		self.stuInParam.szUserName = sUserName.encode()
		self.stuInParam.szPassword = sPassword.encode()
		self.stuInParam.emSpecCap = EM_LOGIN_SPAC_CAP_TYPE.TCP
		self.stuInParam.pCapParam = None

		self.stuOutParam = NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY()
		self.stuOutParam.dwSize = sizeof(NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY)

		print("DVR参数初始化成功")

		self.lUserID = self.NET_DVR_Login()

		print('大华DVR初始化完毕,登录状态为:', self.lUserID, '注意大华设备登陆,返回0为失败,正负值都为成功')

	def DisConnectCallBack(self):
		pass

	def ReConnectCallBack(self):
		pass

	def CaptureCallBack(lLoginID, pBuf, RevLen, EncodeType, CmdSerial, dwUser):
		if lLoginID == 0:
			return
		print('Enter CaptureCallBack')

	# 拉流回调函数功能
	def RealDataCallBack(self, lRealHandle, dwDataType, pBuffer, dwBufSize, param, dwUser):
		if lRealHandle == self.playID:
			data_buffer = cast(pBuffer, POINTER(c_ubyte * dwBufSize)).contents
			with open('./data.dav', 'ab+') as data_file:
				data_file.write(data_buffer)
			self.sdk.InputData(self.freePort, pBuffer, dwBufSize)

	# PLAYSDK解码回调函数功能
	def DecodingCallBack(self, nPort, pBuf, nSize, pFrameInfo, pUserData, nReserved2):
		# here get YUV data, pBuf is YUV data IYUV/YUV420 ,size is nSize, pFrameInfo is frame info with height, width.
		data = cast(pBuf, POINTER(c_ubyte * nSize)).contents
		info = pFrameInfo.contents
		# info.nType == 3 is YUV data,others ard audio data.
		# you can parse YUV420 data to RGB
		if info.nType == 3:
			pass

	def NET_DVR_Login(self):

		if not self.lUserID:
			lUserID, device_info, error_msg = self.sdk.LoginWithHighLevelSecurity(self.stuInParam, self.stuOutParam)
			if lUserID != 0:
				self.device_info = device_info
				for i in range(int(device_info.nChanNum)):
					print('lUserID,channle', lUserID, i)
				return lUserID
			else:
				print('登陆失败,', device_info)
				return None
		else:
			result = self.sdk.Logout(self.lUserID)
			if result:
				self.lUserID = None

	# 预览实现
	def Play_Cam(self, hwnd, channel):
		hwnd = int(hwnd)
		channel = int(channel)
		stream_type = SDK_RealPlayType.Realplay_1
		m_lRealHandle = self.sdk.RealPlayEx(self.lUserID, channel, int(hwnd), stream_type)
		if (m_lRealHandle == 0):
			error_info = self.GetServerInfo()
			print("预览失败：" + str(error_info))
			return 'shibai'
		else:
			print("预览成功")
			return m_lRealHandle

	def Get_Last_Error(self):
		error_code = self.sdk.GetLastErrorMessage()
		# print('error code', error_code)
		return error_code

	def Stop_Play_Cam(self, lRealHandle):
		if lRealHandle:
			result = self.sdk.StopRealPlayEx(lRealHandle)
		if result == 1:
			print('dahua cam 停止成功')
			return True
		else:
			print('dahua cam 停止失败')
			return False

	def GetServerInfo(self):
		info = str('dahua:' + self.sDVRIP) + ':' + str(self.sUserName) + ':' + str(self.sDVRPort)
		print(info)
		return info

	def Rec_Cam(self, lRealHandle, file):

		file = bytes(file, 'utf-8')

		file = c_char_p(file)

	def Capture_Cam(self, lUserID, channel):
		dwUser = 0
		self.sdk.SetSnapRevCallBack(self.CaptureCallBack, dwUser)
		channel = int(channel)
		snap = SNAP_PARAMS()
		snap.Channel = channel
		snap.Quality = 1
		snap.mode = 0
		# 抓图
		self.sdk.SnapPictureEx(lUserID, snap)

	def Stop_Rec_Cam(self, lRealHandle, ):
		pass

	def Close(self):
		print(self.lUserID)
		if self.lUserID != 0 and self.lUserID != None:
			self.sdk.Logout(self.lUserID)
		self.sdk.Cleanup()

	def check_device_online(self):
		if self.lUserID == None:
			self.lUserID = self.NET_DVR_Login()
			if self.lUserID == None:
				return False
			else:
				return True
		else:
			time = NET_TIME()
			print(self.lUserID, int(EM_DEV_CFG_TYPE.TIMECFG), -1, time, sizeof(NET_TIME))
			result = self.sdk.GetDevConfig(int(self.lUserID), int(EM_DEV_CFG_TYPE.TIMECFG), -1, time, sizeof(NET_TIME))
			print(result)
			if not result:
				print(self.sdk.GetLastErrorMessage())
			else:
				print(result)

			if result == 0:
				return False
			if result == 1:
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
	server1 = DAHUA_DVR(sDVRIP='47.92.89.1', sDVRPort=8101, sUserName='admin', sPassword='abcd1234')
	server1.GetServerInfo()
	server1.check_device_online()
	server1.Play_Cam(hwnd1, 0)
	window.mainloop()
