# __author: TungShine
# __date: 2017/9/4
# __description:

import json

dic = {'name': 'alex', 'age': '18'}
f = open('JSON_text', 'w')

# data = json.dumps(dic)
# f.write(data)
# f.close()

data = json.dump(dic, f)
f.close()
