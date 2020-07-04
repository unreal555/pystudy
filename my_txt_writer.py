import os


line=(r'asdfadfasdf',r'a',r'asdfasdfasdfasdfasdf',r'asdfasdfasd',r'fas',r'df,asdfasd,fasdfasdfadfasd,',23)




def write_txt(file_path,data,tab=1,enter=1,codec='utf-8',debug=False):
    '''
    :param f:    文件绝对路径或相对路径
    :param data:  要写入的内容，str，tuple，or list
    :param tab:    前面几个制表符
    :param codec:    编码，默认utf-8
    :return:    True or False
    '''
    tab='\t'*tab
    enter='\r\n'*enter

    dir,filename=os.path.split(file_path)

    if  not isinstance(data,(tuple,list,str)):
        print('输入data类型为{}，类型错误，只接受str，list，tupple'.format(type(data)))

    if os.path.exists(dir):
        pass
    else:
        pritn('没有这个目录，正在创建这个目录，{}'.format(dir))


    if  not os.path.exists(file_path):
        with open(file_path,'w',encoding=codec) as f:
            f.write('')


    if  os.path.exists(file_path) and os.path.isfile(file_path):
        if isinstance(data,str):
            with open(file_path,'a',encoding=codec) as f:
                f.write(tab+str(data)+enter)
                if debug:print('{}写入成功'.format(data))

        if isinstance(data,(tuple,list)):
            for line in data:
                with open(file_path,'a',encoding=codec) as f:
                    f.write(tab+str(line)+enter)
                    if debug:print('{}写入成功'.format(line))







if __name__ == '__main__':
    write_txt('./text.txt',tab=0,enter=4,data=line,debug=True)

