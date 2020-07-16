import os
import logging

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
                with open(file,'a',encoding=codec) as f:
                    f.write(tab+str(line)+enter)
                    logging.info('{}写入成功'.format(line))




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

    line = (r'asdfadfasdf', r'a', r'asdfasdfasdfasdfasdf', r'asdfasdfasd', r'fas', r'df,asdfasd,fasdfasdfadfasd,', 23)

    write_txt('./text.txt', tab=1, enter=1, data=line, debug=True)

