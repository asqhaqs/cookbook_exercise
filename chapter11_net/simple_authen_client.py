from socket import socket, AF_INET, SOCK_STREAM
import hmac

def client_authenticate(connection, secret_key):
    '''
    验证客户端程序
    :param connection: 代表 网络连接
    :param secret_key: 客户端及服务端之间的key
    '''
    message = connection.recv(32)
    hash = hmac.new(secret_key, message)
    digest = hash.digest()
    connection.send(digest)

secret_key = b'peekaboo'
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 18000))
client_authenticate(s, secret_key)
s.send(b'Hello World')
resp = s.recv(1024)
print(resp)
