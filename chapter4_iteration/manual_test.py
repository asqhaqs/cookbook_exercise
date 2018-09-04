# -*- coding:utf-

# 让python2 使用中文编码

with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line)
    except StopIteration:
        pass

with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line)

# 用生成器函数来实现一种新的迭代模式


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

# 生成器机制
def countdown(n):
    print('Starting to count from', n)
    while n >0:
        yield n
        n -= 1
    print('Done!')


c = countdown(5)
print(c)
print(next(c))


# 定义一个树结构，并且实现一个迭代器

class Node:

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    # python 3.3 以上支持
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

# 例子
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
        
