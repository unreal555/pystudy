# coding: utf-8
# Team : None
# Author：zl
# Date ：2020/6/19 0019 下午 1:30
# Tool ：PyCharm

import os
import time
import re


class logger():
    __huan_hang = '\r\n'
    __mark = ' # # # '
    __log = ''
    __file = ''
    __debug = False

    @staticmethod
    def __get_time(self):
        return  time.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def __clean_str(self,s):
        return re.sub('[\r\n\t ]*','',s)

    def __init__(self, path='.', name='log', debug=False):

        print(path,name)

        self.__debu = debug

        self.__file=None

        if self.__debug: print('初始化logger')

        if 'txt' in path and os.path.exists(path) and os.path.isfile(path):
            self.__file = path

        if 'txt' not in name:
            name = name + '.txt'

        if os.path.isdir(path):
            self.__file = os.path.join(path, name)

        print(self.__file)

        if os.path.isfile(self.__file):
            with open(self.__file, 'r', encoding='utf-8') as f:
                self.__log = f.read()
            log = self.__get_time(self) + '\t' + '打开日志,开始记录'
            self.__do(log)

        else:
            if not os.path.exists(path):
                if self.__debug: print('创建日志路径{}'.format(dir))
                os.makedirs(path)
            log = self.__get_time(self) + '\t' + '创建日志'
            self.__do(log)

    def write(self, *info):

        if len(info) == 0:
            if self.__debug: print('内容为空,请输入有效的日志')
            return False

        if len(info) == 1:
            try:
                log = str(info[0])
                log = self.__get_time(self) + '\t' + log
                self.__do(log)
                return True

            except Exception as  e:
                if self.__debug: print(e)
                if self.__debug: print('日志必须为文本,请检查输入')
                return False

        if len(info) > 1:
            log = [self.__get_time(self)]

            try:
                for i in info:
                    log.append(str(i))

                log = '\t'.join(log)
                self.__do(log)
                return True

            except Exception as e:
                if self.__debug: print(e)
                if self.__debug: print('日志必须为文本,请检查输入')
                return False

    def check(self, target):
        if target == '' or not isinstance(target, str):
            return False
        if target in self.__log:
            return True
        else:
            return False

    def get_recorde(self):
        with open(self.__file,'r',encoding='utf-8') as f:
            result=f.readlines()
        print(result)
        result=[x for x in result if len(self.__clean_str(self,x))!=0]
        return result



    def find_lost(self, reg=r'''##(\d+)##'''):

        result = [int(x) for x in re.findall(reg, self.__log, re.S)]
        if result == []:
            print('查询结果为空,日志没有记录,或者正则表达式错误,请检查')
            return False
        else:
            return sorted(set(range(min(result), max(result))) - set(result))

    def rebulid(self):
        with open(self.__file, 'r', encoding='utf-8') as f:
            content = f.read()

        result = re.findall(r'{}(.*?){}'.format(self.__mark, self.__mark), content, re.S)

        path, file = os.path.split(self.__file)
        filename, ext = os.path.splitext(file)
        backup_name = os.path.join(path, filename + '-' + 'backup-' + time.strftime('%Y-%m-%d-%H-%M-%S') + ext)

        os.renames(self.__file, backup_name)
        for i in result:
            if i == '':
                continue
            self.__do(i)

        log = self.__get_time(self) + '\t' + '重建'

        self.__do(log)

        log = self.__get_time(self) + '\t' + '重建完成'

        self.__do(log)

    def __do(self, log):
        if self.__debug: print('写入日志{}'.format(log))
        if self.__debug: print('日志位置{}'.format(self.__file))
        with open(self.__file, 'a', encoding='utf-8') as f:
            f.write(self.__mark)
            f.write(log)
            f.write(self.__mark)
            f.write(self.__huan_hang)
            f.flush()

    def __del__(self):
        self.__huan_hang = ''
        self.__mark = ''
        self.__log = ''
        self.__file = ''
        self.__debug = ''
        del self.__huan_hang
        del self.__mark
        del self.__log
        del self.__file
        del self.__debug


if __name__ == '__main__':
    logger = logger('e://log-less.txt')
