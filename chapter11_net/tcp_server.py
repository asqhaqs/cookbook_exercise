from socketserver import BaseRequestHandler, TCPServer, StreamRequestHandler, ThreadingTCPServer


# class EchoHandler(BaseRequestHandler):
#     def handle(self):
#         print('get connection from', self.client_address)
#         while True:
#             msg = self.request.recv(8192)
#             if not msg:
#                 break
#             self.request.send(msg)

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('get connection from', self.client_address)
        i = 0
        while True:
            msg = self.request.recv(5)
            if not msg:
                print("the msg number is: " + str(i))
                break
            print(msg)
            i = i + 1



class EchoHandler2(StreamRequestHandler):
    def handle(self):
        print('get connection from', self.client_address)
        for line in self.rfile:
            self.wfile.write(line)

if __name__ == '__main__':
    # 单线程服务器
    serv = TCPServer(('', 20001), EchoHandler)
    serv.serve_forever()

    # 多线程服务器
    # serv = ThreadingTCPServer(('', 20000), EchoHandler2)
    # serv.serve_forever()