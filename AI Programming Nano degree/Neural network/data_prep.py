import numpy as np
import pandas as pd

data = pd.read_csv('student_data.csv', delimiter=',')
data = pd.get_dummies(data, columns=['rank'])

scaled_cols = ['gre', 'gpa']
for col in scaled_cols:
    mean, std = data[col].mean(), data[col].std()
    data.loc[:, col] = (data.loc[:, col] - mean) / std
np.random.seed(42)
sample = np.random.choice(data.index, size=int(data.shape[0] * 0.9))

data, test_data = data.ix[sample], data.drop(sample, axis=0)

features, targets = data.drop('admit', axis=1), data['admit']
features_test, targets_test = test_data.drop(
    'admit', axis=1), test_data['admit']
