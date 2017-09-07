# __author   :   TungShine
# __date     :   2017/8/23
import time


def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print(end - start)

    return inner


def foo():
    print('foo...')
    time.sleep(2)


@show_time  # bar = show_time(bar) # 等价与@show_time函数
def bar():
    print('bar...')


bar()
