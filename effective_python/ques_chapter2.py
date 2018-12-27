# -*- coding:utf-

# 让python2 使用中文编码


# 讲解python作用域的问题，闭包变量的作用域往往是内部的，容易出错，所以用列表来代替
def sort_priority2(numbers,group):
    found = [False]
    def helper(x):
        if x in group:
            found[0] = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found[0]


numbers = [9, 3, 2, 1, 5, 4, 7, 6]
group = [2, 3, 6, 7]
found = sort_priority2(numbers, group)
print("Found: ", found)
print(numbers)


def sort_priority3(numbers,group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found


numbers = [9, 3, 2, 1, 5, 4, 7, 6]
group = [2, 3, 6, 7]
found = sort_priority3(numbers, group)
print("Found: ", found)
print(numbers)


'''
第16条：考虑用生成器来改写直接返回列表的函数 
'''

def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


address = 'Four score and seven years ago...'
result = index_words(address)
print('the index', result[:])


# 改写1
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


result1 = list(index_words_iter(address))
print('the index iter', result1[:])


# 改写2 解决读取文件过大导致内存耗尽的问题
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


with open(u'E:\项目文档\storm交接-王彬\交接注意事项\交接笔记.txt', 'r') as f:
    it = index_file(f)
    # for item in it:
    #     print('begin')
    #     print('go', item)


'''第十八条： 用数量可变的位置参数使代码更可读 '''


# 版本1
def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))


log('My numbers are', [1, 2])
log('Hi there', [])


# 版本2
def log2(message, *values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))


log2('My numbers are', 1, 2)
log2('Hi there')
favorites = [7, 33, 99]
log2('Favorite colors', *favorites)  # 对于列表参数来说需要这样调用


'''
第20条：用None 和 文档字符串来描述具有动态默认值的参数 
'''
import datetime
import time


# 默认参数值是模块加载后就初始化了的
def log(message, when=datetime.datetime.now()):
    print('%s: %s' % (when, message))


log('Hi there!')
time.sleep(1)
log('Hi again!')


# 重写方法
def log_default(message, when=None):
    """

    :param message: Message to print
    :param when: datetime of when the message occurred. Defaults to the present time
    """
    when = datetime.datetime.now() if when is None else when
    print('%s: %s' % (when, message))


log_default('Hi there!')
time.sleep(1)
log_default('Hi again!')