# __author   :   TungShine
# __date     :   2017/8/17
# 格式化字符串

name = 'tung'
age = 22
job = 'engineer'
salary = 22222

msg = '''
--------------------info %s-----------------
Name:%s 
Age:%d
Job:%s
Salary:%d
--------------------end---------------------
you live in %s years
''' % (name, name, age, job, salary, 65 - age)
print(msg)

str = 'hi {name} {fuck}'
print(str.format(name=name, fuck=job))
print(str.format_map({"name": name, "fuck": job}))
