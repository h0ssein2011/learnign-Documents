import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr_list=[arr[i] for i in range(len(arr)-1,-1,-1) ]
    arr=numpy.array(arr_list ,float)
    return(arr)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
