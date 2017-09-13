# __author: TungShine
# __date: 2017/9/13
# __description:

"""
class MyException(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


try:
    raise MyException("出错了...")
except MyException as e:
    print(e)
"""

# assert 条件  断言

print(123)
assert 1 == 2
print(456)

# 断言就是指，条件不成立就直接报错，成立才往后执行
