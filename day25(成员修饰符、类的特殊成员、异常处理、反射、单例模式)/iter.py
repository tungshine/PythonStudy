# __author: TungShine
# __date: 2017/9/12
# __description:


class Foo():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __iter__(self):
        return iter([11, 22, 33])


li = Foo('tang', 18)

# 1. 执行li对象的类Foo中的__iter__方法，并获取返回值
# 2. 循环上一步中返回的对象
for i in li:
    print(i)
