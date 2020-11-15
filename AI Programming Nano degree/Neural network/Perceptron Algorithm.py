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
    else:
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
