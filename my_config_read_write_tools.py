import configparser
import os

def read_config(section,path=os.path.join('.','config.ini')):
    '''
    读取path指定的配置文件，默认为本目录config.ini
    读取section指定的配置段，以字典的形式返回该section的key，value
    '''

    config = configparser.ConfigParser()

    if os.path.exists(path):
        try:
            config.read(path,encoding='utf-8')
        except configparser.MissingSectionHeaderError as e:
            print('配置文件无任何section，请检查配置文件')
            return(1)
        except Exception as e:
            print(e)
            print('读取配置文件错误，请检查配置文件')
            return (1)
    else:
        print('未找到配置文件')
        return(1)


    if config.has_section(section):
        result={}
        for key in config[section]:
            result[key]=config.get(section,key)
        return result
    else:
        print('配置文件中，没有您指定的%s段'%section)
        return (2)


def write_config(section,path=os.path.join('.','config.ini'),**kwargs):
    '''
    读取path指定的配置文件，默认为本目录config.ini
    写入key=value到指定的section
    '''
    if kwargs==None:
        print('未提交key,value')
        return(0)

    config = configparser.ConfigParser()

    if os.path.exists(path):
        try:
            config.read(path,encoding='utf-8')
        except configparser.MissingSectionHeaderError as e:
            print('配置文件无任何section，请检查配置文件')
            return(1)
        except Exception as e:
            print(1)
            print('读取配置文件错误，请检查配置文件')
            return (1)
    else:
        print('未找到配置文件')
        return(1)


    if config.has_section(section):
        for key in kwargs.keys():
            config.set(section,key,kwargs[key])
        config.write(open(path,'w',encoding='utf-8'))
    else:
        print('配置文件中，没有您指定的%s段'%section)
        return (2)


if __name__=='__main__':

    result=read_config('proxy')
    print(result)
    write_config('proxy',proxy='',proxy4='')
