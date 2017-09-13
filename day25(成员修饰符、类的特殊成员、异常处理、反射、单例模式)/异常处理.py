# __author: TungShine
# __date: 2017/9/13
# __description:


def db():
    return False


def index():
    try:
        # 代码块
        r = input('>>')
        int(r)

        result = db()
        if not result:
            # 主动触发异常
            raise Exception('数据库处理错误')
    except Exception as e:
        # e是Exception对象，对象中封装了错误信息
        # 上述代码块如果出错，自动执行当前块的内容
        print(e)
    # else:
    #     # 程序不出错就执行
    #     pass
    # finally:
    #     # 最后执行
    #     pass

index()