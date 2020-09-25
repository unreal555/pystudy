# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/8/24 0024 上午 9:56
# Tool ：PyCharm

from PIL import Image
import os


basedir = r'''.'''

def pic_resize(source,dest='',save_as_jpg=True,q=90,size=1920):
    try:
        
        file_path,full_file_name=os.path.split(source)
        file_name,file_ext=os.path.splitext(full_file_name)


        if save_as_jpg==True and str.lower(file_ext) not in ['.jpg','.jpeg']:
            dest_full_file_name=file_name+'.jpg'
        else:
            dest_full_file_name=full_file_name

        if dest=='':
            dest=os.path.join(file_path,dest_full_file_name)
        else:
            dest=os.path.join(dest,dest_full_file_name)


        img = Image.open(source)
        w, h = img.size
        bili = 1
        if w < size or h < size:
            bili = 1
        else:
            bili=max(size/w,size/h)
            
        img = img.resize((int(w * bili), int(h * bili)), Image.ANTIALIAS)

        

        img.save(dest,quality=q)


        if save_as_jpg==True and str.lower(file_ext) not in ['jpg','jpeg'] :
            
            os.remove(source)

        
        return True
    
    except Exception as e:
        print(source,'错误',e)
        return False


print(pic_resize('./Image001.png',dest='c:/',save_as_jpg=True,q=95,size=1000))
