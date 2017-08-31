# __author   :   TungShine
# __date     :   2017/8/22


def print_info(**kwargs):  # 在传参是，以name='shine'键值对形式传参，2个'*'是将参数以字典的形式传参
    # print(kwargs)
    for i in kwargs:
        s = ':'.join([i, str(kwargs.get(i))])
        print(s)


# print_info(name='shine', age=12, job='IT', sex='male')


def add(*args):  # 将多个没有参数名称的参数以元组的形式传参
    _sum = 0
    for i in args:
        _sum += i
    print(_sum)


# add(1, 2, 3, 4)


def f(*args, **kwargs):
    print(args)
    for i in kwargs:
        s = ':'.join([i, str(kwargs[i])])
        print(s)


print(f(1, 2, 3, 'sss', [1, 2], hobby='s'))
