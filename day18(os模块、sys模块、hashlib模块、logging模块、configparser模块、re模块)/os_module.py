# __author: TungShine
# __date: 2017/8/31

import os

# print(os.getcwd())  # 当前工作目录的路径
# os.chdir('c:\\Users')  # 更改工作目录
# print(os.curdir)  # 获取当前目录
# os.mkdir('test')  # 创建文件夹,只能创建一级目录
# os.rmdir('test')  # 删除当前目录存在子目录的情况下，不能删除
# os.rmdir('test\\shine')  # 只会删除子目录
# os.makedirs('test\\sss')  # 可以创建文件夹及其子目录
# os.removedirs('test\\sss')  # 删除文件夹及其子目录
# os.remove() # 只能删除文件
# print(os.listdir('E:/python/PythonStudy'))
# print(os.path.dirname('E:/python/PythonStudy/day13'))  # 获取当前目录的父目录路径

# info = os.stat('E:/python/PythonStudy/day13')  # 获取文件信息，其中路径用绝对路径
# print(info.st_size)  # 文件大小
# print(info.st_atime)  # 最后访问时间
# print(info.st_mtime)  # 最后修改时间
# print(info.st_ctime)  # 最后更改时间
#
# print(os.path.dirname(__file__))

os.system('dir')