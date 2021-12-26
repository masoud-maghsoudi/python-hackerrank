import numpy


def arrays(arr):
    arr.reverse()
    return(numpy.array(arr, float))


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
