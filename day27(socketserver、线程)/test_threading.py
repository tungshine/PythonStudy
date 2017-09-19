# __author: TungShine
# __date: 2017/9/19
# __description:

import time
import threading

begin = time.time()


def foo(n):
    for i in range(10):
        print('foo %s --- % s' % (n, i))
        time.sleep(1)  # sleep不占cpu


def bar(n):
    for i in range(10):
        print('bar %s --- % s' % (n, i))
        time.sleep(2)  # sleep不占cpu


t1 = threading.Thread(target=foo, args=(1,))
t2 = threading.Thread(target=bar, args=(2,))
t1.start()
t2.start()

print('main...')

t1.join()
t2.join()

end = time.time()
print(end - begin)
