
"""
通过socket实现一个网络服务，要求服务器端和客户端可以通过SSL实现身份验证，并且对传输数据进行加密
"""

from socket import socket, AF_INET, SOCK_STREAM
import ssl

KEYFILE = 'server_key.pem'  # 服务器私钥
CERTFILE = 'server_cert.pem' # 服务器证书

def echo_client(s):
    while True:
        data = s.recv(8192)
        if data == b'':
            break
        s.send(data)
    s.close()
    print('Connection closed')

def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(1)
    s_ssl = ssl.wrap_socket(s, keyfile=KEYFILE, certfile=CERTFILE, server_side=True)

    while True:
        try:
            connection, address_from_client = s_ssl.accept()
            print('Got connection', connection, address_from_client)
            echo_client(connection)
        except Exception as e:
            print('{}: {}'.format(e.__class__.__name__, e))

echo_server(('', 20000))