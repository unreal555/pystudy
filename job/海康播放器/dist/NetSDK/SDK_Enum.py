from enum import IntEnum


class EM_EVENT_IVS_TYPE(IntEnum):
    """
    智能事件类型, 在RealLoadPicture或fAnalyzerDataCallBack接口中使用
    intelligent event type, used in RealLoadPicture or fAnalyzerDataCallBack
    """
    ALL = 0x00000001,              # 订阅所有事件; subscription all event
    CROSSLINEDETECTION = 0x00000002,#警戒线事件(对应 DEV_EVENT_CROSSLINE_INFO);cross line event(Corresponding to DEV_EVENT_CROSSLINE_INFO)
    TRAFFICJUNCTION = 0x00000017,  # 交通路口事件(对应 DEV_EVENT_TRAFFICJUNCTION_INFO);traffic junction event(Corresponding to DEV_EVENT_TRAFFICJUNCTION_INFO)
    FACEDETECT = 0x0000001A,       # 人脸检测事件(对应 NET_DEV_EVENT_FACEDETECT_INFO); face detection(Corresponding to NET_DEV_EVENT_FACEDETECT_INFO)
    FACERECOGNITION = 0x00000117   # 人脸识别事件(对应NET_DEV_EVENT_FACERECOGNITION_INFO); face recognition(Corresponding to NET_DEV_EVENT_FACERECOGNITION_INFO)

class EM_QUERY_DEV_INFO_TYPE(IntEnum):
    """
    查询设备信息, 在接口QueryDevInfo中使用
    query device info, used in QueryDevInfo
    """
    NET_QUERY_GET_CAMERA_STATE = 0x0e,  # 获取摄像机状态,pInBuf= NET_IN_GET_CAMERA_STATEINFO*, pOutBuf= NET_OUT_GET_CAMERA_STATEINFO *;
                                        # query camera state, pInBuf= NET_IN_GET_CAMERA_STATEINFO*, pOutBuf= NET_OUT_GET_CAMERA_STATEINFO *

class SDK_ALARM_TYPE(IntEnum):
    EVENT_MOTIONDETECT = 0x218f   #视频移动侦测事件(对应结构体 ALARM_MOTIONDETECT_INFO);Video motion detect event  (Corresponding to structure ALARM_MOTIONDETECT_INFO)

class EM_LOGIN_SPAC_CAP_TYPE(IntEnum):
    """
    登陆方式;Login mode
    """
    TCP = 0                         # TCP登陆, 默认方式;TCP login, default
    ANY = 1                         # 无条件登陆;No criteria login
    SERVER_CONN = 2                 # 主动注册的登入;auto sign up login
    MULTICAST = 3                   # 组播登陆;multicast login, default
    UDP = 4                         # UDP方式下的登入;UDP method login
    MAIN_CONN_ONLY = 6              # 只建主连接下的登入;only main connection login
    SSL = 7                         # SSL加密方式登陆;SSL encryption login
    INTELLIGENT_BOX = 9             # 登录智能盒远程设备;login IVS box remote device
    NO_CONFIG = 10                  # 登录设备后不做取配置操作;login device do not config
    U_LOGIN = 11                    # 用U盾设备的登入;USB key device login
    LDAP = 12                       # LDAP方式登录;LDAP login
    AD = 13                         # AD（ActiveDirectory）登录方式;AD, ActiveDirectory,  login
    RADIUS = 14                     # Radius 登录方式;Radius  login
    SOCKET_5 = 15                   # Socks5登陆方式;Socks5 login
    CLOUD = 16                      # 云登陆方式;cloud login
    AUTH_TWICE = 17                 # 二次鉴权登陆方式;dual authentication loin
    TS = 18                         # TS码流客户端登陆方式;TS stream client login
    P2P = 19                        # 为P2P登陆方式;web private login
    MOBILE = 20                     # 手机客户端登陆;mobile client login
    INVALID = 21                    # 无效的登陆方式;invalid login


class SDK_RealPlayType(IntEnum):
    """
    预览类型, 对应RealPlayEx接口;Preview type.Corresponding to RealPlayEx
    """
    Realplay = 0,                    # 实时预览;Real-time preview
    Multiplay = 1,                   # 多画面预览;Multiple-channel preview
    Realplay_0 = 2,                  # 实时监视 - 主码流, 等同于Realplay;Real-time monitor-main stream. It is the same as DH_RType_Realplay
    Realplay_1 = 3,                  # 实时监视 - 从码流1;1 Real-time monitor -- extra stream 1
    Realplay_2 = 4,                  # 实时监视 - 从码流2;2 Real-time monitor -- extra stream 2
    Realplay_3 = 5,                  # 实时监视 - 从码流3;3 Real-time monitor -- extra stream 3
    Multiplay_1 = 6,                 # 多画面预览－1画面;Multiple-channel preview--1-window
    Multiplay_4 = 7,                 # 多画面预览－4画面;Multiple-channel preview--4-window
    Multiplay_8 = 8,                 # 多画面预览－8画面;Multiple-channel preview--8-window
    Multiplay_9 = 9,                 # 多画面预览－9画面;Multiple-channel preview--9-window
    Multiplay_16 = 10,               # 多画面预览－16画面;Multiple-channel preview--16-window
    Multiplay_6 = 11,                # 多画面预览－6画面;Multiple-channel preview--6-window
    Multiplay_12 = 12,               # 多画面预览－12画面;Multiple-channel preview--12-window
    Multiplay_25 = 13,               # 多画面预览－25画面;Multi-window tour--25-windows
    Multiplay_36 = 14,               # 多画面预览－36画面;Multi-window preview--36-windows
    Multiplay_64 = 15,               # 多画面预览－64画面;Multi-window preview--64-windows
    Multiplay_255 = 16,              # 不修改当前预览通道数;Do not modify the current preview channel number
    Realplay_Test = 255,             # 带宽测试码流;test stream


class EM_SEND_SEARCH_TYPE(IntEnum):
    """
    下发搜索类型,send search type
    """
    MULTICAST_AND_BROADCAST = 0,   # 组播和广播搜索;multicast and broadcast search
    MULTICAST = 1,  # 组播搜索;multicast search
    BROADCAST = 2,  # 广播搜索;broadcast search

class EM_VEHICLE_DIRECTION(IntEnum):
    """
    车辆方向; vehicle direction
    """
    UNKOWN = 0, # 未知;unknown
    HEAD = 1, # 车头;head
    TAIL = 2, # 车尾;rear

class EM_OPEN_STROBE_STATE(IntEnum):
    """
    开闸状态;open strobe state
    """
    UNKOWN = 0,  # 未知状态;unknown
    CLOSE = 1,   # 关闸;close
    AUTO = 2,    # 自动开闸;auto open
    MANUAL = 3,  # 手动开闸;manual open

class EM_TIME_TYPE(IntEnum):
    """
    时间类型;time type
    """
    ABSLUTE = 0,  # 绝对时间;absolute time
    RELATIVE = 1, # 相对时间, 相对于视频文件头帧为时间基点, 头帧对应于UTC(0000 - 00 - 00 00: 00:00)
                  # Relative time, relative to the video file header frame as the time basis points, the first frame corresponding to the UTC (0000-00-00 00:00:00)

class EM_COLOR_TYPE(IntEnum):
    """
    颜色类型;color type
    """
    RED = 0,      # 红色
    YELLOW = 1,   # 黄色
    GREEN = 2,    # 绿色
    CYAN = 3,     # 青色
    BLUE = 4,     # 蓝色
    PURPLE = 5,   # 紫色
    BLACK = 6,    # 黑色
    WHITE = 7,    # 白色
    MAX = 8,

