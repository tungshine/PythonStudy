# __author: TungShine
# __date: 2017/9/1
import hashlib

# m = hashlib.md5()
# print(m)
# m.update('hello world'.encode('utf8'))  # 在Python3中，字符串默认是unicode格式
# # print(m.hexdigest())
# m.update('alex'.encode('utf8'))
# print(m.digest())  # 打印二进制
# print(m.hexdigest())  # 打印十六进制
#
# m2 = hashlib.md5()
# m2.update('hello worldalex'.encode('utf8'))  # update，就是在原有字符串基础上拼接上新的字符串
# print(m2.hexdigest())


m3 = hashlib.sha256()
m3.update('hello world'.encode('utf8'))
print(m3.hexdigest())