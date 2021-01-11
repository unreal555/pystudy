from ctypes import *
import platform
import re
import os

def system_get_platform_info():
    sys_platform = platform.system().lower().strip()
    python_bit = platform.architecture()[0]
    python_bit_num = re.findall('(\d+)\w*', python_bit)[0]
    return sys_platform, python_bit_num

sys_platform, python_bit_num = system_get_platform_info()
system_type = sys_platform + python_bit_num

netsdkdllpath_dict = {'windows64': os.path.dirname(__file__) + '\\Libs\\win64\\'+'dhnetsdk.dll', 'windows32': os.path.dirname(__file__) + '\\Libs\\win32\\'+'dhnetsdk.dll',
                      'linux64': os.path.dirname(__file__) + '/Libs/linux64/libdhnetsdk.so', 'linux32': os.path.dirname(__file__) + '/Libs/linux32/libdhnetsdk.so'}
configdllpath_dict = {'windows64': os.path.dirname(__file__) + '\\Libs\\win64\\'+'dhconfigsdk.dll', 'windows32': os.path.dirname(__file__) + '\\Libs\\win32\\'+'dhconfigsdk.dll',
                      'linux64': os.path.dirname(__file__) + '/Libs/linux64/libdhconfigsdk.so', 'linux32': os.path.dirname(__file__) + '/Libs/linux32/libdhconfigsdk.so'}
playsdkdllpath_dict = {'windows64': os.path.dirname(__file__) + '\\Libs\\win64\\'+'dhplay.dll', 'windows32': os.path.dirname(__file__) + '\\Libs\\win32\\'+'dhplay.dll',
                      'linux64': os.path.dirname(__file__) + '/Libs/linux64/libdhplay.so', 'linux32': os.path.dirname(__file__) + '/Libs/linux32/libdhplay.so'}

C_LLONG_DICT = {'windows64': c_longlong, 'windows32': c_long, 'linux32': c_long, 'linux64': c_long}
C_LONG_DICT = {'windows64': c_long, 'windows32': c_long, 'linux32': c_int, 'linux64': c_int}
C_LDWORD_DICT = {'windows64': c_longlong, 'windows32': c_ulong, 'linux32': c_long, 'linux64': c_long}
C_DWORD_DICT = {'windows64': c_ulong, 'windows32': c_ulong, 'linux32': c_uint, 'linux64': c_uint}

C_LLONG = C_LLONG_DICT[system_type]
C_LONG = C_LONG_DICT[system_type]
C_LDWORD = C_LDWORD_DICT[system_type]
C_DWORD = C_DWORD_DICT[system_type]
C_TP_U64 = c_ulonglong
C_BOOL = c_int
C_UINT = c_uint
C_BYTE = c_ubyte
C_ENUM = c_int

if sys_platform == 'linux':
    load_library = cdll.LoadLibrary
    CB_FUNCTYPE = CFUNCTYPE
elif sys_platform == 'windows':
    load_library = windll.LoadLibrary
    CB_FUNCTYPE = WINFUNCTYPE
else:
    print("************不支持的平台**************")
    exit(0)

netsdkdllpath = netsdkdllpath_dict[system_type]
configdllpath = configdllpath_dict[system_type]
playsdkdllpath = playsdkdllpath_dict[system_type]


class NETSDK_INIT_PARAM(Structure):
    """
    初始化参数;Initialization parameter
    """
    _fields_ = [
        ("nThreadNum", c_int),                 # 指定NetSDK常规网络处理线程数, 当值为0时, 使用内部默认值; specify netsdk's normal network process thread number, zero means using default value
        ("bReserved", c_ubyte * 1024),         # 保留字节; reserved
    ]


class NET_PARAM(Structure):
    """
    设置登入时的相关参数;The corresponding parameter when setting log in
    """
    _fields_ = [
        ("nWaittime", c_int),                 # 等待超时时间(毫秒为单位),为0默认5000ms;Waiting time(unit is ms), 0:default 5000ms.
        ("nConnectTime", c_int),              # 连接超时时间(毫秒为单位),为0默认1500ms;Connection timeout value(Unit is ms), 0:default 1500ms.
        ("nConnectTryNum", c_int),            # 连接尝试次数,为0默认1次;Connection trial times, 0:default 1.
        ("nSubConnectSpaceTime", c_int),      # 子连接之间的等待时间(毫秒为单位),为0默认10ms;Sub-connection waiting time(Unit is ms), 0:default 10ms.
        ("nGetDevInfoTime", c_int),           # 获取设备信息超时时间,为0默认1000ms;Access to device information timeout, 0:default 1000ms.
        ("nConnectBufSize", c_int),           # 每个连接接收数据缓冲大小(字节为单位),为0默认250*1024;Each connected to receive data buffer size(Bytes), 0:default 250*1024
        ("nGetConnInfoTime", c_int),          # 获取子连接信息超时时间(毫秒为单位),为0默认1000ms;Access to sub-connect information timeout(Unit is ms), 0:default 1000ms.
        ("nSearchRecordTime", c_int),         # 按时间查询录像文件的超时时间(毫秒为单位),为0默认为3000ms;Timeout value of search video (unit ms), default 3000ms
        ("nsubDisconnetTime", c_int),         # 检测子链接断线等待时间(毫秒为单位),为0默认为60000ms;dislink disconnect time,0:default 60000ms
        ("byNetType", c_ubyte),               # 网络类型, 0-LAN, 1-WAN;net type, 0-LAN, 1-WAN
        ("byPlaybackBufSize", c_ubyte),       # 回放数据接收缓冲大小（M为单位）,为0默认为4M;playback data from the receive buffer size(m),when value = 0,default 4M
        ("bDetectDisconnTime", c_ubyte),      # 心跳检测断线时间(单位为秒),为0默认为60s,最小时间为2s;Pulse detect offline time(second) .When it is 0, the default setup is 60s, and the min time is 2s
        ("bKeepLifeInterval", c_ubyte),       # 心跳包发送间隔(单位为秒),为0默认为10s,最小间隔为2s;Pulse send out interval(second). When it is 0, the default setup is 10s, the min internal is 2s.
        ("nPicBufSize", c_int),               # 实时图片接收缓冲大小（字节为单位）,为0默认为2*1024*1024;actual pictures of the receive buffer size(byte)when value = 0,default 2*1024*1024
        ("bReserved", c_ubyte*4)              # 保留字段字段;reserved
    ]


class NET_DEVICEINFO(Structure):
    """
    设备信息;Device info
    """
    _fields_ = [
        ('sSerialNumber', c_char * 48),     # 序列号;serial number
        ('byAlarmInPortNum', c_ubyte),      # DVR报警输入个数;DVR alarm input amount
        ('byAlarmOutPortNum', c_ubyte),     # DVR报警输出个数;DVR alarm output amount
        ('byDiskNum', c_ubyte),             # DVR硬盘个数;DVR HDD amount
        ('byDVRType', c_ubyte),             # DVR类型,见枚举 NET_DEVICE_TYPE DVR type.Please refer to NET_DEVICE_TYPE
        ('byChanNum', c_ubyte),             # DVR通道个数,登陆成功时有效,当登陆失败原因为密码错误时,通过此参数通知用户,剩余登陆次数,为0时表示此参数无效; DVR channel amount,When login failed due to password error, notice user via this parameter, remaining login times, is 0 means this parameter is invalid
    ]


class LOG_SET_PRINT_INFO(Structure):
    """
    SDK全局日志打印信息;SDK global log print
    """
    _fields_ = [
        ('dwSize', C_DWORD),                # 结构体大小;Structure size
        ('bSetFilePath', c_int),            # 是否重设日志路径;reset log path
        ('szLogFilePath', c_char * 260),    # 日志路径(默认"./sdk_log/sdk_log.log");log path(default"./sdk_log/sdk_log.log")
        ('bSetFileSize', c_int),            # 是否重设日志文件大小;reset log size
        ('nFileSize', c_uint),              # 每个日志文件的大小(默认大小10240), 单位:KB;each log file size(default size 10240), unit:KB
        ('bSetFileNum', c_int),             # 是否重设日志文件个数;reset log file number
        ('nFileNum', c_uint),               # 绕接日志文件个数(默认大小10);log file quantity(default size 10)
        ('bSetPrintStrategy', c_int),       # 是否重设日志打印输出策略;reset log print strategy
        ('nPrintStrategy', c_uint),         # 日志输出策略, 0:输出到文件(默认); 1:输出到窗口;log out strategy, 0: output to file(defualt); 1:output to window
        ('byReserved', c_ubyte * 4),        # 字节对齐;Byte alignment
        ('cbSDKLogCallBack', CB_FUNCTYPE(c_int, c_char_p, c_uint, C_LDWORD)),   # 日志回调，需要将sdk日志回调出来时设置，默认为None,对应SDK_Callback的fSDKLogCallBack;log callback, (default None),corresponding to SDK_Callback's fSDKLogCallBack
        ('dwUser', C_LDWORD)                # 用户数据;UserData
    ]


class DEVICE_NET_INFO_EX(Structure):
    """
    设备信息;Device info
    """
    _fields_ = [
        ('iIPVersion', c_int),          # 4代表IPV4,6代表IPV6;4 for IPV4, 6 for IPV6
        ('szIP', c_char*64),            # IP IPV4形如"192.168.0.1" IPV6形如"2008::1/64",;IP IPV4 likes "192.168.0.1" ,IPV6 likes "2008::1/64"
        ('nPort', c_int),               # tcp端口;Port
        ('szSubmask', c_char*64),       # 子网掩码 IPV6无子网掩码;Subnet mask
        ('szGateway', c_char*64),       # 网关;Gate way
        ('szMac', c_char*40),           # MAC地址;Mac
        ('szDeviceType', c_char*32),    # 设备类型;Device type
        ('byManuFactory', c_ubyte),     # 目标设备的生产厂商,具体参考sdk_enum.py的EM_IPC_TYPE;Manu factory,refer to EM_IPC_TYPE in sdk_enum.py
        ('byDefinition', c_ubyte),      # 1-标清 2-高清;1-Standard definition 2-High definition
        ('bDhcpEn', c_bool),            # Dhcp使能状态, true-开, false-关;Dhcp, true-open, false-close
        ('byReserved1', c_ubyte),       # 字节对齐;reserved
        ('verifyData', c_char * 88),    # 校验数据 通过异步搜索回调获取(在修改设备IP时会用此信息进行校验);ECC data
        ('szSerialNo', c_char * 48),    # 序列号;serial no
        ('szDevSoftVersion', c_char * 128),  # 设备软件版本号;soft version
        ('szDetailType', c_char * 32),  # 设备型号;device detail type
        ('szVendor', c_char * 128),     # OEM客户类型; OEM type
        ('szDevName', c_char * 64),     # 设备名称;device name
        ('szUserName', c_char * 16),    # 登陆设备用户名（在修改设备IP时需要填写）;user name for log in device(it need be filled when modify device ip)
        ('szPassWord', c_char * 16),    # 登陆设备密码（在修改设备IP时需要填写）;pass word for log in device(it need be filled when modify device ip)
        ('nHttpPort', c_ushort),        # HTTP服务端口号;HTTP server port
        ('wVideoInputCh', c_ushort),    # 视频输入通道数;count of video input channel
        ('wRemoteVideoInputCh', c_ushort),  # 远程视频输入通道数;count of remote video input
        ('wVideoOutputCh', c_ushort),   # 视频输出通道数;count of video output channel
        ('wAlarmInputCh', c_ushort),    # 报警输入通道数;count of alarm input
        ('wAlarmOutputCh', c_ushort),   # 报警输出通道数;count of alarm output
        ('bNewWordLen', c_int),         # TRUE使用新密码字段szNewPassWord;TRUE:szNewPassWord Enable
        ('szNewPassWord', c_char*64),   # 登陆设备密码（在修改设备IP时需要填写）;pass word for log in device(it need be filled when modify device ip)
        ('byInitStatus', c_ubyte),      # 设备初始化状态，按位确定初始化状态;init status
			                            # bit0~1：0-老设备，没有初始化功能 1-未初始化账号 2-已初始化账户;bit0~1：0-old device, can not be init; 1-not init; 2-already init
                                        # bit2~3：0-老设备，保留 1-公网接入未使能 2-公网接入已使能;bit2~3：0-old device,reserved; 1-connect to public network disable; 2-connect to public network enable
                                        # bit4~5：0-老设备，保留 1-手机直连未使能 2-手机直连使能;bit4~5：0-old device,reserved; 1-connect to cellphone disable; 2-connect to cellphone enable
                                        # bit6~7: 0- 未知 1-不支持密码重置 2-支持密码重置;bit6~7: 0- unknown 1-unsupported reset password 2-support password
        ('byPwdResetWay', c_ubyte),     # 支持密码重置方式：按位确定密码重置方式，只在设备有初始化账号时有意义;the way supported for reset password:make sense when the device is init
                                        # bit0-支持预置手机号 bit1-支持预置邮箱 ,bit2-支持文件导出;bit0-support reset password by cellphone; bit1-support reset password by mail; bit2-support reset password by XML file;
                                        # bit3-支持密保问题 bit4-支持更换手机号;bit3-support reset password by security question; bit4-support reset password by change cellphone
        ('bySpecialAbility', c_ubyte),  # 设备初始化能力，按位确定初始化能力,高八位 bit0-2D Code修改IP: 0 不支持 1 支持, bit1-PN制:0 不支持 1支持
                                        # ENGLISH_LANG:special ability of device ,high eight bit, bit0-2D Code:0 support  1 no support, bit1-PN:0 support  1 no support
        ('szNewDetailType', c_char*64),     # 设备型号;device detail type
        ('bNewUserName', c_int),        # true(szNewUserName)字段;TRUE:szNewUserName enable
        ('szNewUserName', c_char * 64), # 登陆设备用户名（在修改设备IP时需要填写）;new user name for login device(it need be filled when modify device ip)
        ('byPwdFindVersion', c_ubyte),  # 密码找回的版本号,设备支持密码重置时有效;;password find version, effective when device supports reset password
                                        # 0-设备使用的是老方案的密码重置版本;1-支持预留联系方式进行密码重置操作;2-支持更换联系方式进行密码重置操作;
                                        # ENGLISH_LANG:0-device of old scheme reset password version;1-support reset password by reserved contact;2-support reset password by change contact;
        ('szDeviceID', c_char * 24),    # 定制字段, 不作为通用协议，不对接通用客户端;Custom item, do not use for general client
        ('dwUnLoginFuncMask', C_DWORD), # Bit0 Wifi列表扫描及WLan设置,Bit1 支持会话外修改过期密码;function mask before login, Bit0 means wifi config
        ('szMachineGroup', c_char * 64),  # 设备分组;machine group
        ('cReserved', c_char * 12),     # 扩展字段;reserved
    ]


class DEVICE_NET_INFO_EX2(Structure):
    """
    对应StartSearchDevicesEx接口;Corresponding to StartSearchDevicesEx
    """
    _fields_ = [
        ('stuDevInfo', DEVICE_NET_INFO_EX), # 设备信息结构体;device net info
        ('szLocalIP', c_char*64),           # 搜索到设备的本地IP地址;local ip
        ('cReserved', c_char*2048)          # 保留字段;reserved
    ]


class NET_DEVICEINFO_Ex(Structure):
    """
    设备信息扩展;Device extension info
    """
    _fields_ = [
        ('sSerialNumber', c_char * 48),     # 序列号;serial number
        ('nAlarmInPortNum', c_int),         # DVR报警输入个数;count of DVR alarm input
        ('nAlarmOutPortNum', c_int),        # DVR报警输出个数;count of DVR alarm output
        ('nDiskNum', c_int),                # DVR硬盘个数;number of DVR disk
        ('nDVRType', c_int),                # DVR类型;DVR type, refer to NET_DEVICE_TYPE
        ('nChanNum', c_int),                # DVR通道个数;number of DVR channel
        ('byLimitLoginTime', c_char),       # 在线超时时间,为0表示不限制登陆,非0表示限制的分钟数;Online Timeout, Not Limited Access to 0, not 0 Minutes Limit Said
        ('byLeftLogTimes', c_char),         # 当登陆失败原因为密码错误时,通过此参数通知用户,剩余登陆次数,为0时表示此参数无效; When login failed due to password error, notice user via this parameter, remaining login times, is 0 means this parameter is invalid
        ('bReserved', c_char * 2),          # 保留字节,字节对齐;keep bytes, bytes aligned
        ('nLockLeftTime', c_int),           # 当登陆失败,用户解锁剩余时间（秒数）, -1表示设备未设置该参数;when log in failed, the left time for users to unlock (seconds), -1 indicate the device haven't set the parameter
        ('Reserved', c_char * 24),          # 保留;reserved
    ]


class NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY(Structure):
    """
    LoginWithHighLevelSecurity 输入参数;LoginWithHighLevelSecurity input param
    """
    _fields_ = [
        ('dwSize', C_DWORD),          # 结构体大小;Structrue size
        ('szIP', c_char*64),          # IP地址;IP address
        ('nPort', c_int),             # 端口;Port
        ('szUserName', c_char * 64),  # 用户名;User name
        ('szPassword', c_char * 64),  # 密码;Password
        ('emSpecCap', c_int),         # 登录模式,具体信息见sdk_enum.py内的EM_LOGIN_SPAC_CAP_TYPE;Spec login cap，refer to EM_LOGIN_SPAC_CAP_TYPE in sdk_enum.py
        ('byReserved', c_ubyte*4),    # 保留字节;Reserved
        ('pCapParam', c_void_p)       # emSpecCap = 0,pCapParam:None;emSpecCap = 0,pCapParam:None
                                      # emSpecCap = 2,pCapParam:None;emSpecCap = 2,pCapParam:None
                                      # emSpecCap = 3,pCapParam:None;emSpecCap = 3,pCapParam:None
                                      # emSpecCap = 4,pCapParam:None;emSpecCap = 4,pCapParam:None
                                      # emSpecCap = 6,pCapParam:None;emSpecCap = 6,pCapParam:None
                                      # emSpecCap = 7,pCapParam:None;emSpecCap = 7,pCapParam:None
                                      # emSpecCap = 9,pCapParam:填入远程设备的名字的字符串;emSpecCap = 9,pCapParam is string of remote device name
                                      # emSpecCap = 12,pCapParam:None;emSpecCap = 12,pCapParam:None
                                      # emSpecCap = 13,pCapParam:None;emSpecCap = 13,pCapParam:None
                                      # emSpecCap = 14,pCapParam:None;emSpecCap = 14,pCapParam:None
                                      # emSpecCap = 15,pCapParam:Socks5服务器的IP&&port&&ServerName&&ServerPassword字符串;emSpecCap = 15,pCapParam:IP&&port&&ServerName&&ServerPassword string of Socket5 server
                                      # emSpecCap = 16,pCapParam:SOCKET值;emSpecCap = 16,pCapParam:SOCKET value
                                      # emSpecCap = 19,pCapParam:None;emSpecCap = 19,pCapParam:None
                                      # emSpecCap = 20,pCapParam:None;emSpecCap = 20,pCapParam:None
    ]


class NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY(Structure):
    """
       LoginWithHighLevelSecurity 输出参数;LoginWithHighLevelSecurity output param
       """
    _fields_ = [
        ('dwSize', C_DWORD),                               # 结构体大小;Structrue size
        ('stuDeviceInfo', NET_DEVICEINFO_Ex),              # 设备信息;Device info
        ('nError', c_int),                                 # 错误码，见 Login 接口错误码;Error
        ('byReserved', c_ubyte * 132)                      # 预留字段,;Reserved
    ]


