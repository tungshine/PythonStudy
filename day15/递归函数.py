# __author   :   TungShine
# __date     :   2017/8/22

x = 6


def factorial(n):
    # ret = 1
    # for i in range(1, n + 1):     # 普通求一个数的阶乘
    #     ret = ret * i
    # return ret

    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


print(factorial(5))

