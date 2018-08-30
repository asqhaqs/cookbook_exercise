import heapq


# 实现类的优先队列
class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('doo'), 1)
q.push(Item('baby'), 2)
q.push(Item('gogogo'), 3)

print(q.pop())
print(q.pop())
print(q.pop())