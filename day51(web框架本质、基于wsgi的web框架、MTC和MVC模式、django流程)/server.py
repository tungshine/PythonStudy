# __author: TungShine
# __date: 2017/9/20
# __description:


import socket


def handle_request(client):
    buf = client.recv(1024)
    print(buf.decode('utf8'))
    client.send('HTTP/1.1 200 OK\r\n\r\n'.encode('utf8'))
    with open('templates/index.html', 'rb') as f:
        data = f.read()
    client.send(data)


def main():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('localhost', 80))
    sk.listen(5)

    while True:
        connection, address = sk.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()
