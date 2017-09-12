# __author: TungShine
# __date: 2017/9/12
# __description:


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print('init')
        pass

    def __call__(self, *args, **kwargs):
        # print('call')
        pass

    def __int__(self):
        return 111

    def __str__(self):  # 类似java中toString()方法
        return 'fuck'

    def __add__(self, other):
        return 'fuck'

    def __del__(self):
        print('虚构方法，对象被销毁时，自动执行')

    def __getitem__(self, item):
        return item + 10

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print(key)


# obj = Foo()
# obj()  # 对象后面再加上()时,类中的方法必须加上系统的内置方法__call__()
# print(int(obj))  # 在用int()方法将对象转换为int类型时,自动执行__int__()方法,并将返回值赋值给int对象

# print(str(obj))  # 同理用str()方法也是如此,但不是必须要在类中加上__str__()方法
# print(obj)  # 在程序内部,先调用str(obj)方法,将obj转换为str对象,然后在调用__str__()方法

# obj2 = Foo()
# r = obj + obj2  # 2个对象相加时,自动执行第一个对象中的__add__()方法,并且将第二个对象当作参数传入
# print(r, type(r))

# obj = Foo('tang', 28)
# print(obj.__dict__)  # 将对象中的成员按照字典的方式输出
# print(Foo.__dict__)  # 将 类 中的成员按照字典的方式输出

# li = Foo('tang', 28)
# # print(li[7])  # 自动执行li对象类中的 __getitem__()方法，索引当作参数传给item

# li[100] = 'shine'
# del li[999]  # 与类中对应方法一一对应
