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

os.getcwd()  # 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  # 改变当前脚本工作目录；相当于shell下cd
os.curdir  # 返回当前目录: ('.')
os.pardir  # 获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')  # 可生成多层递归目录
os.removedirs('dirname1')  # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')  # 生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')  # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')  # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  # 删除一个文件
os.rename("oldname", "newname")  # 重命名文件/目录
os.stat('path/filename')  # 获取文件/目录信息
os.sep  # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep  # 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep  # 输出用于分割文件路径的字符串
os.name  # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  # 运行shell命令，直接显示
os.environ  # 获取系统环境变量
