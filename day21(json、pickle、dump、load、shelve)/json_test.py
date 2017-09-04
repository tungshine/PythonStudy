# __author: TungShine
# __date: 2017/9/4
# __description:

import json

dic = {'name': 'alex', 'age': '18'}

data = json.dumps(dic)
f = open('JSON_text', 'w')
f.write(data)
f.close()
