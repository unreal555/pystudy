#!/bin/py
#   -*-coding:utf-8-*-
from cx_Freeze import setup, Executable

setup(
    name="xuexiqiangguo",
    version="1.0",
    description="rename_files",
    author='zl',
    executables=[Executable("xuexiqiangguo.py")])  # cx1.py为要打包的文件
