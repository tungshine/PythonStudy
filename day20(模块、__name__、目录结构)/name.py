# __author: TungShine
# __date: 2017/9/4
# __description: __name__


def hello():
    print('hello')


if __name__ == '__main__':  # 防止其它模块调用该模块时，该方法多次调用
    hello()
