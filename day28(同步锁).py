# __author: TungShine
# __date: 2017/9/21
# __description:

import time
import threading


def add_num():
    global num  # 在每个线程中都获取这个全局变量
    # num -= 1

    """
        在cpu切换的时候因为num的值赋值给temp，
        可能在cpu切换到另一个线程的时候做了值减一的操作，
        再切换回来的时候还是做的100-1的操作
    """
    temp = num
    # print('---get num:', num)
    time.sleep(0.00000001)
    num = temp - 1


num = 100  # 设定一个共享变量

thread_list = []
for i in range(100):
    t = threading.Thread(target=add_num)
    t.start()
    thread_list.append(t)

for t in thread_list:  # 等待所有线程执行完毕
    t.join()

print('final num:', num)
