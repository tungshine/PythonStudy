# __author: TungShine
# __date: 2017/9/11
# __description:


class BaseRequest:
    def __init__(self):
        print("BaseRequest.init")


class RequestHandler(BaseRequest):
    def __init__(self):
        print("RequestHandler.init")

    def server_forever(self):
        print("RequestHandler.server_forever")
        """
        注意此时的self代表的是什么,此处self代表的是下面代码中Son()的对象,寻找规则按照 "多继承.py"中来
        """
        self.process_request()

    def process_request(self):
        print("RequestHandler.process_request")


class Minx:
    def process_request(self):
        print("Minx.process_request")


class Son(Minx, RequestHandler):
    pass


obj = Son()
obj.server_forever()
