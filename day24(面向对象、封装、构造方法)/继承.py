# __author: TungShine
# __date: 2017/9/8
# __description: 继承


class Father():
    def smoke(self):
        print(self)
        print('smoke...')
        pass

    def drink(self):
        print(self)
        print('drink...')
        pass


class Son(Father):  # 子类,派生类

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def playing(self):
        print('playing...')
        print(self)
        pass


f = Father()
print(f)  # <__main__.Father object at 0x00000290D2F69EB8>
s = Son('tang', 28)
s.drink()  # <__main__.Son object at 0x00000290D2F69F60> s中的self是形参,此时代指s对象
s.playing()  # <__main__.Son object at 0x00000290D2F69F60> 调用父类方法的时候,self依然是方法调用的调用者即s对象
