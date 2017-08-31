# __author   :   TungShine
# __date     :   2017/8/23


def outer():
    x = 10

    def inner(m):
        return x + m

    return inner


y = outer()(10)  # 外部要用函数内部变量时，使用闭包取得函数内部变量
print(y)
