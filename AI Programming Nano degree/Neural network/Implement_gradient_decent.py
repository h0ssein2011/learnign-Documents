# read data from data file and
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('student_data.csv', delimiter=',')

print(data[:10])


# data celean up
# one hot encoding
data = pd.get_dummies(data, prefix='rank', columns=['rank'])
print(data[:10])

# sacaling

data['gre'] = data['gre'] / max(data['gre'])
data['gpa'] = data['gpa'] / max(data['gpa'])

print(data[:10])
epochs = 25


def sigmoid(x):
    return 1.0 / (1+np.exp(-x))


def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))


X = data.drop('admit', axis=1)
y = data['admit']
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, train_size=0.8, random_state=0)

n_records, n_features = X_train.shape[0], X_train.shape[1]
learnrate = 1.0 / n_records

weights = np.random.normal(scale=1.0 / n_records**0.5, size=n_features)
print('initail weights :', weights)
# forward
for x, y in zip(np.array(X_train), np.array(y_train)):

    h = np.dot(x, weights)
    nn_output = sigmoid(h)

    error = y - nn_output

    error_term = error * nn_output * (1 - nn_output)

    del_w = learnrate * error_term * x

    weights -= del_w

print(weights)
# update weights
