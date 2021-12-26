import numpy

N, M = list(map(int, input().split()))
a, b = [], []
for _ in range(N):
    a.append(input().split())
for _ in range(N):
    b.append(input().split())
A = numpy.array(a, int)
B = numpy.array(b, int)

print(A+B, A-B, A*B, A//B, A % B, A**B, sep='\n')