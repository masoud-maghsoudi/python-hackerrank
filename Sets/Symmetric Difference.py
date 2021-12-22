M_size = int(input())
M = set(map(int,input().split()))
N_size = int(input())
N = set(map(int,input().split()))

U = M.union(N)
INT = M.intersection(N)
result = list(U.difference(INT))
result.sort()
for i in result:
    print(i)
