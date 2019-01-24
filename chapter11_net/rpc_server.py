import pickle
from multiprocessing.connection import Listener
from threading import Thread

# 这里是通过进程间通信（socket方式）实现的rpc调用 具体说明见 p468页
class RPCHandler:
    def __init__(self):
        self._functions = {}

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                # 接收消息
                func_name, args, kwargs = pickle.loads(connection.recv())
                # 执行RPC并且返回结果
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass

def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()

# 远程调用方法
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

# 使用handler 来注册方法
handler = RPCHandler()
handler.register_function(add)
handler.register_function(sub)


rpc_server(handler, ('localhost', 17000), authkey=b'peekaboo')