class EM_EVENT_FILETAG(IntEnum):
    """
    事件文件的文件标签类型;event file's tag type
    """
    ATMBEFOREPASTE = 1,  # ATM贴条前;Before ATM Paste
    ATMAFTERPASTE = 2,   # ATM贴条后;After ATM Paste

class EM_TRAFFICCAR_MOVE_DIRECTION(IntEnum):
    """
    交通车辆行驶方向类型;traffic car move direction type
    """
    UNKNOWN = 0,  # 未知的;unknown
    STRAIGHT = 1,  # 直行;straight
    TURN_LEFT = 2,  # 左转;turn left
    TURN_RIGHT = 3,  # 右转;turn right
    TURN_AROUND = 4,  # 掉头;turn around

class EM_TRAFFICCAR_CAR_TYPE(IntEnum):
    """
    车辆类型;car type
    """
    UNKNOWN = 0,    # 未知;Unknown
    TRUST_CAR = 1,  # 白名单车辆;trust car
    SUSPICIOUS_CAR = 2,  # 黑名单车辆;suspicious car
    NORMAL_CAR = 3,      # 非白名单且非黑名单车辆;normal car

class EM_TRAFFICCAR_LANE_TYPE(IntEnum):
    """
    车道类型;Lane type
    """
    UNKNOWN = 0,    # 未知;unknown
    NORMAL = 1,     # 普通车道;Normal
    NONMOTOR = 2,   # 非机动车车道;Non-motor
    LIGHT_DUTY = 3, # 小型车车道;Light-Duty
    BUS = 4,        # 公交车车道;Bus
    EMERGENCY = 5,  # 应急车道;Emergency
    DANGEROUS = 6,  # 危险品车道;Dangerous

class EM_NTP_STATUS(IntEnum):
    """
    NTP校时状态;NTP status
    """
    UNKNOWN = 0,        # 未知;Unknown
    DISABLE = 1,        # 不使能;Disable
    SUCCESSFUL = 2,     # 成功;Successful
    FAILED = 3,         # 失败;Failed

class EM_VEHICLE_TYPE(IntEnum):
    """
    收费站车型分类;Vehicle type inToll station
    """
    UNKNOWN = 0,        # 未知
    PASSENGERCAR1 = 1,  # 客1
    TRUCK1 = 2,         # 货1
    PASSENGERCAR2 = 3,  # 客2
    TRUCK2 = 4,         # 货2
    PASSENGERCAR3 = 5,  # 客3
    TRUCK3 = 6,         # 货3
    PASSENGERCAR4 = 7,  # 客4
    TRUCK4 = 8,         # 货4
    PASSENGERCAR5 = 9,  # 客5
    TRUCK5 = 10,        # 货5


class EM_SNAPCATEGORY(IntEnum):
    """
    抓拍的类型;snap category
    """
    MOTOR = 0,          # 机动车;motor
    NONMOTOR = 1,       # 非机动车;nonmotor

class EM_VEHICLE_TYPE_BY_FUNC(IntEnum):
    """
    按功能划分的车辆类型;vehicle type by function
    """
    UNKNOWN = 0,            # 未知;unknown
    #以下为特种车辆类型;special vehicle types follow
    TANK_CAR = 1,           # 危化品车辆;tank car
    SLOT_TANK_CAR = 2,      # 槽罐车;slot tank car
    DREGS_CAR = 3,          # 渣土车;dregs car
    CONCRETE_MIXER_TRUCK = 4,  # 混凝土搅拌车;concrete mixer truck
    TAXI = 5,               # 出租车;taxi
    POLICE = 6,             # 警车;police car
    AMBULANCE = 7,          # 救护车;ambulance
    GENERAL = 8,            # 普通车;general car
    WATERING_CAR = 9,       # 洒水车;watering car
    FIRE_ENGINE = 10,       # 消防车;fire engine
    MACHINESHOP_TRUCK = 11, # 工程车;machineshop truck
    POWER_LOT_VEHICLE = 12, # 粉粒物料车;power lot vehicle
    SUCTION_SEWAGE_TRUCK = 13,  # 吸污车;suction sewage truck
    NORMAL_TANK_TRUCK = 14,     # 普通罐车;normal tank truck
    SCHOOL_BUS = 15,            # 校车;school bus
    EXCAVATOR = 16,             # 挖掘机;exvavator
    BULLDOZER = 17,             # 推土车;bulldozer
    CRANE = 18,                 # 吊车;crane
    PUMP_TRUCK = 19,            # 泵车;pump truck

class EM_STANDARD_VEHICLE_TYPE(IntEnum):
    """
    标准车辆类型;standard vehicle type
    """
    UNKNOWN = 0,            # 未知
    MOTOR = 1,              # 机动车
    BUS = 2,                # 公交车
    UNLICENSED_MOTOR = 3,       # 无牌机动车
    LARGE_CAR = 4,  # 大型汽车
    MICRO_CAR = 5,  # 小型汽车
    EMBASSY_CAR = 6,  # 使馆汽车
    MARGINAL_CAR = 7,  # 领馆汽车
    AREAOUT_CAR = 8,  # 境外汽车
    FOREIGN_CAR = 9,  # 外籍汽车
    FARM_TRANS_CAR = 10,  # 农用运输车
    TRACTOR = 11,  # 拖拉机
    TRAILER = 12,  # 挂车
    COACH_CAR = 13,  # 教练汽车
    TRIAL_CAR = 14,  # 试验汽车
    TEMPORARYENTRY_CAR = 15,  # 临时入境汽车
    TEMPORARYENTRY_MOTORCYCLE = 16,  # 临时入境摩托
    TEMPORARY_STEER_CAR = 17,  # 临时行驶车
    LARGE_TRUCK = 18,  # 大货车
    MID_TRUCK = 19,  # 中货车
    MICRO_TRUCK = 20,  # 小货车
    MICROBUS = 21,  # 面包车
    SALOON_CAR = 22,  # 轿车
    CARRIAGE = 23,  # 小轿车
    MINI_CARRIAGE = 24,  # 微型轿车
    SUV_MPV = 25,  # SUV或者MPV
    SUV = 26,  # SUV
    MPV = 27,  # MPV
    PASSENGER_CAR = 28,  # 客车
    MOTOR_BUS = 29,  # 大客车
    MID_PASSENGER_CAR = 30,  # 中客车
    MINI_BUS = 31,  # 小客车
    PICKUP = 32,  # 皮卡车
    OILTANK_TRUCK = 33,  # 油罐车

class EM_OVERSEA_VEHICLE_CATEGORY_TYPE(IntEnum):
    """
    海外车辆类型中的子类别，一个车辆只能是子类型的某一种。（海外专用);subcategories of oversea vehicle types
    """
    UNKNOWN = 0,                # 未知;unknown
    MOTORCYCLE = 1,             # 摩托车;motorcycle
    LIGHT_GOODS_VEHICLE = 2,    # 轻型货车;light goods vehicle
    COMPANY_VEHICLE = 3,        # 公司用私家车;company vehicle
    PRIVATE_VEHICLE = 4,        # 个人用私家车;private vehicle
    TAXI = 5,                   # TAXI或者快线车;taxi
    TRAILER = 6,                # 拖车;trailer
    ENGINEERING_PLANT_VEHICLE = 7,  # 工程车;engineering plant vehicle
    VERY_HEAVY_GOODS_VEHICLE = 8,   # 超大货车;very heavy goods vehicle
    HEAVY_GOODS_VEHICLE = 9,        # 大货车;heavy goods vehicle
    PUBLIC_BUS = 10,                # 公共BUS;public bus
    PRIVATE_BUS = 11,               # 私营BUS;private bus
    SPECIAL_VEHICLE = 12,           # 特殊车辆;special vehicle

