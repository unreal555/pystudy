class MyException(Exception):
    def __init__(self, msg): #msg参数用于接收自己触发异常时传进来的错误描述信息
        self.msg = msg
    def __str__(self): #格式化输出
        return "[Internal Logic Error:] %s" % (self.msg)

