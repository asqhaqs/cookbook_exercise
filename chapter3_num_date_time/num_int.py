# -*- coding:utf-

# 让python2 使用中文编码

print(round(1.23, 1))

print(round(1.27, 1))

print(round(1.27114, 4))

print(round(1124132423, -3))

a = 4.2
b = 2.1
print(a+b)
if a+b != 6.3:
    print('no')

from decimal import Decimal

# 精确小数
a = Decimal('4.2')
b = Decimal('2.1')
if a+b == Decimal('6.3'):
    print('ok')

# 对数字进行格式化输出
x = 123.456
s = format(x, '0.2f')
print(s)
print(format(x, 'e'))

# 二进制，八进制，十六进制
x = 1234
print(bin(x))
print(oct(x))
print(hex(x))
# 去掉前面的标志位
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))