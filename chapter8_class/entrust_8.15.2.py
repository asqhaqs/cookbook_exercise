# -*- coding:utf-*-


class A:

    def spam(self, x):
        print("A : spam {}".format(x))
        pass

    def foo(self):
        pass

class B:

    def __init__(self):
        self._a = A()

    def bar(self):
        print("A: bar")
        pass

    #批量委托方法, 该方法能用来寻找所有的属性，如果该属性不存在，则会调用这个方法
    def __getattr__(self, name):
        return getattr(self._a, name)


if __name__ == "__main__":
    b = B()
    b.bar()
    b.spam("hahaha")