class EM_COMMON_SEAT_TYPE(IntEnum):
    """
    座驾类型;Seat type
    """
    UNKNOWN = 0,    # 未识别
    MAIN = 1,       # 主驾驶
    SLAVE = 2,      # 副驾驶

class NET_SAFEBELT_STATE(IntEnum):
    """
    安全带状态;Safe belt state
    """
    SS_NUKNOW = 0,              # 未知;Unknown
    SS_WITH_SAFE_BELT = 1,      # 已系安全带;with safe  belt
    SS_WITHOUT_SAFE_BELT = 2,   # 未系安全带;without safe belt

class NET_SUNSHADE_STATE(IntEnum):
    """
    遮阳板状态; Sun shade state
    """
    SS_NUKNOW_SUN_SHADE = 0,  # 未知;Unknown
    SS_WITH_SUN_SHADE = 1,    # 有遮阳板;with sun shade
    SS_WITHOUT_SUN_SHADE = 2, # 无遮阳板;without sun shade

class EM_CARD_PROVINCE(IntEnum):
    """
    卡号省份;card province
    """
    UNKNOWN = 10,  # 解析出错，未知省份;UNKNOWN
    BEIJING = 11,  # 北京;BeiJing
    TIANJIN = 12,  # 天津;TianJin
    HEBEI = 13,  # 河北;HeBei
    SHANXI_TAIYUAN = 14,  # 山西;ShanXi, the provincial capital is TaiYuan
    NEIMENGGU = 15,  # 内蒙古;NeiMengGu
    LIAONING = 21,  # 辽宁;LiaoNing
    JILIN = 22,  # 吉林;JiKin
    HEILONGJIANG = 23,  # 黑龙江;HeiLongJiang
    SHANGHAI = 31,  # 上海;ShangHai
    JIANGSU = 32,  # 江苏;JiangSu
    ZHEJIANG = 33,  # 浙江;ZheJiang
    ANHUI = 34,  # 安徽;AnHui
    FUJIAN = 35,  # 福建;FuJian
    JIANGXI = 36,  # 江西;JiangXi
    SHANDONG = 37,  # 山东;ShanDong
    HENAN = 41,  # 河南;HeNan
    HUBEI = 42,  # 湖北;HuBei
    HUNAN = 43,  # 湖南;HuNan
    GUANGDONG = 44,  # 广东;GuangDong
    GUANGXI = 45,  # 广西;GuangXi
    HAINAN = 46,  # 海南;HaiNan
    CHONGQING = 50,  # 重庆;ChongQing
    SICHUAN = 51,  # 四川;SiChuan
    GUIZHOU = 52,  # 贵州;GuiZhou
    YUNNAN = 53,  # 云南;YunNan
    XIZANG = 54,  # 西藏;XiZang
    SHANXI_XIAN = 61,  # 陕西;ShanXi , the provincial capital is XiAn
    GANSU = 62,  # 甘肃;GanSu
    QINGHAI = 63,  # 青海;QingHai
    NINGXIA = 64,  # 宁夏;NingXia
    XINJIANG = 65,  # 新疆;XinJiang
    XIANGGANG = 71,  # 香港;XiangGang
    AOMEN = 82,  # 澳门;AoMen

class EM_PLATE_TYPE(IntEnum):
    """
    号牌类型;the tpye of the plate
    """
    OTHER = 0,  # 其他车;Other
    BIG_CAR = 1,  # 大型汽车;big car
    SMALL_CAR = 2,  # 小型汽车;small car
    EMBASSY_CAR = 3,  # 使馆汽车;embassy car
    CONSULATE_CAR = 4,  # 领馆汽车;consulate car
    ABROAD_CAR = 5,  # 境外汽车;abroad car
    FOREIGN_CAR = 6,  # 外籍汽车;foreign car
    LOW_SPEED_CAR = 7,  # 低速车;Low speed car
    COACH_CAR = 8,  # 教练车;coach car plate
    MOTORCYCLE = 9,  # 摩托车;motorcycle plate
    NEW_POWER_CAR = 10,  # 新能源车;new power car
    POLICE_CAR = 11,  # 警用车;police car
    HONGKONG_MACAO_CAR = 12,  # 港澳两地车;Hongkong Macao car
    ARMEDPOLICE_CAR = 13,  # 武警车辆;Armed police car
    MILITARY_CAR = 14,  # 军队车辆;Military vehicles
    TEMPORARY_LICENSE_FOR_NON_MOTOR_VEHICLES = 15,  # 非机动车临时牌照;Temporary license for non motor vehicles
    OFFICIAL_LICENSE_PLATE_FOR_NON_MOTOR_VEHICLE = 16,  # 非机动车牌正式牌照;Official license plate of non motor vehicle

class EM_CAR_COLOR_TYPE(IntEnum):
    """
    车身颜色;car color
    """
    WHITE = 0,  # 白色;white
    BLACK = 1,  # 黑色;black
    RED = 2,  # 红色;red
    YELLOW = 3,  # 黄色;yellow
    GRAY = 4,  # 灰色;gray
    BLUE = 5,  # 蓝色;blue
    GREEN = 6,  # 绿色;green
    PINK = 7,  # 粉色;pink
    PURPLE = 8,  # 紫色;purple
    DARK_PURPLE = 9,  # 暗紫色;dark purple
    BROWN = 10,  # 棕色;brown
    MAROON = 11,  # 粟色;marron
    SILVER_GRAY = 12,  # 银灰色;silver gray
    DARK_GRAY = 13,  # 暗灰色;dark gray;
    WHITE_SMOKE = 14,  # 白烟色;white smoke;
    DEEP_ORANGE = 15,  # 深橙色;deep orange
    LIGHT_ROSE = 16,  # 浅玫瑰色;light rose
    TOMATO_RED = 17,  # 番茄红色;tomato red
    OLIVE = 18,  # 橄榄色;olive
    GOLDEN = 19,  # 金色;golden
    DARK_OLIVE = 20,  # 暗橄榄色;dark olive
    YELLOW_GREEN = 21,  # 黄绿色;yellow green
    GREEN_YELLOW = 22,  # 绿黄色;green yellow
    FOREST_GREEN = 23,  # 森林绿;forest green
    OCEAN_BLUE = 24,  # 海洋绿;ocean blue
    DEEP_SKYBLUE = 25,  # 深天蓝;deep sky blue
    CYAN = 26,  # 青色;cyan
    DEEP_BLUE = 27,  # 深蓝色;deep blue
    DEEP_RED = 28,  # 深红色;deep red
    DEEP_GREEN = 29,  # 深绿色;deep green
    DEEP_YELLOW = 30,  # 深黄色;deep yellow
    DEEP_PINK = 31,  # 深粉色;deep pink
    DEEP_PURPLE = 32,  # 深紫色;deep purple
    DEEP_BROWN = 33,  # 深棕色;deep brown
    DEEP_CYAN = 34,  # 深青色;deep cyan
    ORANGE = 35,  # 橙色;orange
    DEEP_GOLDEN = 36,  # 深金色;deep golden
    OTHER = 255,  # 未识别、其他;other


