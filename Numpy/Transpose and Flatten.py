import numpy
N, M = list(map(int, input().split()))
arr = []
for i in range(N):
    arr.append(input().split())
A = numpy.array(arr, int)
print(A.transpose(), A.flatten(), sep='\n')