class NET_IN_STARTSERACH_DEVICE(Structure):
    """
    StartSearchDevicesEx接口输入参数;StartSearchDevicesEx input param
    """
    _fields_ = [
        ('dwSize', C_DWORD),            # 结构体大小;Structrue size
        ('szLocalIp', c_char*64),       # 发起搜索的本地IP;local IP
        ('cbSearchDevices', CB_FUNCTYPE(None, C_LLONG, POINTER(DEVICE_NET_INFO_EX2), c_void_p)),   #设备信息回调函数;search device call back
        ('pUserData', c_void_p),        # 用户自定义数据;user data
        ('emSendType', c_int)           # 下发搜索类型,对应EM_SEND_SEARCH_TYPE;send search type,refer to EM_SEND_SEARCH_TYPE
    ]


class NET_OUT_STARTSERACH_DEVICE(Structure):
    """
        StartSearchDevicesEx接口输出参数;StartSearchDevicesEx output param
        """
    _fields_ = [
        ('dwSize', C_DWORD)           # 结构体大小，ENGLISH_LANG:Structrue size
    ]


class DEVICE_IP_SEARCH_INFO_IP(Structure):
    """
    具体待搜索的IP信息;the IPs info for search
    """
    _fields_ = [
        ('IP', c_char*64)               # 具体待搜索的IP信息;the IP for search
    ]


class DEVICE_IP_SEARCH_INFO(Structure):
    """
    SearchDevicesByIPs接口输入参数; SearchDevicesByIPs input param
    """
    _fields_ = [
        ('dwSize', C_DWORD),                      # 结构体大小;Structure size
        ('nIpNum', c_int),                        # 当前搜索的IP个数;the IPs number for search
        ('szIP', DEVICE_IP_SEARCH_INFO_IP * 256)  # 具体待搜索的IP信息;the IPs info for search
    ]


class NET_IN_INIT_DEVICE_ACCOUNT(Structure):
    """
       InitDevAccount接口输入参数;InitDevAccount interface input param
       """
    _fields_ = [
        ('dwSize', C_DWORD),            # 结构体大小;Structure size
        ('szMac', c_char*40),           # 设备mac地址;mac addr
        ('szUserName', c_char * 128),   # 用户名;user name
        ('szPwd', c_char * 128),        # 设备密码;password
        ('szCellPhone', c_char * 32),   # 预留手机号;cellphone
        ('szMail', c_char * 64),        # 预留邮箱;mail addr
        ('byInitStatus', c_ubyte),      # 该字段废弃;this field already abandoned
        ('byPwdResetWay', c_ubyte),     # 设备支持的密码重置方式：搜索设备接口(StartSearchDevicesEx、SearchDevicesByIPs回调函数)返回字段byPwdResetWay的值
                                          # 该值的具体含义见 DEVICE_NET_INFO_EX2 结构体，需要与设备搜索接口返回的 byPwdResetWay 值保持一致
                                          # bit0 : 1-支持预留手机号，此时需要在szCellPhone数组中填入预留手机号(如果需要设置预留手机) ;
                                          # bit1 : 1-支持预留邮箱，此时需要在szMail数组中填入预留邮箱(如果需要设置预留邮箱)
                                          # the way supported for reset password:byPwdResetWay value of StartSearchDevicesEx's , SearchDevicesByIPs's callback function
                                          # the meaning of this parameter refers to DEVICE_NET_INFO_EX2, the value must be same as byPwdResetWay returned by StartSearchDevicesEx,SearchDevicesByIPs
                                          # bit0 : 1-support reset password by cellphone, you should set cellphone in szCellPhone if you need to set cellphone
                                          # bit1 : 1-support reset password by mail, you should set mail address in szMail if you need to set mail address
        ('byReserved', c_ubyte*2)       # 保留字段;Reserve
    ]


class NET_OUT_INIT_DEVICE_ACCOUNT(Structure):
    """
    InitDevAccount接口输出参数;InitDevAccount interface output param
    """
    _fields_ = [
        ('dwSize', C_DWORD)           # 结构体大小;Structrue size
    ]


class NET_TIME(Structure):
    """
    时间;time
    """
    _fields_ = [
        ('dwYear', C_DWORD),    # 年;Year
        ('dwMonth', C_DWORD),   # 月;Month
        ('dwDay', C_DWORD),     # 日;Date
        ('dwHour', C_DWORD),    # 时;Hour
        ('dwMinute', C_DWORD),  # 分;Minute
        ('dwSecond', C_DWORD)   # 秒;Second
    ]

class NET_RECORDFILE_INFO(Structure):
    """
    录像文件信息; Record file information
    """
    _fields_ = [
        ('ch', c_uint),                # 通道号; Channel number
        ('filename', c_char * 124),    # 文件名; File name
        ('framenum', c_uint),          # 文件总帧数; the total number of file frames
        ('size', c_uint),              # 文件长度, 单位为Kbyte; File length, unit: Kbyte
        ('starttime', NET_TIME),       # 开始时间; Start time
        ('endtime', NET_TIME),         # 结束时间; End time
        ('driveno', c_uint),           # 磁盘号(区分网络录像和本地录像的类型,0－127表示本地录像,其中64表示光盘1,128表示网络录像); HDD number
        ('startcluster', c_uint),      # 起始簇号; Initial cluster number
        ('nRecordFileType', c_ubyte),  # 录象文件类型  0：普通录象；1：报警录象；2：移动检测；3：卡号录象；4：图片, 5: 智能录像, 19: POS录像, 255:所有录像; Recorded file type  0:general record;1:alarm record ;2:motion detection;3:card number record ;4:image ; 19:Pos record ;255:all
        ('bImportantRecID', c_ubyte),  # 0:普通录像 1:重要录像; 0:general record 1:Important record
        ('bHint', c_ubyte),            # 文件定位索引(nRecordFileType==4<图片>时,bImportantRecID<<8 +bHint ,组成图片定位索引 ); Document Indexing
        ('bRecType', c_ubyte)          # 0-主码流录像 1-辅码1流录像 2-辅码流2 3-辅码流3录像; 0-main stream record 1-sub1 stream record 2-sub2 stream record 3-sub3 stream record
    ]


class NET_TIME_EX(Structure):
    """
    时间;time
    """
    _fields_ = [
        ('dwYear', C_DWORD),        # 年;Year
        ('dwMonth', C_DWORD),       # 月;Month
        ('dwDay', C_DWORD),         # 日;Date
        ('dwHour', C_DWORD),        # 时;Hour
        ('dwMinute', C_DWORD),      # 分;Minute
        ('dwSecond', C_DWORD),      # 秒;Second
        ('dwMillisecond', C_DWORD), # 毫秒;Millisecond
        ('dwUTC', C_DWORD),         # utc时间(获取时0表示无效，非0有效,下发无效);utc query: zero means invaild, non-zero means vaild;  set:invalid
        ('dwReserved', C_DWORD)     # 预留字段;reserved data
    ]

class SDK_RECT(Structure):
    """
     区域；各边距按整长8192的比例;Zone;Each margin is total lenght :8192
     """
    _fields_ = [
        ('left', c_long),       # 左;left
        ('top', c_long),        # 顶;top
        ('right', c_long),      # 右;right
        ('bottom', c_long)      # 底;bottom
    ]

class SDK_POINT(Structure):
    """
     二维空间点;2 dimension point
     """
    _fields_ = [
        ('nx', c_short),        # x轴;x
        ('ny', c_short)         # y轴;y
    ]

class SDK_PIC_INFO(Structure):
    """
     物体对应图片文件信息;picture info
     """
    _fields_ = [
        ('dwOffSet', C_DWORD),      # 文件在二进制数据块中的偏移位置, 单位:字节;current picture file's offset in the binary file, byte
        ('dwFileLenth', C_DWORD),   # 文件大小, 单位:字节;current picture file's size, byte
        ('wWidth', c_ushort),       # 图片宽度, 单位:像素;picture width, pixel
        ('wHeight', c_ushort),      # 图片高度, 单位:像素;picture high, pixel
        ('pszFilePath', c_char_p),  # 文件路径;File path
                                    # 鉴于历史原因,该成员只在事件上报时有效,用户使用该字段时需要自行申请空间进行拷贝保存;User use this field need to apply for space for copy and storage,When submit to the server, the algorithm has checked the image or not
        ('bIsDetected', c_ubyte),   # 图片是否算法检测出来的检测过的提交识别服务器时,则不需要再时检测定位抠图,1:检测过的,0:没有检测过;When submit to the server, the algorithm has checked the image or not
        ('bReserved', c_ubyte*3),   # 预留字节数;reserved data
        ('nFilePathLen', c_int),    # 文件路径长度 既pszFilePath 用户申请的大小;File path Len of pszFilePath
        ('stuPoint', SDK_POINT)     # 小图左上角在大图的位置，使用绝对坐标系;The upper left corner of the figure is in the big picture. Absolute coordinates are used
    ]


class SDK_MSG_OBJECT(Structure):
    """
    视频分析物体信息结构体;Struct of object info for video analysis
    """
    _pack_ = 4  # 补齐
    _fields_ = [
        ('nObjectID', c_int),           # 物体ID,每个ID表示一个唯一的物体;Object ID,each ID represent a unique object
        ('szObjectType', c_char*128),   # 物体类型;Object type
        ('nConfidence', c_int),         # 置信度(0~255),值越大表示置信度越高;Confidence(0~255),a high value indicate a high confidence
        ('nAction', c_int),             # 物体动作:1:Appear 2:Move 3:Stay 4:Remove 5:Disappear 6:Split 7:Merge 8:Rename;Object action:1:Appear 2:Move 3:Stay 4:Remove 5:Disappear 6:Split 7:Merge 8:Rename
        ('BoundingBox', SDK_RECT),      # 包围盒;BoundingBox
        ('Center', SDK_POINT),          # 物体型心;The shape center of the object
        ('nPolygonNum', c_int),         # 多边形顶点个数;the number of culminations for the polygon
        ('Contour', SDK_POINT * 16),    # 较精确的轮廓多边形;a polygon that have a exactitude figure
        ('rgbaMainColor', C_DWORD),     # 表示车牌、车身等物体主要颜色；按字节表示,分别为红、绿、蓝和透明度,例如:RGB值为(0,255,0),透明度为0时, 其值为0x00ff0000.
                                        # The main color of the object;the first byte indicate red value, as byte order as green, blue, transparence, for example:RGB(0,255,0),transparence = 0, rgbaMainColor = 0x00ff0000.
        ('szText', c_char * 128),       # 物体上相关的带0结束符文本,比如车牌,集装箱号等等;the interrelated text of object,such as number plate,container number
                                            # "ObjectType"为"Vehicle"或者"Logo"时（尽量使用Logo。Vehicle是为了兼容老产品）表示车标,支持："ObjectType","Vehicle" or "Logo", try to use Logo.Vehicle is used to be compatible with old product, means logo, support:
                                            # "Unknown"未知;Unknown
                                            # "Audi" 奥迪;Audi
                                            # "Honda" 本田;Honda
                                            # "Buick" 别克;Buick
                                            # "Volkswagen" 大众;Volkswagen
                                            # "Toyota" 丰田;Toyota
                                            # "BMW" 宝马;BMW
                                            # "Peugeot" 标致;Peugeot
                                            # "Ford" 福特;Ford
                                            # "Mazda" 马自达;Mazda
                                            # "Nissan" 尼桑(日产);Nissan
                                            # "Hyundai" 现代;Hyundai
                                            # "Suzuki" 铃木;Suzuki
                                            # "Citroen" 雪铁龙;Citroen
                                            # "Benz" 奔驰;Benz
                                            # "BYD" 比亚迪;BYD
                                            # "Geely" 吉利;Geely
                                            # "Lexus" 雷克萨斯;Lexus
                                            # "Chevrolet" 雪佛兰;Chevrolet
                                            # "Chery" 奇瑞;Chery
                                            # "Kia" 起亚;Kia
                                            # "Charade" 夏利;Charade
                                            # "DF" 东风;DF
                                            # "Naveco" 依维柯;Naveco
                                            # "SGMW" 五菱;SGMW
                                            # "Jinbei" 金杯;Jinbei
                                            # "JAC" 江淮;JAC
                                            # "Emgrand" 帝豪;Emgrand
                                            # "ChangAn" 长安;ChangAn
                                            # "Great Wall" 长城;Great Wall
                                            # "Skoda" 斯柯达;Skoda
                                            # "BaoJun" 宝骏;BaoJun
                                            # "Subaru" 斯巴鲁;Subaru
                                            # "LandWind" 陆风;LandWind
                                            # "Luxgen" 纳智捷;Luxgen
                                            # "Renault" 雷诺;Renault
                                            # "Mitsubishi" 三菱;Mitsubishi
                                            # "Roewe" 荣威;Roewe
                                            # "Cadillac" 凯迪拉克;Cadillac
                                            # "MG" 名爵;MG
                                            # "Zotye" 众泰;Zotye
                                            # "ZhongHua" 中华;ZhongHua
                                            # "Foton" 福田;Foton
                                            # "SongHuaJiang" 松花江;SongHuaJiang
                                            # "Opel" 欧宝;Opel
                                            # "HongQi" 一汽红旗;HongQi
                                            # "Fiat" 菲亚特;Fiat
                                            # "Jaguar" 捷豹;Jaguar
                                            # "Volvo" 沃尔沃;Volvo
                                            # "Acura" 讴歌;Acura
                                            # "Porsche" 保时捷;Porsche
                                            # "Jeep" 吉普;Jeep
                                            # "Bentley" 宾利;Bentley
                                            # "Bugatti" 布加迪;Bugatti
                                            # "ChuanQi" 传祺;ChuanQi
                                            # "Daewoo" 大宇;Daewoo
                                            # "DongNan" 东南;DongNan
                                            # "Ferrari" 法拉利;Ferrari
                                            # "Fudi" 福迪;Fudi
                                            # "Huapu" 华普;Huapu
                                            # "HawTai" 华泰;HawTai
                                            # "JMC" 江铃;JMC
                                            # "JingLong" 金龙客车;JingLong
                                            # "JoyLong" 九龙;JoyLong
                                            # "Karry" 开瑞;Karry
                                            # "Chrysler" 克莱斯勒;Chrysler
                                            # "Lamborghini" 兰博基尼;Lamborghini
                                            # "RollsRoyce" 劳斯莱斯;RollsRoyce
                                            # "Linian" 理念;Linian
                                            # "LiFan" 力帆;LiFan
                                            # "LieBao" 猎豹;LieBao
                                            # "Lincoln" 林肯;Lincoln
                                            # "LandRover" 路虎;LandRover
                                            # "Lotus" 路特斯;Lotus
                                            # "Maserati" 玛莎拉蒂;Maserati
                                            # "Maybach" 迈巴赫;Maybach
                                            # "Mclaren" 迈凯轮;Mclaren
                                            # "Youngman" 青年客车;Youngman
                                            # "Tesla" 特斯拉;Tesla
                                            # "Rely" 威麟;Rely
                                            # "Lsuzu" 五十铃;Lsuzu
                                            # "Yiqi" 一汽;Yiqi
                                            # "Infiniti" 英菲尼迪;Infiniti
                                            # "YuTong" 宇通客车;YuTong
                                            # "AnKai" 安凯客车;AnKai
                                            # "Canghe" 昌河;Canghe
                                            # "HaiMa" 海马;HaiMa
                                            # "Crown" 丰田皇冠;Crown
                                            # "HuangHai" 黄海;HuangHai
                                            # "JinLv" 金旅客车;JinLv
                                            # "JinNing" 精灵;JinNing
                                            # "KuBo" 酷博;KuBo
                                            # "Europestar" 莲花;Europestar
                                            # "MINI" 迷你;MINI
                                            # "Gleagle" 全球鹰;Gleagle
                                            # "ShiDai" 时代;ShiDai
                                            # "ShuangHuan" 双环;ShuangHuan
                                            # "TianYe" 田野;TianYe
                                            # "WeiZi" 威姿;WeiZi
                                            # "Englon" 英伦;Englon
                                            # "ZhongTong" 中通客车;ZhongTong
                                            # "Changan" 长安轿车;Changan
                                            # "Yuejin" 跃进;Yuejin
                                            # "Taurus" 金牛星;Taurus
                                            # "Alto" 奥拓;Alto
                                            # "Weiwang" 威旺;Weiwang
                                            # "Chenglong" 乘龙;Chenglong
                                            # "Haige" 海格;Haige
                                            # "Shaolin" 少林客车;Shaolin
                                            # "Beifang" 北方客车;Beifang
                                            # "Beijing" 北京汽车;Beijing
                                            # "Hafu" 哈弗;Hafu
                                            # "BeijingTruck" 北汽货车;BeijingTruck
                                            # "Besturn" 奔腾;Besturn
                                            # "ChanganBus" 长安客车;ChanganBus
                                            # "Dodge" 道奇;Dodge
                                            # "DongFangHong" 东方红;DongFangHong
                                            # "DongFengTruck" 东风货车;DongFengTruck
                                            # "DongFengBus" 东风客车;DongFengBus
                                            # "MultiBrand" 多品牌;MultiBrand
                                            # "FotonTruck" 福田货车;FotonTruck
                                            # "FotonBus" 福田客车;FotonBus
                                            # "GagcTruck" 广汽货车;GagcTruck
                                            # "HaFei" 哈飞;HaFei
                                            # "HowoBus" 豪沃客车;HowoBus
                                            # "JACTruck" 江淮货车;JACTruck
                                            # "JACBus" 江淮客车;JACBus
                                            # "JMCTruck" 江铃货车;JMCTruck
                                            # "JieFangTruck" 解放货车;JieFangTruck
                                            # "JinBeiTruck" 金杯货车;JinBeiTruck
                                            # "KaiMaTruck" 凯马货车;KaiMaTruck
                                            # "CoasterBus" 柯斯达客车;CoasterBus
                                            # "MudanBus" 牡丹客车;MudanBus
                                            # "NanJunTruck" 南骏货车;NanJunTruck
                                            # "QingLing" 庆铃;QingLing
                                            # "NissanCivilian" 日产碧莲客车;NissanCivilian
                                            # "NissanTruck" 日产货车;NissanTruck
                                            # "MitsubishiFuso" 三菱扶桑;MitsubishiFuso
                                            # "SanyTruck" 三一货车;SanyTruck
                                            # "ShanQiTruck" 陕汽货车;ShanQiTruck
                                            # "ShenLongBus" 申龙客车;ShenLongBus
                                            # "TangJunTruck" 唐骏货车;TangJunTruck
                                            # "MicroTruck" 微货车;MicroTruck
                                            # "VolvoBus" 沃尔沃客车;VolvoBus
                                            # "LsuzuTruck" 五十铃货车;LsuzuTruck
                                            # "WuZhengTruck" 五征货车;WuZhengTruck
                                            # "Seat" 西雅特;Seat
                                            # "YangZiBus" 扬子客车;YangZiBus
                                            # "YiqiBus" 一汽客车;YiqiBus
                                            # "YingTianTruck" 英田货车;YingTianTruck
                                            # "YueJinTruck" 跃进货车;YueJinTruck
                                            # "ZhongDaBus" 中大客车;ZhongDaBus
                                            # "ZxAuto" 中兴;ZxAuto
                                            # "ZhongQiWangPai" 重汽王牌;ZhongQiWangPai
                                            # "WAW" 奥驰;WAW
                                            # "BeiQiWeiWang" 北汽威旺;BeiQiWeiWang
                                            # "BYDDaimler"	比亚迪戴姆勒;BYDDaimler
                                            # "ChunLan" 春兰;ChunLan
                                            # "DaYun" 大运;DaYun
                                            # "DFFengDu" 东风风度;DFFengDu
                                            # "DFFengGuang" 东风风光;DFFengGuang
                                            # "DFFengShen" 东风风神;DFFengShen
                                            # "DFFengXing" 东风风行;DFFengXing
                                            # "DFLiuQi" 东风柳汽;DFLiuQi
                                            # "DFXiaoKang" 东风小康;DFXiaoKang
                                            # "FeiChi" 飞驰;FeiChi
                                            # "FordMustang" 福特野马;FordMustang
                                            # "GuangQi" 广汽;GuangQi
                                            # "GuangTong" 广通;GuangTong
                                            # "HuiZhongTruck" 汇众重卡;HuiZhongTruck
                                            # "JiangHuai" 江环;JiangHuai
                                            # "SunWin" 申沃;SunWin
                                            # "ShiFeng" 时风;ShiFeng
                                            # "TongXin" 同心;TongXin
                                            # "WZL" 五洲龙;WZL
                                            # "XiWo" 西沃;XiWo
                                            # "XuGong" 徐工;XuGong
                                            # "JingGong" 精工;JingGong
                                            # "SAAB" 萨博;SAAB
                                            # "SanHuanShiTong" 三环十通;SanHuanShiTong
                                            # "KangDi" 康迪;KangDi
                                            # "YaoLong" 耀隆;YaoLong
        ('szObjectSubType', c_char*62),     # 物体子类别,根据不同的物体类型,可以取以下子类型：
                                            # Vehicle Category:"Unknown"  未知,"Motor" 机动车,"Non-Motor":非机动车,"Bus": 公交车,"Bicycle" 自行车,"Motorcycle":摩托车,"PassengerCar":客车,
                                            # "LargeTruck":大货车,    "MidTruck":中货车,"SaloonCar":轿车,"Microbus":面包车,"MicroTruck":小货车,"Tricycle":三轮车,    "Passerby":行人
                                            # "DregsCar":渣土车, "Excavator":挖掘车, "Bulldozer":推土车, "Crane":吊车, "PumpTruck":泵车, "MachineshopTruck":工程车
                                            # Plate Category："Unknown" 未知,"Normal" 蓝牌黑牌,"Yellow" 黄牌,"DoubleYellow" 双层黄尾牌,"Police" 警牌"Armed" 武警牌,
                                            # "Military" 部队号牌,"DoubleMilitary" 部队双层,"SAR" 港澳特区号牌,"Trainning" 教练车号牌
                                            # "Personal" 个性号牌,"Agri" 农用牌,"Embassy" 使馆号牌,"Moto" 摩托车号牌,"Tractor" 拖拉机号牌,"Other" 其他号牌
                                            # "Civilaviation"民航号牌,"Black"黑牌
                                            # "PureNewEnergyMicroCar"纯电动新能源小车,"MixedNewEnergyMicroCar,"混合新能源小车,"PureNewEnergyLargeCar",纯电动新能源大车
                                            # "MixedNewEnergyLargeCar"混合新能源大车
                                            # HumanFace Category:"Normal" 普通人脸,"HideEye" 眼部遮挡,"HideNose" 鼻子遮挡,"HideMouth" 嘴部遮挡,"TankCar"槽罐车(装化学药品、危险品)
                                            # object sub type,different object type has different sub type:
                                            # Vehicle Category:"Unknown","Motor","Non-Motor","Bus","Bicycle","Motorcycle",
                                            # "DregsCar", "Excavator", "Bulldozer", "Crane", "PumpTruck", "MachineshopTruck"
                                            # Plate Category:"Unknown","mal","Yellow","DoubleYellow","Police","Armed",
                                            # "Military","DoubleMilitary","SAR","Trainning"
                                            # "Personal" ,"Agri","Embassy","Moto","Tractor","Other"
                                            # HumanFace Category:"Normal","HideEye","HideNose","HideMouth","TankCar"
        ('wColorLogoIndex', c_ushort),      # 车标索引;the index of car logo
        ('wSubBrand', c_ushort),            # 车辆子品牌 需要通过映射表得到真正的子品牌 映射表详见开发手册;Specifies the sub-brand of vehicle,the real value can be found in a mapping table from the development manual
        ('byReserved1', c_ubyte),           # 保留字段;Reserve
        ('bPicEnble', c_bool),              # 是否有物体对应图片文件信息; picture info enable
        ('stPicInfo', SDK_PIC_INFO),        # 物体对应图片信息;picture info
        ('bShotFrame', c_bool),             # 是否是抓拍张的识别结果;is shot frame
        ('bColor', c_bool),                 # 物体颜色(rgbaMainColor)是否可用; rgbaMainColor is enable
        ('byReserved2', c_ubyte),           # 保留字段;Reserve
        ('byTimeType', c_ubyte),            # 时间表示类型,详见EM_TIME_TYPE说明;Time indicates the type of detailed instructions, EM_TIME_TYPE
        ('stuCurrentTime', NET_TIME_EX),    # 针对视频浓缩,当前时间戳（物体抓拍或识别时,会将此识别智能帧附在一个视频帧或jpeg图片中,此帧所在原始视频中的出现时间）
                                            # in view of the video compression,current time(when object snap or reconfnition, the frame will be attached to the frame in a video or pictures,means the frame in the original video of the time)
        ('stuStartTime', NET_TIME_EX),      # 开始时间戳（物体开始出现时);strart time(object appearing for the first time)
        ('stuEndTime', NET_TIME_EX),        # 结束时间戳（物体最后出现时）;end time(object appearing for the last time)
        ('stuOriginalBoundingBox', SDK_RECT),  # 包围盒(绝对坐标);original bounding box(absolute coordinates)
        ('stuSignBoundingBox', SDK_RECT),   # 车标坐标包围盒;sign bounding box coordinate
        ('dwCurrentSequence', C_DWORD),     # 当前帧序号（抓下这个物体时的帧）; The current frame number (frames when grabbing the object)
        ('dwBeginSequence', C_DWORD),       # 开始帧序号（物体开始出现时的帧序号）;Start frame number (object appeared When the frame number,
        ('dwEndSequence', C_DWORD),         # 结束帧序号（物体消逝时的帧序号）;The end of the frame number (when the object disappearing Frame number)
        ('nBeginFileOffset', c_int64),      # 开始时文件偏移, 单位: 字节（物体开始出现时,视频帧在原始视频文件中相对于文件起始处的偏移）;At the beginning of the file offset, Unit: Word Section (when objects began to appear, the video frames in the original video file offset relative to the beginning of the file,
        ('nEndFileOffset', c_int64),        # 结束时文件偏移, 单位: 字节（物体消逝时,视频帧在原始视频文件中相对于文件起始处的偏移）;At the end of the file offset, Unit: Word Section (when the object disappeared, video frames in the original video file offset relative to the beginning of the file)
        ('byColorSimilar', c_ubyte*8),      # 物体颜色相似度,取值范围：0-100,数组下标值代表某种颜色,详见EM_COLOR_TYPE;Object color similarity, the range :0-100, represents an array subscript Colors, see EM_COLOR_TYPE,
        ('byUpperBodyColorSimilar', c_ubyte*8), # 上半身物体颜色相似度(物体类型为人时有效);When upper body color similarity (valid object type man ,
        ('byLowerBodyColorSimilar', c_ubyte*8), # 下半身物体颜色相似度(物体类型为人时有效);Lower body color similarity when objects (object type human valid ,
        ('nRelativeID', c_int),             # 相关物体ID;ID of relative object
        ('szSubText', c_char*20),           # "ObjectType"为"Vehicle"或者"Logo"时,表示车标下的某一车系,比如奥迪A6L,由于车系较多,SDK实现时透传此字段,设备如实填写。
                                            # "ObjectType"is "Vehicle" or "Logo",  means a certain brand under LOGO, such as Audi A6L, since there are so many brands, SDK sends this field in real-time ,device filled as real.
        ('wBrandYear', c_ushort)            # 车辆品牌年款 需要通过映射表得到真正的年款 映射表详见开发手册;Specifies the model years of vehicle. the real value can be found in a mapping table from the development manual
    ]

