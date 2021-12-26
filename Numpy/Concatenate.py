import numpy
N, M, P = list(map(int, input().split()))
arr1, arr2 = [], []
for _ in range(N): arr1.append(input().split())
for _ in range(M): arr2.append(input().split())
A = numpy.array(arr1, int)
B = numpy.array(arr2, int)
print(numpy.concatenate((A,B)))