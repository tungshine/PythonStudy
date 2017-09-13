# __author: TungShine
# __date: 2017/9/13
# __description: 单例模式


# class Foo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print('show')
#
#
# v = None
# while True:
#     if v:
#         print(v)
#         v.show()
#     else:
#         v = Foo('tang', 18)
#         v.show()


class Foo:
    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v


obj = Foo.get_instance()
obj2 = Foo.get_instance()
obj3 = Foo.get_instance()
print(obj)
print(obj2)
print(obj3)
