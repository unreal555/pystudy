import os
import datetime
import time
from concurrent.futures import ThreadPoolExecutor

def set_time(year,month,day,hour,min):

    #设定日期
    _date = datetime.datetime.strptime("{}/{}/{}".format(year,month,day),"%Y/%m/%d")
    #设定时间为 0点30分
    _time = '{}.{}.01'.format(hour,min)
    #设定时间
    os.system('time {}'.format(_time))
    os.system('date {}'.format(_date))


def get():

    while True:

        year=input('input year:')
        month=input('input month:')
        day=input('input day:')
        hour=input('input hour:')
        min=input('input min:')
        if year=='q':
            exit()
        print('set',year,month,day,hour,min)

        set_time(year,month,day,hour,min)


get()