class EM_USE_PROPERTY_TYPE(IntEnum):
    """
    使用性质;use property
    """
    NONOPERATING = 0,  # 非营运;not operating
    HIGWAY = 1,  # 公路客运,旅游客运;higway,tourist
    BUS = 2,  # 公交客运;bus
    TAXI = 3,  # 出租客运;taxi
    FREIGHT = 4,  # 货运;freight
    LEASE = 5,  # 租赁;lease
    SECURITY = 6,  # 警用,消防,救护,工程救险;for police,for fire police,for rescue or engineering emergency
    COACH = 7,  # 教练;for coach
    SCHOOLBUS = 8,  # 幼儿校车,小学生校车,其他校车;kindergarten school bus,pupil school bus,other school bus
    FOR_DANGE_VEHICLE = 9,  # 危化品运输;for dangerous goods transportation
    OTHER = 10,  # 其他;Other
    ONLINE_CAR_HAILING = 11,  # 网约车;Online car-hailing
    NON_MOTORIZED_TAKE_OUT_VEHICLE = 12,  # 非机动外卖车;Non motorized take out vehicle
    NON_MOTORIZED_EXPRESS_CAR = 13,  # 非机动快递车;Non motorized express car

class EM_NONMOTOR_OBJECT_STATUS(IntEnum):
    """
    事件/物体状态;things/objects status
    """
    UNKNOWN = 0, # 未识别;unknown
    NO = 1,      # 否;no
    YES = 2,     # 是;yes

class EM_EMOTION_TYPE(IntEnum):
    """
    表情;Emotion
    """
    UNKNOWN = 0,  # 未知;unknown
    NORMAL = 1,  # 普通/正常;normal
    SMILE = 2,  # 微笑;smile
    ANGER = 3,  # 愤怒;anger
    SADNESS = 4,  # 悲伤;sadness
    DISGUST = 5,  # 厌恶;disgust
    FEAR = 6,  # 害怕;fear
    SURPRISE = 7,  # 惊讶;surprise
    NEUTRAL = 8,  # 正常;neutral
    LAUGH = 9,  # 大笑;laugh
    HAPPY = 10,  # 高兴;happy
    CONFUSED = 11,  # 困惑;confused
    SCREAM = 12,  # 尖叫;scream
    CALMNESS = 13,  # 平静;calmness

class EM_CLOTHES_TYPE(IntEnum):
    """
    衣服类型;Clothes type
    """
    UNKNOWN = 0,  # 未知;unknown
    LONG_SLEEVE = 1,  # 长袖;long sleeve
    SHORT_SLEEVE = 2,  # 短袖;short sleeve
    TROUSERS = 3,  # 长裤;trousers
    SHORTS = 4,  # 短裤;shorts
    SKIRT = 5,  # 裙子;skirt
    WAISTCOAT = 6,  # 背心;waistcoat
    MINIPANTS = 7,  # 超短裤;mini-pants
    MINISKIRT = 8,  # 超短裙;mini-skirt

class EM_OBJECT_COLOR_TYPE(IntEnum):
    """
    颜色类型;Color type
    """
    UNKNOWN = 0,  # 未知;unknown
    WHITE = 1,  # 白色;white
    ORANGE = 2,  # 橙色;orange
    PINK = 3,  # 粉色;pink
    BLACK = 4,  # 黑色;black
    RED = 5,  # 红色;red
    YELLOW = 6,  # 黄色;yellow
    GRAY = 7,  # 灰色;gray
    BLUE = 8,  # 蓝色;blue
    GREEN = 9,  # 绿色;green
    PURPLE = 10,  # 紫色;purple
    BROWN = 11,  # 棕色;purple
    SLIVER = 12,  # 银色;sliver
    DARKVIOLET = 13,  # 暗紫罗兰色;darkviolet
    MAROON = 14,  # 栗色;maroon
    DIMGRAY = 15,  # 暗灰色;dimgray
    WHITESMOKE = 16,  # 白烟色;whitesmoke
    DARKORANGE = 17,  # 深橙色;darkorange
    MISTYROSE = 18,  # 浅玫瑰色;mistyrose
    TOMATO = 19,  # 番茄红色;tomato
    OLIVE = 20,  # 橄榄色;olive
    GOLD = 21,  # 金色;gold
    DARKOLIVEGREEN = 22,  # 暗橄榄绿色;darkolivegreen
    CHARTREUSE = 23,  # 黄绿色;chartreuse
    GREENYELLOW = 24,  # 绿黄色;green-yellow
    FORESTGREEN = 25,  # 森林绿色;forest-green
    SEAGREEN = 26,  # 海洋绿色;sea-green
    DEEPSKYBLUE = 27,  # 深天蓝色;deepsky-blue
    CYAN = 28,  # 青色;cyan
    OTHER = 29,  # 无法识别;other

class EM_HAS_HAT(IntEnum):
    """
    是否戴帽子;Has hat
    """
    UNKNOWN = 0,  # 未知;Unknown
    NO = 1,       # 不戴帽子;Not has hat
    YES = 2,      # 戴帽子;Has hat

class EM_CAP_TYPE(IntEnum):
    """
    帽子类型;Cap type
    """
    UNKNOWN = 0,   # 未知;unknown
    ORDINARY = 1,  # 普通帽子;ordinary
    HELMET = 2,    # 头盔;helmet
    SAFE = 3,      # 安全帽;safe hat

class EM_HAIR_STYLE(IntEnum):
    """
    头发样式;hair style
    """
    UNKNOWN = 0,  # 未知
    LONG_HAIR = 1,  # 长发
    SHORT_HAIR = 2,  # 短发
    PONYTAIL = 3,  # 马尾
    UPDO = 4,  # 盘发
    HEAD_BLOCKED = 5,  # 头部被遮挡
    NONE = 6,  # 无头发

class EM_SEX_TYPE(IntEnum):
    """
    性别;sex
    """
    UNKNOWN = 0, # 未知;unknown
    MALE = 1, # 男性;male
    FEMALE = 2, # 女性;female

class EM_COMPLEXION_TYPE(IntEnum):
    """
    肤色;Complexion
    """
    NODISTI = 0,  # 未识别;Not distinguish
    YELLOW = 1,  # 黄;Yellow
    BLACK = 2,  # 黑;Black
    WHITE = 3,  # 白;White

class EM_EYE_STATE_TYPE(IntEnum):
    """
    眼睛状态;eyes state
    """
    UNKNOWN = 0,  # 未知;unknown
    NODISTI = 1,  # 未识别;no disringuish
    CLOSE = 2,    # 闭眼;close eyes
    OPEN = 3,     # 睁眼;open eyes

class EM_MOUTH_STATE_TYPE(IntEnum):
    """
    嘴巴状态; mouth state type
    """
    UNKNOWN = 0,    # 未知;Unknown
    NODISTI = 1,    # 未识别;no disringuish
    CLOSE = 2,      # 闭嘴;close mouth
    OPEN = 3,       # 张嘴;open mouth

class EM_MASK_STATE_TYPE(IntEnum):
    """
    口罩状态;mask state type
    """
    UNKNOWN = 0,  # 未知;unknown
    NODISTI = 1,  # 未识别;no disringuish
    NOMASK = 2,   # 没戴口罩;no mask
    WEAR = 3,     # 戴口罩;wearing mask

class EM_BEARD_STATE_TYPE(IntEnum):
    """
    胡子状态;beard state type
    """
    UNKNOWN = 0,  # 未知;unknown
    NODISTI = 1,  # 未识别;no disringuish
    NOBEARD = 2,  # 没胡子;no beard
    HAVEBEARD = 3,  # 有胡子;have beard

class EM_HAS_GLASS(IntEnum):
    """
    是否带眼镜;Glasses state
    """
    UNKNOWN = 0,  # unknown
    NO = 1,  # unwear
    NORMAL = 2,  # wear normal glasses
    SUN = 3,  # wear sun glasses
    BLACK = 4,  # wear black glasses

class EM_STRABISMUS_TYPE(IntEnum):
    """
    斜视状态;Strabismus type
    """
    UNKNOWN = 0,    # 未知;unknown
    NORMAL = 1,     # 正常;normal
    YES = 2,        # 斜视;Strabismus

