# -*- coding:utf-*-
import collections
import bisect

class A(collections.Iterable):
    pass


class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial else []

    # 需要实现的方法
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)


if __name__ == "__main__":
    items = SortedItems([5, 1, 2, 4])
    print(list(items))
    print(items[1])
    print(items[-1])
    items.add(2)
    print(list(items))
    print(items[1:4])

    for n in items:
        print(n)
