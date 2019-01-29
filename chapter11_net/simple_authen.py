import hmac
import os
from socket import socket, AF_INET, SOCK_STREAM



def server_authenticate(connection, secret_key):
    '''
    需要客户端验证
    '''
    message = os.urandom(32)
    connection.send(message)
    hash = hmac.new(secret_key, message)
    digest = hash.digest()
    response = connection.recv(len(digest))
    return hmac.compare_digest(digest, response)

secret_key = b'peekaboo'
def echo_handler(client_sock):
    if not server_authenticate(client_sock, secret_key):
        print("未通过认证，关闭连接")
        client_sock.close()
        return
    while True:
        msg = client_sock.recv(8192)
        print(msg)
        if not msg:
            print("发送为空，停止返回消息")
            break
        print("发送不为空，返回消息")
        client_sock.sendall(msg)

def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    while True:
        connection, addressforcon = s.accept()
        echo_handler(connection)


echo_server(('localhost', 18000))
