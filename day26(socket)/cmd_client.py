# __author: TungShine
# __date: 2017/9/18
# __description:


import socket

sk = socket.socket()

sk.connect(('127.0.0.1', 9999))
while True:
    inp = input(">>>")
    if inp == 'exit':
        break
    sk.send(bytes(inp, 'utf8'))
    result_len = int(str(sk.recv(1024), 'utf8'))  # 按照1024接收，如果接收的服务器端sendall过来的数据超过1024，则需要继续接收
    sk.send('111')
    print(result_len)
    data = bytes()
    while len(data) != result_len:
        data += sk.recv(1024)
    print(str(data, 'gbk'))

sk.close()
