#!/bin/py
#   -*-coding:utf-8-*-
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
        try:
            print('执行语句为:',sql,';参数为:',args,'\r\n')
            r = self.__cursor.execute(sql,args)
        except Exception as e:
            print(e)
            return 0
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

        #print(sql,values)

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




create_test_desc_sql = r'''
    CREATE TABLE `test_desc`  (
      `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
      `source` varchar(100) CHARACTER SET utf8  NOT NULL COMMENT '数据来源（爬取网站域名）',
      `source_id` varchar(500) CHARACTER SET utf8 NOT NULL COMMENT '资源主键ID',
      `source_link` varchar(1000) CHARACTER SET utf8  NOT NULL COMMENT '资源网络地址',
      `weight` int(11) NOT NULL DEFAULT 0 COMMENT '权重',
      `count` int(11) NOT NULL DEFAULT 0 COMMENT '爬取次数',
      `last_date` date DEFAULT '2019-01-01' COMMENT '最后爬取日期',
      PRIMARY KEY (`id`) USING BTREE
    ) ENGINE = InnoDB AUTO_INCREMENT = 413790 CHARACTER SET = utf8 ;
'''
create_test_group_sql=r'''
    CREATE TABLE `test_group`  (
      `id` int(20) NOT NULL AUTO_INCREMENT  COMMENT '主键ID',
      `t_id` int(20) NOT NULL COMMENT '研究项目ID',
      `category` varchar(50)  DEFAULT NULL COMMENT '分类（试验药、对照药）',
      `name` varchar(500) DEFAULT NULL COMMENT '名称',
      `usage` text  COMMENT '用法',
      `group` varchar(500) DEFAULT NULL COMMENT '组别',
      `sample_size` int(11) DEFAULT NULL COMMENT '样本量',
      `intervention` text COMMENT '干预措施',
      `intervention_code` varchar(100) DEFAULT NULL COMMENT '干预措施代码或名称',
      PRIMARY KEY (`id`) USING BTREE
    ) ENGINE = InnoDB CHARACTER SET = utf8  COMMENT = '分组与干预措施';
'''
drop_test_desc_sql='''
    drop table  if exists `test_desc`;
'''
drop_test_group_sql='''
    drop table  if exists `test_group`;
'''

t={                                                    #对应一个试验的网页内容
    'test_desc':{                                   #对应一个试验的基本信息,保存在数据库t.test_desc中,内容为字典,可
                                                    #直接用insert_sql写数据库,在写该数据是应获得id值作为外键
        'source':'dfgg',
        'source_id':'dfgdfd',
        'source_link':'fdfdfgd',
        'weight':0,
        'count':1,
        'last_date':'2019-01-01',
        } ,

    'test_group':                             #对应一个试验的分组信息,内包含多条记录,内容为list,不能直接写数据库,应用for循环写入
         [{                                  #记录1
            'category':'对照药',
            'name':'测试1',
            'usage':'测试1',
            'group':'测试1',
            'sample_size':110,
            'intervention':'测试1',
            'intervention_code':'测试1',
         },
         {                                   #记录2
             'category': '试验药',
             'name': '策士2',
             'usage': '策士2',
             'group': '策士2',
             'sample_size': 50,
             'intervention': '策士2',
             'intervention_code': '',
         }]

   }

db=My_sql()                           #创建mysql连接,参数见My_sql init函数定义
# r=db.exe_sql(drop_test_group_sql)          #执行sql语句,如果表test_group存在,则删除
# r=db.exe_sql(drop_test_desc_sql)               #执行sql语句,如果表test_desc存在,则删除
# r=db.exe_sql(create_test_desc_sql)            #执行SQL语句,创建test_desc表
# r=db.exe_sql(create_test_group_sql)           执行SQL语句,创建test_group表

t_id=db.insert_record('test_desc',t['test_desc'])   #插入试验基本信息记录,并获得id值,作为其他表的外键

for record in t['test_group']:                #依次读取试验分组信息记录
    if record==[]:
        continue
    record['t_id']=t_id                    #在记录中,增加t_id字段及值
    db.insert_record('test_group', record)   #插入记录

