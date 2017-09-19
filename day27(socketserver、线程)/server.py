# __author: TungShine
# __date: 2017/9/19
# __description:
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('服务器启动...')

        while True:
            conn = self.request
            print(self.client_address)
            while True:
                client_data = conn.recv(1024)
                print(str(client_data, 'utf8'))
                print('waiting...')
                conn.sendall(client_data)
            conn.close()


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    server.serve_forever()
