from .SDK_Struct import *
from .SDK_Enum import *
from .SDK_Callback import *

error_code = {
    0: '没有错误',
    -1: '未知错误',
    1: '系统出错',
    2: '网络错误,可能是因为网络超时',
    3: '设备协议不匹配',
    4: '句柄无效',
    5: '打开通道失败',
    6: '关闭通道失败',
    7: '用户参数不合法',
    8: 'SDK初始化出错',
    9: 'SDK清理出错',
    10: '申请render资源出错',
    11: '打开解码库出错',
    12: '关闭解码库出错',
    13: '多画面预览中检测到通道数为0',
    14: '录音库初始化失败',
    15: '录音库未经初始化',
    16: '发送音频数据出错',
    17: '实时数据已经处于保存状态',
    18: '未保存实时数据',
    19: '打开文件出错',
    20: '启动云台控制定时器失败',
    21: '对返回数据的校验出错',
    22: '没有足够的缓存',
    23: '当前SDK未支持该功能',
    24: '查询不到录象',
    25: '无操作权限',
    26: '暂时无法执行',
    27: '未发现对讲通道',
    28: '未发现音频',
    29: '网络SDK未经初始化',
    30: '下载已结束',
    31: '查询结果为空',
    32: '获取系统属性配置失败',
    33: '获取序列号失败',
    34: '获取常规属性失败',
    35: '获取DSP能力描述失败',
    36: '获取网络配置失败',
    37: '获取通道名称失败',
    38: '获取视频属性失败',
    39: '获取录象配置失败',
    40: '获取解码器协议名称失败',
    41: '获取232串口功能名称失败',
    42: '获取解码器属性失败',
    43: '获取232串口配置失败',
    44: '获取外部报警输入配置失败',
    45: '获取动态检测报警失败',
    46: '获取设备时间失败',
    47: '获取预览参数失败',
    48: '获取自动维护配置失败',
    49: '获取视频矩阵配置失败',
    50: '获取区域遮挡配置失败',
    51: '获取图象水印配置失败',
    52: '获取配置失败位置：组播端口按通道配置',
    55: '修改常规属性失败',
    56: '修改网络配置失败',
    57: '修改通道名称失败',
    58: '修改视频属性失败',
    59: '修改录象配置失败',
    60: '修改解码器属性失败',
    61: '修改232串口配置失败',
    62: '修改外部输入报警配置失败',
    63: '修改动态检测报警配置失败',
    64: '修改设备时间失败',
    65: '修改预览参数失败',
    66: '修改自动维护配置失败',
    67: '修改视频矩阵配置失败',
    68: '修改区域遮挡配置失败',
    69: '修改图象水印配置失败',
    70: '修改无线网络信息失败',
    71: '选择无线网络设备失败',
    72: '修改主动注册参数配置失败',
    73: '修改摄像头属性配置失败',
    74: '修改红外报警配置失败',
    75: '修改音频报警配置失败',
    76: '修改存储位置配置失败',
    77: '音频编码接口没有成功初始化',
    78: '数据过长',
    79: '设备不支持该操作',
    80: '设备资源不足',
    81: '服务器已经启动',
    82: '服务器尚未成功启动',
    83: '输入序列号有误',
    84: '获取硬盘信息失败',
    85: '获取连接Session信息',
    86: '输入密码错误超过限制次数',
    100: '密码不正确',
    101: '帐户不存在',
    102: '等待登录返回超时',
    103: '帐号已登录',
    104: '帐号已被锁定',
    105: '帐号已被列为黑名单',
    106: '资源不足,系统忙',
    107: '登录设备超时,请检查网络并重试',
    108: '网络连接失败',
    109: '登录设备成功,但无法创建视频通道,请检查网络状况',
    110: '超过最大连接数',
    111: '只支持3代协议',
    112: '未插入U盾或U盾信息错误',
    113: '客户端IP地址没有登录权限',
    117: '账号或密码错误',
    118: '设备尚未初始化，不能登录，请先初始化设备',
    119: '登录受限,可能是IP受限、时间段受限、有效期受限',
    120: 'Render库打开音频出错',
    121: 'Render库关闭音频出错',
    122: 'Render库控制音量出错',
    123: 'Render库设置画面参数出错',
    124: 'Render库暂停播放出错',
    125: 'Render库抓图出错',
    126: 'Render库步进出错',
    127: 'Render库设置帧率出错',
    128: 'Render库设置显示区域出错',
    129: 'Render库获取当前播放时间出错',
    140: '组名已存在',
    141: '组名不存在',
    142: '组的权限超出权限列表范围',
    143: '组下有用户,不能删除',
    144: '组的某个权限被用户使用,不能出除',
    145: '新组名同已有组名重复',
    146: '用户已存在',
    147: '用户不存在',
    148: '用户权限超出组权限',
    149: '保留帐号,不容许修改密码',
    150: '密码不正确',
    151: '密码不匹配',
    152: '账号正在使用中',
    300: '获取网卡配置失败',
    301: '获取无线网络信息失败',
    302: '获取无线网络设备失败',
    303: '获取主动注册参数失败',
    304: '获取摄像头属性失败',
    305: '获取红外报警配置失败',
    306: '获取音频报警配置失败',
    307: '获取存储位置配置失败',
    308: '获取邮件配置失败',
    309: '暂时无法设置',
    310: '配置数据不合法',
    311: '获取夏令时配置失败',
    312: '设置夏令时配置失败',
    313: '获取视频OSD叠加配置失败',
    314: '设置视频OSD叠加配置失败',
    315: '获取CDMA\GPRS网络配置失败',
    316: '设置CDMA\GPRS网络配置失败',
    317: '获取IP过滤配置失败',
    318: '设置IP过滤配置失败',
    319: '获取语音对讲编码配置失败',
    320: '设置语音对讲编码配置失败',
    321: '获取录像打包长度配置失败',
    322: '设置录像打包长度配置失败',
    323: '不支持网络硬盘分区',
    324: '获取设备上主动注册服务器信息失败',
    325: '主动注册重定向注册错误',
    326: '断开主动注册服务器错误',
    327: '获取mms配置失败',
    328: '设置mms配置失败',
    329: '获取短信激活无线连接配置失败',
    330: '设置短信激活无线连接配置失败',
    331: '获取拨号激活无线连接配置失败',
    332: '设置拨号激活无线连接配置失败'
}


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(*args, **kwargs)
        return self.__instance


