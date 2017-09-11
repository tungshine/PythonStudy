# __author: TungShine
# __date: 2017/9/11
# __description:


class Base:
    def a(self):
        print('base.a')


class F0(Base):
    def a1(self):
        print('F0.a')


class F1(F0):
    def a1(self):
        print('F1.a')


class F2(Base):
    def a(self):
        print('F2.a')


class S(F1, F2):
    pass


"""
在类继承多个父类中有相同方法时,寻找方法时默认先找继承的第一个类中的
方法(如果继承的类也继承了类,会找到没有父类为止),直到没有找到为止,再开始找第二个
继承的类,可以认为执行顺序为从做到右,从下到上
"""
obj = S()
obj.a()
