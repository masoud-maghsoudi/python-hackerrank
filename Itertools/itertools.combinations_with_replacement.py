from itertools import combinations_with_replacement
S = list(input().split())
A = list(S[0])
A.sort()
result = list(combinations_with_replacement(A,int(S[1])))

for i in result:
    print(''.join(i))