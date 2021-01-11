from ctypes import *
from .SDK_Struct import DEVICE_NET_INFO_EX, DEVICE_NET_INFO_EX2, NET_RECORDFILE_INFO, C_LLONG, C_LDWORD, C_DWORD, CB_FUNCTYPE, PLAY_FRAME_INFO


# 断线回调函数;Network disconnection callback function
# 参数列表(param list)：
#     lLoginID:登录句柄; Login handle
#     pchDVRIP:IP地址;IP address
#     nDVRPort:端口号;Port
#     dwUser:用户数据;user data
fDisConnect = CB_FUNCTYPE(None, C_LLONG, c_char_p, c_long, C_LDWORD)

# 断线重连回调函数;network re-connection callback function
# 参数列表(param list)：
#     lLoginID:登录句柄; Login handle
#     pchDVRIP:IP地址;IP address
#     nDVRPort:端口号;Port
#     dwUser:用户数据;user data
fHaveReConnect = CB_FUNCTYPE(None, C_LLONG, c_char_p, c_long, C_LDWORD)

# SDK日志回调函数;SDK log callback
# 参数列表(param list)：
#     szLogBuffer:日志缓冲;log buffer
#     nLogSize:日志长度;log size
#     dwUser:用户数据;user data
fSDKLogCallBack = CB_FUNCTYPE(c_int, c_char_p, c_uint, C_LDWORD)

# 异步搜索设备回调函数;Asynchronism search device call
# 参数列表(param list):
#     lSearchHandle：搜索句柄;Search device handle
#     pDevNetInfo:设备信息;Device info
#     pUserData:用户数据信息;User data
fSearchDevicesCBEx = CB_FUNCTYPE(None, C_LLONG, POINTER(DEVICE_NET_INFO_EX2), c_void_p)

# 搜索设备回调函数;Asynchronism search device call
# 参数列表(param list):
#     pDevNetInfo:设备信息;Device info
#     pUserData:用户数据信息;User data
fSearchDevicesCB = CB_FUNCTYPE(None, POINTER(DEVICE_NET_INFO_EX), c_void_p)


# 智能分析数据回调; # intelligent analysis data callback
# 参数列表(param list):
#     lAnalyzerHandle：RealLoadPictureEx接口返回的句柄; handle of RealLoadPictureEx return
#     dwAlarmType:EM_EVENT_IVS_TYPE事件类型; EM_EVENT_IVS_TYPE event type
#     pAlarmInfo:事件信息; event information
#     pBuffer:图片数据缓存; picture buffer
#     dwBufSize:图片数据缓存大小; picture buffer size
#     dwUser:RealLoadPictureEx输入的用户数据信息; user data from RealLoadPictureEx function
#     nSequence:表示上传的相同图片情况,为0时表示是第一次出现,为2表示最后一次出现或仅出现一次,为1表示此次之后还有; instruct the repeat picture's station,0 instruct the first time it appear, 2 instruct the last time it appear or it only appear once,1 instruct it will appear next time
#     reserved:int nState = (int)reserved 表示当前回调数据的状态, 为0表示当前数据为实时数据,为1表示当前回调数据是离线数据,为2时表示离线数据传送结束; int nState = (int) reserved means current callback data status;when it is 1, it means current data is real time and current callback data is offline;when it is 2,it means offline data send structure
fAnalyzerDataCallBack = CB_FUNCTYPE(None, C_LLONG, C_DWORD, c_void_p, POINTER(c_ubyte), C_DWORD, C_LDWORD, c_int, c_void_p)

# 抓图回调函数原形(pBuf内存由SDK内部申请释放) ；Snapshot callback function original shape
# 参数列表(param list):
#     lLoginID：登录句柄; Login handle
#     pBuf:图片缓存；picture data buffer
#     RevLen:图片大小；picture len
#     EncodeType:编码类型，10：表示jpeg图片 0：mpeg4的i帧；Encode type,10: jpeg 0: number i frame of mpeg4
#     CmdSerial:请求填的序号；Serial
#     dwUser:SetSnapRevCallBack接口输入的用户数据信息; user data from SetSnapRevCallBack function
fSnapRev = CB_FUNCTYPE(None, C_LLONG, POINTER(c_ubyte), c_uint, c_uint, C_DWORD, C_LDWORD)

