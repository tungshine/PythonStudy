# __author   :   TungShine
# __date     :   2017/8/31

import time

# print(help(time))  # 获取api
# print(time.time())  # 打印当前时间到1970年1月1日的时间戳
# print(time.clock())  # 计算CPU执行时间，当前程序执行时间

# print(time.gmtime())  # 结构化时间，获取0时区的时间
# print(time.asctime())  # 将时间元组转换为字符串
# struct_time = time.localtime()  # 获取本地结构化时间
# print(time.strftime('%Y-%m-%d %H:%M:%S', struct_time))  # 自定义时间格式
# print(time.strptime('2017-08-31 11:26:38', '%Y-%m-%d %H:%M:%S'))  # 将自定义时间转换为结构化时间
# current_time = time.strptime('2017-08-31 11:26:38', '%Y-%m-%d %H:%M:%S')
# print(current_time.tm_wday)  # 获取本周第几天
# print(current_time.tm_year)  # 获取年份
# print(current_time.tm_mday)
# print(time.ctime(1464654654))  # 将时间戳转换为本地字符串
