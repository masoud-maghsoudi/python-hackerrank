import itertools

N = int(input())
S = list(input().split())
K = int(input())
pos = 0

total = tuple(itertools.combinations(S,K))
for i in total:
    if 'a' in i: pos += 1
print(pos/len(total))