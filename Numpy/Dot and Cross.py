import numpy
dim = int(input())
tmp, arr = [], []
for i in range(2):
    tmp.clear()
    for j in range(dim):
        tmp.append(input().split())
    arr.append(numpy.array(tmp, int))
print(numpy.dot(arr[0], arr[1]), sep='\n')