class EM_CLASS_TYPE(IntEnum):
    """
    大类业务方案;class type
    """
    UNKNOWN = 0,  # 未知业务;unknown
    VIDEO_SYNOPSIS = 1,  # 视频浓缩;video synopsis
    TRAFFIV_GATE = 2,  # 卡口;traffic gate
    ELECTRONIC_POLICE = 3,  # 电警;electronic police
    SINGLE_PTZ_PARKING = 4,  # 单球违停;single ptz parking
    PTZ_PARKINBG = 5,  # 主从违停;ptz parking
    TRAFFIC = 6,  # 交通事件"Traffic";Traffic
    NORMAL = 7,  # 通用行为分析"Normal";Normal
    PRISON = 8,  # 监所行为分析"Prison";Prison
    ATM = 9,  # 金融行为分析"ATM";ATM
    METRO = 10,  # 地铁行为分析;metro
    FACE_DETECTION = 11,  # 人脸检测"FaceDetection";FaceDetection
    FACE_RECOGNITION = 12,  # 人脸识别"FaceRecognition";FaceRecognition
    NUMBER_STAT = 13,  # 人数统计"NumberStat";NumberStat
    HEAT_MAP = 14,  # 热度图"HeatMap";HeatMap
    VIDEO_DIAGNOSIS = 15,  # 视频诊断"VideoDiagnosis";VideoDiagnosis
    VIDEO_ENHANCE = 16,  # 视频增强;video enhance
    SMOKEFIRE_DETECT = 17,  # 烟火检测;smokefire detect
    VEHICLE_ANALYSE = 18,  # 车辆特征识别"VehicleAnalyse";VehicleAnalyse
    PERSON_FEATURE = 19,  # 人员特征识别;person feature
    SDFACEDETECTION = 20,  # 多预置点人脸检测"SDFaceDetect";SDFaceDetect
    # 配置一条规则但可以在不同预置点下生效
    HEAT_MAP_PLAN = 21,  # 球机热度图计划"HeatMapPlan";HeatMapPlan
    NUMBERSTAT_PLAN = 22,  # 球机客流量统计计划 "NumberStatPlan";NumberStatPlan
    ATMFD = 23,  # 金融人脸检测，包括正常人脸、异常人脸、相邻人脸、头盔人脸等针对ATM场景特殊优化;ATM face detect
    HIGHWAY = 24,  # 高速交通事件检测"Highway";Highway
    CITY = 25,  # 城市交通事件检测 "City";City
    LETRACK = 26,  # 民用简易跟踪"LeTrack";LeTrack
    SCR = 27,  # 打靶相机"SCR";SCR
    STEREO_VISION = 28,  # 立体视觉(双目)"StereoVision";StereoVision
    HUMANDETECT = 29,  # 人体检测"HumanDetect";HumanDetect
    FACE_ANALYSIS = 30,  # 人脸分析 "FaceAnalysis";FaceAnalysis
    EM_CALSS_XRAY_DETECTION = 31,  # X光检测 "XRayDetection";XRayDetection
    STEREO_NUMBER = 32,  # 双目相机客流量统计 "StereoNumber";StereoNumber
    CROWDDISTRIMAP = 33,  # 人群分布图;crowd distrimap
    OBJECTDETECT = 34,  # 目标检测;object detect
    FACEATTRIBUTE = 35,  # IVSS人脸检测 "FaceAttribute";FaceAttribute
    FACECOMPARE = 36,  # IVSS人脸识别 "FaceCompare";FaceCompare
    EM_CALSS_STEREO_BEHAVIOR = 37,  # 立体行为分析 "StereoBehavior";StereoBehavior
    EM_CALSS_INTELLICITYMANAGER = 38,  # 智慧城管 "IntelliCityMgr";IntelliCityMgr
    EM_CALSS_PROTECTIVECABIN = 39,  # 防护舱（ATM舱内）"ProtectiveCabin";ProtectiveCabin
    EM_CALSS_AIRPLANEDETECT = 40,  # 飞机行为检测 "AirplaneDetect";AirplaneDetect
    EM_CALSS_CROWDPOSTURE = 41,  # 人群态势（人群分布图服务）"CrowdPosture";CrowdPosture
    PHONECALLDETECT = 42,  # 打电话检测 "PhoneCallDetect";PhoneCallDetect
    SMOKEDETECTION = 43,  # 烟雾检测 "SmokeDetection";SmokeDetection
    BOATDETECTION = 44,  # 船只检测 "BoatDetection";BoatDetection
    SMOKINGDETECT = 45,  # 吸烟检测 "SmokingDetect";SmokingDetect
    WATERMONITOR = 46,  # 水利监测 "WaterMonitor";WaterMonitor
    GENERATEGRAPHDETECTION = 47,  # 生成图规则 "GenerateGraphDetection";GenerateGraphDetection
    TRAFFIC_PARK = 48,  # 交通停车 "TrafficPark";TrafficPark
    OPERATEMONITOR = 49,  # 作业检测 "OperateMonitor";OperateMonitor
    INTELLI_RETAIL = 50,  # 智慧零售大类 "IntelliRetail";IntelliRetail
    CLASSROOM_ANALYSE = 51,  # 教育智慧课堂"ClassroomAnalyse";ClassroomAnalyse
    FEATURE_ABSTRACT = 52,  # 特征向量提取大类 "FeatureAbstract";FeatureAbstract
    FACEBODY_DETECT = 53,  # 人体检测大类 "FaceBodyDetect";FaceBodyDetect
    FACEBODY_ANALYSE = 54,  # 人体识别大类 "FaceBodyAnalyse";FaceBodyAnalyse
    VEHICLES_DISTRI = 55,  # 车辆密度 "VehiclesDistri";VehiclesDistri
    INTELLI_BREED = 56,  # 智慧养殖检测 "IntelliBreed";IntelliBreed
    INTELLI_PRISON = 57,  # 监狱行为分析 "IntelliPrison";IntelliPrison
    ELECTRIC_DETECT = 58,  # 电力检测 "ElectricDetect";ElectricDetect
    RADAR_DETECT = 59,  # 雷达检测 "RadarDetect";RadarDetect
    PARKINGSPACE = 60,  # 车位检测大类 "ParkingSpace";ParkingSpace
    INTELLI_FINANCE = 61,  # 智慧金融 "IntelliFinance";IntelliFinance
    CROWD_ABNORMAL = 62,  # 人群异常检测 "CrowdAbnormal";CrowdAbnormal
    ANATOMY_TEMP_DETECT = 63,  # 人体温智能检测 "AnatomyTempDetect";AnatomyTempDetect
    WEATHER_MONITOR = 64,  # 天气监控 "WeatherMonitor";WeatherMonitor

class EM_PLATE_COLOR_TYPE(IntEnum):
    """
    车牌颜色;Plate color
    """
    UNKNOWN = 0,  # 未知 "Unknown";Unknown
    OTHER = 1,  # 其他颜色 "Other";Other
    BLUE = 2,  # 蓝色 "Blue";Blue
    YELLOW = 3,  # 黄色 "Yellow";Yellow
    WHITE = 4,  # 白色 "White";White
    BLACK = 5,  # 黑色 "Black";Black
    RED = 6,  # 红色 "Red";Red
    GREEN = 7,  # 绿色 "Green";Green
    SHADOW_GREEN = 8,  # 渐变绿 "ShadowGreen";ShadowGreen
    YELLOW_GREEN = 9,  # 黄绿双拼 "YellowGreen";YellowGreen


