# __author: TungShine
# __date: 2017/9/21
# __description: Web Server Gateway Interface


from wsgiref.simple_server import make_server


def index(request):
    print(request['QUERY_STRING'])
    with open('templates/index.html', 'rb') as f:
        data = f.read()
    return [data]


def book(request):
    print(request['QUERY_STRING'])
    with open('templates/book.html', 'rb') as f:
        data = f.read()
        """
            页面传值：
            运用自定义模板方式将文件中内容替换掉
        """
        _data = data.decode('utf8').replace('{{name}}', '大数据')
    return [_data.encode('utf8')]


def routers():
    """
    可以作为菜单管理
    """
    urlpatterns = (
        ('/book', book),
        ('/index', index),
    )
    return urlpatterns


def application(environ, start_response):
    # 通过environ封装成一个所以请求信息的对象
    # start_response可以很方便的设置响应头
    start_response('200 OK', [('Content-Type', 'text/html')])
    request_url = environ['PATH_INFO']
    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == request_url:
            func = item[1]
            break
    if func:
        return func(environ)
    else:
        return [b'<h1 style="color:red">404</h1>']


# 封装socket对象以及准备过程（socket，bind，listen）
httpd = make_server('', 8080, application)

print('Server HTTP on port 8080...')

# 开始监听HTTP请求：
httpd.serve_forever()
