# __author: TungShine
# __date: 2017/9/18
# __description:

import socket
import os

sk = socket.socket()
sk.bind(('127.0.0.1', 9999))
sk.listen(3)  # 表示等待连接数为3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

while 1:
    conn, address = sk.accept()  # 接收客户端与服务器之间建立的连接，以元组的形式返回
    while True:
        # 1. 接收客户端打包发送的文件包
        data = conn.recv(1024)
        cmd, file_name, file_size = bytes.decode(data, 'utf8').split('|')

        # 2. 接收客户端上传到服务器端的文件的绝对路径
        path = os.path.join(BASE_DIR, 'ftp', file_name)

        file_size = int(file_size)

        f = open(path, 'ab')

        has_receive = 0
        while has_receive != file_size:
            _data = conn.recv(1024)
            f.write(_data)
            has_receive += len(_data)

sk.close()
