import numpy
numpy.set_printoptions(legacy='1.13')
dim = list(map(int, input().split()))
print(numpy.eye(*dim))