class SDK_EVENT_FILE_INFO(Structure):
    """
    事件对应文件信息;event file info
    """
    _fields_ = [
        ('bCount', c_ubyte),                # 当前文件所在文件组中的文件总数;the file count in the current file's group
        ('bIndex', c_ubyte),                # 当前文件在文件组中的文件编号(编号1开始);the index of the file in the group
        ('bFileTag', c_ubyte),              # 文件标签, EM_EVENT_FILETAG;file tag, see the enum struct EM_EVENT_FILETAG
        ('bFileType', c_ubyte),             # 文件类型,0-普通 1-合成 2-抠图;file type,0-normal 1-compose 2-cut picture
        ('stuFileTime', NET_TIME_EX),       # 文件时间;file time
        ('nGroupId', C_DWORD)               # 同一组抓拍文件的唯一标识;the only id of one group file
    ]

class SDK_RESOLUTION_INFO(Structure):
    """
    图片分辨率;pic resolution
    """
    _fields_ = [
        ('snWidth', c_ushort),      # 宽;width
        ('snHight', c_ushort)       # 高;hight
    ]

class EVENT_CUSTOM_WEIGHT_INFO(Structure):
    """
    建委地磅定制称重信息;custom weight info
    """
    _fields_ = [
        ('dwRoughWeight', C_DWORD),     # 毛重,车辆满载货物重量。单位KG;Rough Weight,unit:KG
        ('dwTareWeight', C_DWORD),      # 皮重,空车重量。单位KG;Tare Weight,unit:KG
        ('dwNetWeight', C_DWORD),       # 净重,载货重量。单位KG;Net Weight,unit:KG
        ('bReserved', c_ubyte*28)       # 预留字节;Rough Weight,unit:KG
    ]

class NET_RADAR_FREE_STREAM(Structure):
    """
    雷达自由流信息;Radar free stream information
    """
    _fields_ = [
        ('nABSTime', C_TP_U64),             # 1年1月1日0时起至今的毫秒数;millisecond from 0001-01-01 00:00:00
        ('nVehicleID', c_int),              # 车辆ID;Vehicle ID
        ('unOBUMAC', c_uint),               # OBU的MAC地址;MAC of on board unit
        ('byReserved', c_ubyte*16)          # 保留字节;reserved
    ]

class EVENT_JUNCTION_CUSTOM_INFO(Structure):
    """
    卡口事件专用定制上报内容，定制需求增加到Custom下;custom info in
    """
    _fields_ = [
        ('stuWeightInfo', EVENT_CUSTOM_WEIGHT_INFO),    # 原始图片信息;custom weight info
        ('nCbirFeatureOffset', C_DWORD),                # 数据偏移，单位字节 （由于结构体保留字节有限的限制,添加在此处， 下同）;Content Based Image Retrieval Feature offset,Unit:Byte
        ('nCbirFeatureLength', C_DWORD),                # 数据大小，单位字节;Content Based Image Retrieval Feature length,Unit:Byte
        ('dwVehicleHeadDirection', C_DWORD),            # 车头朝向 0:未知 1:左 2:中 3:右;Head direction 0:Unknown 1:left 2:center 3:right
        ('byReserved1', c_ubyte*4),                     # 字节对齐;Align
        ('stuRadarFreeStream', NET_RADAR_FREE_STREAM),  # 雷达自由流信息;Radar free stream info
        ('bReserved', c_ubyte*12)                       # 预留字节;Reserved
    ]

class NET_GPS_INFO(Structure):
    """
    GPS信息;GPS Infomation
    """
    _pack_ = 4                              # 补齐
    _fields_ = [
        ('nLongitude', c_uint),             # 经度(单位是百万分之一度);Longitude(unit:1/1000000 degree)
                                            # 西经：0 - 180000000	实际值应为: 180*1000000 – dwLongitude;west Longitude: 0 - 180000000 practical value = 180*1000000 - dwLongitude
                                            # 东经：180000000 - 360000000	实际值应为: dwLongitude – 180*1000000;east Longitude: 180000000 - 360000000    practical value = dwLongitude - 180*1000000
                                            # 如: 300168866应为（300168866 - 180 * 1000000）/ 1000000 即东经120.168866度;eg: Longitude:300168866  (300168866 - 180*1000000)/1000000  equal east Longitude 120.168866 degree
        ('nLatidude', c_uint),              # 纬度(单位是百万分之一度);Latidude(unit:1/1000000 degree)
                                            # 南纬：0 - 90000000 实际值应为: 90*1000000 – dwLatidude;north Latidude: 0 - 90000000				practical value = 90*1000000 - dwLatidude
                                            # 北纬：90000000 – 180000000	实际值应为: dwLatidude – 90*1000000;south Latidude: 90000000 - 180000000	practical value = dwLatidude - 90*1000000
                                            # 如: 120186268应为 (120186268 - 90*1000000)/1000000 即北纬30. 186268度;eg: Latidude:120186268 (120186268 - 90*1000000)/1000000 equal south Latidude 30. 186268 degree
        ('dbAltitude', c_double),           # 高度,单位为米;altitude,unit:m
        ('dbSpeed', c_double),              # 速度,单位km/H;Speed,unit:km/H
        ('dbBearing', c_double),            # 方向角,单位°;Bearing,unit:°
        ('bReserved', c_ubyte*8)            # 保留字段;Reserved bytes
    ]

class NET_COLOR_RGBA(Structure):
    """
    颜色RGBA;color RGBA
    """
    _fields_ = [
        ('nRed', c_int),            # 红;red
        ('nGreen', c_int),          # 绿;green
        ('nBlue', c_int),           # 蓝;blue
        ('nAlpha', c_int)           # 透明;transparent
    ]

class NET_EXTENSION_INFO(Structure):
    """
    事件扩展信息;Extension info
    """
    _fields_ = [
        ('szEventID', c_char*52),       # 国标事件ID;Chinese standard event ID
        ('byReserved', c_ubyte*80)      # 保留字节;Reserved
    ]

class DRIVING_DIRECTION(Structure):
    """
    行驶方向;Driving direction
    """
    _fields_ = [
        ('DrivingDirection', c_char*256)    # 行驶方向;Driving direction
    ]

class SDK_SIG_CARWAY_INFO_EX(Structure):
    """
    车检器冗余信息;Vehicle detector redundancy info
    """
    _fields_ = [
        ('byRedundance', c_ubyte*8),        # 由车检器产生抓拍信号冗余信息;The vehicle detector generates the snap signal redundancy info
        ('bReserved', c_ubyte * 120)        # 保留字段;Reserved
    ]



class NET_WHITE_LIST_AUTHORITY_LIST(Structure):
    """
    白名单权限列表;authority list of white list
    """
    _fields_ = [
        ('bOpenGate', c_int),      # 是否有开闸权限;true:having open gate authority,false:no having open gate authority
        ('bReserved', c_ubyte*16)  # 保留字节;reserved
    ]


class NET_TRAFFICCAR_WHITE_LIST(Structure):
    """
    白名单信息;white list information
    """
    _fields_ = [
        ('bTrustCar', c_int),         # 车牌是否属于白名单;true: the car is trust car,false:the car is not trust car
        ('stuBeginTime', NET_TIME),   # 白名单起始时间;begin time of white list
        ('stuCancelTime', NET_TIME),  # 白名单过期时间;cancel time of white list
        ('stuAuthorityList', NET_WHITE_LIST_AUTHORITY_LIST),  # 白名单权限列表;authority list of white list
        ('bReserved', c_ubyte*32)     # 保留字节;Reserved
    ]

class NET_TRAFFICCAR_BLACK_LIST(Structure):
    """
    黑名单信息;Blacklist information
    """
    _fields_ = [
        ('bEnable', c_int),          # 黑名单信息;Enable blacklist
        ('bIsBlackCar', c_int),      # 车牌是否属于黑名单;Whether is the plate on the blacklist or not
        ('stuBeginTime', NET_TIME),  # 黑名单起始时间;Begin time
        ('stuCancelTime', NET_TIME), # 黑名单过期时间;Cancel time
        ('bReserved', c_ubyte * 32)  # 保留字节;Reserved
    ]

class NET_RECT(Structure):
    """
    事件上报携带卡片信息;Incidents reported to carry the card information
    """
    _fields_ = [
        ('nLeft', c_int),       # 左;Left
        ('nTop', c_int),        # 顶;Top
        ('nRight', c_int),      # 右;Right
        ('nBottom', c_int)      # 底;Bottom
    ]

