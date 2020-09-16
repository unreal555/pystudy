import os
import re
from my_get_dir_file_list import    get_dirs_files_list  as get

from my_logger import logger

basedir=r'C:\Users\Administrator\Documents\pic'

logger=logger(name='html.txt')

for xiangce in get(basedir,'dir'):
    for dir in get(xiangce,'dir'):
        item=re.split(r'[\\/]',dir)[-1]
        if logger.check(item):
            print('{}跳过'.format(item))
            continue

        with open(os.path.join(dir,'index.html'),'a',encoding='utf-8') as f:
            f.write('<meta charset="utf-8">')
            f.write('<h3>{}</h3>'.format(item))
        for file in get(dir,'jpg','jpeg','png'):
            path,filename=os.path.split(file)
            

            with open(os.path.join(path,'index.html'),'a',encoding='utf-8') as f:
                f.write('<img src="{}"/>'.format(filename))
        logger.write(item)



        
    break
