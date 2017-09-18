# __author: TungShine
# __date: 2017/9/18
# __description:

import socket
import os

sk = socket.socket()
sk.connect(('127.0.0.1', 9999))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

while True:
    inp = input(">>>").strip()  # 设定ftp上传格式： post|test.png

    # 1. 获取文件路径、文件名称
    cmd, path = inp.split('|')
    path = os.path.join(BASE_DIR, path)
    file_name = os.path.basename(path)  # 根据文件路径，取到最后一个文件的名字
    # 2. 获取文件大小
    file_size = os.stat(path).st_size  # <class 'int'>int类型

    # 3. 将文件信息打包上传到服务器， 通知服务器
    file_info = 'post|%s|%s' % (file_name, file_size)
    sk.sendall(str.encode(file_info, 'utf8'))

    has_sent = 0

    f = open(path, 'rb')

    while has_sent != file_size:
        # 4. 打开文件
        data = f.read(1024)
        has_sent += len(data)
        sk.sendall(data)
    print('上传成功')
sk.close()
