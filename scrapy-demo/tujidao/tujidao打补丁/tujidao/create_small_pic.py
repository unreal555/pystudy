# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/8/24 0024 上午 9:56
# Tool ：PyCharm

from PIL import Image
import os
from my_get_dir_file_list import get_dirs_files_list
from my_logger import logger

basedir = r'''C:\Users\Administrator\Desktop\p'''
suoluedir = r'''C:\Users\Administrator\Desktop\s'''

basedir = str.lower(basedir)
suoluedir = str.lower(suoluedir)
right = logger(suoluedir)
wrong = logger(dir=suoluedir, name='wrong.txt')


def pic_resize(s, t):
    img = Image.open(s)
    w, h = img.size
    bili = 1
    if w < 500 or h < 500:
        bili = 1
    else:
        bili = 0.1

    img = img.resize((int(w * bili), int(h * bili)), Image.ANTIALIAS)
    img.save(t)


for xilie in get_dirs_files_list(basedir, 'dir'):
    for taotu in get_dirs_files_list(xilie, 'dir'):
        if right.check(taotu[4:]):
            print('{}已处理，跳过'.format(taotu))
            continue
        right.write(taotu)
        for tupian in get_dirs_files_list(taotu, 'jpg', 'png', 'jpeg'):

            try:
                s_dir, filename = os.path.split(tupian)
                t_dir = s_dir.replace(basedir, suoluedir)

                if s_dir == t_dir:
                    break

                t = os.path.join(t_dir, filename)
                if not os.path.exists(t_dir):
                    os.makedirs(t_dir)
                print(tupian, t)
                pic_resize(tupian, t)
            except Exception as e:
                print(e)
                wrong.write(t)
