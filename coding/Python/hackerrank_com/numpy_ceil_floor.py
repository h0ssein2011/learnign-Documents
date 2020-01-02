import numpy
#to set print
numpy.set_printoptions(sign=' ')

a = numpy.array(input().split(),float)

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
