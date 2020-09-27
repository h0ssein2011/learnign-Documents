age = int(input('Enter your age: '))
if age >= 18 : 
    print('You are old enough to learn to drive')
else:
    print(f'You need {18 - age} more years to learn to drive.')

my_age = int(input('Enter your age: '))
your_age = 30

if my_age > your_age:
    print('You are older than me')
elif  my_age == your_age :
    print('we are twins!')
elif my_age == your_age + 1 :
    print('you are 1 year older than me')
else :
    print(f'you are {your_age - my_age} years older than me')

a = int(input('Enter a number: '))
b = int(input('Enter a number: '))

if a > b :
    print('a is greter than b')
elif a < b :
    print('a is less than b')
else:
    print('a is equal b')

grade = int(input('Enter the grade:'))

if grade >= 80 :
    print('A')
elif grade >= 70 and grade < 89:
    print('B')
elif grade >= 60 and grade < 69:
    print('C')
elif grade >= 50 and grade < 59:
    print('D')
elif grade >= 0 and grade < 49:
    print('F')

month  = input('Enter the month').capitalize()

if month in (['September', 'October' , 'November']):
    print('the season is Autumn')

if month in (['December', 'January' , 'February']):
    print('the season is Winter')

if month in (['March', 'April' , 'May']):
    print('the season is Spring')


if month in (['June', 'July' , 'August']):
    print('the season is Summer')

fruits = ['banana', 'orange', 'mango', 'lemon']

fav_fruit = input('Enter your favourite Fruit')
if fav_fruit not in fruits :
    fruits.append(fav_fruit)
    print(fruits)


person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
    'street': 'Space street',
    'zipcode': '02210'
}
}

if person['skills'] :
    print(person['skills'][int(len(person['skills'])/2)])
    
print(person['skills'] and 'Python' in person['skills'])

if person['skills'] and len(person['skills']) == 2 and ['JavaScript' ,'React'] in person['skills'] :
    print('He is a front end developer')

if person['skills'] and len(person['skills']) == 3 and ['Node' ,'Python','MongoDB'] in person['skills']:
    print('He is a backend developer')

if person['skills'] and len(person['skills']) == 3 and ['React' ,'Node','MongoDB'] in person['skills']:
    print('He is a fullstack developer')

else :
    print('unknown title')
    
if person['is_marred'] and person['country'] == 'Finland' :
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married ' )
