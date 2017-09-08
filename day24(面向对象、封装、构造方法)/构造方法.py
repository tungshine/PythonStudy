# __author: TungShine
# __date: 2017/9/8
# __description: 类的构造方法


class Person:
    def __init__(self, name, age):  # 调用类时,系统默认先调用执行__init__方法
        """
        构造方法，构造方法的特性,类名()自动执行构造方法
        """
        self.name = name
        self.age = age

    def show(self):
        print('%s-%s' % (self.name, self.age))


p = Person('tang', 28)

p.show()
