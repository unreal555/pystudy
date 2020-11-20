import os
import sys
from sss import get_files

def my_rename(ext_key=None,t_ext=None):


    work_path = os.getcwd()

    files=get_files(work_path)


    def rename_ext(ext_key,t_ext):

        for file in files:

            print(file)

            f_path,f_filename=os.path.split(file)

            f_name,f_ext=os.path.splitext(f_filename)

            print(f_path,'-----',f_name,'-----',f_ext)

            if '.' not in t_ext:
                t_ext='.'+t_ext

            if str.lower(f_ext).replace('.','')==str.lower(ext_key):

                os.rename(os.path.join(f_path,f_name+f_ext),os.path.join(f_path,f_name+t_ext))
                #os.rename(os.path.join(f_path,f_name+f_ext),os.path.join(f_path,f_name+t_ext))

    def rename_filename():
        
        count=1
        
        for file in files:

            f_path,f_filename=os.path.split(file)

            f_name,f_ext=os.path.splitext(f_filename)

            os.rename(os.path.join(f_path,f_name+f_ext),os.path.join(f_path,str(count)+f_ext))

            count+=1
                

                

    if ext_key == None and  t_ext == None:
        rename_filename()
    else:
        rename_ext(ext_key,t_ext)

        
if __name__ == '__main__':

    print(sys.argv)
    
    if len(sys.argv)==1:
        my_rename()

    elif len(sys.argv)==3:
        
        my_rename(sys.argv[1],sys.argv[2])
        
        



