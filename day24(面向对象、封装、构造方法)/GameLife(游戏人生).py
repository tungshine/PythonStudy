# __author: TungShine
# __date: 2017/9/11
# __description:


class Person:
    def __init__(self, name, age, sex, fight):
        self.name = name
        self.age = age
        self.sex = sex
        self.fight = fight

    def grass_fight(self):
        self.fight -= 200

    def self_practice(self):
        self.fight += 100

    def multiplayer_game(self):
        self.fight -= 500

    def _detail(self):
        detail = "姓名%s;性别%s;年龄%s;战斗力%s;" % (self.name, self.sex, self.age, self.fight)
        print(detail)


#
# role_list = []
#
# y_n = input('是否创建角色? y/n')
# if y_n == 'y':
#     name = input("请输入名称：")
#     age = input("请输入年龄：")
#     sex = input("请输入性别：")
#     fight = input("请输入战斗力：")
cangjingjing = Person("苍井井", "女", 18, 15000)
cangjingjing._detail()
