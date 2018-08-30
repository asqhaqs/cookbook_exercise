import heapq

#找到最大或最小的n个数
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))


#更复杂的情况
portfollo = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'IM', 'shares': 100, 'price': 94.1},
    {'name': 'IB', 'shares': 100, 'price': 81.1},
    {'name': 'IfsdBM', 'shares': 1, 'price': 9.1},
    {'name': 'IB2', 'shares': 120, 'price': 54.1},
    {'name': 'IB', 'shares': 10, 'price': 88.1},
    {'name': 'IBs', 'shares': 120, 'price': 91.1},
    {'name': 'IBt', 'shares': 120, 'price': 95.1},
    {'name': 'IBg', 'shares': 10, 'price': 80.1},
]
cheap = heapq.nsmallest(3, portfollo, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfollo, key= lambda s: s['price'])

print(cheap, expensive)