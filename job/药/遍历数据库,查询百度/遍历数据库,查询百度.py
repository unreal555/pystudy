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
import my_html_tools
import re 

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

    '''
    t_hospital

    t_trial_site

    site_name
    '''

    s='''
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Cookie: BIDUPSID=7F8C9C0EE862951DE88883F5F8C86030; PSTM=1600238944; BAIDUID=7F8C9C0EE862951D14E7508E748F73B3:FG=1; BD_UPN=12314353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ispeed_lsm=4; H_PS_PSSID=7513_32617_1468_32733_7567_7546_31253_32705_7624_32116_32718_26350_22160; H_PS_645EC=989b8apFEAQBwKxpCAlsWdtKzBIWJRSTzUxQCUIMjJZd7MYJUhhcjyHKODQ
Host: www.baidu.com
Pragma: no-cache
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36

'''

    headers=my_html_tools.tras_header(s)    #转换headers
    
    api_url=r'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd='   #百度查询入口
    
    
    sql='select id,site_name  from t_trial_site'     #从t_trial_site提取id和医院名称
    
    db=My_sql()            # 初始化数据库
    r=db.exe_sql(sql)     #执行语句,并获得返回值

    
    for idd,site_name in r:    #遍历返回值
        print(idd,site_name)
        
        url=api_url+site_name   #拼接查询地址



        page=my_html_tools.my_request(url,headers=headers,debug=False)   #获得页面
        print(page)
  
        r=re.findall(r'''<divclass="result-opc-container"srcid=".*?"fk="(.*?)"id="1".*?mu="(.*?)".*?</div>''',my_html_tools.qu_kong_ge(page))    #提取第一条记录的名称和url

        if len(r)>0:      #判断对否提取到信息
            
            r=r[0]
            
            if len(r)==2:      #  判断是否提取到网页里的医院名称和url
                baidu_name,baidu_url=r
                
                if '://' in baidu_url:            #去掉https://或者http://,只保留url,防止查询数据库干扰
                    baidu_url=baidu_url.split('://')[1]


                sql='select * from  t_hospital where locate("%s",website)'%baidu_url              #拼接t_hospital表查询语句,

                r=db.exe_sql(sql)          # 输出结果
                    
                print(r)


            print(idd,site_name,baidu_name,baidu_url,'\r\n')

            
            my_html_tools.random_wait()   #随机等待,防止被封


            


            

                
        else:
            print('未查出')   #网页查不到,跳过
            my_html_tools.random_wait()         #随机等待,
            continue
        
 

        


    



















        