class DEV_EVENT_TRAFFIC_TRAFFICCAR_INFO(Structure):
    """
    交通车辆信息;TrafficCar information
    """
    _fields_ = [
        ('szPlateNumber', c_char * 32),     # 车牌号码;plate number
        ('szPlateType', c_char * 32),       # 号牌类型 "Unknown" 未知; "Normal" 蓝牌黑牌; "Yellow" 黄牌; "DoubleYellow" 双层黄尾牌;Plate type: "Unknown" =Unknown; "Normal"=Blue and black plate. "Yellow"=Yellow plate. "DoubleYellow"=Double-layer yellow plate
                                            # "Police" 警牌; "Armed" 武警牌; "Military" 部队号牌; "DoubleMilitary" 部队双层;"Police"=Police plate ; "Armed"= =Military police plate; "Military"=Army plate; "DoubleMilitary"=Army double-layer
                                            # "SAR" 港澳特区号牌; "Trainning" 教练车号牌; "Personal" 个性号牌; "Agri" 农用牌;"SAR" =HK SAR or Macao SAR plate; "Trainning" =rehearsal plate; "Personal"=Personal plate; "Agri"=Agricultural plate
                                            # "Embassy" 使馆号牌; "Moto" 摩托车号牌; "Tractor" 拖拉机号牌; "Other" 其他号牌; "Embassy"=Embassy plate; "Moto"=Moto plate ; "Tractor"=Tractor plate; "Other"=Other plate
        ('szPlateColor', c_char * 32),      # 车牌颜色    "Blue","Yellow", "White","Black","YellowbottomBlackText","BluebottomWhiteText","BlackBottomWhiteText","ShadowGreen","YellowGreen"
                                            # plate color, "Blue","Yellow", "White","Black","YellowbottomBlackText","BluebottomWhiteText","BlackBottomWhiteText","ShadowGreen","YellowGreen"
        ('szVehicleColor', c_char * 32),    # 车身颜色    "White", "Black", "Red", "Yellow", "Gray", "Blue","Green";vehicle color, "White", "Black", "Red", "Yellow", "Gray", "Blue","Green"
        ('nSpeed', c_int),                  # 速度,单位Km/H;speed, Km/H
        ('szEvent', c_char*64),             # 触发的相关事件,参见事件列表Event List,只包含交通相关事件;trigger event type
        ('szViolationCode', c_char * 32),   # 违章代码;violation code
        ('szViolationDesc', c_char * 64),   # 违章描述;violation describe
        ('nLowerSpeedLimit', c_int),        # 速度下限;lower speed limit
        ('nUpperSpeedLimit', c_int),        # 速度上限;upper speed limit
        ('nOverSpeedMargin', c_int),        # 限高速宽限值,单位：km/h;over speed margin, km/h
        ('nUnderSpeedMargin', c_int),       # 限低速宽限值,单位：km/h;under speed margin, km/h
        ('nLane', c_int),                   # 车道,参见事件列表Event List中卡口和路口事件;lane
        ('nVehicleSize', c_int),            # 车辆大小,-1表示未知,否则按位;vehicle size, see VideoAnalyseRule's describe
                                             # 第0位:"Light-duty", 小型车;Bit 0:"Light-duty", small car
                                             # 第1位:"Medium", 中型车;Bit 1:"Medium", medium car
                                             # 第2位:"Oversize", 大型车;Bit 2:"Oversize", large car
                                             # 第3位:"Minisize", 微型车;Bit 3:"Minisize", mini car
                                             # 第4位:"Largesize", 长车;Bit 4:"Largesize", long car
        ('fVehicleLength', c_float),        # 车辆长度,单位米;vehicle length, Unit:m
        ('nSnapshotMode', c_int),           # 抓拍方式,0-未分类,1-全景,2-近景,4-同向抓拍,8-反向抓拍,16-号牌图像;snap mode 0-normal,1-globle,2-near,4-snap on the same side,8-snap on the reverse side,16-plant picture
        ('szChannelName', c_char*32),       # 本地或远程的通道名称,可以是地点信息,来源于通道标题配置ChannelTitle.Name;channel name
        ('szMachineName', c_char*256),      # 本地或远程设备名称,来源于普通配置General.MachineName;Machine name
        ('szMachineGroup', c_char * 256),   # 机器分组或叫设备所属单位,默认为空,用户可以将不同的设备编为一组,便于管理,可重复;machine group
        ('szRoadwayNo', c_char*64),         # 道路编号;road way number
        ('szDrivingDirection', DRIVING_DIRECTION * 3),      # 行驶方向 , "DrivingDirection" : ["Approach", "上海", "杭州"];DrivingDirection: for example ["Approach", "Shanghai", "Hangzhou"]
                                                            # "Approach"-上行,即车辆离设备部署点越来越近；"Leave"-下行;"Approach" means driving direction,where the car is more near;"Leave"-means where if mor far to the car
                                                            # 即车辆离设备部署点越来越远,第二和第三个参数分别代表上行和下行的两个地点;the second and third param means the location of the driving direction
        ('szDeviceAddress', c_char_p),      # 设备地址,OSD叠加到图片上的,来源于配置TrafficSnapshot.DeviceAddress,'\0'结束;device address,OSD superimposed onto the image,from TrafficSnapshot.DeviceAddress,'\0'means end.
        ('szVehicleSign', c_char*32),       # 车辆标识, 例如 "Unknown"-未知, "Audi"-奥迪, "Honda"-本田 ...;Vehicle identification, such as "Unknown" - unknown "Audi" - Audi, "Honda" - Honda ...
        ('stuSigInfo', SDK_SIG_CARWAY_INFO_EX),             # 由车检器产生抓拍信号冗余信息;Generated by the vehicle inspection device to capture the signal redundancy
        ('szMachineAddr', c_char_p),        # 设备部署地点;Equipment deployment locations
        ('fActualShutter', c_float),        # 当前图片曝光时间,单位为毫秒;Current picture exposure time, in milliseconds
        ('byActualGain', c_ubyte),          # 当前图片增益,范围为0~100;Current picture gain, ranging from 0 to 100
        ('byDirection', c_ubyte),           # 车道方向,0-南向北 1-西南向东北 2-西向东 3-西北向东南 4-北向南 5-东北向西南 6-东向西 7-东南向西北 8-未知 9-自定义;
                                            # Lane Direction,0 - south to north 1- Southwest to northeast 2 - West to east, 3 - Northwest to southeast 4 - north to south 5 - northeast to southwest 6 - East to West 7 - Southeast to northwest 8 - Unknown 9-customized
        ('byReserved', c_ubyte*2),          # 预留字节;Reserved
        ('szDetailedAddress', c_char_p),    # 详细地址, 作为szDeviceAddress的补充;Address, as szDeviceAddress supplement
        ('szDefendCode', c_char*64),        # 图片防伪码;waterproof
        ('nTrafficBlackListID', c_int),     # 关联黑名单数据库记录默认主键ID, 0,无效；> 0,黑名单数据记录;Link black list data recorddefualt main keyID, 0, invalid, > 0, black list data record
        ('stuRGBA', NET_COLOR_RGBA),        # 车身颜色RGBA;bofy color RGBA
        ('stSnapTime', NET_TIME),           # 抓拍时间;snap time
        ('nRecNo', c_int),                  # 记录编号;Rec No
        ('szCustomParkNo', c_char*33),      # 自定义车位号（停车场用）;self defined parking space number, for parking
        ('byReserved1', c_ubyte * 3),       # 预留字节;Reserved
        ('nDeckNo', c_int),                 # 车板位号;Metal plate No.
        ('nFreeDeckCount', c_int),          # 空闲车板数量;Free metal plate No.
        ('nFullDeckCount', c_int),          # 占用车板数量;Occupized metal plate No.
        ('nTotalDeckCount', c_int),         # 总共车板数量;Total metal plate No.
        ('szViolationName', c_char * 64),   # 违章名称;violation name
        ('nWeight', c_uint),                # 车重(单位 Kg);Weight of car(kg)
        ('szCustomRoadwayDirection', c_char * 32),  # 自定义车道方向,byDirection为9时有效;custom road way, valid when byDirection is 9
        ('byPhysicalLane', c_ubyte),        # 物理车道号,取值0到5;the physical lane number,value form 0 to 5
        ('byReserved2', c_ubyte * 3),       # 预留字节;Reserved
        ('emMovingDirection', c_int),       # 车辆行驶方向,值的意义见EM_TRAFFICCAR_MOVE_DIRECTION;moving direction
        ('stuEleTagInfoUTC', NET_TIME),     # 对应电子车牌标签信息中的过车时间(ThroughTime);corresponding to throughTime
        ('stuCarWindowBoundingBox', NET_RECT),          # 车窗包围盒，0~8191;The BoundingBox of car window , 0~8191
        ('stuWhiteList', NET_TRAFFICCAR_WHITE_LIST),    # 白名单信息;white list information
        ('emCarType', c_int),               # 车辆类型,详见EM_TRAFFICCAR_CAR_TYPE;car type,refer to EM_TRAFFICCAR_CAR_TYPE
        ('emLaneType', c_int),              # 车道类型,详见EM_TRAFFICCAR_LANE_TYPE;Lane type,refer to EM_TRAFFICCAR_LANE_TYPE
        ('szVehicleBrandYearText', c_char * 64),        # 车系年款翻译后文本内容;Translated year of vehicle
        ('szCategory', c_char * 32),        # 车辆子类型;category
        ('stuBlackList',NET_TRAFFICCAR_BLACK_LIST),     # 黑名单信息;Blacklist information
        ('bReserved', c_ubyte * 240)        # 保留字节,留待扩展;Reserved bytes.
    ]

class EVENT_CARD_INFO(Structure):
    """
    事件上报携带卡片信息;Incidents reported to carry the card information
    """
    _fields_ = [
        ('szCardNumber', c_char*36),       # 卡片序号字符串;Card number string
        ('bReserved', c_ubyte*32)          # 保留字节,留待扩展;Reserved bytes, leave extended
    ]

class SDK_MSG_OBJECT_EX(Structure):
    """
    视频分析物体信息扩展结构体;Video analysis object info expansion structure
    """
    _pack_ = 4  # 补齐
    _fields_ = [
        ('dwSize', C_DWORD),            # 结构体大小;Structure size
        ('nObjectID', c_int),           # 物体ID,每个ID表示一个唯一的物体;object ID, each ID means a exclusive object
        ('szObjectType', c_char * 128), # 物体类型;object type
        ('nConfidence', c_int),         # 置信度(0~255),值越大表示置信度越高;confidence coefficient (0~255),  value the bigger means  confidence coefficient the higher
        ('nAction', c_int),             # 物体动作:1:Appear 2:Move 3:Stay 4:Remove 5:Disappear 6:Split 7:Merge 8:Rename;object  motion :1:Appear 2:Move 3:Stay 4:Remove 5:Disappear 6:Split 7:Merge 8:Rename
        ('BoundingBox', SDK_RECT),      # 包围盒;box
        ('Center', SDK_POINT),          # 物体型心;object model center
        ('nPolygonNum', c_int),         # 多边形顶点个数;polygon vertex number
        ('Contour', SDK_POINT * 16),    # 较精确的轮廓多边形;relatively accurate outline the polygon
        ('rgbaMainColor', C_DWORD),     # 表示车牌、车身等物体主要颜色；按字节表示,分别为红、绿、蓝和透明度,例如:RGB值为(0,255,0),透明度为0时, 其值为0x00ff0000.;means plate, vehicle body and etc. object major color, by byte means , are red, green, blue and transparency , such as:RGB value is (0,255,0), transparency is 0, its value is 0x00ff0000.
        ('szText', c_char * 128),       # 同SDK_MSG_OBJECT相应字段;same as SDK_MSG_OBJECT corresponding field
        ('szObjectSubType', c_char * 64), # 物体子类别,根据不同的物体类型,可以取以下子类型,同NET_MSG_OBJECT相应字段;object sub type , according to different object  types , may use the following sub type,same as NET_MSG_OBJECT field
        ('byReserved1', c_ubyte * 3),   # 保留字节;Reserved
        ('bPicEnble', c_bool),          # 是否有物体对应图片文件信息;object corresponding to picture file info or not
        ('stPicInfo', SDK_PIC_INFO),    # 物体对应图片信息;object corresponding to picture info
        ('bShotFrame', c_bool),         # 是否是抓拍张的识别结果;snapshot recognition result or not
        ('bColor', c_bool),             # 物体颜色(rgbaMainColor)是否可用;object  color (rgbaMainColor) usable or not
        ('bLowerBodyColor', c_ubyte),   # 下半身颜色(rgbaLowerBodyColor)是否可用;lower color (rgbaLowerBodyColor) usable or not
        ('byTimeType', c_ubyte),        # 时间表示类型,详见EM_TIME_TYPE说明;time means type ,  see EM_TIME_TYPE note
        ('stuCurrentTime', NET_TIME_EX),# 针对视频浓缩,当前时间戳（物体抓拍或识别时,会将此识别智能帧附在一个视频帧或jpeg图片中,此帧所在原始视频中的出现时间）
                                        # for video compression,  current time stamp, object snapshot or recognition,  attach this recognition frame in one vire frame or jpegpicture, this frame appearance time in original video,
        ('stuStartTime', NET_TIME_EX),  # 开始时间戳（物体开始出现时）;start time stamp, object start appearance
        ('stuEndTime', NET_TIME_EX),    # 结束时间戳（物体最后出现时）;end time stamp, object last aapearance
        ('stuOriginalBoundingBox', SDK_RECT),   # 包围盒(绝对坐标);box(absolute coordinate)
        ('stuSignBoundingBox', SDK_RECT),       # 车标坐标包围盒;LGO coordinate box
        ('dwCurrentSequence', C_DWORD),         # 当前帧序号（抓下这个物体时的帧）;current frame no., snapshot this object frame
        ('dwBeginSequence', C_DWORD),   # 开始帧序号（物体开始出现时的帧序号）;start frame no., object start appearance frame no.
        ('dwEndSequence', C_DWORD),     # 结束帧序号（物体消逝时的帧序号）;end frame no., object disappearance frame no.
        ('nBeginFileOffset', C_LLONG),  # 开始时文件偏移, 单位: 字节（物体开始出现时,视频帧在原始视频文件中相对于文件起始处的偏移）
                                        # start file shift, unit: byte, object start appearance, video in original video file moves toward file origin
        ('nEndFileOffset', C_LLONG),    # 结束时文件偏移, 单位: 字节（物体消逝时,视频帧在原始视频文件中相对于文件起始处的偏移）
                                        # End file shift, unit: byte, object disappearance, video in original video file moves toward file origin
        ('byColorSimilar', c_ubyte * 8),            # 物体颜色相似度,取值范围：0-100,数组下标值代表某种颜色,详见 EM_COLOR_TYPE
                                                    # object  color similarity, take  value range :0-100, group subscript value represents certain color ,  see EM_COLOR_TYPE
        ('byUpperBodyColorSimilar', c_ubyte * 8),   # 上半身物体颜色相似度(物体类型为人时有效);upper object  color  similarity (object  type as human is valid )
        ('byLowerBodyColorSimilar', c_ubyte * 8),   # 下半身物体颜色相似度(物体类型为人时有效);lower object  color  similarity (object  type as human is valid )
        ('nRelativeID', c_int),                     # 相关物体ID;related object ID
        ('szSubText', c_char * 20),                 # "ObjectType"为"Vehicle"或者"Logo"时,表示车标下的某一车系,比如奥迪A6L,由于车系较多,SDK实现时透传此字段,设备如实填写。
                                                    # "ObjectType"is "Vehicle"or "Logo",  means LOGO lower brand, such as Audi A6L, since there are many brands, SDK shows this field in real-time,device filled as real.
        ('nPersonStature', c_int),                  # 入侵人员身高,单位cm;Intrusion staff height, unit cm
        ('emPersonDirection', c_int),               # 人员入侵方向,详见EM_MSG_OBJ_PERSON_DIRECTION;Staff intrusion direction,refer to EM_MSG_OBJ_PERSON_DIRECTION
        ('rgbaLowerBodyColor', C_DWORD)             # 使用方法同rgbaMainColor,物体类型为人时有效;Use direction same as rgbaMainColor,object  type as human is valid
    ]

class SDK_EXTRA_PLATE_NUMBER(Structure):
    """
    额外车牌信息;Extra plate number
    """
    _fields_ = [
        ('szNumber', c_char*32)  # 额外车牌信息;Extra plate number
    ]

class EVENT_COMM_STATUS(Structure):
    """
    违规状态;illegal state type of driver
    """
    _fields_ = [
        ('bySmoking', c_ubyte),     # 是否抽烟;smoking
        ('byCalling', c_ubyte),     # 是否打电话;calling
        ('szReserved', c_char*14),  # 预留字段;reversed
    ]

class EVENT_COMM_SEAT(Structure):
    """
    驾驶位违规信息;driver's illegal info
    """
    _fields_ = [
        ('bEnable', c_int),               # 是否检测到座驾信息;whether seat info detected
        ('emSeatType', c_int),            # 座驾类型, 0:未识别; 1:主驾驶; 2:副驾驶,详见EM_COMMON_SEAT_TYPE;seat type,refer to EM_COMMON_SEAT_TYPE
        ('stStatus', EVENT_COMM_STATUS),  # 违规状态;illegal state
        ('emSafeBeltStatus', c_int),      # 安全带状态,详见NET_SAFEBELT_STATE;safe belt state,refer to NET_SAFEBELT_STATE
        ('emSunShadeStatus', c_int),      # 遮阳板状态,详见NET_SUNSHADE_STATE;sun shade state,refer to NET_SUNSHADE_STATE
        ('szReserved', c_ubyte * 24),     # 预留字节; reversed
    ]

class EVENT_COMM_ATTACHMENT(Structure):
    """
    车辆物件;car attachment
    """
    _fields_ = [
        ('emAttachmentType', c_int),    # 物件类型,详见EVENT_COMM_ATTACHMENT;type，refer to EVENT_COMM_ATTACHMENT
        ('stuRect', NET_RECT),          # 坐标;coordinate
        ('bReserved', c_ubyte*20),      # 预留字节;reserved
    ]

class EVENT_PIC_INFO(Structure):
    """
    交通抓图图片信息;traffic event snap picture info
    """
    _fields_ = [
        ('nOffset', C_DWORD),  # 原始图片偏移，单位字节;offset,Unit:byte
        ('nLength', C_DWORD),  # 原始图片长度，单位字节;length of picture,Unit:byte
    ]

class NET_RFIDELETAG_INFO(Structure):
    """
    RFID 电子车牌标签信息;the info of RFID electronic tag
    """
    _fields_ = [
        ('szCardID', c_ubyte*16),       # 卡号;card ID
        ('nCardType', c_int),           # 卡号类型, 0:交通管理机关发行卡, 1:新车出厂预装卡;card type, 0:issued by transport administration offices, 1:new factory preloaded card
        ('emCardPrivince', c_int),      # 卡号省份,详见EM_CARD_PROVINCE;card privince,refer to EM_CARD_PROVINCE
        ('szPlateNumber', c_char*32),   # 车牌号码;plate number
        ('szProductionDate', c_char * 16),  # 出厂日期;production data
        ('emCarType', c_int),           # 车辆类型,详见EM_CAR_TYPE;car type,refer to EM_CAR_TYPE
        ('nPower', c_int),              # 功率,单位：千瓦时，功率值范围0~254；255表示该车功率大于可存储的最大功率值
                                        # power, unit:kilowatt-hour, range:0~254, 255 means larger than maximum power value can be stored
        ('nDisplacement', c_int),       # 排量,单位：百毫升，排量值范围0~254；255表示该车排量大于可存储的最大排量值
                                        # displacement, unit:100ml, range:0~254, 255 means larger than maximum displacement value can be stored
        ('nAntennaID', c_int),          # 天线ID，取值范围:1~4;antenna ID, range:1~4
        ('emPlateType', c_int),         # 号牌种类,详见EM_PLATE_TYPE;plate type,refer to EM_PLATE_TYPE
        ('szInspectionValidity', c_char*16),    # 检验有效期，年-月;validity of inspection, year-month
        ('nInspectionFlag', c_int),     # 逾期未年检标志, 0:已年检, 1:逾期未年检;the flag of inspetion, 0:already inspection, 1:not inspection
        ('nMandatoryRetirement', c_int), # 强制报废期，从检验有效期开始，距离强制报废期的年数;the years form effective inspection preiod to compulsory discarding preiod
        ('emCarColor', c_int),           # 车身颜色，详见EM_CAR_COLOR_TYPE;car color,refer to EM_CAR_COLOR_TYPE
        ('nApprovedCapacity', c_int),    # 核定载客量，该值<0时：无效；此值表示核定载客，单位为人;authorized capacity, unit:people, <0:incalid
        ('nApprovedTotalQuality', c_int), # 此值表示总质量，单位为百千克；该值<0时：无效；该值的有效范围为0~0x3FF，0x3FF（1023）表示数据值超过了可存储的最大值;total weight, unit:100kg, range:0~0x3FF,  0x3FF1023:larger than maximum value can be stored, <0:invalid
        ('stuThroughTime', NET_TIME_EX),  # 过车时间;the time when the car is pass
        ('emUseProperty', c_int),         # 使用性质,详见EM_USE_PROPERTY_TYPE;use property,refer to EM_USE_PROPERTY_TYPE
        ('szPlateCode', c_char*8),        # 发牌代号，UTF-8编码;Licensing code, UTF-8 encoding
        ('szPlateSN', c_char * 16),       # 号牌号码序号，UTF-8编码;Plate number, serial number, UTF-8 code
        ('szTID', c_char * 64),           # 标签(唯一标识), UTF-8编码;Label (Unique identifier), UTF-8 encoding
        ('bReserved', c_ubyte * 40),      # 保留字节,留待扩展;Reserved
    ]

