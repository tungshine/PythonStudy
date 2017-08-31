# __author: TungShine
# __date: 2017/8/31

import random


# print(random.random())  # 默认生成0到1之间的随机数
# print(random.randint(1, 8))  # 生成1到8之间的整数，包括8
# print(random.choice('hello'))
# print(random.choice(['hello', 1, 2, [4, 5]]))
# print(random.shuffle(['hello', 1, 2, [4, 5]]))
# print(random.sample(['hello', 1, 2, [4, 5]], 2)) # 随机取2个元素
# print(random.randrange(1, 3))  # 生成1到3之间在整数，不包括3

# print(chr(65))  # 按照ASSIC表中十进制数字转义成字符串

# 生成随机数
def v_code(x):
    code = ''
    for i in range(x):
        num = random.randrange(10)
        letter = chr(random.randrange(65, 91))
        _letter = random.choice([num, letter])
        code = ''.join([code, str(_letter)])
    return code


print(v_code(5))
