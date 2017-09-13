# __author: TungShine
# __date: 2017/9/13
# __description: 通过类直接寻找成员


class Foo:
    stat = '123'

    def __init__(self, name, age):
        self.name = name
        self.age = age


r = getattr(Foo, 'stat')
print(r)
