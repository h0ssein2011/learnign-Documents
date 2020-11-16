import pandas as pd
import numpy as np
import csv
import random


epochs = 500
random.seed(42)

w1 = random.randint(0, 255)
w2 = random.randint(0, 255)
b = random.randint(0, 255)
lr = 0.1


def step(x):
    if x >= 0:
        return 1

    return 0


with open('data.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')

    for i in range(epochs):

        for row in csv_reader:
            if step(float(row[0]) * w1 + float(row[1]) * w2 + b) == 1 and int(row[2]) == 0:
                w1 -= lr
                w2 -= lr
                b -= lr
                print(
                    f'misclassified in {row[0], row[1],row[2]} the step is:{step(float(row[0]) * w1 + float(row[1]) * w2 + b)} new parameter are:{w1,w2,b}')
            elif step(float(row[0]) * w1 + float(row[1]) * w2 + b) == 0 and int(row[2]) == 1:
                w1 += lr
                w2 += lr
                b += lr
                print(
                    f'misclassified in {row[0], row[1],row[2]} the step is:{step(float(row[0]) * w1 + float(row[1]) * w2 + b)} new parameter are:{w1,w2,b}')


print('**********************Done***************************')
print(w1, w2, b)


# udacity approach


# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)


def stepFunction(t):
    if t >= 0:
        return 1
    return 0


def prediction(X, W, b):
    return stepFunction((np.matmul(X, W)+b)[0])

# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.


def perceptronStep(X, y, W, b, learn_rate=0.01):
    for i in range(len(X)):
        y_hat = prediction(X[i], W, b)
        if y[i]-y_hat == 1:
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
            b += learn_rate
        elif y[i]-y_hat == -1:
            W[0] -= X[i][0]*learn_rate
            W[1] -= X[i][1]*learn_rate
            b -= learn_rate
    return W, b

# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.


def trainPerceptronAlgorithm(X, y, learn_rate=0.01, num_epochs=25):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2, 1))
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
    return boundary_lines


df = pd.read_csv('data.csv', delimiter=',', names=['0', '1', '2'])
X = df.loc[:, ['0', '1']]
X = X.to_numpy()
y = df.loc[:, ['2']]
y = y.to_numpy()


test_boundery = trainPerceptronAlgorithm(X, y)
print(test_boundery)
