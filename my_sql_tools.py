#!/bin/py
#-*-coding:utf-8-*-

'''
注意如果表,字段名和保留字重复,用反引号``包裹

类型                     大小(单位：字节)
TinyBlob                   最大 255
Blob                         最大 65K
MediumBlob            最大 16M
LongBlob                 最大 4G

TINYTEXT	256 bytes	256 bytes
TEXT	65,535 bytes	约 64kb
MEDIUMTEXT	16,777,215 bytes	约 16MB
LONGTEXT	4,294,967,295 bytes	约 4GB

'''

import pymysql

import time

class My_sql():
    
    __conn=''
    
    __cursor=''
    
    def __init__(self,host='127.0.0.1',user='root',passwd='',port=3306,charset='utf8mb4',db='T'):##注意字符集不能有-,port必须是整数
        
        print('初始化数据库:%s\r\n'%db)
        
        if isinstance(port,int):
            
            try:
                
                self.__conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
                
                self.__cursor = self.__conn.cursor()

            except Exception as e:
                
                print('初始化数据库错误,请检查数据库参数有无错误,错误信息为:\r\n',e)

                exit()
        else:
            
            raise Exception('port must be int')


    def check_sql(self,sql):
        
        if not isinstance(sql,str):
            
            print('sql must be str type')
            
        key_word=str.upper(sql.split(' ')[0])

        print(key_word)


        if key_word in ['INSERT']:
            
            print('use insert_sql func')

        
        elif key_word in ['UPDATE']:
            
            print('use update_sql func')

        else:

            print('use exe_sql func')


        

    def exe_sql(self,sql,return_content=True,*args):

        if 'update'  in  str.lower(sql) or 'insert'  in  str.lower(sql):
            

            print('warnning: 插入或者修改记录,请使用insert_sql和update_sql方法')

            
        print('执行语句为:', sql, '\r\n')

        r='False'

        try:
            
            r = self.__cursor.execute(sql,args)
            
        except Exception as e:
            
            print('发生异常,错误为:',e)
            
            return False

        if r!='False':
            
            if return_content==True:

                result=self.__cursor.fetchall()
            
                return result
            
            if return_content==False:

                return r
            

    def update_sql(self,sql):

        if 'update' not in  str.lower(sql):

            print('update关键字 not in sql,请检查...')

            return False            
        
        print('执行语句为:', sql, '\r\n')

        r='False'

        try:
            
            r = self.__cursor.execute(sql)

        except Exception as e:
            
            print('发生异常,错误为:',e)
            
            self.__conn.rollback()
            
            return False

        

        if r!='False':

            self.__conn.commit()

            return r


    def insert_sql(self,sql):

        if 'insert' not in  str.lower(sql):

            print('insert关键字 not in sql,请检查...')

            return False            
        
        print('执行语句为:', sql, '\r\n')

        r='False'

        try:
            
            r = self.__cursor.execute(sql)

        except Exception as e:
            
            print('发生异常,错误为:',e)
            
            self.__conn.rollback()
            
            return False

        

        if r!='False':

            result=self.__cursor.fetchall()
            
            print('写入记录成功')
            
            id = self.__conn.insert_id()
            
            self.__conn.commit()
            
            print('插入的记录号为:', id, '\r\n')
            
            self.__conn.commit()

            return id 
                    
        else:
            
            print('记录插入失败')
            
            return False
 

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

        #print(sql, values)

        r='False'
        
        try:
            
            r=self.__cursor.execute(sql,values)
            
        except Exception as e:
            
            self.____cursor.execute.rollback()
            
            print(e)

        if r!='False':
                        
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
        
        print('释放Mysql连接%s'%type(self))


if __name__ == '__main__':
    #sql = ''' t_hospital set logo'='sadfasdf ','website'='asdfasdf ','category'=11111,'level'=45,'update_user_id'=1224334,'update_time'=time.time(),'full_name_cn'='sdsd','country'='sdsd','is_register'=3,'is_del'=2,'create_user_id'=5645454,'create_time'=time.time()}'''              # 从t_trial_site提取id和医院名称
    sql='''select * from t_hospital limit 2'''
    #sql='''show columns from t_hospital'''

    #item={'logo':'sadfasdf ','website':'asdfasdf ','category':11111,'level':45,'update_user_id':1224334,'update_time':time.time(),'full_name_cn':'sdsd','country':'sdsd','is_register':3,'is_del':2,'create_user_id':3344,'create_time':time.time()}
    #db=My_sql(port=330)            # 初始化数据库
    #r=db.insert_record(table_name='t_hospital',record=item)     #执行语句,并获得返回值

    #print(r)
    db=My_sql()
    for i in db.exe_sql(sql):
        print(i)

    