class EVENT_COMM_INFO(Structure):
    """
    事件上报携带卡片信息;Incidents reported to carry the card information
    """
    _fields_ = [
        ('emNTPStatus', c_int),      # NTP校时状态,详见EM_NTP_STATUS;NTP time sync status,refer to EM_NTP_STATUS
        ('nDriversNum', c_int),      # 驾驶员信息数;driver info number
        ('pstDriversInfo', POINTER(SDK_MSG_OBJECT_EX)),  # 保驾驶员信息数据;driver info data
        ('pszFilePath', c_char_p),   # 本地硬盘或者sd卡成功写入路径,为None时,路径不存在;writing path for local disk or sd card, or write to default path if None
        ('pszFTPPath', c_char_p),    # 设备成功写到ftp服务器的路径;ftp path
        ('pszVideoPath', c_char_p),  # 当前接入需要获取当前违章的关联视频的FTP上传路径;ftp path for assocated video
        ('stCommSeat', EVENT_COMM_SEAT*8),  # 驾驶位信息;Seat info
        ('nAttachmentNum', c_int),   # 车辆物件个数;Car Attachment number
        ('stuAttachment', EVENT_COMM_ATTACHMENT*8),   # 车辆物件信息;Car Attachment
        ('nAnnualInspectionNum', c_int),        # 年检标志个数;Annual Inspection number
        ('stuAnnualInspection', NET_RECT*8),    # 年检标志;Annual Inspection
        ('fHCRatio', c_float),       # HC所占比例，单位：%/1000000;The ratio of HC,unit,%/1000000
        ('fNORatio', c_float),       # NO所占比例，单位：%/1000000;The ratio of NO,unit,%/1000000
        ('fCOPercent', c_float),     # CO所占百分比，单位：% 取值0~100;The percent of CO,unit,% ,range from 0 to 100
        ('fCO2Percent', c_float),    # CO2所占百分比，单位：% 取值0~100;The percent of CO2,unit: % ,range from 0 to 100
        ('fLightObscuration', c_float), # 不透光度，单位：% 取值0~100;The obscuration of light,unit,% ,range from 0 to 100
        ('nPictureNum', c_int),      # 原始图片张数;Original pictures info number
        ('stuPicInfos', EVENT_PIC_INFO*6),  # 原始图片信息;Original pictures info data
        ('fTemperature', c_float),   # 温度值,单位摄氏度;Temperature,unit: centigrade
        ('nHumidity', c_int),        # 相对湿度百分比值;Humidity,unit: %
        ('fPressure', c_float),      # 气压值,单位Kpa;Pressure,unit: Kpa
        ('fWindForce', c_float),     # 风力值,单位m/s;Wind force,unit: m/s
        ('nWindDirection', c_uint),  # 风向,单位度,范围:[0,360];Wind direction,unit: degree,range:[0,360]
        ('fRoadGradient', c_float),  # 道路坡度值,单位度;Road gradient,unit: degree
        ('fAcceleration', c_float),  # 加速度值,单位:m/s2;Acceleration,unit: m/s2
        ('stuRFIDEleTagInfo', NET_RFIDELETAG_INFO),   # RFID 电子车牌标签信息;RFID electronics tag info
        ('stuBinarizedPlateInfo', EVENT_PIC_INFO),    # 二值化车牌抠图;Binarized plate matting
        ('stuVehicleBodyInfo', EVENT_PIC_INFO),       # 车身特写抠图;Vehicle body close-up matting
        ('emVehicleTypeInTollStation', c_int),        # 收费站车型分类,详见EM_VEHICLE_TYPE;Vehicle type inToll station,refer to EM_VEHICLE_TYPE
        ('emSnapCategory', c_int),                    # 抓拍的类型，默认为机动车，详见EM_SNAPCATEGORY;Snap Category;,refer to EM_SNAPCATEGORY
        ('nRegionCode', c_int),                       # 车牌所属地区代码,(孟加拉海外车牌识别项目),默认-1表示未识别;Location code of license plate,(Bangladesh Project),default -1 indicates unrecognized
        ('emVehicleTypeByFunc', c_int),               # 按功能划分的车辆类型，详见EM_VEHICLE_TYPE_BY_FUNC;Vehicle type by function,refer to EM_VEHICLE_TYPE_BY_FUNC
        ('emStandardVehicleType', c_int),             # 标准车辆类型，详见EM_STANDARD_VEHICLE_TYPE;Standard vehicle type,refer to EM_STANDARD_VEHICLE_TYPE
        ('nExtraPlateCount', c_uint),                 # 额外车牌数量;Count of extra plates
        ('szExtraPlateNumber', SDK_EXTRA_PLATE_NUMBER * 3),  # 额外车牌信息;Extra plate number
        ('emOverseaVehicleCategory', c_int),                # 海外车辆类型中的子类别，详见EM_OVERSEA_VEHICLE_CATEGORY_TYPE;oversea vehicle category,refer to EM_OVERSEA_VEHICLE_CATEGORY_TYPE
        ('szProvince', c_char*64),                          # 车牌所属国家的省、州等地区名;Province
        ('bReserved', c_ubyte*500),                         # 预留字节;reserved
        ('szCountry', c_char*20)                            # 国家;Country
    ]
class NET_NONMOTOR_PIC_INFO(Structure):
    """
    非机动车抠图信息;Non-Motor Image
    """
    _fields_ = [
        ('uOffset', c_uint),            # 在二进制数据块中的偏移;Offset
        ('uLength', c_uint),            # 图片大小,单位：字节;Image size, Unit : Byte
        ('uWidth', c_uint),             # 图片宽度;Image Width
        ('uHeight', c_uint),            # 图片高度;Image Height
        ('szFilePath', c_char*260),     # 文件路径;FilePath
        ('byReserved', c_ubyte*512),    # 保留字节;Reserved
    ]

class RIDER_FACE_IMAGE_INFO(Structure):
    """
    骑车人脸图片信息;face image information
    """
    _fields_ =[
        ('nOffSet', c_uint),    # 在二进制数据块中的偏移;image offset in the data
        ('nLength', c_uint),    # 图片大小,单位字节;Image size, Unit : Byte
        ('nWidth', c_uint),     # 图片宽度(像素);Image width(pixel)
        ('nHeight', c_uint),    # 图片高度(像素);Image height(pixel)
        ('byReserved', c_ubyte*48), # 保留字节;Reserved
    ]

class NET_FACE_ATTRIBUTE_EX(Structure):
    """
    人脸属性;Face attribute
    """
    _fields_ =[
        ('emSex', c_uint),                  # 性别，详见EM_SEX_TYPE;Sex，refer to EM_SEX_TYPE
        ('nAge', c_int),                    # 年龄,-1表示该字段数据无效;age,-1 means invalid
        ('emComplexion', c_int),            # 肤色,详见EM_COMPLEXION_TYPE;Complexion,refer to EM_COMPLEXION_TYPE
        ('emEye', c_int),                   # 眼睛状态,详见EM_EYE_STATE_TYPE;Eye state,refer to EM_EYE_STATE_TYPE
        ('emMouth', c_int),                 # 嘴巴状态,详见EM_MOUTH_STATE_TYPE;Mouth state,refer to EM_MOUTH_STATE_TYPE
        ('emMask', c_int),                  # 口罩状态,详见EM_MASK_STATE_TYPE;Mask state,refer to EM_MASK_STATE_TYPE
        ('emBeard', c_int),                 # 胡子状态,详见EM_BEARD_STATE_TYPE;Beard state,refer to EM_BEARD_STATE_TYPE
        ('nAttractive', c_int),             # 魅力值, 0未识别，识别时范围1-100,得分高魅力高;Attractive, 0 Not distinguish,Range[1,100]
        ('emGlass', c_int),                 # 眼镜,详见EM_HAS_GLASS;Glasses,refer to EM_HAS_GLASS
        ('emEmotion', c_int),               # 表情,详见EM_EMOTION_TYPE;Emotion,refer to EM_EMOTION_TYPE
        ('stuBoundingBox', SDK_RECT),       # 包围盒(8192坐标系);BoundingBox(8192 Coordinate)
        ('bReserved1', C_BYTE*4), 
        ('emStrabismus', c_int),            # 斜视状态,详见EM_STRABISMUS_TYPE;Strabismus,refer to EM_STRABISMUS_TYPE
        ('byReserved', c_ubyte*64),         # 保留字节,留待扩展;Reserved
    ]

class NET_RIDER_INFO(Structure):
    """
    骑车人信息;Rider information
    """
    _fields_ = [
        ('bFeatureValid', c_int),       # 是否识别到特征信息, TRUE时下面数据才有效;Enable
        ('emSex', c_int),               # 性别,详见EM_SEX_TYPE;its sex,refer to EM_SEX_TYPE
        ('nAge', c_int),                # 年龄;its age
        ('emHelmet', c_int),            # 头盔状态,详见EM_NONMOTOR_OBJECT_STATUS;Whether or not wearing a helmet,refer to EM_NONMOTOR_OBJECT_STATUS
        ('emCall', c_int),              # 是否在打电话,详见EM_NONMOTOR_OBJECT_STATUS;Whether on the phone,refer to EM_NONMOTOR_OBJECT_STATUS
        ('emBag', c_int),               # 是否有背包,详见EM_NONMOTOR_OBJECT_STATUS; Whether or not have bag,refer to EM_NONMOTOR_OBJECT_STATUS
        ('emCarrierBag', c_int),        # 有没有手提包,详见EM_NONMOTOR_OBJECT_STATUS;Whether or not have carrierbag,refer to EM_NONMOTOR_OBJECT_STATUS
        ('emUmbrella', c_int),          # 是否打伞,详见EM_NONMOTOR_OBJECT_STATUS;Whether an umbrella,refer to EM_NONMOTOR_OBJECT_STATUS
        ('emGlasses', c_int),           # 是否有带眼镜,详见EM_NONMOTOR_OBJECT_STATUS; Whether or not wear glasses,refer to EM_NONMOTOR_OBJECT_STATUS
        ('emMask', c_int),              # 是否带口罩,详见EM_NONMOTOR_OBJECT_STATUS;Whether to wear a face mask,refer to EM_NONMOTOR_OBJECT_STATUS
        ('emEmotion', c_int),           # 表情,详见EM_EMOTION_TYPE;Emotion,refer to EM_EMOTION_TYPE
        ('emUpClothes', c_int),         # 上衣类型,详见EM_CLOTHES_TYPE;UpClothes type,refer to EM_CLOTHES_TYPE
        ('emDownClothes', c_int),       # 下衣类型,详见EM_CLOTHES_TYPE;DownClothes type,refer to EM_CLOTHES_TYPE
        ('emUpperBodyColor', c_int),    # 上衣颜色,详见EM_OBJECT_COLOR_TYPE;UpClothes color,refer to EM_OBJECT_COLOR_TYPE
        ('emLowerBodyColor', c_int),    # 下衣颜色,详见EM_OBJECT_COLOR_TYPE;DownClothes color,refer to EM_OBJECT_COLOR_TYPE
        ('bHasFaceImage', c_int),       # 是否有骑车人人脸抠图信息;Whether rider's face image information is contained
        ('stuFaceImage', RIDER_FACE_IMAGE_INFO),    # 骑车人人脸特写描述;Rider face image
        ('bHasFaceAttributes', c_int),  # 是否有人脸属性;Whether rider's face Attributes is contained
        ('stuFaceAttributes', NET_FACE_ATTRIBUTE_EX),   # 人脸属性;face Attributes
        ('emHasHat', c_int),            # 是否戴帽子,详见EM_HAS_HAT;whether has hat,refer to EM_HAS_HAT
        ('emCap', c_int),               # 帽类型,详见EM_CAP_TYPE;Cap type,refer to EM_CAP_TYPE
        ('emHairStyle', c_int),         # 头发样式,详见EM_HAIR_STYLE; Hair style,refer to EM_HAIR_STYLE
        ('byReserved', c_ubyte*304),    # 保留字节;Reserved
    ]

class SCENE_IMAGE_INFO(Structure):
    """
    全景广角图;Scene image
    """
    _fields_ = [
        ('nOffSet', c_uint),            # 在二进制数据块中的偏移;image offset in the data
        ('nLength', c_uint),            # 图片大小,单位字节;image data length
        ('nWidth', c_uint),             # 图片宽度(像素);image width(pixel)
        ('nHeight', c_uint),            # 图片高度(像素);image Height(pixel)
        ('byReserved', c_ubyte*56),     # 预留字节;Reserved
    ]

class FACE_SCENE_IMAGE(Structure):
    """
   人脸全景图; Face scene image
    """
    _fields_ = [
        ('nOffSet', c_uint),    # 在二进制数据块中的偏移;image offset in the data
        ('nLength', c_uint),    # 图片大小,单位字节;image data length
        ('nWidth', c_uint),     # 图片宽度(像素);image width(pixel)
        ('nHeight', c_uint),    # 图片高度(像素);image Height(pixel)
        ('byReserved', c_ubyte * 56),  # 预留字节;Reserved
    ]

class NET_NONMOTOR_FEATURE_VECTOR_INFO(Structure):
    """
    非机动车特征值数据在二进制数据中的位置信息;Position info of non-motor feature data in binary data
    """
    _fields_ = [
        ('nOffset', c_uint),            # 非机动车特征值在二进制数据中的偏移, 单位:字节;The offset of non-motor feature data in binary data, unit:bytes
        ('nLength', c_uint),            # 非机动车特征值数据长度, 单位:字节;The length of non-motor feature data, unit:bytes
        ('byReserved', c_ubyte*32),     # 保留字节;Reserved
    ]

class NET_NONMOTOR_PLATE_IMAGE(Structure):
    """
    非机动车车牌图片信息;The plate image of no-motor
    """
    _fields_ = [
        ('nOffset', c_uint),            # 在二进制数据块中的偏移;image offset in the data
        ('nLength', c_uint),            # 图片大小,单位字节;image data length，Unit:byte
        ('nWidth', c_uint),             # 图片宽度;image width
        ('nHeight', c_uint),            # 图片高度;image Height
        ('byReserved', c_ubyte * 512),  # 预留字节;Reserved
    ]


class NET_NONMOTOR_PLATE_INFO(Structure):
    """
    非机动车配牌信息;Plate info of nomotor
    """
    _fields_ = [
        ('szPlateNumber', c_char*128),                  # 非机动车车牌号;plate number
        ('stuBoundingBox', NET_RECT),                   # 包围盒， 非机动车矩形框，0~8191相对坐标;BoundingBox Rect, 0~8192
        ('stuOriginalBoundingBox', NET_RECT),           # 包围盒， 非机动车矩形框，绝对坐标;BoundingBox Rect, absolute coordinates
        ('stuPlateImage', NET_NONMOTOR_PLATE_IMAGE),    # 非机动车车牌抠图;plate image info
        ('emPlateColor', c_int),                        # 车牌颜色; Plate color
        ('byReserved', c_ubyte*132),                    # 保留;Reserved

    ]


class EVENT_INTELLI_COMM_INFO(Structure):
    """
    智能报警事件公共信息;intelli event comm info
    """
    _fields_ = [
        ('emClassType', c_int),             # 智能事件所属大类,详见EM_CLASS_TYPE;class type，refer to EM_CLASS_TYPE
        ('nPresetID', c_int),               # 该事件触发的预置点，取值范围为0~255，大于0表示在此预置点时有效。
                                            # Preset ID, value range is 0~255 and when the value is greater than 0 is valied
        ('bReserved', c_ubyte*124),         # 保留字节,留待扩展;reserved
    ]

class EVENT_PLATE_INFO(Structure):
    """
    车辆信息，记录了车头、车尾车牌号和车牌颜色;Plate info, Record the plate number and color of the front and back of the car
    """
    _fields_ = [
        ('szFrontPlateNumber', c_char*64),      # 车头车牌号码;front plate number
        ('emFrontPlateColor', c_int),           # 车头车牌颜色,详见EM_PLATE_COLOR_TYPE;front plate color,refer to EM_PLATE_COLOR_TYPE
        ('szBackPlateNumber', c_char * 64),     # 车尾车牌号码;back plate number
        ('emBackPlateColor', c_int),            # 车尾车牌颜色,详见EM_PLATE_COLOR_TYPE;back plate color,refer to EM_PLATE_COLOR_TYPE
        ('reversed', c_ubyte*128),              # 保留;reserved
    ]

class VA_OBJECT_NONMOTOR(Structure):
    """
    非机动车对象;Nonmotor
    """
    _fields_ = [
        ('nObjectID', c_int),           # 物体ID,每个ID表示一个唯一的物体;Object id
        ('emCategory', c_int),          # 非机动车子类型,详见EM_CATEGORY_NONMOTOR_TYPE;Non-motor type,refer to EM_CATEGORY_NONMOTOR_TYPE
        ('stuBoundingBox', SDK_RECT),   # 包围盒， 非机动车矩形框，0~8191相对坐标;BoundingBox Rect, 0~8192
        ('stuOriginalBoundingBox', SDK_RECT),   # 包围盒， 非机动车矩形框，绝对坐标;BoundingBox Rect, absolute coordinates
        ('stuMainColor', NET_COLOR_RGBA),       # 非机动车颜色, RGBA;Non-motor color (RGBA value)
        ('emColor', c_int),                     # 非机动车颜色, 枚举,详见EM_OBJECT_COLOR_TYPE;Non-motor color enumeration，refer to EM_OBJECT_COLOR_TYPE
        ('bHasImage', c_int),                   # 是否有抠图; whether has image or not
        ('stuImage', NET_NONMOTOR_PIC_INFO),    # 物体截图;Image information
        ('nNumOfCycling', c_int),               # 骑车人数量;The number of rider
        ('stuRiderList', NET_RIDER_INFO*16),    # 骑车人特征,个数和nNumOfCycling关联;The information of rider
        ('stuSceneImage', SCENE_IMAGE_INFO),    # 全景广角图;SceneImage
        ('stuFaceSceneImage', FACE_SCENE_IMAGE),    # 人脸全景广角图; Face SceneImage
        ('nNumOfFace', c_int),                      # 检测到的人脸数量;The number of face
        ('fSpeed', c_float),                        # 物体速度，单位为km/h;Object speed, Unit:km/h
        ('stuNonMotorFeatureVectorInfo', NET_NONMOTOR_FEATURE_VECTOR_INFO), #  非机动车特征值数据在二进制数据中的位置信息
                                                                            # Position info of non-motor feature data in binary data
        ('emNonMotorFeatureVersion', c_int),    #  非机动车特征值版本号,详见EM_FEATURE_VERSION;Non-motor feature data version，refer to EM_FEATURE_VERSION
        ('stuNomotorPlateInfo', NET_NONMOTOR_PLATE_INFO),  #  非机动车牌信息;Plate info of nomotor
        ('stuObjCenter', SDK_POINT),            # 物体型心(不是包围盒中心), 0-8191相对坐标, 相对于大图; Center of object(not center of bounding box), 0-8191 relative coordinates, relative to large graph
        ('byReserved', c_ubyte*3072),           # 保留;Reserved
    ]

