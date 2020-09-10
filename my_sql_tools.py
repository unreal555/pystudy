#!/bin/py
#-*-coding:utf-8-*-
'''
注意如果表,字段名和保留字重复,用反引号``包裹
'''
import pymysql
class My_sql():
    __conn=''
    __cursor=''
    def __init__(self,host='58.59.25.122',user='work',passwd='work',port=3336,charset='utf8',db='T'):##注意字符集不能有-,port必须是整数
        print('初始化类%s'%type(self))
        if isinstance(port,int):
            try:
                self.__conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
                self.__cursor = self.__conn.cursor()

            except Exception as e:
                print('初始化错误:',e)
                return False
        else:
            raise Exception('port must be int')

    def exe_sql(self,sql,*args):
        print('执行语句为:', sql, ';参数为:', args, '\r\n')

        r=False

        try:
            r = self.__cursor.execute(sql,args)
        except Exception as e:
            print('发生异常,错误为:',e)
            return False

        if r:
            result=self.__cursor.fetchall()
            return result
        else:
            return 0

    def insert_record(self,table_name,record):
        if (not isinstance(table_name,str)) or table_name=='':
            print('插入的表名有误,请检查')
            return False

        if not isinstance(record,dict):
            print('记录类型错误,接受dict')
            return False


        keys = ', '.join(['`'+x+'`' for x in record.keys() ])
        values=list(record.values())

        marks = ', '.join(['%s'] * len(values))
        sql = "insert into %s (%s) values (%s)" % (table_name,keys, marks)

        print(sql, values)

        r=False
        try:
            r=self.__cursor.execute(sql,values)
        except Exception as e:
            print(e)

        if r:
            result=self.__cursor.fetchall()
            print('写入{}成功'.format(record))
            id = self.__conn.insert_id()
            self.__conn.commit()
            print('插入的记录号为:', id, '\r\n')
            return id
        else:
            print('记录插入失败')
            return False



    def __del__(self):
        self.__cursor.close()
        self.__conn.close()
        print('释放mysql连接%s'%type(self))


if __name__ == '__main__':
    sql='show tables'
    db=My_sql()
    r=db.exe_sql(sql)
    for i in r:
        print(type(i))