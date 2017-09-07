# __author: TungShine
# __date: 2017/9/7
# __description:


class Person:
    def foo(self, arg):
        print(self, arg)


p = Person()
print(p)
p.foo('111\n')

p2 = Person()
print(p2)
p2.foo('222\n')

p3 = Person()
p3.name = 'tang'
p3.foo('333')
# 以上3个对象的引用在内存空间都是只想的同一块地址
