# __author   :   TungShine
# __date     :   2017/8/21
import time

data = {
    "四川省": {
        "成都市": {
            "高新区": {
                "软件园": {},
                "环球中心": {},
            },
            "武侯区": {
                "数码广场": {},
                "省体育馆": {},
            },
            "成华区": {
                "电子科技大学": {},
            },
        },
        "遂宁市": {
            "船山区": {},
            "安居区": {},
            "大英县": {},
        }
    },
    "北京市": {
        "北京市辖区": {
            "东城区": {
                "天安门": {},
            },
            "西城区": {
                "中关村": {},
            },
            "朝阳区": {
                "鸟巢": {},
            },
        },
    },
}


def logger(msg, log_type):
    if log_type == 'info':
        log_type = 'INFO'
    elif log_type == 'warn':
        log_type == 'WARN'
    else:
        log_type == 'DEBUG'
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    f = open('log.log', 'a', encoding="utf8")
    log = '\n{time} [{type}] {msg} '
    f.write(log.format(time=current_time, msg=msg, type=log_type))
    f.close()


def show_province():
    with open('json', 'r', encoding='utf-8') as read:
        for i in read.readlines():
            s = ''.join([i])
    return s


def add_province():
    with open('json', 'w', encoding='utf8') as write:
        write.write(str(data))


# add_province
pro = show_province()
pro = eval(pro)
for i in pro:
    print(i)


def print_info(name, age, sex):
    print('Name: %s' % name)
    print('Age: %d' % age)
    print('Sex: %s' % set)


# print_info('shine', 28, 'male', job='IT')
