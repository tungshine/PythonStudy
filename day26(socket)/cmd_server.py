# __author: TungShine
# __date: 2017/9/18
# __description:
import socket
import subprocess

sk = socket.socket()
sk.bind(('127.0.0.1', 9999))
sk.listen(3)  # 表示等待连接数为3

while 1:
    conn, address = sk.accept()  # 接收客户端与服务器之间建立的连接，以元组的形式返回
    while True:
        try:
            data = conn.recv(1024)
        except Exception:
            break
        if not data:
            break
        print('....', str(data, "utf8"))

        obj = subprocess.Popen(str(data, "utf8"), shell=True, stdout=subprocess.PIPE)
        cmd_result = obj.stdout.read()
        result_length = bytes(str(len(cmd_result)), 'utf8')
        conn.sendall(result_length)  # 传输内容必须是bytes类型

        conn.recv(1024)  # 解决粘包现象,目的是隔开2个send同时在一直容易发生的粘包现象

        conn.sendall(cmd_result)

sk.close()
