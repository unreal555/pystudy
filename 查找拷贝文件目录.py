# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/9/8 0008 下午 2:53
# Tool ：PyCharm
import shutil
from my_get_files_include_subdir  import get_paths

for i in get_paths('h://tujidao','dir',content=['徐微微']):
    print(i)
    shutil.copytree(i + '//', r'C:\\Users\\Administrator\\Desktop\p\\' + re.split(r'[\\/]', i)[-1], dirs_exist_ok=True)

