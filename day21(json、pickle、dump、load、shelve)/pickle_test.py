# __author: TungShine
# __date: 2017/9/4

import pickle


def foo():
    print('ok')


data = pickle.dumps(foo)

f = open('PICKLE_text', "wb")
f.write(data)
f.close()
