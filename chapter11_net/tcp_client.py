from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))
response = s.send(b'Hello')
result = s.recv(8192)

print(response)
print(result)