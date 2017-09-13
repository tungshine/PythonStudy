# __author: TungShine
# __date: 2017/9/13
# __description:


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return "%s-%s" % (self.name, self.age)


obj = Foo('tang', 18)
# b = "name"

# 以字符串形式取对象中变量的值

# print(obj.__dict__[b])

# 去哪个对象里面取什么变量的内容
func = getattr(obj, "show")
_type = type(func)

attr_name = _type.__name__
print(attr_name)
r = func()
print(r)

setattr(obj, "k1", "v1")
print(obj.k1)

ret = hasattr(obj, "show")
print(ret)


# 以上是通过对象寻找成员
