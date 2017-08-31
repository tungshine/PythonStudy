# __author   :   TungShine
# __date     :   2017/8/16
# cascade 级联
area = {
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


def _cascade():
    back_flag = False
    exit_flag = False
    while not back_flag and not exit_flag:
        for key in area:
            print(key)
        choice = input("1>>").strip()
        if choice in area:
            while not back_flag and not exit_flag:
                for key2 in area[choice]:
                    print(key2)
                choice2 = input("2>>").strip()
                if choice2 == 'b':
                    back_flag = True
                if choice2 in area[choice]:
                    while not back_flag and not exit_flag:
                        for key3 in area[choice][choice2]:
                            print(key3)
                        choice3 = input("3>>").strip()
                        if choice3 == 'b':
                            back_flag = True
                        if choice3 == 'q':
                            exit_flag = True
                        if choice3 in area[choice][choice2]:
                            while not back_flag and not exit_flag:
                                for key4 in area[choice][choice2][choice3]:
                                    print(key4)
                                choice4 = input("4>>").strip()
                                print("last level")
                                if choice4 == 'b':
                                    back_flag = True
                                if choice4 == 'q':
                                    exit_flag = True
                            else:
                                back_flag = False
                    else:
                        back_flag = False
            else:
                back_flag = False

_cascade()

