import os
import re
import my_changliang


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
        if debug:print('输入data类型为{}，类型错误，只接受str，list，tupple'.format(type(data)))

    if not os.path.exists(dir):
        if debug:print('没有这个目录，正在创建这个目录，{}'.format(dir))
        os.makedirs(dir)


    if  not os.path.exists(file):
        if debug:print('没有这个目录，正在创建这个文件，{}'.format(filename))
        with open(file,'w',encoding=codec) as f:
            f.write('')


    if  os.path.exists(file) and os.path.isfile(file):
        if isinstance(data,str):
            with open(file,'a',encoding=codec) as f:
                f.write(tab+str(data)+enter)
                if debug:print('{}写入成功'.format(data))

        if isinstance(data,(tuple,list)):
            for line in data:
                if len(line)==0:
                    continue
                with open(file,'a',encoding=codec) as f:
                    f.write(tab+str(line)+enter)
                    if debug:print('{}写入成功'.format(line))

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
        if debug:print('要消除的垃圾信息为空,请检查grabage？')
        return False

    if not isinstance(grabage, (list,tuple)):
        if debug:print('垃圾信息只接受队列和元组')
        return False

    if (not isinstance(source,str)) or source=='':
        if debug:print('待处理的source字符串为空,或不是str类型')
        return False

    for i in grabage:
        target=target.replace(i,'')
    return target





if __name__ == '__main__':


    write_txt('./pic/list.txt',data=['sdfaasdfasdf','asdfasdf  '],debug=True)