# 消息回调函数原形(pBuf内存由SDK内部申请释放) ；Alarm message callback function original shape(pBuf memory was managed by SDK )
# 参数列表(param list):
#     lCommand：报警类型；alarm type
#     lLoginID:登录句柄; Login handle
#     pBuf:报警信息；alarm info
#     dwBufLen:报警信息大小；alarm info len
#     pchDVRIP:IP地址;IP address
#     nDVRPort:端口号;Port
#     bAlarmAckFlag:TRUE,该事件为可以进行确认的事件；FALSE,该事件无法进行确认;TRUE,the event is affirmable event;FALSE,the event is not affirmable event
#     nEventID:用于对 AlarmAck 接口的入参进行赋值,当 bAlarmAckFlag 为 TRUE 时,该数据有效；nEventID is used by AlarmAck interface, when bAlarmAckFlag is TRUE, this data is efficient
#     dwUser:SetDVRMessCallBackEx1接口输入的用户数据信息; user data from SetDVRMessCallBackEx1 function
fMessCallBackEx1 = CB_FUNCTYPE(None, c_long, C_LLONG, POINTER(c_char), C_DWORD, POINTER(c_char), c_long, c_int, c_long, C_LDWORD)
# 回放进度回调函数; play back progress callback
# 参数列表(param list):
#     lPlayHandle：RealLoadPictureEx接口返回的句柄; handle of RealLoadPictureEx return
#     dwTotalSize: 下载数据总大小； total size of this download
#     dwDownLoadSize: 当前已下载数据的大小，dwDownLoadSize == -1 表示用户回放或者下载进度完成，dwDownLoadSize ==- 2 表示用户没有回放或者下载操作权限； current download size，-1:playback has over，-2:write file failed
#     dwUser:用户数据； user data
fDownLoadPosCallBack = CB_FUNCTYPE(None, C_LLONG, C_DWORD, C_DWORD, C_LDWORD)

# 回放数据回调; Playback data callback function
# 若设备传过来的码流是不加密的,dwDataType:0-不加密的录像文件原始数据
# 若设备传过来的码流是加密的,dwDataType: 0-解密后的大华私有码流(帧数据）,2-加密的原始码流
# If the stream is unencrypted,dwDataType:0-the original unencrypted stream
# If the stream is encrypted,dwDataType: 0-the decrypted stream(the frame data),2-the original encrypted stream
#  Whether the stream is encrypted,should call CLIENT_GetConfig(NET_EM_CFG_MEDIA_ENCRYPT) to get it;
#   If bKeyFrameEncryptEnable is TRUE,it means the stream is encrypted, otherwise it means the stream is unencrypted;
#   If you want to tramsmit the original stream,Before call playaback interface,you should call CLIENT_GetConfig(NET_EM_CFG_MEDIA_ENCRYPT) to know whether the stream is encrypted.
#   If the stream is encrypted, then should call CLIENT_AttachVK to attach VK info, At last should call CLIENT_GetVK to Get VK info.
# 参数列表(param list):
#     lRealHandle：回放数据句柄; playback handle
#     dwDataType:数据类型； data type
#     pBuffer:数据缓冲区，内存由SDK内部申请释放; data buffer, memory malloc or free was managed by SDK interior
#     dwBufSize:数据缓存大小； pBuffer's size
#     dwUser:用户数据； user data
fDataCallBack = CB_FUNCTYPE(c_int, C_LLONG, C_DWORD, POINTER(c_ubyte), C_DWORD, C_LDWORD)

# 按时间回放进度回调函数; Playback process by time callback function original shape
# 参数列表(param list):
#     lPlayHandle：RealLoadPictureEx接口返回的句柄; handle of RealLoadPictureEx return
#     dwTotalSize: 下载数据总大小； total size of this download
#     dwDownLoadSize: 当前已下载数据的大小； current download size
#     index: 文件序列; file index
#     recordfileinfo: 录像文件信息; record file information
#     dwUser:用户数据； user data
fTimeDownLoadPosCallBack = CB_FUNCTYPE(None, C_LLONG, C_DWORD, C_DWORD, c_int, NET_RECORDFILE_INFO, C_LDWORD)


# 实时监视数据回调函数原形--扩展(pBuffer内存由SDK内部申请释放); Obtain corresponding stream by filtering dwDataType, stream type refers to EM_REALDATA_FLAG
# 通过 dwDataType 过滤得到对应码流，具体码流类型请参考 EM_REALDATA_FLAG; 转码流时 dwDataType 值请参考 NET_DATA_CALL_BACK_VALUE 说明; The dwDataType value in stream converting refers to NET_DATA_CALL_BACK_VALUE
# 当转码流时，param 为具体的转码信息（视频帧、音频帧等信息），对应结构体 NET_STREAMCONVERT_INFO; when convert stream, param refers to frame info(video frame info or audio frame info), param's type is NET_STREAMCONVERT_INFO
# 参数列表(param list):
#     lRealHandle：监视句柄; monitor handle
#     dwDataType: 回调数据类型；callback data type
#     pBuffer: 回调数据缓存； byte array, length is dwBufSize
#     dwBufSize: 回调数据的缓存大小; pBuffer's size
#     param: 参数结构体的指针; pointer to parameter structure,based on different type
#     dwUser:用户数据； user data
fRealDataCallBackEx2 = CB_FUNCTYPE(None, C_LLONG, C_DWORD, POINTER(c_byte), C_DWORD, C_LLONG, C_LDWORD)


# decoding callback function.
# 参数列表(param list):
#     nPort：channel no
#     pBuf: A/V data after decoding
#     nSize: pBuf length of A/V data after decoding
#     pFrameInfo: image and audio, refer to FRAME_INFO structure
#     pUserData: User defined data
#     nReserved2: reserved parameter
fDecCBFun = CB_FUNCTYPE(None, c_int, c_char_p, c_int, POINTER(PLAY_FRAME_INFO), c_void_p, c_int)