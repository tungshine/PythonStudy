# __author: TungShine
# __date: 2017/9/14
# __description:


import socket


def start_server():
    sk = socket.socket()
    sk.bind(('127.0.0.1', 9999))
    sk.listen(3)  # 表示等待连接数为3
    return sk


def send_msg(conn, msg):
    pass


sk = start_server()
# conn, address = sk.accept()  # 接收客户端与服务器之间建立的连接，以元组的形式返回

while 1:

    conn, address = sk.accept()

    while True:
        try:
            data = conn.recv(1024)
            print("....", str(data, "utf8"))
        except ConnectionResetError as e:
            print(e)
        if not data:
            conn.close()
            conn, address = sk.accept()
            print(address)
            continue
        inp = input('>>>')
        conn.send(bytes(inp, 'utf8'))  # 传输内容必须是bytes类型

    sk.close()
