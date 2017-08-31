# __author   :   TungShine
# __date     :   2017/8/21

s1 = set(['shine', 1, 2])
# s2 = set('shine')
# print(s)
# print(s2)

# s1 = set("123")
# s2 = set("23456")
# print(len(s1 or s2), s1 or s2)  # 集合中2个集合or， 返回第一个集合中所有元素
# print(len(s1 and s2), s1 and s2)  # 2个集合and， 返回第二个集合中所有元素
#
# print(len(s1.union(s2)), s1.union(s2))  # 返回2个集合的并集，即2个集合中所有元素
# print(len(s1 | s2), s1 | s2)
#
# print(len(s1.intersection(s2)), s1.intersection(s2))  # 返回2个集合的交集,即2个集合中的公共元素
# print(len(s1 & s2), s1 & s2)
#
# print(len(s1.difference(s2)), s1.difference(s2))  # 返回在s1中但不在s2中的元素集合，in s1 not in s2
# print(len(s1 - s2), s1 - s2)
#
# print(len(s1.symmetric_difference(s2)), s1.symmetric_difference(s2))  # 返回2个集合中不重复的元素
# print(len(s1 ^ s2), s1 ^ s2)

print(s1)
s1.add('ok')
print(s1)
s1.update('sdf') # 将'sdf'拆分成s、d、f在添加到集合中
print(s1)
s1.remove('ok')
print(s1)