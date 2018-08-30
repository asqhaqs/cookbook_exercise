
# -*- coding:utf-

# 让python2 使用中文编码

from fnmatch import fnmatch, fnmatchcase

flag = fnmatch('foo.txt', '*.txt')
if flag:
    print 'ok'

flag1 = fnmatch('foo.txt', '*.TXT')
if flag1:
    print 'ok'

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

if(re.match(r'\d+/\d+/\d+', text1)):
    print('yes')
else:
    print('np')

datepat = re.compile(r'\d+/\d+/\d+')

# match 只是匹配第一个， findall 可以匹配字符串中所有符合条件的

if(datepat.match(text1)):
    print('yes')
else:
    print('np')


if(datepat.match(text2)):
    print('yes')
else:
    print('np')

text = 'Today is 30/08/2018. pycon starts 29/08/2018.'
print(datepat.findall(text))

# 加入捕获组
text3 = '11/27/2012'
datepat1 = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat1.match(text3)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))

result = datepat1.findall(text)
print(result)
for month, day, year in result:
    print('{}-{}-{}'.format(year, month, day))