1  # coding: utf-8
2  # Team : None
3  # Author：zl
4  # Date ：2020/6/19 0019 下午 1:30
5  # Tool ：PyCharm

import os
import time
import re

class logger():

    __huan_hang = '\r\n'
    __mark=' # # # '
    __log=''
    __file=''

    def __init__(self,file=os.path.join('.','log.txt')):

        self.__file=file
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                self.__log=f.read()
            log=time.strftime('%Y-%m-%d %H:%M:%S')+'\t'+'打开日志,开始记录'
            self.__do(log)

        else:

            log = time.strftime('%Y-%m-%d %H:%M:%S') + '\t' + '创建日志'
            self.__do(log)

    def __do(self,log):
        with open(self.__file, 'a', encoding='utf-8') as f:
            f.write(self.__mark)
            f.write(log)
            f.write(self.__mark)
            f.write(self.__huan_hang)
            f.flush()

    def write(self,*info):

        if len(info)==0:
            print('内容为空,请输入有效的日志')
            return False

        if len(info)==1:
            try:
                log=str(info[0])
                log=time.strftime('%Y-%m-%d %H:%M:%S')+'\t'+log
                self.__do(log)
                return True

            except Exception as  e:
                print(e)
                print('日志必须为文本,请检查输入')
                return False

        if len(info)>1:
            log=[time.strftime('%Y-%m-%d %H:%M:%S')]

            try:
                for i in info:
                    log.append(str(i))

                log = '\t'.join(log)
                self.__do(log)
                return True

            except Exception as e:
                print(e)
                print('日志必须为文本,请检查输入')
                return False

    def check(self,target):
        if target=='' or not isinstance(target,str):
            return False
        if target in self.__log:
            return True
        else:
            return False

    def rebulid(self):
        with open(self.__file,'r',encoding='utf-8') as f:
            content=f.read()

        result=re.findall(r'{}(.*?){}'.format(self.__mark,self.__mark),content,re.S)

        os.renames(self.__file,self.__file+'.{}'.format(time.strftime('%Y-%m-%d-%H-%M-%S')))

        log = time.strftime('%Y-%m-%d %H:%M:%S') + '\t' + '重建'

        self.__do(log)

        for i in result:
            if i=='':
                continue
            self.__do(i)

        log= time.strftime('%Y-%m-%d %H:%M:%S') + '\t' + '重建完成'

        self.__do(log)

    def __del__(self):
        self.__huan_hang=''
        self.__mark=''
        self.__log=''
        self.__file=''
        del self.__huan_hang
        del self.__mark
        del self.__log
        del self.__file



if __name__=='__main__':
    logger=logger()
    logger.write('asdadfalsdjfklasdadg')
    logger.write('asdadfalsdjfklasdadg', 'assdsd')
    print(logger.check('sdadfalsdjfkla'))

    del logger




