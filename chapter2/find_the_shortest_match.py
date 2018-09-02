
# -*- coding:utf-
# 让python2 使用中文编码

import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer say "yep."'
result = str_pat.findall(text1)

print(result)
# ['yep.']

text2 = 'Computer say "yep.", but jerry say "no."'
result2 = str_pat.findall(text2)

# 匹配错误
print(result2)
# ['yep.", but jerry say "no.']

# 加？让*匹配不使用贪心模式
str_pat = re.compile(r'\"(.*?)\"')
result3 = str_pat.findall(text2)

print(result3)


# 编写多行模式的正则表达式，一般出现在想使用. 来匹配任意字符，但是句点不能匹配换行符
# 这里来匹配c语言的注释
comment = re.compile(r'/\*(.*?)\*/')
text3 = '/* this is a comment */'
text4 = '''  /* this is a 
               ***********
               multiline comment */ '''
result4 = comment.findall(text3)
print(result4)

# 不匹配多行
result5 = comment.findall(text4)
print(result5)

# 添加对换行符的支持
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
result = comment.findall(text4)
print(result)

# 或者直接这样，使用re.DOTALL 使得句点匹配所有的字符
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
result = comment.findall(text4)
print(result)