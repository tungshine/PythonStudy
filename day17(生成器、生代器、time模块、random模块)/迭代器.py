# __author   :   TungShine
# __date     :   2017/8/31


# 生成器都是迭代器，迭代器不一定是生成器

l = [1, 2, 3, 4]
d = iter(l)
print(d)

# for 循环内部三件事情
# 1. 调用可迭代对象在iter方法返回一个迭代对象
# 2. 不断调用迭代对象的next方法
# 3. 处理StopIteration

# for i in [1, 2, 34]:
#     print(iter([1, 2, 34]))


print(isinstance(l, list))
