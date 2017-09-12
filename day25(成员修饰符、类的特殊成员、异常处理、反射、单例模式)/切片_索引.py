# __author: TungShine
# __date: 2017/9/12
# __description:


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        # 如果item是基本类型：int， str， 索引获取
        # 如果是slice对象的话，就是切片
        # print(item, type(item))
        if type(item) == slice:
            print('起始', item.start)
            print('结束', item.stop)
            print('步长', item.step)
            print('调用这希望做切片处理')
        else:
            print('调用这做索引处理')

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print(key)


li = Foo('tang', 18)
li[123]
li[1: 4: 2]  # 切片
