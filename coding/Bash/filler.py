import pandas as pd

input = pd.read_csv('input.csv')

with open('sample_text.txt', 'r') as f:
    text = f.read()
Args = text.count('??')
for i in range(2):
    first = text.find('??')
    print(first)
    text = text[:first]+ input.iloc[i, 0] + text[first+2:]
    print(text)
    print('*'*100)



# for i in range(Args):
#     text.find('??')
# print(text)
