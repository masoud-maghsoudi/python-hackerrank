import numpy
numpy.set_printoptions(legacy='1.13')
N, M = list(map(int, input().split()))
arr = []
for _ in range(N):
    arr.append(input().split())
A = numpy.array(arr, int)
print(numpy.mean(A, axis=1), numpy.var(A, axis=0), numpy.std(A), sep='\n')