class DEV_EVENT_TRAFFICJUNCTION_INFO(Structure):
    """
    事件类型TRAFFICJUNCTION(交通路口老规则事件/视频电警上的交通卡口老规则事件)对应的数据块描述信息;Event Type TRAFFICJUNCTION (transportation card traffic junctions old rule event / video port on the old electric alarm event rules) corresponding to the description of the data block
    """
    _fields_ = [
        ('nChannelID', c_int),              # 通道号;ChannelId
        ('szName', c_char*128),             # 事件名称;event name
        ('byMainSeatBelt', c_ubyte),        # 主驾驶座,系安全带状态,1-系安全带,2-未系安全带;main driver, seat, safety belt , 1-fastened, 2-unfastened
        ('bySlaveSeatBelt', c_ubyte),       # 副驾驶座,系安全带状态,1-系安全带,2-未系安全带;co-drvier, seat, safety belt, 1-fastened, 2-unfastened
        ('byVehicleDirection', c_ubyte),    # 当前被抓,拍到的车辆是车头还是车尾,具体请见 EM_VEHICLE_DIRECTION;Current snapshot is head or rear, see  EM_VEHICLE_DIRECTION
        ('byOpenStrobeState', c_ubyte),     # 开闸状态,具体请见EM_OPEN_STROBE_STATE;Open status, see EM_OPEN_STROBE_STATE
        ('PTS', c_double),                  # 时间戳(单位是毫秒);PTS(ms)
        ('UTC', NET_TIME_EX),               # 事件发生的时间;the event happen time
        ('nEventID', c_int),                # 事件ID;event ID
        ('stuObject', SDK_MSG_OBJECT),      # 检测到的物体;have being detected object
        ('nLane', c_int),                   # 对应车道号;road number
        ('dwBreakingRule', C_DWORD),        # 违反规则掩码,第一位:闯红灯;BreakingRule's mask,first byte: crash red light;
                                            # 第二位:不按规定车道行驶;secend byte:break the rule of driving road number;
                                            # 第三位: 逆行;the third byte:converse;
                                            # 第四位：违章掉头;the forth byte:break rule to turn around;
                                            # 第五位: 交通堵塞;the five byte:traffic jam;
                                            # 第六位: 交通异常空闲;the six byte:traffic vacancy;
                                            # 第七位:压线行驶;否则默认为: 交通路口事件;the seven byte: Overline; defalt:trafficJunction
        ('RedLightUTC', NET_TIME_EX),       # 红灯开始UTC时间;the begin time of red light
        ('stuFileInfo', SDK_EVENT_FILE_INFO),  # 事件对应文件信息;event file info
        ('nSequence', c_int),               # 表示抓拍序号,如3,2,1,1表示抓拍结束,0表示异常结束;snap index,such as 3,2,1,1 means the last one,0 means there has some exception and snap stop
        ('nSpeed', c_int),                  # 车辆实际速度Km/h;car's speed (km/h)
        ('bEventAction', c_ubyte),          # 事件动作,0表示脉冲事件,1表示持续性事件开始,2表示持续性事件结束;Event action,0 means pulse event,1 means continuous event's begin,2means continuous event's end;
        ('byDirection', c_ubyte),           # 路口方向,1-表示正向,2-表示反向;Intersection direction 1 - denotes the forward 2 - indicates the opposite
        ('byLightState', c_ubyte),          # LightState表示红绿灯状态:0 未知,1 绿灯,2 红灯,3 黄灯;LightState means red light status:0 unknown,1 green,2 red,3 yellow
        ('byReserved', c_ubyte),            # 保留字节;reserved
        ('byImageIndex', c_ubyte),          # 图片的序号, 同一时间内(精确到秒)可能有多张图片, 从0开始;Serial number of the picture, in the same time (accurate to seconds) may have multiple images, starting from 0
        ('stuVehicle', SDK_MSG_OBJECT),     # 车身信息;vehicle info
        ('dwSnapFlagMask', C_DWORD),        # 抓图标志(按位),0位:"*",1位:"Timing",2位:"Manual",3位:"Marked",4位:"Event",5位:"Mosaic",6位:"Cutout"
                                            # snap flags(by bit),0bit:"*",1bit:"Timing",2bit:"Manual",3bit:"Marked",4bit:"Event",5bit:"Mosaic",6bit:"Cutout"
        ('stuResolution', SDK_RESOLUTION_INFO),  # 对应图片的分辨率;picture resolution
        ('szRecordFile', c_char*128),            # 报警对应的原始录像文件信息;Alarm corresponding original video file information
        ('stuCustomInfo', EVENT_JUNCTION_CUSTOM_INFO),  # 报警对应的原始录像文件信息;custom info
        ('byPlateTextSource', c_ubyte),     # 车牌识别来源, 0:本地算法识别,1:后端服务器算法识别;the source of plate text, 0:Local,1:Server
        ('bReserved1', c_ubyte*3),          # 保留字节,留待扩展.;Reserved bytes, leave extended_
        ('stuGPSInfo', NET_GPS_INFO),       # GPS信息 车载定制;GPS info ,use in mobile DVR/NVR
        ('byNoneMotorInfo', c_ubyte),       # 0-无非机动车人员信息信息,1-有非机动车人员信息信息;specified the person info of none motor
                                            # 此字段为1时下面11个字段生效;1 means 11 fields followed is valid
        ('byBag', c_ubyte),                 # 是否背包, 0-未知 1-不背包   2-背包;0-unknown 1-no bag   2-bag
        ('byUmbrella', c_ubyte),            # 是否打伞, 0-未知 1-不打伞   2-打伞;0-unknown 1-no umbrella   2-Umbrella
        ('byCarrierBag', c_ubyte),          # 手提包状态,0-未知 1-没有 2-有;0-unknown 1-no carrierBag 2-carrierBag
        ('byHat', c_ubyte),                 # 是否戴帽子, 0-未知 1-不戴帽子 2-戴帽子;0-unknown 1-no helmet 2-helmet
        ('byHelmet', c_ubyte),              # 头盔状态,0-未知 1-没有 2-有;0-unknown 1-no hat 2-hat
        ('bySex', c_ubyte),                 # 性别,0-未知 1-男性 2-女性;0-unknown 1-man 2-woman
        ('byAge', c_ubyte),                 # 年龄;age
        ('stuUpperBodyColor', NET_COLOR_RGBA),      # 上身颜色;upper body color
        ('stuLowerBodyColor', NET_COLOR_RGBA),      # 下身颜色;lower body color
        ('byUpClothes', c_ubyte),                   # 上身衣服类型 0:未知 1:长袖 2:短袖 3:长裤 4:短裤 5:裙子 6:背心 7:超短裤 8:超短裙;upper clothes 0:unknown 1:long sleeve 2:short sleeve 3:trousers 4:breeches 5:skirt 6:vest 7:minipants 8:miniskirt
        ('byDownClothes', c_ubyte),                 # 下身衣服类型 0:未知 1:长袖 2:短袖 3:长裤 4:短裤 5:裙子 6:背心 7:超短裤 8:超短裙;lower clothes 0:unknown 1:long sleeve 2:short sleeve 3:trousers 4:breeches 5:skirt 6:vest 7:minipants 8:miniskirt
        ('stuExtensionInfo', NET_EXTENSION_INFO),   # 扩展信息;Extension info
        ('bReserved', c_ubyte*22),                  # 保留字节,留待扩展;Reserved bytes, leave extended
        ('nTriggerType', c_int),                    # TriggerType:触发类型,0车检器,1雷达,2视频,3RSU;Trigger Type:0 vehicle inspection device, 1 radar, 2 video, 3 RSU
        ('stTrafficCar', DEV_EVENT_TRAFFIC_TRAFFICCAR_INFO),         # 交通车辆信息;Traffic vehicle info
        ('dwRetCardNumber', C_DWORD),           # 卡片个数;Card Number
        ('stuCardInfo', EVENT_CARD_INFO*16),    # 卡片信息;Card information
        ('stCommInfo', EVENT_COMM_INFO),        # 公共信息;public info
        ('bNonMotorInfoEx', c_int),             # 是否有非机动车信息;Non-motor info enable
        ('stuNonMotor', VA_OBJECT_NONMOTOR),    # 非机动车信息;Non-motor information
        ('stuIntelliCommInfo', EVENT_INTELLI_COMM_INFO),  # 智能事件公共信息;intelli comm info
        ('byReserved2', c_ubyte*1916)           # 保留字节,留待扩展;Reserved
    ]


class EVENT_INFO(Structure):
    """
    事件信息;Event info
    """
    _fields_ = [
        ('nEvent', c_int),                  # 事件类型,参见智能事件类型，如 EVENT_IVS_ALL;Event type, see intelligent analysis event type,like EVENT_IVS_ALL
        ('arrayObejctType', c_int * 16),    # 支持的物体类型，当前支持 EM_OBJECT_TYPE.HUMAN, EM_OBJECT_TYPE.VECHILE, EM_OBJECT_TYPE.NOMOTOR, EM_OBJECT_TYPE.ALL,参考EM_OBJECT_TYPE;object type, currently support EM_OBJECT_TYPE_HUMAN, EM_OBJECT_TYPE_VECHILE, EM_OBJECT_TYPE_NOMOTOR, EM_OBJECT_TYPE_ALL
        ('nObjectCount', c_int),            # szObejctType 数量;szObejctType's count
        ('byReserved', c_ubyte * 512),      # 预留字段;reserved
    ]


class NET_IN_PLAY_BACK_BY_TIME_INFO(Structure):
    """
    录像回放入参信息; record play back parameter in
    """
    _fields_ = [
        ('stStartTime', NET_TIME),                      # 开始时间; Begin time
        ('stStopTime', NET_TIME),                       # 结束时间; End time
        ('hWnd', c_long),                               # 播放窗格, 可为NULL; Play window
        ('cbDownLoadPos', CB_FUNCTYPE(None, C_LLONG, C_DWORD, C_DWORD, C_LDWORD)), # 进度回调，对应SDK_Callback的fDownLoadPosCallBack; Download pos callback，corresponding to SDK_Callback's fDownLoadPosCallBack
        ('dwPosUser', C_LDWORD),                        # 进度回调用户信息; Pos user
        ('fDownLoadDataCallBack', CB_FUNCTYPE(c_int, C_LLONG, C_DWORD, POINTER(c_ubyte), C_DWORD, C_LDWORD)), # 数据回调，对应SDK_Callback的fDataCallBack; Download data callback，corresponding to SDK_Callback's fDataCallBack
        ('dwDataUser', C_LDWORD),                       # 数据回调用户信息; Data user
        ('nPlayDirection', c_int),                      # 播放方向, 0:正放; 1:倒放; Playback direction
        ('nWaittime', c_int),                           # 接口超时时间, 目前倒放使用; Watiting time
        ('pstuEventInfo', POINTER(EVENT_INFO)),         # 事件信息（定制），用户分配内存，不用时赋值为NULL; Event info(customized), user allocate memory
        ('nEventInfoCount', c_uint),                    # pstuEventInfo 个数，最大为 16; pstuEventInfo's count, max num is 16
        ('bReserved', c_ubyte * 1012),                  # 预留字段; reserved
    ]

class NET_OUT_PLAY_BACK_BY_TIME_INFO(Structure):
    """
    录像回放出参信息; record play back parameter out
    """
    _fields_ = [
        ('bReserved', c_ubyte * 1024),                # 预留字节; reserved
    ]

class SNAP_PARAMS(Structure):
    """
    抓图参数结构体;Snapshot parameter structure
    """
    _fields_ = [
        ('Channel', c_uint),            # 抓图的通道；Snapshot channel
        ('Quality', c_uint),            # 画质；1~6；Image quality:level 1 to level 6
        ('ImageSize', c_uint),          # 画面大小；0：QCIF,1：CIF,2：D1；Video size;0:QCIF,1:CIF,2:D1
        ('mode', c_uint),               # 抓图模式；-1:表示停止抓图, 0：表示请求一帧, 1：表示定时发送请求, 2：表示连续请求；Snapshot mode;0:request one frame,1:send out requestion regularly,2: Request consecutively
        ('InterSnap', c_uint),          # 时间单位秒；若mode=1表示定时发送请求时,只有部分特殊设备(如：车载设备)支持通过该字段实现定时抓图时间间隔的配置
                                        # Time unit is second.If mode=1, it means send out requestion regularly. The time is valid.
        ('CmdSerial', c_uint),          # 请求序列号，有效值范围 0~65535，超过范围会被截断为 unsigned short；Request serial number，valid value:0~65535
        ('Reserved', c_uint*4),         # 预留字节;reserved
    ]

class NET_MOTIONDETECT_REGION_INFO(Structure):
    """
    动检区域信息;Region info of motion detection
    """
    _fields_ = [
        ('nRegionID', c_uint),          # 区域ID;region ID
        ('szRegionName', c_char*64),    # 区域名称;region name
        ('bReserved', c_ubyte*508),     # 保留字节;reserved
    ]

class ALARM_MOTIONDETECT_INFO(Structure):
    """
    报警事件类型SDK_ALARM_TYPE.EVENT_MOTIONDETECT(视频移动侦测事件)对应的数据描述信息;alarm event type SDK_ALARM_TYPE.EVENT_MOTIONDETECT (video motion detection event) corresponding data description info
    """
    _fields_ = [
        ('dwSize', C_DWORD),  # 结构体大小；Structure size
        ('nChannelID', c_int),                          # 通道号;channel
        ('PTS', c_double),                              # 时间戳(单位是毫秒);timestamp (unit is millisecond)
        ('UTC', NET_TIME_EX),                           # 事件发生的时间;event occurrence time
        ('nEventID', c_int),                            # 事件ID;event ID
        ('nEventAction', c_int),                        # 事件动作,0表示脉冲事件,1表示持续性事件开始,2表示持续性事件结束;event action, 0 means pulse event, 1 means continuous event begin, 2 means continuous event end;
        ('nRegionNum', c_uint),                         # 动检区域个数;count of region
        ('stuRegion', NET_MOTIONDETECT_REGION_INFO*32),    # 动检区域信息;region info of motion detection
        ('bSmartMotionEnable', c_int),                  # 智能动检是否使能;smart motion detection is enable or not
        ('nDetectTypeNum', c_uint),                     # 动检触发类型个数;count of triggeing motion detection type
        ('emDetectType', c_int*32),                     # 动检触发类型, 当nRegionNum大于0时，和stuRegion数组一一对应,参考枚举EM_MOTION_DETECT_TYPE;triggeing motion detection type, when nRegionNum>0，one-to-one correspondence with stuRegion if nRegionNum is biger than 0，refer to EM_MOTION_DETECT_TYPE
														# 若nRegionNum为0，触发区域未知，不与窗口绑定，默认第一个元素表示触发类型;the type is the first value of emDetectType if nRegionNum is 0
    ]


class NET_FACE_INFO(Structure):
    """
    多人脸检测信息; multi faces detect info
    """
    _fields_ = [
        ('nObjectID', c_int),               # 物体ID,每个ID表示一个唯一的物体;object id
        ('szObjectType', c_char * 128),     # 物体类型;object type
        ('nRelativeID', c_int),             # 这张人脸抠图所属的大图的ID;same with the source picture id
        ('BoundingBox', SDK_RECT),          # 包围盒;bounding box
        ('Center', SDK_POINT),              # 物体中心;object center
    ]

class NET_FEATURE_VECTOR(Structure):
    """
    存储IVSS项目招行VIP需求,特征值信息; Feature data Information
    """
    _fields_ = [
        ('dwOffset', C_DWORD),  # 人脸小图特征值在二进制数据块中的偏移;Face feature data offset in data block(Unit:BYTE)
        ('dwLength', C_DWORD),  # 人脸小图特征值长度，单位:字节;Face feature data length(Unit:BYTE)
        ('byReserved', c_ubyte * 120),  # 保留;Reserved
    ]


class NET_EULER_ANGLE(Structure):
    """
    姿态角数据; euler angle
    """
    _fields_ = [
        ('nPitch', c_int),      # 仰俯角;pitch
        ('nYaw', c_int),        # 偏航角;yaw
        ('nRoll', c_int),       # 翻滚角;roll
    ]

class NET_HUMAN_TEMPERATURE_INFO(Structure):
    """
    人体温信息; Information of human body temperature
    """
    _fields_ = [
        ('dbTemperature', c_double),        # 温度;Temperature
        ('emTemperatureUnit', c_int),       # 温度单位，参考EM_HUMAN_TEMPERATURE_UNIT;Temperature unit,refer to EM_HUMAN_TEMPERATURE_UNIT
        ('bIsOverTemp', c_int),             # 是否超温;Is over temperature
        ('bIsUnderTemp', c_int),            # 是否低温;Is under temperature
        ('bReserved', c_ubyte * 132),       # 预留字段;Reserved
    ]

class DEV_EVENT_FACEDETECT_INFO(Structure):
    """
    事件类型FACEDETECT(人脸检测事件)对应的数据块描述信息; the describe of FACEDETECT's data
    """
    _fields_ = [
        ('nChannelID', c_int),                          # 通道号；channel ID
        ('szName', c_char * 128),                       # 事件名称;event name
        ('bReserved1', c_char * 4),                     # 字节对齐;byte alignment
        ('PTS', c_double),                              # 时间戳(单位是毫秒);PTS(ms)
        ('UTC', NET_TIME_EX),                           # 事件发生的时间;the event happen time
        ('nEventID', c_int),                            # 事件ID;event ID
        ('stuObject', SDK_MSG_OBJECT),                  # 检测到的物体;have being detected object
        ('stuFileInfo', SDK_EVENT_FILE_INFO),           # 事件对应文件信息;event file info
        ('bEventAction', c_ubyte),                      # 事件动作,0表示脉冲事件,1表示持续性事件开始,2表示持续性事件结束;Event action: 0 means pulse event,1 means continuous event's begin,2means continuous event's end;
        ('reserved', c_ubyte * 2),                      # 保留字节;reserved
        ('byImageIndex', c_ubyte),                      # 图片的序号, 同一时间内(精确到秒)可能有多张图片, 从0开始;Serial number of the picture, in the same time (accurate to seconds) may have multiple images, starting from 0
        ('nDetectRegionNum', c_int),                    # 规则检测区域顶点数;detect region point number
        ('DetectRegion', SDK_POINT * 20),               # 规则检测区域;detect region
        ('dwSnapFlagMask', C_DWORD),                    # 抓图标志(按位),具体见NET_RESERVED_COMMON;flag(by bit),see NET_RESERVED_COMMON
        ('szSnapDevAddress', c_char * 260),             # 抓拍当前人脸的设备地址,如：滨康路37号;snapshot current face device address
        ('nOccurrenceCount', c_uint),                   # 事件触发累计次数;event trigger accumilated times
        ('emSex', c_int),                               # 性别，参考EM_DEV_EVENT_FACEDETECT_SEX_TYPE;sex type,refer to EM_DEV_EVENT_FACEDETECT_SEX_TYPE
        ('nAge', c_ubyte),                              # 年龄,-1表示该字段数据无效;age, invalid if it is -1
        ('nFeatureValidNum', c_uint),                   # 人脸特征数组有效个数,与 emFeature 结合使用;invalid number in array emFeature
        ('emFeature', c_uint * 32),                     # 人脸特征数组,与 nFeatureValidNum 结合使用，参考EM_DEV_EVENT_FACEDETECT_FEATURE_TYPE;human face features,refer to EM_DEV_EVENT_FACEDETECT_FEATURE_TYPE
        ('nFacesNum', c_int),                           # 指示stuFaces有效数量;number of stuFaces
        ('stuFaces', NET_FACE_INFO * 10),               # 多张人脸时使用,此时没有Object;when nFacesNum > 0, stuObject invalid
        ('stuIntelliCommInfo', EVENT_INTELLI_COMM_INFO),# 智能事件公共信息;public info
        ('emRace', c_int),                              # 参考EM_RACE_TYPE;race,refer to EM_RACE_TYPE
        ('emEye', c_int),                               # 眼睛状态，参考EM_EYE_STATE_TYPE;eyes state,refer to EM_EYE_STATE_TYPE
        ('emMouth', c_int),                             # 嘴巴状态，参考EM_MOUTH_STATE_TYPE;mouth state,refer to EM_MOUTH_STATE_TYPE
        ('emMask', c_int),                              # 口罩状态，参考EM_MASK_STATE_TYPE;mask state,refer to EM_MASK_STATE_TYPE
        ('emBeard', c_int),                             # 胡子状态，参考EM_BEARD_STATE_TYPE;beard state,refer to EM_BEARD_STATE_TYPE
        ('nAttractive', c_int),                         # 魅力值, -1表示无效, 0未识别，识别时范围1-100,得分高魅力高;Attractive value, -1: invalid, 0:no disringuish，range: 1-100, the higher value, the higher charm
        ('szUID', c_char * 32),                         # 抓拍人员写入数据库的唯一标识符;The unique identifier of the snap person to write to the database
        ('bReserved2', C_BYTE*4),
        ('stuFeatureVector', NET_FEATURE_VECTOR),       # 特征值信息;Feature data information
        ('szFeatureVersion', c_char * 32),              # 特征值算法版本;The version of the feature data algorithm
        ('emFaceDetectStatus', c_int),                  # 人脸在摄像机画面中的状态，参考EM_FACE_DETECT_STATUS;The status of person in camera picture,refer to EM_FACE_DETECT_STATUS
        ('stuFaceCaptureAngle', NET_EULER_ANGLE),       # 人脸在抓拍图片中的角度信息, nPitch:抬头低头的俯仰角, nYaw左右转头的偏航角, nRoll头在平面内左偏右偏的翻滚角;euler angle of face in the capture picture, nPitch:pitch of the head, nYaw: yaw of the head, nRoll:roll of the head
                                                        # 角度值取值范围[-90,90], 三个角度值都为999表示此角度信息无效;range of the angle value is [-90,90], stuFaceCaptureAngle is invalid if the three angles are 999.
        ('dHumanSpeed', c_double),                      # 人的运动速度, km/h;human speed, km/h
        ('nFaceAlignScore', c_int),                     # 人脸对齐得分分数,范围 0~10000,-1为无效值;The score of face picture align.The range is 0~10000,-1 is invalid
        ('nFaceClarity', c_int),                        # 人脸清晰度分数,范围 0~10000,-1为无效值;The score of face picture clarity.The range is 0~10000,-1 is invalid
        ('bHumanTemperature', c_int),                   # 人体温信息是否有效;Whether the information of human body temperature is valid
        ('stuHumanTemperature', NET_HUMAN_TEMPERATURE_INFO),        # 人体温信息, bHumanTemperature为TURE时有效;Information of human body temperature, It is valid whne bHumanTemperature is TURE
        ('bReserved', c_ubyte * 480),                   # 保留字节,留待扩展;Reserved
    ]

