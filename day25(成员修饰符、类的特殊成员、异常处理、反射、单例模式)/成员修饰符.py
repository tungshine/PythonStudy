# __author: TungShine
# __date: 2017/9/12
# __description:


class Foo:
    """
    变量前面加上2个下滑线表示该变量为私有变量,类外部不能直接访问,可以通过方法调用来调用该私有变量
    同理方法也是一样
    """
    __v = '123'

    def __init__(self):
        pass

    def show(self):
        return Foo.__v

    @staticmethod
    def show_static():
        return Foo.__v

    def __private_func(self):
        return self.__v

    def private_func(self):
        return self.__private_func()


# print(Foo.__v)  # AttributeError: type object 'Foo' has no attribute '__v'
print(Foo().show())
print(Foo.show_static())
# print(Foo().__private_func())  # AttributeError: 'Foo' object has no attribute '__private_func'
print(Foo().private_func())

"""
对于有继承关系的,子类不能直接访问父类在私有字段/方法
"""
