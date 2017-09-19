# __author: TungShine
# __date: 2017/9/19
# __description:


import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9999))
print('客户端启动...')
while True:
    inp = input(">>>")
    if inp == 'exit':
        break
    sk.send(bytes(inp, 'utf8'))
    data = sk.recv(1024)
    print(str(data, 'utf8'))