class EM_USEDEV_MODE(IntEnum):
    """
    对讲方式； Audio talk way
    """
    TALK_CLIENT_MODE = 0        # 设置客户端方式进行语音对讲； Set client-end mode to begin audio talk
    TALK_SERVER_MODE = 1        # 设置服务器方式进行语音对讲； Set server mode to begin audio talk
    TALK_ENCODE_TYPE = 2        # 设置语音对讲编码格式(对应DHDEV_TALKDECODE_INFO)； Set encode format for audio talk
    ALARM_LISTEN_MODE = 3       # 设置报警订阅方式； Set alarm subscribe way
    CONFIG_AUTHORITY_MODE = 4   # 设置通过权限进行配置管理； Set user right to realize configuration management
    TALK_TALK_CHANNEL = 5       # 设置对讲通道(0~MaxChannel-1)； set talking channel(0~MaxChannel-1)
    RECORD_STREAM_TYPE = 6      # 设置待查询及按时间回放的录像码流类型(0-主辅码流,1-主码流,2-辅码流)； set the stream type of the record for query(0-both main and extra stream,1-only main stream,2-only extra stream)
    TALK_SPEAK_PARAM = 7        # 设置语音参数,对应结构体 NET_SPEAK_PARAM； set speaking parameter,corresponding to NET_SPEAK_PARAM
    RECORD_TYPE = 8             # 设置按时间录像回放及下载的录像文件类型(详见NET_RECORD_TYPE)； Set by time video playback and download the video file TYPE (see.net RECORD TYPE)
    TALK_MODE3 = 9              # 设置三代设备的语音对讲参数, 对应结构体 NET_TALK_EX； Set voice intercom parameters of three generations of equipment and the corresponding structure NET_TALK_EX
    PLAYBACK_REALTIME_MODE = 10 # 设置实时回放功能(0-关闭,1开启)； set real time playback function(0-off, 1-on)
    TALK_TRANSFER_MODE = 11     # 设置语音对讲是否为转发模式, 对应结构体 NET_TALK_TRANSFER_PARAM； Judge the voice intercom if it was a forwarding mode, (corresponding to  NET_TALK_TRANSFER_PARAM)
    TALK_VT_PARAM = 12          # 设置VT对讲参数, 对应结构体 NET_VT_TALK_PARAM； Set VT Talk param (corresponding to  NET_VT_TALK_PARAM)
    TARGET_DEV_ID = 13          # 设置目标设备标示符, 用以查询新系统能力(非0-转发系统能力消息)； set target device identifier for searching system capacity information, (not zero - locate device forwards the information)
    AUDIO_RECORD_LENGTH = 15    # 设置录音缓存, 对应为一个int； set audio record length, corresponding to a int


class EM_STREAM_TYPE(IntEnum):
    """
    码流类型； stream type
    """
    UNKNOWN = 0,    # 未知状态； unknown
    MAIN = 1,       # 主码流； main
    EXTRA1 = 2,     # 辅码流1； extra1
    EXTRA2 = 3,     # 辅码流2； extra2
    EXTRA3 = 4,     # 辅码流3； extra3


class EM_QUERY_RECORD_TYPE(IntEnum):
    """
    录像查询类型； Type of video search
    """
    ALL = 0,                    # 所有录像; All the recorded video
    ALARM = 1,                  # 外部报警录像; The video of external alarm
    MOTION_DETECT = 2,          # 动态检测报警录像; The video of dynamic detection alarm
    ALARM_ALL = 3,              # 所有报警录像; All the alarmed video
    CARD = 4,                   # 卡号查询; query by the card number
    CONDITION = 5,              # 按条件查询; query by condition
    JOIN = 6,                   # 组合查询; combination query
    CARD_PICTURE = 8,           # 按卡号查询图片, HB - U、NVS等使用; query pictures by the card number, used by HB-U,NVS
    PICTURE = 9,                # 查询图片, HB - U、NVS等使用; query pictures, used by HB-U,NVS
    FIELD = 10,                 # 按字段查询; query by field
    INTELLI_VIDEO = 11,         # 智能录像查询; Smart record search
    NET_DATA = 15,              # 查询网络数据, 金桥网吧等使用; query network data, used by Jinqiao Internet Bar
    TRANS_DATA = 16,            # 查询透明串口数据录像; query the video of serial data
    IMPORTANT = 17,             # 查询重要录像; query the important video
    TALK_DATA = 18,             # 查询录音文件; query the recording file
    POS = 19,                   # POS录像; query the pos record
    INVALID = 256,              # 无效的查询类型; invalid query type


class EM_DEV_CFG_TYPE(IntEnum):
    """
    配置类型,GetDevConfig和SetDevConfig使用； Configuration type，used by GetDevConfig and SetDevConfig
    """
    TIMECFG = 0x0008,                    # DVR时间配置; DVR time setup

class EM_MOTION_DETECT_TYPE(IntEnum):
    """
    动检触发类型；Type of triggeing motion detection
    """
    UNKNOWN = 0,                # 未知;unknown
    HUMAN = 1,                  # 人;human
    VEHICLE = 2,                # 车;vechicle
    HUMAN_AND_VEHICLE = 3,      # 人和车;human and vechicle

class EM_DEV_EVENT_FACEDETECT_SEX_TYPE(IntEnum):
    """
    人脸检测对应性别类型；sex type of dectected human face
    """
    UNKNOWN = 0,    # 未知;unknown
    MAN = 1,        # 男性;male
    WOMAN = 2,      # 女性;female


class EM_DEV_EVENT_FACEDETECT_FEATURE_TYPE(IntEnum):
    """
    人脸检测对应人脸特征类型； feature type of detected human face
    """
    UNKNOWN = 0,        # 未知;unknown
    WEAR_GLASSES = 1,   # 戴眼镜;wearing glasses
    SMILE = 2,          # 微笑;smile
    ANGER = 3,          # 愤怒;anger
    SADNESS = 4,        # 悲伤;sadness
    DISGUST = 5,        # 厌恶;disgust
    FEAR = 6,           # 害怕;fear
    SURPRISE = 7,       # 惊讶;surprise
    NEUTRAL = 8,        # 正常;neutral
    LAUGH = 9,          # 大笑;laugh
    NOGLASSES = 10,     # 没戴眼镜;not wear glasses
    HAPPY = 11,         # 高兴;happy
    CONFUSED = 12,      # 困惑;confused
    SCREAM = 13,        # 尖叫;scream
    WEAR_SUNGLASSES = 14, # 戴太阳眼镜;wearing sun glasses


class EM_RACE_TYPE(IntEnum):
    """
    """
    UNKNOWN = 0, 
    NODISTI = 1, 
    YELLOW = 2, 
    BLACK = 3,   
    WHITE = 4,  

class EM_FACE_DETECT_STATUS(IntEnum):
    """
    人脸在摄像机画面中的状态；the status of person in camera picture
    """
    UNKNOWN = 0,    # 未知;unknown
    APPEAR = 1,     # 出现;appear
    INPICTURE = 2,  # 在画面中;in picture
    EXIT = 3,       # 离开;exit

class EM_HUMAN_TEMPERATURE_UNIT(IntEnum):
    """
    人体测温温度单位；Temperature unit of human temperature detection
    """
    UNKNOWN = 0,        # 未知;unknown
    CENTIGRADE = 1,     # 摄氏度;Centigrade
    FAHRENHEIT = 2,     # 华氏度;Fahrenheit
    KELVIN = 3,         # 开尔文;Kelvin

class EM_PERSON_FEATURE_STATE(IntEnum):
    """
    人员建模状态；person feature state
    """
    UNKNOWN = 0,        # 未知;unknown
    FAIL = 1,           # 建模失败,可能是图片不符合要求,需要换图片;failed to model, need to change the picture
    USEFUL = 2,         # 有可用的特征值;success to model, the data can be used for face recognition
    CALCULATING = 3,    # 正在计算特征值;under calculating
    UNUSEFUL = 4,       # 已建模，但算法升级导致数据不可用，需要重新建模;once modeling was successful, but became unusable after upgrading, need to abstract


