import numpy
N, M = list(map(int, input().split()))
arr = []
for _ in range(N):
    arr.append(input().split())
A = numpy.array(arr, int)
print(numpy.prod(numpy.sum(A, axis=0)))