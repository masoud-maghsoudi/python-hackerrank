from itertools import permutations

S = list(input().split())

result = list(permutations((list(S[0])),int(S[1])))
result.sort()

for i in result:
    print(''.join(i))