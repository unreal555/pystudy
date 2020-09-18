from unrar import rarfile
import os



def rar(path,to='.',pwd=''):

    try:
        
        if os.path.exists(path) and os.path.isfile(path):
            rar=rarfile.RarFile(path)

        
        if pwd=='':
            rar.extractall(to)
        else:
            rar.extractall(to,pwd=pwd)

        return True
    
    except Exception as e:
        print(e)
        return False
        
    


extract_all_files('d://1.rar',pwd='123')
