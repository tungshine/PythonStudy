# __author   :   TungShine
# __date     :   2017/8/18

import copy

# s = [[1,2], 'Shine', 'Hello']
# s2 = s.copy()
#
# s2[0][1] = 3
# print(s)

husband = ['shine', 123, [15000, 9000]]

wife = husband.copy()
wife[0] = 'love'
wife[1] = 456

husband[2][1] -= 3000

xiaosan = copy.deepcopy(husband)
xiaosan[0] = 'xiaosan'

xiaosan[2][1] -= 1000
wife[2][1] -= 2000

print(wife)
print(xiaosan)