class FACERECOGNITION_PERSON_INFO(Structure):
    """
    人员信息; person info
    """
    _fields_ = [
        ('szPersonName', c_char * 16),      # 姓名,此参数作废；name
        ('wYear', c_ushort),                # 出生年,作为查询条件时,此参数填0,则表示此参数无效;birth year
        ('byMonth', c_ubyte),               # 出生月,作为查询条件时,此参数填0,则表示此参数无效;birth month
        ('byDay', c_ubyte),                 # 出生日,作为查询条件时,此参数填0,则表示此参数无效;birth day
        ('szID', c_char * 32),              # 人员唯一标示(身份证号码,工号,或其他编号);the unicle ID for the person
        ('bImportantRank', c_ubyte),        # 人员重要等级,1~10,数值越高越重要,作为查询条件时,此参数填0,则表示此参数无效;importance level,1~10,the higher value the higher level
        ('bySex', c_ubyte),                 # 性别,1-男,2-女,作为查询条件时,此参数填0,则表示此参数无效;sex, 0-man, 1-female
        ('wFacePicNum', c_ushort),          # 图片张数;picture number
        ('szFacePicInfo', SDK_PIC_INFO * 48),  # 当前人员对应的图片信息;picture info
        ('byType', c_ubyte),                # 人员类型,详见 EM_PERSON_TYPE;Personnel types, see EM_PERSON_TYPE
        ('byIDType', c_ubyte),              # 证件类型,详见 EM_CERTIFICATE_TYPE;Document types, see EM_CERTIFICATE_TYPE
        ('byGlasses', c_ubyte),             # 是否戴眼镜，0-未知 1-不戴 2-戴;Whether wear glasses or not,0-unknown,1-not wear glasses,2-wear glasses
        ('byAge', c_ubyte),                 # 年龄,0表示未知;Age,0 means unknown
        ('szProvince', c_char * 64),        # 省份;flag(by bit),see NET_RESERVED_COMMON;province
        ('szCity', c_char * 64),            # 城市;snapshot current face device address;city
        ('szPersonNameEx', c_char * 64),    # 姓名,因存在姓名过长,16字节无法存放问题,故增加此参数,;Name, the name is too long due to the presence of 16 bytes can not be Storage problems, the increase in this parameter
        ('szUID', c_char * 32),             # 人员唯一标识符,首次由服务端生成,区别于ID字段,修改,删除操作时必填;person unique ID
        ('szCountry', c_char * 3),          # 国籍,符合ISO3166规范;country
        ('byIsCustomType', c_ubyte),        # 人员类型是否为自定义: 0 使用Type规定的类型 1 自定义,使用szPersonName字段;using person type: 0 using byType, 1 using szPersonName
        ('pszComment', c_char_p),           # 备注信息, 用户自己申请内存的情况时;comment info, when the memory is alloced by user,
                                                # 下方bCommentLen需填写对应的具体长度值，推荐长度 NET_COMMENT_LENGTH;the value of bCommentLen needs to be filled in，recommended length is NET_COMMENT_LENGTH
        ('pszGroupID', c_char_p),           # 人员所属组ID, 用户自己申请内存的情况时;group ID, when the memory is alloced by user,
                                                # 下方bGroupIdLen需填写对应的具体长度值，推荐长度 NET_GROUPID_LENGTH;the value of bGroupIdLen needs to be filled in，recommended length is NET_GROUPID_LENGTH
        ('pszGroupName', c_char_p),         # 人员所属组名, 用户自己申请内存的情况时;group name, when the memory is alloced by user,
											    # 下方bGroupNameLen需填写对应的具体长度值，推荐长度 NET_GROUPNAME_LENGTH;the value of bGroupNameLen needs to be filled in，recommended length is NET_GROUPNAME_LENGTH
        ('pszFeatureValue', c_char_p),      # 人脸特征, 用户自己申请内存的情况时;the face feature , when the memory is alloced by user,
											    # 下方bFeatureValueLen需填写对应的具体长度值，推荐长度 NET_FEATUREVALUE_LENGTH;the value of bFeatureValueLen needs to be filled in，recommended length is NET_FEATUREVALUE_LENGTH
        ('bGroupIdLen', c_ubyte),           # pszGroupID的长度;len of pszGroupID
        ('bGroupNameLen', c_ubyte),         # pszGroupName的长度;len of pszGroupName
        ('bFeatureValueLen', c_ubyte),      # pszFeatureValue的长度;len of pszFeatureValue
        ('bCommentLen', c_ubyte),           # pszComment的长度;len of pszComment
        ('emEmotion', c_int),               # 表情，参考EM_DEV_EVENT_FACEDETECT_FEATURE_TYPE;Emotion,refer to EM_DEV_EVENT_FACEDETECT_FEATURE_TYPE
    ]

class CUSTOM_PERSON_INFO(Structure):
    """
    注册人员信息扩展结构体; extension of registered personnel information
    """
    _fields_ = [
        ('szPersonInfo', c_char * 64),      # 人员扩展信息;personnel extension information
        ('byReserved', c_ubyte * 124),      # 保留字节;Reserved bytes
    ]

class FACERECOGNITION_PERSON_INFOEX(Structure):
    """
    人员信息扩展结构体; expansion of  personnel information
    """
    _fields_ = [
        ('szPersonName', c_char * 64),      # 姓名；name
        ('wYear', c_ushort),                # 出生年,作为查询条件时,此参数填0,则表示此参数无效;birth year
        ('byMonth', c_ubyte),               # 出生月,作为查询条件时,此参数填0,则表示此参数无效;birth month
        ('byDay', c_ubyte),                 # 出生日,作为查询条件时,此参数填0,则表示此参数无效;birth day
        ('bImportantRank', c_ubyte),        # 人员重要等级,1~10,数值越高越重要,作为查询条件时,此参数填0,则表示此参数无效;importance level,1~10,the higher value the higher level
        ('bySex', c_ubyte),                 # 性别,1-男,2-女,作为查询条件时,此参数填0,则表示此参数无效;sex, 0-man, 1-female
        ('szID', c_char * 32),              # 人员唯一标示(身份证号码,工号,或其他编号);the unicle ID for the person
        ('wFacePicNum', c_ushort),          # 图片张数;picture number
        ('szFacePicInfo', SDK_PIC_INFO * 48),  # 当前人员对应的图片信息;picture info
        ('byType', c_ubyte),                # 人员类型,详见 EM_PERSON_TYPE;Personnel types, see EM_PERSON_TYPE
        ('byIDType', c_ubyte),              # 证件类型,详见 EM_CERTIFICATE_TYPE;Document types, see EM_CERTIFICATE_TYPE
        ('byGlasses', c_ubyte),             # 是否戴眼镜，0-未知 1-不戴 2-戴;Whether wear glasses or not,0-unknown,1-not wear glasses,2-wear glasses
        ('byAge', c_ubyte),                 # 年龄,0表示未知;Age,0 means unknown
        ('szProvince', c_char * 64),        # 省份;flag(by bit),see NET_RESERVED_COMMON;province
        ('szCity', c_char * 64),            # 城市;snapshot current face device address;city
        ('szUID', c_char * 32),             # 人员唯一标识符,首次由服务端生成,区别于ID字段,修改,删除操作时必填;person unique ID
        ('szCountry', c_char * 3),          # 国籍,符合ISO3166规范;country
        ('byIsCustomType', c_ubyte),        # 人员类型是否为自定义: 0 使用Type规定的类型 1 自定义,使用szCustomType字段;using person type: 0 using byType, 1 using szCustomType
        ('szCustomType', c_char * 16),      # 人员自定义类型;custom type of person
        ('szComment', c_char * 100),        # 备注信息;comment info
        ('szGroupID', c_char * 64),         # 人员所属组ID;group ID
        ('szGroupName', c_char * 128),      # 人员所属组名, 用户自己申请内存的情况时;group name
        ('emEmotion', c_int),               # 表情，参考EM_DEV_EVENT_FACEDETECT_FEATURE_TYPE;Emotion,refer to EM_DEV_EVENT_FACEDETECT_FEATURE_TYPE
        ('szHomeAddress', c_char * 128),    # 注册人员家庭地址;home address of the person
        ('emGlassesType', c_int),           # 眼镜类型，参考EM_GLASSES_TYPE;glasses type,refer to EM_GLASSES_TYPE
        ('emRace', c_int),                  # 参考EM_RACE_TYPE;race,refer to EM_RACE_TYPE
        ('emEye', c_int),                   # 眼睛状态，参考EM_EYE_STATE_TYPE;eye state,refer to EM_EYE_STATE_TYPE
        ('emMouth', c_int),                 # 嘴巴状态，参考EM_MOUTH_STATE_TYPE;mouth state,refer to EM_MOUTH_STATE_TYPE
        ('emMask', c_int),                  # 口罩状态，参考EM_MASK_STATE_TYPE;mask state,refer to EM_MASK_STATE_TYPE
        ('emBeard', c_int),                 # 胡子状态，参考EM_BEARD_STATE_TYPE;beard state,refer to EM_BEARD_STATE_TYPE
        ('nAttractive', c_int),             # 魅力值, -1表示无效, 0未识别，识别时范围1-100,得分高魅力高;attractive, -1:invalid, 0:unknown，1-100
        ('emFeatureState', c_int),          # 人员建模状态, 详见EM_PERSON_FEATURE_STATE;person feature state,refer to EM_PERSON_FEATURE_STATE
        ('bAgeEnable', c_int),              # 是否指定年龄段;age range is enabled
        ('nAgeRange', c_int * 2),           # 年龄范围;age range
        ('nEmotionValidNum', c_int),        # 人脸特征数组有效个数,与 emFeature 结合使用, 如果为0则表示查询所有表情;invalid number in array emEmotion, 0 means all emotion
        ('emEmotions', c_int * 32),         # 人脸特征数组,与 byFeatureValidNum 结合使用  设置查询条件的时候使用，参考EM_DEV_EVENT_FACEDETECT_FEATURE_TYPE;human emotion  set the query condition，refer to EM_DEV_EVENT_FACEDETECT_FEATURE_TYPE
        ('nCustomPersonInfoNum', c_int),    # 注册人员信息扩展个数;extension number of registered personnel information
        ('szCustomPersonInfo', CUSTOM_PERSON_INFO * 4),  # 注册人员信息扩展;extension of registered personnel information
        ('emRegisterDbType', c_int),        # 注册库类型，参考EM_REGISTER_DB_TYPE;type of register face DB
        ('stuEffectiveTime', NET_TIME),     # 有效期时间;effective time
        ('emFeatureErrCode', c_int),        # 建模失败原因，参考EM_PERSON_FEATURE_ERRCODE;error code of person feature,refer to EM_PERSON_FEATURE_ERRCODE
        ('byReserved', c_ubyte * 1112),     # 保留字节;Reserved bytes
    ]

class SDK_PIC_INFO_EX3(Structure):
    """
    物体对应图片文件信息(包含图片路径); picture info
    """
    _fields_ = [
        ('dwOffSet', C_DWORD),          # 文件在二进制数据块中的偏移位置, 单位:字节;current picture file's offset in the binary file, byte
        ('dwFileLenth', C_DWORD),       # 文件大小, 单位:字节;current picture file's size, byte
        ('wWidth', c_ushort),           # 图片宽度, 单位:像素;picture width, pixel
        ('wHeight', c_ushort),          # 图片高度, 单位:像素;picture high, pixel
        ('szFilePath', c_char * 64),    # 文件路径; File path
        ('bIsDetected', c_ubyte),       # 图片是否算法检测出来的检测过的提交识别服务器时, 则不需要再时检测定位抠图,1:检测过的,0:没有检测过;When submit to the server, the algorithm has checked the image or not
        ('bReserved', c_ubyte * 11),    # 预留字段;Reserved
    ]

class CANDIDATE_INFO(Structure):
    """
    候选人员信息; cadidate person info
    """
    _fields_ = [
        ('stPersonInfo', FACERECOGNITION_PERSON_INFO),          # 人员信息;person info
                                                                    # 布控（黑名单）库, 指布控库中人员信息；
                                                                    # 历史库, 指历史库中人员信息
                                                                    # 报警库, 指布控库的人员信息
        ('bySimilarity', c_ubyte),                              # 和查询图片的相似度,百分比表示,1~100;similarity
        ('byRange', c_ubyte),                                   # 人员所属数据库范围,详见EM_FACE_DB_TYPE; Range officer's database, see EM_FACE_DB_TYPE
        ('byReserved1', c_ubyte * 2),                           # 预留字段;Reserved
        ('stTime', NET_TIME),                                   # 当byRange为历史数据库时有效,表示查询人员出现的时间;When byRange historical database effectively, which means that the query time staff appeared
        ('szAddress', c_ubyte * 260),                           # 当byRange为历史数据库时有效,表示查询人员出现的地点;When byRange historical database effectively, which means that people place a query appears
        ('bIsHit', c_int),                                      # 是否有识别结果,指这个检测出的人脸在库中有没有比对结果;Is hit, means the result face has compare result in database
        ('stuSceneImage', SDK_PIC_INFO_EX3),                    # 人脸全景图;Scene Image
        ('nChannelID', c_int),                                  # 通道号;Channel Id
        ('byReserved', c_ubyte * 32),                           # 保留字节;Reserved bytes
    ]

class NET_HISTORY_HUMAN_IMAGE_INFO(Structure):
    """
    历史库人体图片信息; Image info of human in history data base
    """
    _fields_ = [
        ('nLength', c_int),             # 图片大小,单位:字节;Image, unit:byte
        ('nWidth', c_int),              # 图片宽度;Image width
        ('nHeight', c_int),             # 图片高度;Image height
        ('szFilePath', c_char * 260),   # 文件路径;Image path
    ]

class NET_HISTORY_HUMAN_INFO(Structure):
    """
    历史库人体信息; Human info in history data base
    """
    _fields_ = [
        ('emCoatColor', c_int),             # 上衣颜色,参考EM_CLOTHES_COLOR; Coat color,refer to EM_CLOTHES_COLOR
        ('emCoatType', c_int),              # 上衣类型，参考EM_COAT_TYPE; Coat type, refer to EM_COAT_TYPE
        ('emTrousersColor', c_int),         # 裤子颜色,参考EM_CLOTHES_COLOR; Trousers color,refer to EM_CLOTHES_COLOR
        ('emTrousersType', c_int),          # 裤子类型，参考EM_TROUSERS_TYPE; Trousers type,refer to EM_TROUSERS_TYPE
        ('emHasHat', c_int),                # 是否戴帽子，参考EM_HAS_HAT; Has hat or not,refer to EM_HAS_HAT
        ('emHasBag', c_int),                # 是否带包，参考EM_HAS_BAG; Has bag or not,refer to EM_HAS_BAG
        ('stuBoundingBox', NET_RECT),       # 包围盒(8192坐标系); Bounding box
        ('nAge', c_int),                    # 年龄;Age
        ('emSex', c_int),                   # 性别，参考EM_SEX_TYPE;Sex,refer to EM_SEX_TYPE
        ('emAngle', c_int),                 # 角度，参考EM_ANGLE_TYPE;Angle,refer to EM_ANGLE_TYPE
        ('emHasUmbrella', c_int),           # 是否打伞，参考EM_HAS_UMBRELLA;Has umbrella or not,refer to EM_HAS_UMBRELLA
        ('emBag', c_int),                   # 包类型，参考EM_BAG_TYPE;Bag type,refer to EM_BAG_TYPE
        ('emUpperPattern', c_int),          # 上半身衣服图案，参考EM_CLOTHES_PATTERN;Upper pattern,refer to EM_CLOTHES_PATTERN
        ('emHairStyle', c_int),             # 头发样式，参考EM_HAIR_STYLE;Hair style,refer to EM_HAIR_STYLE
        ('emCap', c_int),                   # 帽类型，参考EM_CAP_TYPE;Cap type,refer to EM_CAP_TYPE
        ('emHasBackBag', c_int),            # 是否有背包，参考EM_HAS_BACK_BAG;Has back bag or not,refer to EM_HAS_BACK_BAG
        ('emHasCarrierBag', c_int),         # 是否带手提包，参考EM_HAS_CARRIER_BAG;Has carrier bag or not,refer to EM_HAS_CARRIER_BAG
        ('emHasShoulderBag', c_int),        # 是否有肩包，参考EM_HAS_SHOULDER_BAG;Has shoulder bag or not,refer to EM_HAS_SHOULDER_BAG
        ('emMessengerBag', c_int),          # 是否有斜跨包，参考EM_HAS_MESSENGER_BAG;Has messenger bag or not,refer to EM_HAS_MESSENGER_BAG
        ('stuImageInfo', NET_HISTORY_HUMAN_IMAGE_INFO),         # 人体图片信息;Human image info
        ('stuFaceImageInfo', NET_HISTORY_HUMAN_IMAGE_INFO),     # 人脸图片信息;Face image info
        ('byReserved', c_ubyte * 256),      # 保留字节;Reserved bytes
    ]


