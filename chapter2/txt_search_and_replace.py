
# -*- coding:utf-

# 让python2 使用中文编码

text = 'yeah, I am xd, and I miss you'

s = text.replace('yeah', 'yep')

# 注意原始文本并没有变化
print(text)
print(s)

texts = 'Today is 08/30/2018, and I will go home'
import re

# \3 表示捕获组中的数量
result = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', texts)

print result


# 使用了编译的版本
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
result2 = datepat.sub(r'\3-\1-\2', texts)
print result2

# 指定一个替换函数
from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

result3 = datepat.sub(change_date, texts)
print(result3)