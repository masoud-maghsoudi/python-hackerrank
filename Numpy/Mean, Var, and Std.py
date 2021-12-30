import numpy
a = numpy.array([input().split() for _ in range(int(input().split()[0]))],int)
print(numpy.mean(a,axis=1),numpy.var(a,axis=0),round(numpy.std(a), 11),sep="\n")