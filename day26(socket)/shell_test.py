# __author: TungShine
# __date: 2017/9/18
# __description:


import subprocess

obj = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE)

# print(obj)
data = obj.stdout.read()
print(str(data, 'gbk'))
