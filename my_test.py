# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/7 0007 上午 10:23
# Tool ：PyCharm

import logging

DEBUG = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
DEBUG_LEVEL = 0  #0-4取值
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "  #配置输出日志格式
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S'  # %a 是星期几
logging.basicConfig(level=DEBUG[DEBUG_LEVEL],
                    format=LOG_FORMAT,
                    datefmt=DATE_FORMAT,
                    # filename=r"d:\test\test.log" #有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                    )
                  
              
