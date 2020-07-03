# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/2 0002 下午 1:42
# Tool ：PyCharm


import time
import os
from my_logger import  logger
from my_banquan_set import check_ban_quan
import sina_junshi
import sina_yule
from concurrent.futures import ThreadPoolExecutor

# if check_ban_quan(96):
if 1:

    base_dir='.'
    subdir='data'
    # subdir=str(time.strftime('%Y-%m-%d'))
    logname='log.txt'

    abs_path=os.path.join(base_dir,subdir)
    log_file_path=os.path.join(base_dir,subdir,logname)

    logger=logger(file=log_file_path)

    if not os.path.exists(abs_path):
        os.makedirs(abs_path)

    pool = ThreadPoolExecutor(3)

    # pool.submit(test_proxy, j).add_done_callback(save)
    pool.submit(sina_junshi.Main,logger)
    pool.submit(sina_yule.Main,logger)
else:
    exit()

