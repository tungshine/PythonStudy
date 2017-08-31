# __author   :   TungShine
# __date     :   2017/8/30


def f(n):
    return n ** 3


a = [f(x) for x in range(10)]
print(a)

t = ('123', 8)
a, b = t  # 在列表中或元组中 a,b = t 等价于赋值，但是变量的数量必须和元组或者列表的数量保持一致，否则会报错
print(a)
print(b)
