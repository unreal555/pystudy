import os
import sys
import re
from my_get_files_in_dir import get_files
from my_get_files_in_dir import get_dirs




def clean_empty_dir():
    myself=sys.argv[0]

    work_path = os.getcwd()


    if 'c:' in str.lower(work_path):
        print('待修改的文件夹位于c盘,为安全禁止修改')
        return False

    for dir in get_dirs(work_path):
        if os.listdir(dir)==[]:
            os.rmdir(dir)
    

def my_rename(ext_key=None,t_ext=None):

    myself=sys.argv[0]

    work_path = os.getcwd()

    files=[]

    if 'c:' in str.lower(work_path):
        print('待修改的文件夹位于c盘,为安全禁止修改')
        return False

    for file in get_files(work_path):

        if (str.lower(myself) in str.lower(file)) or '.py' in str.lower(file)  or '.exe' in str.lower(file):

            continue

        else:

            files.append(file)

    def rename_ext(ext_key,t_ext):

        for file in files:

            f_path,f_filename=os.path.split(file)

            f_name,f_ext=os.path.splitext(f_filename)

            #print(f_path,'-----',f_name,'-----',f_ext)

            if '.' not in t_ext:
                t_ext='.'+t_ext

            if str.lower(f_ext).replace('.','')==str.lower(ext_key):

                os.rename(os.path.join(f_path,f_name+f_ext),os.path.join(f_path,f_name+t_ext))
                print(os.path.join(f_path,f_name+f_ext),'    ',os.path.join(f_path,f_name+t_ext))

    def rename_filename():
        
        count=100

        result={}
        
        for file in files:


            f_path,f_filename=os.path.split(file)

            f_name,f_ext=os.path.splitext(f_filename)

            temp=re.findall('\d+',f_name)

            if len(temp)==0:

                t_name=10000000000+count
                
                result[t_name] = (f_path,f_name,f_ext)


            if len(temp)>0:

                print(temp,sum([int(x) for  x in temp]),sum([int(x) for  x in temp])+count)

                t_name=sum([int(x) for  x in temp])+count

                while t_name in result.keys():
                    t_name+=1

                result[t_name] = (f_path,f_name,f_ext)

            count+=1
        

            #print(f_name,t_name)


        count=1

        for key in sorted(result.keys()):
            f_path,f_name,f_ext=result[key]
            os.rename(os.path.join(f_path,f_name+f_ext),os.path.join(f_path,str(count)+f_ext))
            print(os.path.join(f_path, f_name + f_ext), '      ',os.path.join(f_path, str(count) + f_ext))
            count+=1
                

    if ext_key == None and  t_ext == None:
        rename_filename()
    else:
        rename_ext(ext_key,t_ext)

        
if __name__ == '__main__':

    print(sys.argv,len(sys.argv))

    if len(sys.argv)==2 and str.lower(sys.argv[1]) =='-y':
        my_rename()


    if len(sys.argv)==2 and str.lower(sys.argv[1]) =='-clean':
        clean_empty_dir()


    if len(sys.argv)==3:

        s=re.sub('[\'\"]','',sys.argv[1])

        t=re.sub('[\'\"]','',sys.argv[2])

        print(s,t)

        my_rename(s,t)

        



