# __author   :   TungShine
# __date     :   2017/8/23
from functools import reduce

_str = ['a', 'b', 'c', 'd']


# print(abs(-1.4))  # 取绝对值
# print(all([1, 2, '123']))
# print(eval('1.2 + 2.3 + 3.5'))


def fun1(s):
    if s != 'a':
        return s


def fun2(s):
    return s + 'fuck'


# ret = filter(fun1, _str)
# print(fun1(_str))
# print(ret)
# print(list(ret))
#
# ret2 = map(fun2, _str)
# print(ret2)
# print(list(ret2))


def add(x, y):
    return x + y


print(reduce(add, range(1, 100)))  # 遍历列表传到add函数中


def add2(x):
    if x == 1:
        return 1
    return x + add2(x - 1)


print(add2(100))

add3 = lambda a, b: a + b
print(add3(1, 2))

print(reduce(lambda x, y: x * y, range(1, 6)))
