import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.


def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)

    return -1 * np.sum(Y*np.log(P) + (1-Y)*np.log(1-P))


Y = np.array([1, 0, 1, 0, 1, 1, 0, 1, 0, 0])
P = np.array([0.8, 0.7, 0.6, 0.4, 0.2, 0.1, 0.7, 0.8, 0.8, 0.1])


print(cross_entropy(Y, P))
