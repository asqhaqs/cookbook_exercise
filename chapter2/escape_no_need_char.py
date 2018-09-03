# -*- coding:utf-

# 让python2 使用中文编码

#消除空格符

s = ' hello world \n'
result = s.strip()
print(result)

#消除左边的
result1 = s.lstrip()
print(result1)

#消除右边的
result1 = s.rstrip()
print(result1)

#可以指定其他的字符
t = '-------hello========='
result = t.lstrip('-')
print(result)

result = t.strip('-=')
print(result)