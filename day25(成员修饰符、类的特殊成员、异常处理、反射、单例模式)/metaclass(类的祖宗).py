# __author: TungShine
# __date: 2017/9/12
# __description:

"""
class Foo:
    def func(self):
        print(123)


def func(self):
    print(123)


# 类都是type类的对象，常说的对象是 类()的对象
Foo2 = type('Foo', (object,), {'func': func})

print(type(Foo), Foo())
print(type(Foo2), Foo2())
"""


class MyType(type):
    def __int__(self):
        print(123)
        pass


class Foo(object, metaclass=MyType):
    def func(self):
        print('hello')
