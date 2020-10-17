import configparser
import os

class My_Config():

    def __init__(self,path=os.path.join('.', 'config.ini')):

        self.config = configparser.ConfigParser()
        self.path=path

        print('My_Conifg initing...')

        if os.path.exists(self.path) and os.path.isdir(self.path):
            print('文件名错误，已有同名文件夹,请修改')
            exit()

        if os.path.exists(path):
            try:
                self.config.read(path, encoding='gbk')
            except Exception as e:
                print(e)
                print('读取配置文件错误，请检查配置文件')
        else:
            print(self.path,'不存在，创建文件')
            self.config.add_section('defalut')
            self.config.write(open(self.path,'w',encoding='gbk'))



        if len(self.config.sections())==0:
            print('配置文件无任何section，添加默认section')
            self.config.add_section('defalut')
            self.config.write(open(self.path,'w',encoding='gbk'))





        print('My_Conifg init finished...')


    def get_sections(self):
        return self.config.sections()

    def get_section_items(self,section):
        return self.config.items(section)

    def write_section(self,section):
        if section=='':
            print('无section名,退出')
            return False
        try:
            self.config.add_section(section)
            with open(self.path,'w+',encoding='gbk') as f:
                self.config.write(f)

        except configparser.DuplicateSectionError as e:
            print('seciton:',section,'has exists')
            return False
        except Exception as e:
            print(e)
            return False
        print('seciton: ', section, ' writed')
        self.config.read(self.path, encoding='gbk')


    def write_seciton_item(self,section,**kwargs):

        if kwargs==None:
            print('无itme数据,返回')
            return False

        if self.config.has_section(section):
            for key in kwargs.keys():
                self.config.set(section,key,kwargs[key])
            with  open(self.path, 'w+',encoding='gbk') as f:
                self.config.write(f)
        else:
            print('配置文件中，没有您指定的section:%s'%section)
            return False
        return True

    def remove_item(self,seciton,*args):
        if not section in self.config.sections():
            print('无%s'%section)
            return False
        if args==None:
            print('无要删除的item')
            return False
        for item in args:
            self.config.remove_option(seciton,item)
        with  open(self.path, 'w+', encoding='gbk') as f:
            self.config.write(f)



if __name__=='__main__':

    config=My_Config('test')