class NetClient(metaclass=Singleton):
    """
    所有sdk接口都定义为该类的类方法
    all function in sdk which used define in this class
    """

    def __init__(self, *args, **kwargs):
        self._load_library()

    @classmethod
    def _load_library(cls):
        try:
            cls.sdk = load_library(netsdkdllpath)
            cls.config_sdk = load_library(configdllpath)
            cls.play_sdk = load_library(playsdkdllpath)
        except OSError as e:
            print('动态库加载失败')

    @classmethod
    def GetLastError(cls) -> int:
        """
        获取错误码;Return the function execution failure code
        """
        return cls.sdk.CLIENT_GetLastError() & 0x7fffffff

    @classmethod
    def GetLastErrorMessage(cls) -> str:
        """
        通过错误码获取错误信息;get the error message by error code
        """
        errcode = cls.GetLastError()
        if isinstance(errcode, int) is True:
            try:
                return error_code[errcode]
            except KeyError:
                return 'There is no such error code'
        else:
            return 'Unknown mistake'

    @classmethod
    def InitEx(cls, call_back: fDisConnect = None, user_data: C_LDWORD = 0, init_param: NETSDK_INIT_PARAM = NETSDK_INIT_PARAM()) -> int:
        """
        初始化接口，之前须先保证该接口调用成功;SDK initialization,called before using the SDK
        :param call_back: 回调函数;call back
        :param user_data:用户数据;user data
        :return:result:成功：1，失败：0；succeed：1，failed：0
        """
        init_param = pointer(init_param)
        result = cls.sdk.CLIENT_InitEx(call_back, user_data, init_param)
        if result != 1:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def Cleanup(cls):
        """
        SDK退出清理,Release sdk source
        """
        cls.sdk.CLIENT_Cleanup()
    @classmethod
    def LoginEx2(cls, ip: str, port: int, username: str, password: str,
                 spec_cap: EM_LOGIN_SPAC_CAP_TYPE = EM_LOGIN_SPAC_CAP_TYPE.TCP,
                 cap_param: c_void_p = None) -> tuple:
        ip = c_char_p(ip.encode())
        port = c_ushort(int(port))
        username = c_char_p(username.encode())
        password = c_char_p(password.encode())
        spec_cap = c_int(spec_cap)
        cap_param = c_void_p(cap_param) if cap_param is not None else None
        error = c_int(0)
        error_message = ''
        device_info = NET_DEVICEINFO_Ex()
        cls.sdk.CLIENT_LoginEx2.restype = C_LLONG
        login_id = cls.sdk.CLIENT_LoginEx2(ip, port, username, password,
                                           spec_cap, cap_param, byref(device_info), byref(error))
        login_error = {
            1: '账号或密码错误',
            2: '用户名不存在',
            3: '登录超时',
            4: '重复登录',
            5: '帐号被锁定',
            6: '帐号被列入黑名单',
            7: '系统忙,资源不足',
            8: '子连接失败',
            9: '主连接失败',
            10: '超过最大连接数',
            11: '只支持3代协议',
            12: '设备未插入U盾或U盾信息错误',
            13: '客户端IP地址没有登录权限',
            18: '设备账号未初始化，无法登陆'
        }
        if login_id == 0:
            try:
                error_message = login_error[error.value]
            except KeyError:
                error_message = 'There is no such error code'
            print(error_message)
        return login_id, device_info, error_message

    @classmethod
    def LoginWithHighLevelSecurity(cls, stuInParam: NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY, stuOutParam: NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY) -> tuple:
        """
        高安全级别登陆;login device with high level security
        :param stuInParam:传入参数结构体;in parameter structure
        :param stuOutParam:传出参数结构体;out parameter structure
        :return:login_id:成功返回登录句柄，失败返回0，登录成功后设备信息保存在NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY的stuDeviceInfo;
                         secssed：login id,failed：0，if login succeed,device info in stuDeviceInfo of NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY
                device_info:输出的设备信息;device information，for output parmaeter
                error_message:登录接口的错误信息；error message of login
        """
        cls.sdk.CLIENT_LoginWithHighLevelSecurity.restype = C_LLONG
        login_id = cls.sdk.CLIENT_LoginWithHighLevelSecurity(byref(stuInParam), byref(stuOutParam))
        login_error = {
            1: '账号或密码错误',
            2: '用户名不存在',
            3: '登录超时',
            4: '重复登录',
            5: '帐号被锁定',
            6: '帐号被列入黑名单',
            7: '系统忙,资源不足',
            8: '子连接失败',
            9: '主连接失败',
            10: '超过最大连接数',
            11: '只支持3代协议',
            12: '设备未插入U盾或U盾信息错误',
            13: '客户端IP地址没有登录权限',
            18: '设备账号未初始化，无法登陆'
        }
        error_message = ''
        device_info = NET_DEVICEINFO_Ex()
        if login_id == 0:
            try:
                error_message = login_error[stuOutParam.nError]
            except KeyError:
                error_message = 'There is no such error code'
            print(error_message)
        else:
            device_info = stuOutParam.stuDeviceInfo
        return login_id, device_info, error_message

    # @classmethod
    # def LoginWithHighLevelSecurity(cls, ip: str, port: int, username: str, password: str,
    #                                spec_cap: EM_LOGIN_SPAC_CAP_TYPE = EM_LOGIN_SPAC_CAP_TYPE.TCP,
    #                                cap_param: c_void_p = None) -> tuple:
    #     """
    #     高安全级别登陆;login device with high level security
    #     :param ip:设备IP;device IP
    #     :param port:设备端口;device port
    #     :param username:用户名;username
    #     :param password:密码;password
    #     :param spec_cap:登陆方式;login mode
    #     :param cap_param:扩展参数，只有当 spec_cap为EM_LOGIN_SPAC_CAP_TYPE.SERVER_CONN时有效;compensation parameter，nSpecCap = EM_LOGIN_SPAC_CAP_TYPE.SERVER_CONN，pCapParam fill in device serial number string(mobile dvr login)
    #     :return:login_id:成功返回登录句柄，失败返回0，登录成功后设备信息保存在NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY的stuDeviceInfo;
    #                      secssed：login id,failed：0，if login succeed,device info in stuDeviceInfo of NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY
    #             device_info:输出的设备信息;device information，for output parmaeter
    #             error_message:登录接口的错误信息；error message of login
    #     """
    #
    #     stuInParam = NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY()
    #     stuInParam.dwSize = sizeof(NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY)
    #     stuInParam.szIP = ip.encode()
    #     stuInParam.nPort = port
    #     stuInParam.szUserName = username.encode()
    #     stuInParam.szPassword = password.encode()
    #     stuInParam.emSpecCap = spec_cap
    #     stuInParam.pCapParam = cap_param
    #
    #     stuOutParam = NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY()
    #     stuOutParam.dwSize = sizeof(NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY)
    #     cls.sdk.CLIENT_LoginWithHighLevelSecurity.restype = C_LLONG
    #     login_id = cls.sdk.CLIENT_LoginWithHighLevelSecurity(byref(stuInParam), byref(stuOutParam))
    #     login_error = {
    #         1: '账号或密码错误',
    #         2: '用户名不存在',
    #         3: '登录超时',
    #         4: '重复登录',
    #         5: '帐号被锁定',
    #         6: '帐号被列入黑名单',
    #         7: '系统忙,资源不足',
    #         8: '子连接失败',
    #         9: '主连接失败',
    #         10: '超过最大连接数',
    #         11: '只支持3代协议',
    #         12: '设备未插入U盾或U盾信息错误',
    #         13: '客户端IP地址没有登录权限',
    #         18: '设备账号未初始化，无法登陆'
    #     }
    #     error_message = ''
    #     device_info = NET_DEVICEINFO_Ex()
    #     if login_id == 0:
    #         try:
    #             error_message = login_error[stuOutParam.nError]
    #         except KeyError:
    #             error_message = 'There is no such error code'
    #         print(error_message)
    #     else:
    #         device_info = stuOutParam.stuDeviceInfo
    #     return login_id, device_info, error_message

    @classmethod
    def SetAutoReconnect(cls, call_back: fHaveReConnect, user_data: C_LDWORD = None):
        """
        设置断线重连成功回调函数,设置后SDK内部断线自动重连;Set re-connection callback function after disconnection. Internal SDK  auto connect again after disconnection
        :param call_back:重连成功回调函数;Reconnect callback
        :param user_data:自定义用户数据;User data
        """
        user_data = byref(c_uint(user_data)) if user_data is not None else None
        cls.sdk.CLIENT_SetAutoReconnect(call_back, user_data)

    @classmethod
    def Logout(cls, login_id: int) -> int:
        """
        向设备注销;Log out the device
        :param login_id:登陆ID,LoginWithHighLevelSecurity返回值;user LoginID,LoginWithHighLevelSecurity's returns value
        :return:result:成功：1，失败：0；succeed：1，failed：0
        """
        login_id = C_LLONG(login_id)
        result = cls.sdk.CLIENT_Logout(login_id)
        if result == 0:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def LogOpen(cls, log_info: LOG_SET_PRINT_INFO) -> int:
        """
        打开日志功能;open log function
        :param log_info:日志相关设置参数; param of log setting
        :return:result:成功：1，失败：0；succeed：1，failed：0
        """
        log_info = pointer(log_info)
        result = cls.sdk.CLIENT_LogOpen(log_info)
        if result != 1:
            print(cls.GetLastErrorMessage())
        return result
    @classmethod
    def LogClose(cls) -> int:
        """
        关闭日志功能;close log function
        :return:result:成功：1，失败：0；succeed：1，failed：0
        """
        result = cls.sdk.CLIENT_LogClose()
        if result != 1:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def RealPlayEx(cls, login_id: int, channel: int, hwnd: int, play_type=SDK_RealPlayType.Realplay) -> C_LLONG:
        """
        开始实时监视;Begin real-time monitor
        :param login_id:登陆句柄,LoginWithHighLevelSecurity返回值;user LoginID,LoginWithHighLevelSecurity's returns value
        :param channel:通道号;real time monitor channel NO.(from 0).
        :param hwnd:窗口句柄;display window handle.
        :param play_type:主码流类型;realplay type
        :return:realplay_id:失败返回0，成功返回大于0的值;failed return 0, successful return the real time monitorID(real time monitor handle),as parameter of related function.
        """

        login_id = C_LLONG(login_id)
        channel = c_int(channel)
        hwnd = c_long(hwnd)
        play_type = c_int(play_type)
        cls.sdk.CLIENT_RealPlayEx.restype = C_LLONG
        realplay_id = cls.sdk.CLIENT_RealPlayEx(login_id, channel, hwnd, play_type)
        if realplay_id == 0:
            print(cls.GetLastErrorMessage())
        return realplay_id

    @classmethod
    def SetRealDataCallBackEx2(cls, realplay_id: int, cbRealData: fRealDataCallBackEx2, dwUser: C_LDWORD, dwFlag: EM_REALDATA_FLAG) -> bool:
        """
        开始实时监视;Begin real-time monitor
        :param realplay_id:监视ID,RealPlayEx返回值;monitor handle,RealPlayEx returns value
        :param cbRealData:回调函数;callback function
        :param dwUser:用户数据;user data
        :param dwFlag:回调数据类型;real data type
        :return:result:成功：1，失败：0；succeed：1，failed：0
        """
        realplay_id = C_LLONG(realplay_id)
        dwFlag = C_DWORD(dwFlag)
        result = cls.sdk.CLIENT_SetRealDataCallBackEx2(realplay_id, cbRealData, dwUser, dwFlag)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def StopRealPlayEx(cls, realplay_id: int) -> int:
        """
        停止实时预览;stop real-time preview
        :param realplay_id:监视ID,RealPlayEx返回值;monitor handle,RealPlayEx returns value
        :return:result:成功：1，失败：0；succeed：1，failed：0
        """
        realplay_id = C_LLONG(realplay_id)
        result = cls.sdk.CLIENT_StopRealPlayEx(realplay_id)
        if result == 0:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def StartSearchDevicesEx(cls, pInBuf: NET_IN_STARTSERACH_DEVICE, pOutBuf: NET_OUT_STARTSERACH_DEVICE) -> C_LLONG:
        """
        异步搜索设备;asynchronism search device
        :param pInBuf:输入参数;input param
        :param pOutBuf:输出参数;output param
        :return:搜索句柄;search handle
        """
        cls.sdk.CLIENT_StartSearchDevicesEx.restype = C_LLONG
        result = cls.sdk.CLIENT_StartSearchDevicesEx(byref(pInBuf), byref(pOutBuf))
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def SearchDevicesByIPs(cls, pIpSearchInfo: DEVICE_IP_SEARCH_INFO, cbSearchDevices: fSearchDevicesCB,
                           dwUserData: C_LDWORD, szLocalIp: c_char_p = None,
                           dwWaitTime: C_DWORD = 5000) -> c_int:
        """
        跨网段搜索设备IP;search device ip cross VLAN
        :param pIpSearchInfo:待搜索的IP信息,ENGLISH_LANG:IP info of
        :param cbSearchDevices:回调函数,ENGLISH_LANG:Search devices call back
        :param dwUserData:用户数据,ENGLISH_LANG:User data
        :param szLocalIp:本地IP,ENGLISH_LANG:Local IP
        :param dwWaitTime:等待时间,ENGLISH_LANG:Wait time c_char_p(szLocalIp.encode())
        :return:1:搜索成功,0:搜索失败;1:search device success,0:search device failed
        """
        szLocalIp = c_char_p(szLocalIp)
        dwUserData = C_LDWORD(dwUserData)
        dwWaitTime = C_DWORD(dwWaitTime)
        result = cls.sdk.CLIENT_SearchDevicesByIPs(byref(pIpSearchInfo), cbSearchDevices, dwUserData, szLocalIp, dwWaitTime)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def StopSearchDevices(cls, lSearchHandle: C_LLONG) -> c_int:
        """
        异步停止搜索设备;stop asynchronism search IPC, NVS and etc in LAN
        :param lSearchHandle:搜索句柄;search handle
        :return:1:停止搜索成功,0:停止搜索失败;1:stop search device success,0:stop search device failed
        """
        lSearchHandle = C_LLONG(lSearchHandle)
        result = cls.sdk.CLIENT_StopSearchDevices(lSearchHandle)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def InitDevAccount(cls, pInitAccountIn: NET_IN_INIT_DEVICE_ACCOUNT, pInitAccountOut: NET_OUT_INIT_DEVICE_ACCOUNT,
                       dwWaitTime: int = 5000, szLocalIp: c_char_p = None) -> c_int:
        """
            初始化设备账户;init account
            :param pInitAccountIn:输入参数结构体NET_IN_INIT_DEVICE_ACCOUNT;input param,corresponding to NET_IN_INIT_DEVICE_ACCOUNT
            :param pInitAccountOut:输出参数结构体NET_OUT_INIT_DEVICE_ACCOUNT;output param,corresponding to NET_OUT_INIT_DEVICE_ACCOUNT
            :return:1:初始化设备账户成功,0:初始化设备账户失败;1:Init device account success,0:Init device account failed
            """
        szLocalIp = c_char_p(szLocalIp)
        result = cls.sdk.CLIENT_InitDevAccount(byref(pInitAccountIn), byref(pInitAccountOut), dwWaitTime, szLocalIp)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def RealLoadPictureEx(cls, lLoginID: C_LLONG, nChannelID: c_int, dwAlarmType: c_ulong,
                          bNeedPicFile: c_int, cbAnalyzerData: fAnalyzerDataCallBack, dwUser: C_LDWORD = 0,
                          reserved: c_void_p = None) -> C_LLONG:
        """
        实时上传智能分析数据图片(扩展接口,bNeedPicFile表示是否订阅图片文件); real load picture of intelligent analysis(expand interface: 'bNeedPicFile == true' instruct load picture file, 'bNeedPicFile == false' instruct not load picture file )
        :param lLoginID:登陆ID; login returns value
        :param nChannelID:通道号; channel id
        :param dwAlarmType:事件类型,参考EM_EVENT_IVS_TYPE; event type see EM_EVENT_IVS_TYPE
        :param bNeedPicFile:是否订阅图片文件; subscribe image file or not,ture-yes,return intelligent image info during callback function,false not return intelligent image info during callback function
        :param cbAnalyzerData:事件回调函数; intelligent data analysis callback
        :param dwUser:用户数据; user data
        :param reserved:保留参数; reserved
        :return:订阅句柄;Handle
        """
        lLoginID = C_LLONG(lLoginID)
        nChannelID = c_int(nChannelID)
        dwAlarmType = c_ulong(dwAlarmType)
        bNeedPicFile = c_int(bNeedPicFile)
        dwUser = C_LDWORD(dwUser)
        reserved = c_void_p(reserved)
        cls.sdk.CLIENT_RealLoadPictureEx.restype = C_LLONG
        event_id = cls.sdk.CLIENT_RealLoadPictureEx(lLoginID, nChannelID, dwAlarmType, bNeedPicFile, cbAnalyzerData,
                                                    dwUser, reserved)
        if not event_id:
            print(cls.GetLastErrorMessage())
        return event_id

    @classmethod
    def StopLoadPic(cls, lAnalyzerHandle:C_LLONG)->c_int:
        """
        停止上传智能分析数据－图片;stop asynchronism search IPC, NVS and etc in LAN
        :param lAnalyzerHandle:订阅句柄,RealLoadPictureEx接口返回值;handle,the value is returned by RealLoadPictureEx
        :return:1:停止订阅成功,0:停止订阅失败;1:StopLoadPic success,0:StopLoadPic failed
        """
        lAnalyzerHandle = C_LLONG(lAnalyzerHandle)
        result = cls.sdk.CLIENT_StopLoadPic(lAnalyzerHandle)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def SetDeviceMode(cls, login_id: int, emType: int, value: c_void_p) -> c_int:
        """
        设置语音对讲模式,客户端方式还是服务器方式(pValue内存由用户申请释放，大小参照EM_USEDEV_MODE对应的结构体); Set audio talk mode(client-end mode or server mode), user malloc pValue's memory,please refer to the corresponding structure of EM_USEDEV_MODE
        :param login_id:登陆句柄,LoginWithHighLevelSecurity返回值;user LoginID,LoginWithHighLevelSecurity's returns value
        :param emType:工作模式类型; user work mode
        :param value:emType对应的结构体; support these emType
        :return:成功：1，失败：0；succeed：1，failed：0
        """
        if login_id == 0:
            return
        login_id = C_LLONG(login_id)
        emType = c_int(emType)
        p_value = pointer(value)
        result = cls.sdk.CLIENT_SetDeviceMode(login_id, emType, p_value)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def QueryRecordFile(cls, login_id: int, channel_id: int, recordfile_type: int,
                        start_time: NET_TIME, end_time: NET_TIME,
                        card_id: str, wait_time:int, is_querybytime:bool) -> tuple:
        """
        查询时间段内的所有录像文件; Search all recorded file sin the specified periods
        :param login_id:登陆句柄,LoginWithHighLevelSecurity返回值;user LoginID,LoginWithHighLevelSecurity's returns value
        :param channel_id:查询通道号; user work mode
        :param recordfile_type:查询类型，参考EM_QUERY_RECORD_TYPE; type of record file,see EM_QUERY_RECORD_TYPE
        :param start_time:起始时间; start time
        :param end_time:结束时间; end time
        :param card_id:卡号; card id
        :param wait_time:超时时间; wait timr
        :param is_querybytime:是否是按时间查询; query by time or not
        :return:result:成功：1，失败：0；succeed：1，failed：0
                file_count:返回文件个数; the file count of query
                recordfile_infos:文件信息; record file infos
        """
        if login_id == 0:
            return
        login_id = C_LLONG(login_id)
        channel_id = c_int(channel_id)
        recordfile_type = c_int(recordfile_type)
        recordfile_infos = NET_RECORDFILE_INFO * 5000
        p_recordfile_infos = recordfile_infos()
        maxlen = sizeof(NET_RECORDFILE_INFO) * 5000
        maxlen = c_int(maxlen)
        file_count = c_int(0)
        is_querybytime = c_bool(is_querybytime)

        result = cls.sdk.CLIENT_QueryRecordFile(login_id, channel_id, recordfile_type, byref(start_time), byref(end_time),
                                                     card_id, p_recordfile_infos, maxlen, byref(file_count), wait_time, is_querybytime)
        if not result:
            print(cls.GetLastErrorMessage())
        else:
            file_count = file_count.value
            file_count = 5000 if file_count > 5000 else file_count
            recordfile_infos = p_recordfile_infos
        return result, file_count, recordfile_infos

    @classmethod
    def PlayBackByTimeEx(cls, login_id: int, channel_id: int,
                         start_time: NET_TIME, end_time: NET_TIME, hwnd: C_LONG,
                         callback_timedownloadpos: fDownLoadPosCallBack, time_UserData: C_LDWORD,
                         callback_timedownloaddata: fDataCallBack, data_UserData: C_LDWORD) -> int:
        """
        查询时间段内的所有录像文件; Search all recorded file sin the specified periods
        :param login_id:登陆句柄,LoginWithHighLevelSecurity返回值;user LoginID,LoginWithHighLevelSecurity's returns value
        :param channel_id:查询通道号; user work mode
        :param in_param:输入参数结构体NET_IN_PLAY_BACK_BY_TIME_INFO; input param,corresponding to NET_IN_PLAY_BACK_BY_TIME_INFO
        :param out_param:输出参数结构体NET_OUT_PLAY_BACK_BY_TIME_INFO; output param,corresponding to NET_OUT_PLAY_BACK_BY_TIME_INFO
        :return:result:成功：1，失败：0；succeed：1，failed：0
        """
        if login_id == 0:
            return 0
        login_id = C_LLONG(login_id)
        channel_id = c_int(channel_id)
        hwnd = C_LONG(hwnd)
        cls.sdk.CLIENT_PlayBackByTimeEx.restype = C_LLONG
        result = cls.sdk.CLIENT_PlayBackByTimeEx(login_id, channel_id, byref(start_time), byref(end_time), hwnd,
                                                 callback_timedownloadpos, time_UserData,
                                                 callback_timedownloaddata, data_UserData)
        if not result:
            print(cls.GetLastErrorMessage())
        return result
    @classmethod
    def PlayBackByTimeEx2(cls, login_id: int, channel_id: int,
                          in_param: NET_IN_PLAY_BACK_BY_TIME_INFO, out_param: NET_OUT_PLAY_BACK_BY_TIME_INFO) -> int:
        """
        查询时间段内的所有录像文件; Search all recorded file sin the specified periods
        :param login_id:登陆句柄,LoginWithHighLevelSecurity返回值;user LoginID,LoginWithHighLevelSecurity's returns value
        :param channel_id:查询通道号; user work mode
        :param in_param:输入参数结构体NET_IN_PLAY_BACK_BY_TIME_INFO; input param,corresponding to NET_IN_PLAY_BACK_BY_TIME_INFO
        :param out_param:输出参数结构体NET_OUT_PLAY_BACK_BY_TIME_INFO; output param,corresponding to NET_OUT_PLAY_BACK_BY_TIME_INFO
        :return:result:成功：1，失败：0；succeed：1，failed：0
        """
        if login_id == 0:
            return 0
        login_id = C_LLONG(login_id)
        channel_id = c_int(channel_id)
        in_param = byref(in_param)
        out_param = byref(out_param)
        cls.sdk.CLIENT_PlayBackByTimeEx2.restype = C_LLONG
        result = cls.sdk.CLIENT_PlayBackByTimeEx2(login_id, channel_id, in_param, out_param)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def StopPlayBack(cls, playback_id: int) -> int:
        """
        停止回放; stop palyback
        :param playback_id:回放句柄, PlayBackByTimeEx2的返回值； palyback handle，PlayBackByTimeEx2's returns value
        :return:result:成功：1，失败：0；succeed：1，failed：0
        """
        if playback_id == 0:
            return
        playback_id = C_LLONG(playback_id)
        result = cls.sdk.CLIENT_StopPlayBack(playback_id)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def PausePlayBack(cls, playback_id: int, is_pause: bool) -> int:
        """
        查询时间段内的所有录像文件; Search all recorded file sin the specified periods
        :param playback_id:回放句柄, PlayBackByTimeEx2的返回值； palyback handle，PlayBackByTimeEx2's returns value
        :param is_pause:操作动作，暂停还是继续; opreate type， pause or continue
        :return:result:成功：1，失败：0；succeed：1，failed：0
        """
        if playback_id == 0:
            return 0
        playback_id = C_LLONG(playback_id)
        is_pause = c_int(is_pause)
        result = cls.sdk.CLIENT_PausePlayBack(playback_id, is_pause)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def DownloadByTimeEx(cls, login_id: int, channel_id: int, recordfile_type: int,
                          start_time: NET_TIME, end_time: NET_TIME, save_filename: str,
                          callback_timedownloadpos: fTimeDownLoadPosCallBack, time_UserData: C_LDWORD,
                          callback_timedownloaddata: fDataCallBack, data_UserData: C_LDWORD, pReserved: int = 0) -> int:
        """
        通过时间下载录像--扩展; Through the time to download the video - extension
        :param login_id:登陆句柄,LoginWithHighLevelSecurity返回值;user LoginID,LoginWithHighLevelSecurity's returns value
        :param channel_id:查询通道号; user work mode
        :param recordfile_type:查询类型，参考EM_QUERY_RECORD_TYPE; type of record file,see EM_QUERY_RECORD_TYPE
        :param start_time:起始时间; start time
        :param end_time:结束时间; end time
        :param save_filename:保存录像的文件名; save file name
        :param callback_timedownloadpos:下载的时间回调; download by time's pos callback
        :param time_UserData:用户数据; callback_timedownloadpos's user data
        :param callback_timedownloaddata:下载的数据回调; video data's callback
        :param data_UserData:用户数据; callback_timedownloaddata's user data
        :return:result:成功：1，失败：0；succeed：1，failed：0
        """
        if login_id == 0:
            return
        login_id = C_LLONG(login_id)
        channel_id = c_int(channel_id)
        save_filename = c_char_p(save_filename.encode('gbk'))
        pReserved = pointer(c_int(pReserved))
        cls.sdk.CLIENT_DownloadByTimeEx.restype = C_LLONG
        result = cls.sdk.CLIENT_DownloadByTimeEx(login_id, channel_id, recordfile_type,
                                                 byref(start_time), byref(end_time), save_filename,
                                                 callback_timedownloadpos, time_UserData,
                                                 callback_timedownloaddata, data_UserData, pReserved)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def StopDownload(cls, download_id: int) -> int:
        """
        停止录像下载;  Stop record download
        :param download_id:下载句柄, DownloadByTimeEx的返回值； download handle，DownloadByTimeEx's returns value
        :return:result:成功：1，失败：0；succeed：1，failed：0
        """
        if download_id == 0:
            return
        download_id = C_LLONG(download_id)
        result = cls.sdk.CLIENT_StopDownload(download_id)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def GetDevConfig(cls, login_id: C_LLONG, cfg_type: C_DWORD, channel_id: C_LONG,
                     out_buffer: C_LLONG, outbuffer_size: C_DWORD,
                     wait_time: int = 5000) -> int:
        """
        查询配置信息； Search configuration information
        :param login_id:登陆句柄,LoginWithHighLevelSecurity返回值;user LoginID,LoginWithHighLevelSecurity's returns value
        :param cfg_type:查询类型，参考EM_QUERY_RECORD_TYPE; type of record file,see EM_QUERY_RECORD_TYPE
        :param channel_id:查询通道号; user work mode
        :param out_buffer:获取的结构体数据; struct data of output
        :param outbuffer_size:out_buffer数据长度; size of out_buffer
        :param wait_time:超时时间; wait time
        :return:result:成功：1，失败：0；succeed：1，failed：0
        """
        if login_id == 0:
            return
        login_id = C_LLONG(login_id)
        channel_id = C_LONG(channel_id)
        out_buffer = pointer(out_buffer)
        outbuffer_size = C_DWORD(outbuffer_size)
        bytes_returned = c_uint(0)
        result = cls.sdk.CLIENT_GetDevConfig(login_id, cfg_type, channel_id, out_buffer, outbuffer_size, byref(bytes_returned), wait_time)
        if not result:
            print(cls.GetLastErrorMessage())
        if outbuffer_size.value != bytes_returned.value:
            print('返回结果出错(Return value is wrong!)')
            result = 0
        return result

    @classmethod
    def SetDevConfig(cls, login_id: C_LLONG, cfg_type: C_DWORD, channel_id: C_LONG,
                     in_buffer: C_LLONG, inbuffer_size: C_DWORD,
                     wait_time: int = 5000) -> int:
        """
        设置配置信息; Set configuration information
        :param login_id:登陆句柄,LoginWithHighLevelSecurity返回值;user LoginID,LoginWithHighLevelSecurity's returns value
        :param cfg_type:查询类型，参考EM_QUERY_RECORD_TYPE; type of record file,see EM_QUERY_RECORD_TYPE
        :param channel_id:查询通道号; user work mode
        :param in_buffer:传入的结构体数据; struct data of input
        :param inbuffer_size:in_buffer数据长度; size of in_buffer
        :param wait_time:超时时间; wait time
        :return:result:成功：1，失败：0；succeed：1，failed：0
        """
        if login_id == 0:
            return
        login_id = C_LLONG(login_id)
        channel_id = C_LONG(channel_id)
        in_buffer = pointer(in_buffer)
        inbuffer_size = C_DWORD(inbuffer_size)
        result = cls.sdk.CLIENT_SetDevConfig(login_id, cfg_type, channel_id, in_buffer, inbuffer_size, wait_time)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def RebootDev(cls, login_id: int) -> int:
        """
        重启设备;  Reboot device
        :param login_id:登陆句柄,LoginWithHighLevelSecurity返回值;user LoginID,LoginWithHighLevelSecurity's returns value
        :return:result:成功：1，失败：0；succeed：1，failed：0
        """
        if login_id == 0:
            return
        login_id = C_LLONG(login_id)
        result = cls.sdk.CLIENT_RebootDev(login_id)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def SetSnapRevCallBack(cls, OnSnapRevMessage: fSnapRev, dwUser: C_LDWORD) -> None:
        """
        设置抓图回调函数;Set snapshot callback function
        :param OnSnapRevMessage:抓图回调;snap receive message
        :param dwUser:用户数据；user data
        :return:None
        """
        dwUser = C_LDWORD(dwUser)
        cls.sdk.CLIENT_SetSnapRevCallBack(OnSnapRevMessage, dwUser)

    @classmethod
    def SnapPictureEx(cls, lLoginID: C_LLONG, par: SNAP_PARAMS, reserved=0)->c_int:
        """
        抓图请求扩展接口;Snapshot request--extensive
        :param lLoginID:登陆句柄,LoginWithHighLevelSecurity返回值;user LoginID,LoginWithHighLevelSecurity's returns value
        :param par:抓图参数结构体;Snapshot parameter structure
        :param reserved:保留字段；reserved
        :return:空；None
        """
        lLoginID = C_LLONG(lLoginID)
        par = pointer(par)
        reserved = pointer(c_int(reserved))
        result = cls.sdk.CLIENT_SnapPictureEx(lLoginID, par, reserved)
        if not result:
            print(cls.GetLastErrorMessage())
        return result



    @classmethod
    def StartListenEx(cls, lLoginID:C_LLONG)->c_int:
        """
        向设备订阅报警--扩展;subscribe alarm---extensive
        :param lLoginID:登陆句柄,LoginWithHighLevelSecurity返回值;user LoginID,LoginWithHighLevelSecurity's returns value
        :return:1:成功，0：失败；1：success,0:failed
        """
        lLoginID = C_LLONG(lLoginID)
        result = cls.sdk.CLIENT_StartListenEx(lLoginID)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def SetDVRMessCallBackEx1(cls, cbMessage:fMessCallBackEx1, dwUser:C_LDWORD)->None:
        """
        设置报警回调函数;Set alarm callback function
        :param cbMessage:消息回调函数原形(pBuf内存由SDK内部申请释放); Alarm message callback function original shape
        :param dwUser:用户数据；user data
        :return:空；None
        """
        dwUser = C_LDWORD(dwUser)
        cls.sdk.CLIENT_SetDVRMessCallBackEx1(cbMessage, dwUser)

    @classmethod
    def StopListen(cls,lLoginID:C_LLONG)->c_int:
        """
        停止订阅报警;Stop subscribe alarm
        :param lLoginID: 登陆句柄,LoginWithHighLevelSecurity返回值;user LoginID,LoginWithHighLevelSecurity's returns value
        :return:1:成功，0：失败；1：success,0:failed
        """
        lLoginID = C_LLONG(lLoginID)
        result = cls.sdk.CLIENT_StopListen(lLoginID)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

    @classmethod
    def RenderPrivateData(cls, realplay_id: C_LLONG, bTrue: bool) -> c_int:
        """
        显示私有数据，例如规则框，规则框报警，移动侦测等;Stop subscribe alarm
        :param realplay_id:监视ID,RealPlayEx返回值;monitor handle,RealPlayEx returns value
        :param lLoginID: 播放句柄,LoginWithHighLevelSecurity返回值;user LoginID,LoginWithHighLevelSecurity's returns value
        :return:1:成功，0：失败；1：success,0:failed
        """
        realplay_id = C_LLONG(realplay_id)
        bTrue = c_int(bTrue)
        result = cls.sdk.CLIENT_RenderPrivateData(realplay_id, bTrue)
        if not result:
            print(cls.GetLastErrorMessage())
        return result


    # **************************
    # **************************
    # 以下都是PlaySDK的接口
    # **************************
    # **************************

    @classmethod
    def GetFreePort(cls) -> tuple:
        """
        Get free port. Range in 101~511
        :return:result: 1：success,0:failed
                port: Get free Port number
        """
        port = c_int()
        result = cls.play_sdk.PLAY_GetFreePort(byref(port))
        if not result:
            print('PLAY_GetFreePort error!')
        return result, port

    @classmethod
    def OpenStream(cls, port: c_int) -> bool:
        """
        Open stream interface (Just the same as open a file)
        :param port: Port number,GetFreePort's returns value
        :return:result: 1：success,0:failed
        """
        result = cls.play_sdk.PLAY_OpenStream(port, None, 0, 900*1024)
        if not result:
            print('PLAY_OpenStream error!')
        return result

    @classmethod
    def SetDecCallBack(cls, port: c_int, decoding_callback: fDecCBFun) -> bool:
        """
        Open stream interface (Just the same as open a file)
        :param port: Port number,GetFreePort's returns value
        :param decoding_callback: decoding call function indicator, cannot be NULL. Call function parameter definitions are as follows.
        :return:result: 1：success,0:failed
        """
        result = cls.play_sdk.PLAY_SetDecCallBack(port, decoding_callback)
        if not result:
            print('PLAY_SetDecCallBack error!')
        return result

    @classmethod
    def InputData(cls, port: c_int, pBuf: POINTER(c_byte), size: c_uint) -> bool:
        """
        Input the stream data you get from the card. Enable stream and Then call PLAY_Play to input data
        :param port: Port number,GetFreePort's returns value
        :param pBuf: Buffer address
        :param nSize: Buffer size
        :return:result: 1：success,0:failed
        """
        result = cls.play_sdk.PLAY_InputData(port, pBuf, size)
        if not result:
            print('PLAY_InputData error!')
        return result

    @classmethod
    def Play(cls, port: c_int, hwnd: int) -> bool:
        """
        Start play. If it is playing, then return current play status to normal speed
        :param port: Port number,GetFreePort's returns value
        :param hwnd: Play window handle
        :return:result: 1：success,0:failed
        """
        hwnd = C_LONG(hwnd)
        result = cls.play_sdk.PLAY_Play(port, hwnd)
        if not result:
            print('PLAY_Play error!')
        return result

    @classmethod
    def ReleasePort(cls, port: c_int) -> bool:
        """
        Release the port got with PLAY_GetFreePort
        :param port: Port number,GetFreePort's returns value
        :return:result: 1：success,0:failed
        """
        result = cls.play_sdk.PLAY_ReleasePort(port)
        if not result:
            print('PLAY_ReleasePort error!')
        return result

    @classmethod
    def CloseStream(cls, port: c_int) -> bool:
        """
        Close stream
        :param port: Port number,GetFreePort's returns value
        :return:result: 1：success,0:failed
        """
        result = cls.play_sdk.PLAY_CloseStream(port)
        if not result:
            print('PLAY_CloseStream error!')
        return result

    @classmethod
    def Stop(cls, port: c_int) -> bool:
        """
        Stop Play
        :param port: Port number,GetFreePort's returns value
        :return:result: 1：success,0:failed
        """
        result = cls.play_sdk.PLAY_Stop(port)
        if not result:
            print('PLAY_Stop error!')
        return result

    @classmethod
    def QueryDevInfo(cls, lLoginID:int, nQueryType:int, pInBuf:c_void_p, pOutBuf:c_void_p, pReserved:c_void_p=None, nWaitTime:int=1000)->int:
        """
        :param lLoginID: 登录句柄，LoginWithHighLevelSecurity返回值;user LoginID,LoginWithHighLevelSecurity's returns value
        :param nQueryType: 查询类型,其值为SDK_enum.py的EM_QUERY_DEV_INFO_TYPE；query type, refer to EM_QUERY_DEV_INFO_TYPE in SDK.Enum.py
        :param pInBuf:结构体输入参数;input param
        :param pOutBuf:结构体输出参数;output param
        :param pReserved:保留字段;Reserved
        :param nWaitTime:等待时间;wait time
        :return:1:成功,0:失败;1:success,0:failed
        """
        lLoginID = C_LLONG(lLoginID)
        pReserved = c_void_p(pReserved)
        result = cls.sdk.CLIENT_QueryDevInfo(lLoginID, nQueryType, byref(pInBuf), byref(pOutBuf), pReserved, nWaitTime)
        if not result:
            print(cls.GetLastErrorMessage())
        return result

__all__ = ['NetSDK', ]
