# __author: TungShine
# __date: 2017/9/4

import shelve

f = shelve.open(r'SHELVE_text')

f['info'] = {'name': 'alex', 'age': '28'}
f['shopping'] = {'name': 'alex', 'price': '100'}


data = f.get('shopping')
print(data)
