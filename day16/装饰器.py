# __author   :   TungShine
# __date     :   2017/8/23
import time


def foo():
    print('foo...')
    time.sleep(2)


def bar():
    print('bar...')


def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print(end - start)

    return inner

