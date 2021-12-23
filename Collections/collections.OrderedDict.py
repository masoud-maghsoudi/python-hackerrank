from collections import OrderedDict

N = int(input())
items = OrderedDict()

for _ in range(N):
    item = input().split()
    item_price = int(item.pop())
    item_name = " ".join(item)
    if item_name in items : items[item_name] += item_price
    else: items[item_name] = item_price
for key, value in items.items():
    print('{} {}'.format(key, value))
