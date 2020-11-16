import numpy as np
# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.


def softmax(L):
    return np.exp(L) / np.sum(np.exp(L))


def softmax1(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result

    # Note: The function np.divide can also be used here, as follows:


def softmax2(L):
    expL = np.exp(L)
    return np.divide(expL, expL.sum())


ls = [1, 2, 3, 4]
print(softmax(ls))
print(softmax1(ls))
print(softmax2(ls))
