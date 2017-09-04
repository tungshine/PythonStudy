# __author: TungShine
# __date: 2017/9/4


import pickle


def foo():
    print('ok')


f = open('PICKLE_text', 'rb')
data = f.read()
func = pickle.loads(data)

func()