class EM_REGISTER_DB_TYPE(IntEnum):
    """
    注册库属性；the type of register face DB
    """
    UNKNOWN = 0,        # 未知;unknown
    NORMAL = 1,         # 普通库;normal
    BLACKLIST = 2,      # 黑名单;black list
    WHITELIST = 3,      # 白名单;white list
    VIP = 4,            # VIP库;VIP
    STAFF = 5,          # 员工库;staff DB
    LEADER = 6,         # 领导库;leader DB

class EM_CLOTHES_COLOR(IntEnum):
    """
    衣服颜色；Clothes color
    """
    UNKNOWN = 0,            # 未知;unknown
    WHITE = 1,              # 白色;White
    ORANGE = 2,             # 橙色;Orange
    PINK = 3,               # 粉色;Pink
    BLACK = 4,              # 黑色;Black
    RED = 5,                # 红色;Red
    YELLOW = 6,             # 黄色;Yellow
    GRAY = 7,               # 灰色;Gray
    BLUE = 8,               # 蓝色;Blue
    GREEN = 9,              # 绿色;Green
    PURPLE = 10,            # 紫色;Purple
    BROWN = 11,             # 棕色;Brown
    OTHER = 12,             # 其他颜色;Other

class EM_COAT_TYPE(IntEnum):
    """
    上衣类型；coat type
    """
    UNKNOWN = 0,                # 未知;unknown
    LONG_SLEEVE = 1,            # 长袖;Long sleeve
    COTTA = 2,                  # 短袖;Cotta
class EM_TROUSERS_TYPE(IntEnum):
    """
    裤子类型；Trousers type
    """
    UNKNOWN = 0,                # 未知;unknown
    TROUSERS = 1,               # 长裤;Trousers
    SHORTS = 2,                 # 短裤;Shorts
    SKIRT = 3,                  # 裙子;Skirt
class EM_HAS_BAG(IntEnum):
    """
    是否戴包(包括背包或拎包)；Has bag
    """
    UNKNOWN = 0,                # 未知;unknown
    NO = 1,                     # 不带包;No bag
    YES = 2,                    # 带包;Has bag
class EM_ANGLE_TYPE(IntEnum):
    """
    角度；Angle
    """
    UNKNOWN = 0,                # 未知;unknown
    FRONT = 1,                  # 正面;front
    SIDE = 2,                   # 侧面;side
    BACK = 3,                   # 背面;back
class EM_HAS_UMBRELLA(IntEnum):
    """
    是否打伞；Umbrella state
    """
    UNKNOWN = 0,                # 未知;unknown
    NO = 1,                     # 未打伞;no umbrella
    YES = 2,                    # 打伞;has umbrella
class EM_BAG_TYPE(IntEnum):
    """
    包类型；bag type
    """
    UNKNOWN = 0,            # 未知;unknown
    HANDBAG = 1,            # 手提包;hand bag
    SHOULDERBAG = 2,        # 肩包;shoulder bag
    KNAPSACK = 3,           # 背包;knapsack
    DRAWBARBOX = 4,         # 拉杆箱;drawar box
    WAISTPACK = 5,          # 腰包;waist pack
    NONE = 6,               # 无包;no bag
class EM_CLOTHES_PATTERN(IntEnum):
    """
    衣服图案；clothes pattern
    """
    UNKNOWN = 0,            # 未知;unknown
    PURE = 1,               # 纯色;pure color
    STRIPE = 2,             # 条纹;Stripe
    PATTERN = 3,            # 图案;Pattern
    GAP = 4,                # 缝隙;Gap
    LATTICE = 5,            # 格子;Lattice
    SPLITJOIN = 6,          # 拼接;split join
class EM_HAS_BACK_BAG(IntEnum):
    """
    是否有背包；Has back bag or not
    """
    UNKNOWN = 0,            # 未知;unknown
    NO = 1,                 # 没有背包;No back bag
    YES = 2,                # 有背包;Has back bag
class EM_HAS_CARRIER_BAG(IntEnum):
    """
    是否有手提包；Has carrier bag or not
    """
    UNKNOWN = 0,            # 未知;unknown
    NO = 1,                 # 没有手提包;No carrier bag
    YES = 2,                # 有手提包;Has carrier bag
class EM_HAS_SHOULDER_BAG(IntEnum):
    """
    是否有肩包；Has shoulder bag or not
    """
    UNKNOWN = 0,            # 未知;unknown
    NO = 1,                 # 没有肩包;No shoulder bag
    YES = 2,                # 有肩包;Has shoulder bag
class EM_HAS_MESSENGER_BAG(IntEnum):
    """
    是否有斜挎包；Has messenger bag or not
    """
    UNKNOWN = 0,            # 未知;unknown
    NO = 1,                 # 没有斜挎包;No messenger bag
    YES = 2,                # 有斜挎包;Has messenger bag

class EM_OBJECT_TYPE(IntEnum):
    """
    对象目标类型；Has messenger bag or not
    """
    UNKNOWN = -1,   # 未知;unknown
    FACE = 0,       # 人脸;Face
    HUMAN = 1,      # 人体;Human
    VECHILE = 2,    # 机动车;Vechile
    NOMOTOR = 3,    # 非机动车;Nomotor
    ALL = 4,        # 所有类型;All


class EM_PERSON_FEATURE_ERRCODE(IntEnum):
    """
    建模失败原因；error code of person feature
    """
    UNKNOWN = -1,           # 未知;unknown
    PIC_FORMAT = 0,         # 图片格式问题;invalid picture format
    NO_FACE = 1,            # 无人脸或不清晰;no face or unclear face
    MULTI_FACE = 2,         # 多个人脸;multi face
    PIC_DECODE_FAIL = 3,    # 图片解码失败;picture decoding failed
    NOT_RECOMMEND = 4,      # 不推荐入库;not recommended for storage
    FACEDB_FAIL = 5,        # 数据库操作失败;failure of database operation
    GET_PICTURE = 6,        # 获取图片失败;fail to ge picture
    SYSTEM_ERROR = 7,       # 系统异常;system error



class EM_REALDATA_FLAG(IntEnum):
    """
    实时监视的实时数据标志, 对应 CLIENT_SetRealDataCallBackEx(Ex2) 中的 dwFlag 参数；real data flag, corresponding param dwFlag in CLIENT_SetRealDataCallBackEx
    支持 '|' 运算符, 如 dwFlag = REALDATA_FLAG_RAW_DATA | REALDATA_FLAG_YUV_DATA； supports '|' operator, like dwFlag = REALDATA_FLAG_RAW_DATA | REALDATA_FLAG_YUV_DATA
    """
    RAW_DATA = 0x01,                    # 原始数据标志,           对应fRealDataCallBack(Ex/Ex2)回调函数中 dwDataType 为0, 0x01 = 0x01 << 0; raw data flag,		        corresponding param dwDataType in fRealDataCallBack / fRealDataCallBackEx is 0, 0x01 = 0x01 << 0
    DATA_WITH_FRAME_INFO = 0x02,        # 带有帧信息的数据标志,   对应fRealDataCallBack(Ex/Ex2)回调函数中 dwDataType 为1, 0x02 = 0x01 << 1; data with frame info flag,	corresponding param dwDataType in fRealDataCallBack / fRealDataCallBackEx is 1, 0x02 = 0x01 << 1
    YUV_DATA = 0x04,                    # YUV 数据标志,           对应fRealDataCallBack(Ex/Ex2)回调函数中 dwDataType 为2, 0x04 = 0x01 << 2; YUV data flag,		        corresponding param dwDataType in fRealDataCallBack / fRealDataCallBackEx is 2, 0x04 = 0x01 << 2
    PCM_AUDIO_DATA = 0x08,              # PCM 音频数据标志,       对应fRealDataCallBack(Ex/Ex2)回调函数中 dwDataType 为3, 0x08 = 0x01 << 3; PCM audio data flag,	    corresponding param dwDataType in fRealDataCallBack / fRealDataCallBackEx is 3, 0x08 = 0x01 << 3

