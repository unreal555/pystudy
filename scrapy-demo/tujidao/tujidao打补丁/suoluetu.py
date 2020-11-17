from PIL import Image
import os
from my_get_dir_file_list import get_dirs_files_list
from my_logger import logger


basedir='''E:\新建文件夹'''
suoluedir='E:\新建文件夹\suoluetu'


basedir=str.lower(basedir)
suoluedir=str.lower(suoluedir)
logger=logger(suoluedir)


def pic_resize(s,t):
    img = Image.open(s)
    w,h=img.size
    bili=1
    if w<800 or h<800:
        bili=1
    else:
        bili=0.1


    img=img.resize((int(w*bili),int(h*bili)),Image.ANTIALIAS)
    img.save(t)


for xilie in get_dirs_files_list(basedir,'dir'):
        for taotu in get_dirs_files_list(xilie,'dir'):
            if logger.check(taotu):
                print('{}已处理，跳过'.format(taotu))
                continue
            logger.write(taotu)
            for tupian in get_dirs_files_list(taotu,'jpg','png','jpeg'):
                s_dir,filename=os.path.split(tupian)
                t_dir=s_dir.replace(basedir,suoluedir)
                t=os.path.join(t_dir,filename)
                if not os.path.exists(t_dir):
                    os.makedirs(t_dir)
                print(tupian ,t)
                pic_resize(tupian,t)
