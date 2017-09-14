# __author: TungShine
# __date: 2017/9/4


import pickle


# def foo():
#     print('ok')
#
#
# f = open('PICKLE_text', 'rb')
# data = f.read()
# func = pickle.loads(data)
#
# func()
f = open('pick1_text', 'rb')
ret = pickle.load(f)
print(ret)