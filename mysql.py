#!/bin/py
#   -*-coding:utf-8-*-

import pymysql
from mytools import execute_lasts_time


class My_sql():
    __conn=''
    __cursor=''
    def __init__(self,host='58.59.25.122',user='test',passwd='594188',port=3336,charset='utf8',db='TD_OA'):##注意字符集不能有-,port必须是整数
        print('初始化类%s'%type(self))
        if isinstance(port,int):
            try:
                self.conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
                self.cursor = self.conn.cursor()

            except Exception as e:
                print(e)
        else:
            raise Exception('port must be int')

    @execute_lasts_time
    def exe_sql(self,sql,*args):
        try:
            print('执行语句为:',sql,';参数为:',args,'\r\n')
            r = self.cursor.execute(sql,args)
            print('cursor=',r)
        except Exception as e:
            print(e)
            return 0
        if r:
            result=self.cursor.fetchall()
            return result
        else:
            return 0

    def __del__(self):
        self.cursor.close()
        self.conn.close()
        print('释放类%s'%type(self))

d=My_sql()
# sql="select * from user  WHERE USER_NAME =%s or LAST_VISIT_IP=%s"      #防止注入，自动拼接参数
# name='张磊'
# ip='60.216.17.130'
sql = '''
    CREATE TABLE USER1 (
    id INT auto_increment PRIMARY KEY ,
    name CHAR(10) NOT NULL UNIQUE,
    age TINYINT NOT NULL
    )ENGINE=innodb DEFAULT CHARSET=utf8;
    '''
r=d.exe_sql(sql)
r=d.exe_sql('select * from user ')