class EM_CAMERA_STATE_TYPE(IntEnum):
    """
    连接状态；Camera connect state
    """
    UNKNOWN = 0,       # 未知;unknown
    CONNECTING = 1,    # 正在连接;connecting
    CONNECTED = 2,     # 已连接;connected
    UNCONNECT = 3,     # 未连接;unconnected
    EMPTY = 4,         # 通道未配置,无信息;channel is not configured, no info
    DISABLE = 5,       # 通道有配置,但被禁用;channel is configured, but it is forbidden

class EM_COMM_ATTACHMENT_TYPE(IntEnum):
    """
    车辆物件类型;Common attachment type
    """
    UNKNOWN = 0,  # 未知类型;Unknown type
    FURNITURE = 1,  # 摆件;Furniture
    PENDANT = 2,  # 挂件;Pendant
    TISSUEBOX = 3,  # 纸巾盒;TissueBox
    DANGER = 4,  # 危险品;Danger
    PERFUMEBOX = 5,  # 香水;perfumebox

class EM_CATEGORY_NONMOTOR_TYPE(IntEnum):
    """
    非机动车子类型;nomotor type
    """
    UNKNOWN = 0,  # 未知;unknown
    TRICYCLE = 1,  # 三轮车;Tricycle
    MOTORCYCLE = 2,  # 摩托车;Motorcycle
    NON_MOTOR = 3,  # 非机动车;Non-Motor
    BICYCLE = 4,  # 自行车;Bicycle
    DUALTRIWHEELMOTORCYCLE = 5,  # 两、三轮摩托车;DualTriWheelMotorcycle
    LIGHTMOTORCYCLE = 6,  # 轻便摩托车;LightMotorcycle
    EMBASSYMOTORCYCLE = 7,  # 使馆摩托车;EmbassyMotorcycle
    MARGINALMOTORCYCLE = 8,  # 领馆摩托车;MarginalMotorcycle
    AREAOUTMOTORCYCLE = 9,  # 境外摩托车;AreaoutMotorcycle
    FOREIGNMOTORCYCLE = 10,  # 外籍摩托车;ForeignMotorcycle
    TRIALMOTORCYCLE = 11,  # 试验摩托车;TrialMotorcycle
    COACHMOTORCYCLE = 12,  # 教练摩托车;CoachMotorcycle
    PASSERBY = 13,  # 行人;Passerby
    VANTRICYCLE = 14,  # 厢式三轮车;VanTricycle
    MANNEDCONVERTIBLETRICYCLE = 15,  # 载人敞篷三轮车;MannedConvertibleTricycle
    NOMANNEDCONVERTIBLETRICYCLE = 16,  # 不载人敞篷三轮车;NoMannedConvertibleTricycle

class EM_FEATURE_VERSION(IntEnum):
    """
    特征值版本类型;The type of feature version
    """
    UNKNOWN = 0,  # 未知;Unknown
    FACE_LARGE_1_01_001 = 1,  # 人脸，大模型，1.01.001;Face，large model，1.01.001
    FACE_LARGE_1_02_001 = 2,  # 人脸，大模型，1.02.001;Face，large model，1.02.001
    FACE_LARGE_1_03_001 = 3,  # 人脸，大模型，1.03.001;Face，large model，1.03.001
    FACE_LARGE_1_04_001 = 4,  # 人脸，大模型，1.04.001;Face，large model，1.04.001
    FACE_MIDDLE_1_01_002 = 31,  # 人脸，中模型，1.01.002;Face，middle model，1.01.002
    FACE_MIDDLE_1_02_002 = 32,  # 人脸，中模型，1.02.002;Face，middle model，1.02.002
    FACE_MIDDLE_1_03_002 = 33,  # 人脸，中模型，1.03.002;Face，middle model，1.03.002
    FACE_MIDDLE_1_04_002 = 34,  # 人脸，中模型，1.04.002;Face，middle model，1.04.002
    FACE_SMALL_1_01_003 = 61,  # 人脸，小模型，1.01.003;Face，small model，1.01.003
    FACE_SMALL_1_02_003 = 62,  # 人脸，小模型，1.02.003;Face，small model，1.02.003
    HUMAN_NONMOTOR = 91,  # 人和非机动车，全局无版本号;Human and non-motor，no version
    HUMAN_NONMOTOR_FLOAT_1_00_01 = 92,  # 人和非机动车，全局浮点，1.00.01;Human and non-motor，global float，1.00.01
    HUMAN_NONMOTOR_HASH_1_00_01 = 93,  # 人和非机动车，全局哈希，1.00.01;Human and non-motor，global hash，1.00.01
    HUMAN_NONMOTOR_FLOAT_1_01_00 = 94,  # 人和非机动车，全局浮点，1.01.00;Human and non-motor，global float，1.01.00
    HUMAN_NONMOTOR_HASH_1_01_00 = 95,  # 人和非机动车，全局哈希，1.01.00;Human and non-motor, global hash, 1.01.01
    TRAFFIC = 121,  # 机动车，全局无版本号;Traffic，no version
    TRAFFIC_FLOAT = 122,  # 机动车，全局浮点版本号0;Traffic，global float, 0
    TRAFFIC_FLOAT_1_00_01 = 123,  # 机动车，全局浮点版本号1.00.01;Traffic，global float, 1.00.01
    TRAFFIC_HASH_1_00_01 = 124,  # 机动车，全局哈希版本号1.00.01;Traffic，global hash, 1.00.01
    TRAFFIC_FLOAT_1_00_02 = 125,  # 机动车，全局浮点版本号1.00.02;Traffic，global float, 1.00.02
    TRAFFIC_HASH_1_00_02 = 126,  # 机动车，全局哈希版本号1.00.02;Traffic，global hash, 1.00.02
    SHANGTANG_FACE_1_5_0 = 151,  # 商汤，人脸，1.5.0;ShangTang，face，1.5.0
    SHANGTANG_FACE_1_8_1 = 152,  # 商汤，人脸，1.8.1;ShangTang，face，1.8.1
    SHANGTANG_FACE_2_1_3 = 153,  # 商汤，人脸，2.1.3;ShangTang，face，2.1.3
    SHANGTANG_FACE_2_39_6 = 154,  # 商汤，人脸，2.39.6;ShangTang，face，2.39.6
    SHANGTANG_FACE_2_39_7 = 155,  # 商汤，人脸，2.39.7;ShangTang，face，2.39.7
    SHANGTANG_FACE_2_39_8 = 156,  # 商汤，人脸，2.39.8;ShangTang，face，2.39.8
    SHANGTANG_FACE_239 = 157,  # 商汤，人脸，239;ShangTang，face，239
    SHANGTANG_FACE_242 = 158,  # 商汤，人脸，242;ShangTang，face，242
    SHANGTANG_FACE_244 = 159,  # 商汤，人脸，244;ShangTang，face，244
    SHANGTANG_FACE_245 = 160,  # 商汤，人脸，245;ShangTang，face，245
    SHENMO_HUMAN_TRAFFIC_NON_2_5_7 = 182,  # 深瞐，人脸/机动车/非机动车，2.5.7;ShenMo，human/traffic/non-motor，2.5.7
