# __author   :   TungShine
# __date     :   2017/8/30


# 生成器的2种生成方式
# 1. s = (x * 2 for x in range(5))  # 是生成器对象，是一个可迭代对象
# print(s)
# # while True:
# #     try:
# #         print(next(s))
# #     except StopIteration:
# #         break
# for i in s:
#     print(i)

# 2. yield

def foo():
    print('ok')
    yield 1  # 在函数中出现yield，就是一个生成器对象，而不执行函数中的代码
    print('ok2')
    yield 2  # yield相当于return


#
# g = foo()
# print(g)
#
# next(g)
# next(g)
#
# for i in g:
#     print(i)


# 斐波那契数列
# 0 1 1 2 3 5 8 13 21
def fab(max):
    n, before, after = 0, 0, 1
    while n < max:
        print(before)
        before, after = after, before + after  # 先求和在赋值
        n = n + 1


fab(10)
