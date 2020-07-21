import os
import re
import my_changliang
import logging
biaodian=my_changliang.YING_WEN_BIAO_DIAN+my_changliang.ZHONG_WEN_BIAO_DIAN
zhonwen=my_changliang.ZHONG_WEN_ZI_FU_FOR_RE



def write_txt(file,data,tab=1,enter=1,codec='utf-8',debug=False):
    '''
    :param f:    文件绝对路径或相对路径
    :param data:  要写入的内容，str，tuple，or list
    :param tab:    前面几个制表符
    :param codec:    编码，默认utf-8
    :return:    True or False
    '''
    tab='\t'*tab
    enter='\r\n'*enter+'\r\n'

    dir,filename=os.path.split(file)

    if  not isinstance(data,(tuple,list,str)):
        logging.error('输入data类型为{}，类型错误，只接受str，list，tupple'.format(type(data)))

    if not os.path.exists(dir):
        logging.debug('没有这个目录，正在创建这个目录，{}'.format(dir))
        os.makedirs(dir)


    if  not os.path.exists(file):
        with open(file,'w',encoding=codec) as f:
            f.write('')


    if  os.path.exists(file) and os.path.isfile(file):
        if isinstance(data,str):
            with open(file,'a',encoding=codec) as f:
                f.write(tab+str(data)+enter)
                logging.info('{}写入成功'.format(data))

        if isinstance(data,(tuple,list)):
            for line in data:
                if len(line)==0:
                    continue
                with open(file,'a',encoding=codec) as f:
                    f.write(tab+str(line)+enter)
                    logging.info('{}写入成功'.format(line))

def qu_kong_ge(s):
    if isinstance(s, str):
        return re.sub('\s+', '', s)
    else:
        print('老兄，给字符串')
        return False

def qu_str(source,*grabage):      #去除source中的垃圾,grabage为list,存储垃圾
    target=source

    print('去除以下垃圾字符{}'.format(grabage))
    if len(grabage)==0 :
        logging.error('要消除的垃圾信息为空,请检查grabage？')
        return False

    if not isinstance(grabage, (list,tuple)):
        logging.error('垃圾信息只接受队列和元组')
        return False

    if (not isinstance(source,str)) or source=='':
        logging.error('待处理的source字符串为空,或不是str类型')
        return False

    for i in grabage:
        target=target.replace(i,'')
    return target





if __name__ == '__main__':
    DEBUG = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
    DEBUG_LEVEL = 0  # 0-4取值
    LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "  # 配置输出日志格式
    DATE_FORMAT = '%Y-%m-%d  %H:%M:%S'  # %a 是星期几
    logging.basicConfig(level=DEBUG[DEBUG_LEVEL],
                        format=LOG_FORMAT,
                        datefmt=DATE_FORMAT,
                        # filename=r"d:\test\test.log" #有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                        )




    if __name__ == '__main__':
        pass




