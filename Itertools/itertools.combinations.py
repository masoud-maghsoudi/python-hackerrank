import itertools

inp = input().split()
S = list(inp[0])
S.sort()
for i in range(1,int(inp[1])+1):
    result = list(itertools.combinations(S,i))
    for j in result: print(''.join(j))