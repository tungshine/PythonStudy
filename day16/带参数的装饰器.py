# __author   :   TungShine
# __date     :   2017/8/29

import time


# 装饰器加参数
def show_time(func):
    def inner(x, y):
        start = time.time()
        func(x, y)
        end = time.time()
        print('spend %s' % (end - start))

    return inner
