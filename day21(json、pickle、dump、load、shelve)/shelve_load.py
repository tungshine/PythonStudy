# __author: TungShine
# __date: 2017/9/13
# __description:


import shelve

f = shelve.open(r'SHELVE_text')

data = f.get('shopping')
print(data)
