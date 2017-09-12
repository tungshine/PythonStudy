# __author: TungShine
# __date: 2017/9/11
# __description:


class Pagination:
    def __init__(self, current_page):
        try:
            self.page = int(current_page)
        except Exception:
            self.page = 1

    @property
    def start(self):
        val = (self.page - 1) * 10 + 1
        return val

    @property
    def end(self):
        val = self.page * 10
        return val


li = []
for i in range(1000):
    li.append(i)

while True:
    p = input("请输入要查看的页码：")  # 默认1 ,每页10条
    p = int(p)

    page = Pagination(p)

    print(li[page.start: (page.end + 1)])
