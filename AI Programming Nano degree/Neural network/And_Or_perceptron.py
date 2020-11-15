# And perceptron
import pandas as pd

w1 = 1
w2 = 1
b = -1

inputs = [(0, 0), (1, 0), (0, 1), (1, 1)]
correct_output = [False, False, False, True]

output = []
for inp, cor_output in zip(inputs, correct_output):
    linear_combination = w1 * inp[0] + w2 * inp[1] + b
    out = int(linear_combination > 0)
    is_correct_string = 'Yes' if out == cor_output else 'No'
    output.append([inp[0], inp[1], linear_combination, is_correct_string])

print(output)


# OR perceptron

w1 = 1
w2 = 1
b = 0.5

inputs = [(0, 0), (1, 0), (0, 1), (1, 1)]
correct_output = [False, True, True, True]

output = []
for inp, cor_output in zip(inputs, correct_output):
    linear_combination = w1 * inp[0] + w2 * inp[1] + b
    out = int(linear_combination > 0)
    is_correct_string = 'Yes' if out == cor_output else 'No'
    output.append([inp[0], inp[1], linear_combination, is_correct_string])

print(output)

# NOT perceptron

w1 = -1
w2 = -1
b = 1

inputs = [(0, 0), (1, 0), (0, 1), (1, 1)]
correct_output = [True, False, False, False]

output = []
for inp, cor_output in zip(inputs, correct_output):
    linear_combination = w1 * inp[0] + w2 * inp[1] + b
    out = int(linear_combination > 0)
    is_correct_string = 'Yes' if out == cor_output else 'No'
    output.append([inp[0], inp[1], linear_combination, is_correct_string])

print(output)
