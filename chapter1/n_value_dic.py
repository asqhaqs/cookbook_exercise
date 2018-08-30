from collections import defaultdict

# 一个键对应多个值的字典
d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(3)

b = defaultdict(set)

b['a'].add("2")
b['a'].add(2)
b['b'].add(3)

print(d, b)