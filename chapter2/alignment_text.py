# -*- coding:utf-

# 让python2 使用中文编码

# 对齐文本
text = 'Hello World'

s = text.ljust(20)

print(s)

s = text.rjust(20)
print(s)

s = text.center(20)
print(s)

s = text.ljust(20, '=')
print(s)

s = text.center(20, '*')
print(s)
