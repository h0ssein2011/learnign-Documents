# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


print(len(it_companies))
it_companies.add('Twitter')

it_companies.update({'Snapp','Uber','Revlout','Apple'})
print(it_companies)

it_companies.remove('Snapp')
print(it_companies)

it_companies.discard('Kaggle')
print('discard works \n \n')
# it_companies.remove('Kaggle')

C=A.union(B)
print(C)
print(A.symmetric_difference(B))

del A,B
# print(A)

ages_set = set(age)
print(len(age) == len(ages_set))

sentence = 'I am a teacher and I love to inspire and teach people'
uq_words = set(sentence)
print(uq_words)
print(len(uq_words))
