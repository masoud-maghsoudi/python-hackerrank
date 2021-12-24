from collections import Counter

X = int(input())
inventory = list(map(int, input().split()))
N = int(input())
demand = []
for i in range(N): demand.append(list(map(int, input().split())))
income = 0

for i in demand:
    if i[0] in Counter(inventory).keys():
        income += i[1]
        inventory.remove(i[0])
print(income)
