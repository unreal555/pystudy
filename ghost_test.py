# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/15 0015 上午 11:49
# Tool ：PyCharm


import logging

from ghost import Ghost,Session


DEBUG = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
DEBUG_LEVEL = 0
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "  #配置输出日志格式
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S'  #配置输出时间的格式，注意月份和天数不要搞乱了 %a 是星期几
logging.basicConfig(level=DEBUG[DEBUG_LEVEL],
                    format=LOG_FORMAT,
                    datefmt=DATE_FORMAT,
                    # filename=r"d:\test\test.log" #有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                    )
                  
              
url='http://www.skwen.me/14/14745/201453.html'

gh = Ghost()

se = Session(gh, display = True)

se.open(url)