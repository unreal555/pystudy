from unrar import rarfile
import os



def my_rar(path,to='.',pwd=''):

    try:
        
        if os.path.exists(path) and os.path.isfile(path):
            rar=rarfile.RarFile(path)

        # if pwd=='':
        #     rar.extractall(to)
        # else:
        #     rar.extractall(to,pwd=pwd)

        return True
    
    except Exception as e:
        print(e)
        return False
        
    


rar('d://PyCharm2019.3.1.rar')
