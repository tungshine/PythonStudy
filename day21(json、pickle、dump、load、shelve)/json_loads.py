# __author: TungShine
# __date: 2017/9/4


import json

f = open('JSON_text', 'r')
data = f.read()
dic = json.loads(data)

print(dic['name'])




