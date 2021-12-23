from collections import defaultdict

n , m = list(map(int,input().split()))
A, B = [], []
for i in range(n): A.append(input().strip())
for i in range(m): B.append(input().strip())
result = defaultdict(list)

for i in set(B):
    if i in A:
        for j in range(len(A)):
            if i == A[j]: result[i].append(str(j+1))

for i in B:
    if i in result: print(" ".join(result[i]))
    else: print('-1')
