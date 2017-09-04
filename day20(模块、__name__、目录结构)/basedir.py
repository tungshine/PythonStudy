# __author: TungShine
# __date: 2017/9/4
# __description: 绝对路径

import os

print(__file__)  # 获取文件的相对路径，但是PyCharm帮助程序把绝对路径取出来了，在命令行执行就能看出不同

print(os.path.abspath(__file__))

print(os.path.dirname(os.path.abspath(__file__)))  # os.path.dirname()获取当前路径的父路径


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)