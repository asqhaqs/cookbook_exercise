
# -*- coding:utf-*-

# 让python2 使用中文编码

import os
import mmap

# 对二进制文件做内存映射
def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

# size = 1000000
# with open('data', 'wb') as f:
#     f.seek(size-1)
#     f.write(b'\x00')
#
# m = memory_map('data')
# print(len(m))
# print(m[0:10])

# 处理路径名
path = '/Users/beazley/Data/data.csv'

# 得到最后一个文件名
print(os.path.basename(path))

# 得到目录名
print(os.path.dirname(path))

# join 路径名
print(os.path.join('tmp', 'data', os.path.basename(path)))
print(os.name)

# 检测文件是否存在
if os.path.exists('/etc/passwd'):
    print('true')

# 检测是否为file或者dir
if not os.path.isdir('/etc/passwd'):
    print('True')