# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/2 0002 下午 1:42
# Tool ：PyCharm
import sina
import time
import os
from my_logger import  logger
from my_banquan_set import check_ban_quan

if check_ban_quan(96):

    base_dir='.'
    subdir='data'
    # subdir=str(time.strftime('%Y-%m-%d'))
    logname='log.txt'

    abs_path=os.path.join(base_dir,subdir)
    log_file_path=os.path.join(base_dir,subdir,logname)

    logger=logger(file=log_file_path)

    if not os.path.exists(abs_path):
        os.makedirs(abs_path)

    sina.Main(logger=logger)
else:
    exit()
