# __author: TungShine
# __date: 2017/9/19
# __description:  测试串行与并行


import time
import threading

begin = time.time()


def add(n):
    sum = 0
    for i in range(n):
        sum += i
    print(sum)


# add(30000000)
# add(50000000)


t1 = threading.Thread(target=add, args=(30000000,))
t2 = threading.Thread(target=add, args=(50000000,))
t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print(end - begin)
