#字典上的计算问题

prices = {
    'ACME': 32.12,
    'NBA': 34.12,
    'CBA': 13,
    'FB': 45
}

# zip 函数将字典的key value值翻转
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# 对字典排序
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

min_value = min(prices, key=lambda k: prices[k])
print(min_value)