class CANDIDATE_INFOEX(Structure):
    """
    候选人员信息扩展结构体; cadidate person info
    """
    _fields_ = [
        ('stPersonInfo', FACERECOGNITION_PERSON_INFOEX),        # 人员信息;person info
                                                                    # 布控（黑名单）库, 指布控库中人员信息；
                                                                    # 历史库, 指历史库中人员信息
                                                                    # 报警库, 指布控库的人员信息
        ('bySimilarity', c_ubyte),                              # 和查询图片的相似度,百分比表示,1~100;similarity
        ('byRange', c_ubyte),                                   # 人员所属数据库范围,详见EM_FACE_DB_TYPE; Range officer's database, see EM_FACE_DB_TYPE
        ('byReserved1', c_ubyte * 2),                           # 预留字段;Reserved
        ('stTime', NET_TIME),                                   # 当byRange为历史数据库时有效,表示查询人员出现的时间;When byRange historical database effectively, which means that the query time staff appeared
        ('szAddress', c_ubyte * 260),                           # 当byRange为历史数据库时有效,表示查询人员出现的地点;When byRange historical database effectively, which means that people place a query appears
        ('bIsHit', c_int),                                      # 是否有识别结果,指这个检测出的人脸在库中有没有比对结果;Is hit, means the result face has compare result in database
        ('stuSceneImage', SDK_PIC_INFO_EX3),                    # 人脸全景图;Scene Image
        ('nChannelID', c_int),                                  # 通道号;Channel Id
        ('szFilePathEx', c_char * 256),                         # 文件路径;File path
        ('stuHistoryHumanInfo', NET_HISTORY_HUMAN_INFO),        # 历史库人体信息;Human info in history data base
        ('byReserved', c_ubyte * 136),                          # 保留字节;Reserved bytes
    ]

class NET_FACE_DATA(Structure):
    """
    人脸数据; the data of face
    """
    _fields_ = [
        ('emSex', c_int),               # 性别，参考EM_DEV_EVENT_FACEDETECT_SEX_TYPE;sex type,refer to EM_DEV_EVENT_FACEDETECT_SEX_TYPE
        ('nAge', c_int),                # 年龄,-1表示该字段数据无效;age, invalid if it is -1
        ('nFeatureValidNum', c_uint),   # 人脸特征数组有效个数,与 emFeature 结合使用; invalid number in array emFeature
        ('emFeature', c_int * 32),      # 人脸特征数组,与 nFeatureValidNum 结合使用，参考EM_DEV_EVENT_FACEDETECT_FEATURE_TYPE;human face features,refer to EM_DEV_EVENT_FACEDETECT_FEATURE_TYPE
        ('emRace', c_int),              # 参考EM_RACE_TYPE;race,refer to EM_RACE_TYPE
        ('emEye', c_int),               # 眼睛状态，参考EM_EYE_STATE_TYPE;eyes state,refer to EM_EYE_STATE_TYPE
        ('emMouth', c_int),             # 嘴巴状态，参考EM_MOUTH_STATE_TYPE;mouth state,refer to EM_MOUTH_STATE_TYPE
        ('emMask', c_int),              # 口罩状态，参考EM_MASK_STATE_TYPE;mask state,refer to EM_MASK_STATE_TYPE
        ('emBeard', c_int),             # 胡子状态，参考EM_BEARD_STATE_TYPE;beard state,refer to EM_BEARD_STATE_TYPE
        ('nAttractive', c_int),         # 魅力值, -1表示无效, 0未识别，识别时范围1-100,得分高魅力高;Attractive value, -1: invalid, 0:no disringuish，range: 1-100, the higher value, the higher charm
        ('bReserved1', C_BYTE*4),
        ('stuFaceCaptureAngle', NET_EULER_ANGLE),  # 人脸在抓拍图片中的角度信息,角度值取值范围[-90,90], 三个角度值都为999表示此角度信息无效; euler angle of face in the capture picture,range of the angle value is [-90,90], stuFaceCaptureAngle is invalid if the three angles are 999.
        ('nFaceQuality', c_uint),       # 人脸抓拍质量分数;quality about capture picture
        ('nFaceAlignScore', c_int),     # 人脸对齐得分分数,范围 0~10000,-1为无效值;The score of face picture align.The range is 0~10000,-1 is invalid
        ('nFaceClarity', c_int),        # 人脸清晰度分数,范围 0~10000,-1为无效值;The score of face picture clarity.The range is 0~10000,-1 is invalid
        ('dbTemperature', c_double),    # 温度, bAnatomyTempDetect 为TRUE时有效;Temperature, it is valid when bAnatomyTempDetect is true
        ('bAnatomyTempDetect', c_int),  # 是否人体测温;Is anatomy temperature detection
        ('emTemperatureUnit', c_int),   # 温度单位, bAnatomyTempDetect 为TRUE时有效,参考EM_HUMAN_TEMPERATURE_UNIT;Temperature unit, it is valid when bAnatomyTempDetect is true,refer to EM_HUMAN_TEMPERATURE_UNIT
        ('bIsOverTemp', c_int),         # 是否超温, bAnatomyTempDetect 为TRUE时有效;Is over temperature, it is valid when bAnatomyTempDetect is true
        ('bIsUnderTemp', c_int),        # 是否低温, bAnatomyTempDetect 为TRUE时有效;Is under temperature, it is valid when bAnatomyTempDetect is true
        ('bReserved', c_ubyte * 76),    # 保留字节,留待扩展;Reserved bytes

    ]

class NET_PASSERBY_INFO(Structure):
    """
    路人信息; passerby info
    """
    _fields_ = [
        ('szPasserbyUID', c_char * 32),             # 路人唯一标识符;The unique identifier of the passerby to write to the database
        ('szPasserbyGroupId', c_char * 64),         # 路人库ID;Passerby group ID
        ('szPasserbyGroupName', c_char * 128),      # 路人库名称;Passerby group name
        ('byReserved', c_ubyte * 128),              # 保留;Reserved
    ]


class NET_FACECOMPARISON_PTZ_INFO(Structure):
    """
    人脸比对事件触发对应球机信息; Face matching event triggers corresponding ball machine information
    """
    _fields_ = [
        ('szPresetName', c_char * 64),             # 球机抓拍到人脸时预置点名称;Preset point name when the ball machine captures the face
        ('dwPresetNumber', C_DWORD),         # 球机抓拍到人脸时预置点编号;Preset point number when the ball machine captures the face
        ('byReserved1', c_ubyte * 4),           # 字节对齐;Byte alaginment
        ('byReserved', c_ubyte * 256),           # 保留字节;Reserved
    ]

class NET_CUSTOM_PROJECTS_INFO(Structure):
    """
    项目定制信息; Custom project info
    """
    _fields_ = [
        ('stuGPSInfo', NET_GPS_INFO),             # GPS位置信息;GPS info
        ('stuFaceComparisonPTZInfo', NET_FACECOMPARISON_PTZ_INFO),         # 人脸比对事件触发对应球机信息;Face matching event triggers corresponding ball machine information
        ('szPlateNumber', c_char * 64),           # 人脸比对时车牌信息;License plate information in face comparison
        ('byReserved', c_ubyte * 1024),           # 保留;Reserved
    ]


class DEV_EVENT_FACERECOGNITION_INFO(Structure):
    """
    事件类型FACERECOGNITION(人脸识别)对应的数据块描述信息; the describe of FACERECOGNITION's data
    """
    _fields_ = [
        ('nChannelID', c_int),                          # 通道号；channel ID
        ('szName', c_char * 128),                       # 事件名称;event name
        ('nEventID', c_int),                            # 事件ID;event ID
        ('UTC', NET_TIME_EX),                           # 事件发生的时间;the event happen time
        ('stuObject', SDK_MSG_OBJECT),                  # 检测到的物体;have being detected object
        ('nCandidateNum', c_int),                       # 当前人脸匹配到的候选对象数量;candidate number
        ('stuCandidates', CANDIDATE_INFO * 50),         # 当前人脸匹配到的候选对象信息;candidate info
        ('bEventAction', c_ubyte),                      # 事件动作,0表示脉冲事件,1表示持续性事件开始,2表示持续性事件结束;Event action,0 means pulse event,1 means continuous event's begin,2means continuous event's end;
        ('byImageIndex', c_ubyte),                      # 图片的序号, 同一时间内(精确到秒)可能有多张图片, 从0开始;Serial number of the picture, in the same time (accurate to seconds) may have multiple images, starting from 0
        ('byReserved1', c_ubyte * 2),                   # 字节对齐;byte alignment
        ('bGlobalScenePic', c_int),                     # 全景图是否存在;The existence panorama
        ('stuGlobalScenePicInfo', SDK_PIC_INFO),        # 全景图片信息;Panoramic Photos
        ('szSnapDevAddress',  c_char * 260),            # 抓拍当前人脸的设备地址,如：滨康路37号;Snapshot current face aadevice address
        ('nOccurrenceCount', c_uint),                   # 事件触发累计次数;event trigger accumilated times
        ('stuIntelliCommInfo', EVENT_INTELLI_COMM_INFO),# 智能事件公共信息;intelligent things info
        ('stuFaceData', NET_FACE_DATA),                 # 人脸数据;the data of face
        ('szUID', c_char * 32),                         # 抓拍人员写入数据库的唯一标识符;The unique identifier of the snap person to write to the database
        ('stuFeatureVector', NET_FEATURE_VECTOR),       # 特征值信息;Feature data information
        ('szFeatureVersion', c_char * 32),              # 特征值算法版本;The version of the feature data algorithm
        ('emFaceDetectStatus', c_int),                  # 人脸在摄像机画面中的状态,参考EM_FACE_DETECT_STATUS;The status of person in camera picture,refer to EM_FACE_DETECT_STATUS
        ('szSourceID', c_char * 32),                    # 事件关联ID,同一个物体或图片生成多个事件时SourceID相同;Correlate event ID, events arising from same object or picture could have same correlate event ID
        ('stuPasserbyInfo', NET_PASSERBY_INFO),         # 路人库信息;passerby info
        ('nStayTime', c_uint),                          # 路人逗留时间 单位：秒;stay time Unit:s
        ('stuGPSInfo', NET_GPS_INFO),                   # GPS信息;GPS info
        ('bReserved', c_ubyte * 432),                   # 保留字节,留待扩展;Reserved
        ('nRetCandidatesExNum', c_int),                 # 当前人脸匹配到的候选对象数量实际返回值;the actual return number of stuCandidatesEx
        ('stuCandidatesEx', CANDIDATE_INFOEX * 50),     # 当前人脸匹配到的候选对象信息扩展;the expansion of candidate information
        ('szSerialUUID', c_char * 22),                  # 级联物体ID唯一标识;szSerial UUID
                                                            # 格式如下：前2位%d%d:01-视频片段,02-图片,03-文件,99-其他;The format is as follows：Front 2:%d%d:01-video,02-picture,03-file,99-other;
                                                            # 中间14位YYYYMMDDhhmmss:年月日时分秒;后5位%u%u%u%u%u：物体ID，如00001;Middle 14:YYYYMMDDhhmmss:year,month,day,hour,minute,second;Last 5:%u%u%u%u%u：object ID，as 00001
        ('byReserved', c_ubyte * 2),                    # 对齐;reserved
        ('stuCustomProjects', NET_CUSTOM_PROJECTS_INFO),  # 项目定制信息;Custom project info
        ('bIsDuplicateRemove', c_int),                  # 智慧零售，是否符合去重策略（TRUE：符合 FALSE：不符合）;Smart retail, whether it conforms to the de duplication strategy (true: conforms to false: does not conform to)
        ('byReserved2', c_ubyte * 4),                   # 字节对齐;byte alaginment
    ]


class PLAY_FRAME_INFO(Structure):
    """
    事件类型FACERECOGNITION(人脸识别)对应的数据块描述信息; the describe of FACERECOGNITION's data
    """
    _fields_ = [
        ('nWidth', c_int),                          # Width, unit is pixel, 0 for audio data.
        ('nHeight', c_int),                         # height, 0 for audio data
        ('nStamp', c_int),                          # Time stamp info, unit is ms
        ('nType', c_int),                           # Video frame type,T_AUDIO16,T_RGB32,T_IYUV
        ('nFrameRate', c_int),                      # Video represents frame rate,audio represents sampling rate
    ]

class SCENE_IMAGE_INFO_EX(Structure):
    """
    全景广角图; Scene image
    """
    _fields_ = [
        ('nOffSet', c_uint),             # 在二进制数据块中的偏移;mage offset in the data
        ('nLength', c_uint),             # 图片大小,单位字节;image data length
        ('nWidth', c_uint),              # 图片宽度(像素);image width(pixel)
        ('nHeight', c_uint),             # 图片高度(像素);image Height(pixel)
        ('szFilePath', c_char*260),      # 全景图片路径;file path
        ('byReserved', c_char*512),      # 预留字节;Reserved
    ]


class NET_VAOBJECT_NUMMAN(Structure):
    """
    检测到的人信息; Human info
    """
    _fields_ = [
        ('nObjectID', c_uint),             # 物体ID，每个ID表示一个唯一的物体;Object ID
        ('emUniformStyle', c_int),         # 制服样式,参考EM_UNIFORM_STYLE;Uniform style，refer to EM_UNIFORM_STYLE
        ('stuBoundingBox', NET_RECT),         # 包围盒,手套对象在全景图中的框坐标,为0~8191相对坐标;Bounding box(8192 coordinate system)
        ('stuOriginalBoundingBox', NET_RECT), # 包围盒,绝对坐标;BoundingBox Rect, absolute coordinates
        ('byReserved', c_byte*128),           # 预留字节;Reserved
    ]


class DEV_EVENT_CROSSLINE_INFO(Structure):
    """
    事件类型CROSSLINEDETECTION(警戒线)对应的数据块描述信息; the describe of CROSSLINEDETECTION's data
    """
    _fields_ = [
        ('nChannelID', c_int),              # 通道号;Channel
        ('szName', c_char * 128),           # 事件名称;event name
        ('bReserved1', c_char * 4),         # 字节对齐;byte alignment
        ('PTS', c_double),                  # 时间戳(单位是毫秒);PTS(ms)
        ('UTC', NET_TIME_EX),               # 事件发生的时间;the event happen time
        ('nEventID', c_int),                # 事件ID;event ID
        ('stuObject', SDK_MSG_OBJECT),      # 检测到的物体;have being detected object
        ('stuFileInfo', SDK_EVENT_FILE_INFO),   # 事件对应文件信息;event file info
        ('DetectLine', SDK_POINT*20),           # 规则检测线;rule detect line
        ('nDetectLineNum', c_int),          # 规则检测线顶点数;rule detect line's point number
        ('TrackLine', SDK_POINT*20),        # 物体运动轨迹;object moveing track
        ('nTrackLineNum', c_int),           # 物体运动轨迹顶点数;object moveing track's point number
        ('bEventAction', c_byte),           # 事件动作,0表示脉冲事件,1表示持续性事件开始,2表示持续性事件结束;Event action,0 means pulse event,1 means continuous event's begin,2means continuous event's end;
        ('bDirection', c_byte),             # 表示入侵方向, 0-由左至右, 1-由右至左;direction, 0-left to right, 1-right to left
        ('byReserved', c_byte),             # 字节对齐;byte alignment
        ('byImageIndex', c_byte),           # 图片的序号, 同一时间内(精确到秒)可能有多张图片, 从0开始;Serial number of the picture, in the same time (accurate to seconds) may have multiple images, starting from 0
        ('dwSnapFlagMask', C_DWORD),        # 抓图标志(按位),0位:"*",1位:"Timing",2位:"Manual",3位:"Marked",4位:"Event",5位:"Mosaic",6位:"Cutout";flag(by bit),0bit:"*",1bit:"Timing",2bit:"Manual",3bit:"Marked",4bit:"Event",5bit:"Mosaic",6bit:"Cutout"
        ('nSourceIndex', c_int),            # 事件源设备上的index,-1表示数据无效,-1表示数据无效;the source device's index,-1 means data in invalid
        ('szSourceDevice', c_char*260),     # 事件源设备唯一标识,字段不存在或者为空表示本地设备;the source device's sign(exclusive),field said local device does not exist or is empty
        ('nOccurrenceCount', c_uint),       # 事件触发累计次数;event trigger accumulated times
        ('stuIntelliCommInfo', EVENT_INTELLI_COMM_INFO),    # 智能事件公共信息;intelli comm info
        ('stuExtensionInfo', NET_EXTENSION_INFO),       # 扩展信息;Extension info
        ('stuSceneImage', SCENE_IMAGE_INFO_EX),         # 全景广角图;Scene image
        ('nObjetcHumansNum', c_uint),                   # 检测到人的数量;Number of people detected
        ('stuObjetcHumans', NET_VAOBJECT_NUMMAN * 100), # 检测的到人;People detected
        ('byReserved1', c_byte*512),                    # 预留字节;Reserved
    ]


class NET_IN_GET_CAMERA_STATEINFO(Structure):
    """
    QueryDevInfo 接口 NET_QUERY_GET_CAMERA_STATE 命令入参;QueryDevInfo interface NET_QUERY_GET_CAMERA_STATE command to input parameter
    """
    _fields_ = [
        ('dwSize', C_DWORD),        # 结构体大小;Struct size
        ('bGetAllFlag', c_bool),    # 是否查询所有摄像机状态,若该成员为 TRUE,则 nChannels 成员无需设置;
                                    # if it is to check all the cameras status, if the member is TRUE, then nChannels member is unnecessary to set.
        ('nValidNum', c_int),       # 该成员,bGetAllFlag 为 FALSE时有效,表示 nChannels 成员有效个数
                                    # the member is valid when bGetAllFlag is FALSE, which means valid number of nChannels member
        ('nChannels', c_int*1024),  # 该成员,bGetAllFlag 为 FALSE时有效,将需要查询的通道号依次填入
                                    # The member is valid when bGetAllFlag is FALSE, it is to fill in the channel numbers in turn which needs inquiry.
    ]

class NET_CAMERA_STATE_INFO(Structure):
    """
    摄像机通道信息; Camera state info
    """
    _fields_ = [
        ('nChannel', c_int),    # 摄像机通道号, -1表示通道号无效;camera channel number, -1 means invalid channel number
        ('emConnectionState', c_int),   # 连接状态,参见SDK_Enum.py内的EM_CAMERA_STATE_TYPE;connection state，refer to EM_CAMERA_STATE_TYPE in SDK.Enum.py
        ('szReserved', c_char*1024),    # 保留字节;byte reserved
    ]

class NET_OUT_GET_CAMERA_STATEINFO(Structure):
    """
    QueryDevInfo 接口 NET_QUERY_GET_CAMERA_STATE 命令出参;QueryDevInfo interface NET_QUERY_GET_CAMERA_STATE command to output parameter
    """
    _fields_ = [
        ('dwSize', C_DWORD),        # 结构体大小;Struct size
        ('nValidNum', c_int),       # 查询到的摄像机通道状态有效个数,由sdk返回;valid number of camera channel state, returned by sdk
        ('nMaxNum', c_int),         # pCameraStateInfo 数组最大个数,由用户填写;max number of array, filled in by user
        ('pCameraStateInfo', POINTER(NET_CAMERA_STATE_INFO)),   # 摄像机通道信息数组,由用户分配,大小为sizeof(NET_CAMERA_STATE_INFO)*nMaxNum;camera channel info array, distributed by user,apply to sizeof(NET_CAMERA_STATE_INFO)*nMaxNum;

    ]