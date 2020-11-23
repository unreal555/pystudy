import os
import sys
import re
from my_get_files_in_dir import get_files

def my_rename(ext_key=None,t_ext=None):

    myself=sys.argv[0]

    work_path = os.getcwd()

    files=[]

    for file in get_files(work_path):

        if str.lower(myself) in str.lower(file):

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

                #os.rename(os.path.join(f_path,f_name+f_ext),os.path.join(f_path,f_name+t_ext))
                print(os.path.join(f_path,f_name+f_ext),'    ',os.path.join(f_path,f_name+t_ext))

    def rename_filename():
        
        count=1
        
        for file in files:

            f_path,f_filename=os.path.split(file)

            f_name,f_ext=os.path.splitext(f_filename)

            #os.rename(os.path.join(f_path,f_name+f_ext),os.path.join(f_path,str(count)+f_ext))
            print(os.path.join(f_path, f_name + f_ext), '      ',os.path.join(f_path, str(count) + f_ext))
            count+=1
                

                

    if ext_key == None and  t_ext == None:
        rename_filename()
    else:
        rename_ext(ext_key,t_ext)

        
if __name__ == '__main__':

    print(sys.argv,len(sys.argv))
    
    if len(sys.argv)==1:
        my_rename()

    elif len(sys.argv)==3:

        s=re.sub('[\'\"]','',sys.argv[1])

        t=re.sub('[\'\"]','',sys.argv[2])

        print(s,t)
        
        my_rename(s,t)
        
        



