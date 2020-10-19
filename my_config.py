import configparser
import os

class My_Config():

    def __init__(self,path=os.path.join('.', 'config.ini')):

        self.config = configparser.ConfigParser()
        self.path=path


        print('My_Conifg initing,path is "%s"...'%path)

        if os.path.exists(self.path) and os.path.isdir(self.path):
            print('文件名错误，已有同名文件夹,请修改')
            exit()


        if os.path.exists(path):
            print('配置文件存在,读取中...')
            try:
                self.config.read(path, encoding='gbk')
            except Exception as e:
                print(e)
                print('读取配置文件错误，请检查配置文件')
        else:
            print('配置文件不存在,创建文件并添加默认section')

        if len(self.config.sections())==0:
            print('配置文件无任何section，添加默认section')
            self.config.add_section('default')
            self.config.write(open(self.path,'w',encoding='gbk'))

        print('My_Conifg init finished...')


    def get_sections(self):
        return self.config.sections()

    def get_options(self,section='default'):
        if self.config.has_section(section):
            return self.config.items(section)
        else:
            print('congfigure has not section',section)
            return False

    def get_option(self,section='default',option='default'):
        if self.config.has_option(section,option):
            return self.config.get(section,option)
        else:
            print('congfigure has not section %s or option %s '%(section,option))
            return False

    def write_section(self,section='default'):
        if section=='':
            print('you has not input section name,return false')
            return False
        try:
            self.config.add_section(str(section))
            with open(self.path,'w+',encoding='gbk') as f:
                self.config.write(f)
            print('your section %s has writed to configure'%s)
            return True
        except configparser.DuplicateSectionError as e:
            print('section name',section,'has exists in configure')
            return False
        except Exception as e:
            print('wrong\r\n%s'%e)
            return False

    def remove_section(self,section='default'):
        if section=='':
            print('未指定section名,退出')
            return False
        try:
            self.config.remove_section(section)
            with open(self.path,'w+',encoding='gbk') as f:
                self.config.write(f)
            print('seciton: ', section, ' has removed from configure')
            return True
        except Exception as e:
            print(e)
            return False

    def set_options(self,section='default',**kwargs):

        if len(kwargs)==0:
            print('you has not input options,return false')
            return False

        if self.config.has_section(section):
            for key in kwargs.keys():
                print('write option "',key,'=',kwargs[key] ,'" to ',section)
                self.config.set(section,key,str(kwargs[key]))
            with  open(self.path, 'w+',encoding='gbk') as f:
                self.config.write(f)
            print('write options finished')
            return True
        else:
            print('configure hao not seciton %s, write option fail'%section)
            return False

    def remove_options(self,section='default',*args):
        if not section in self.config.sections():
            print('configure has not section %s,cannt remove it'%section)
            return False
        if len(args)==0:
            print('has not input options')
            return False
        for option in args:
            if self.config.has_option(section,option):
                self.config.remove_option(section,option)
            else:
                print('option ',option,'not in section' ,section)
        with  open(self.path, 'w+', encoding='gbk') as f:
            self.config.write(f)

    def check_section(self,section='default'):
        print('check section %s in or not in configure'%(section))
        if self.config.has_option(section):
            return True
        else:
            return False

    def check_option(self,section='default',option='default'):
        print('check section "%s" option "%s" in or not in configure'%(section,option))
        if self.config.has_option(section,option):
            return True
        else:
            return False



if __name__=='__main__':

    config=My_Config('test.ini')

    print(config.check_option('sss'))


