import configparser
import os

class My_Config():

    def __init__(self,path=os.path.join('.', 'config.ini')):
        print('My_Conifg initing...')
        self.config = configparser.ConfigParser()
        self.path=path
        if os.path.exists(path):
            try:
                self.config.read(path, encoding='gbk')
            except configparser.MissingSectionHeaderError as e:
                print('配置文件无任何section，请检查配置文件')
            except Exception as e:
                print(e)
                print('读取配置文件错误，请检查配置文件')
        else:
            with open(self.path,'w',encoding='gbk')as f:
                f.write()
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

    config=My_Config()
    config.write_seciton_item('test',sss='adddaa',dada='asd')
    print(config.get_section_items('test'))
    for section in config.get_sections():
        print(section)
        print(config.get_section_items(section))
    config.remove_item('test','sss')
