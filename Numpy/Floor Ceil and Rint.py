import numpy
numpy.set_printoptions(legacy='1.13')
arr = input().split()
A = numpy.array(arr, float)
print(numpy.floor(A), numpy.ceil(A), numpy.rint(A), sep='\n')