# this is dictionary tutorial

# create a dictionary of state and their abbreviations
states={
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

#c reate a basic some cities
cities={
    'CA':'Sanfrnasico',
    'MI':'Detroit',
    'FL':'Jacesvoile'
}
# add some more cities
cities['NY']='New York'
cities['OR']='Portland'

#print out some cities
print('-'*10)
print('New York has:',cities['NY'])
print('MI has:',cities['MI'])

# print out some states
print('-'*10)
print('Oregon abbreviations is:',states['Oregon'])
print('Florida abbreviations is:',states['Florida'])

#do it by using state then cities dict
print('-'*10)
print('Michigan has:',cities[states['Michigan']])
print('California has:',cities[states['California']])

#print every state abbreviations
print('-'*10)
for state ,abrv in list(states.items()):
    print('{} state is abbrevated :{}'.format(state,abrv))

#print every city in state
print('-'*10)
for abrve ,city in list(cities.items()):
    print('{} has the {}'.format(abrve,city))

#now do at the same time
print('-'*10)
for state ,abrev in list(states.items()):
    print('{} state is abbrevated {}'.format(state,abrev))
    print('and has {}'.format(cities[abrev]))

print('-'*10)
#safely get an abbreviations by state that may not exist
state=states.get('Texas')

if not state:
    print('Sorry, no Texas')

# get a city with default value
city=cities.get('Tx','Does not exist')
print('city for Texas is',city)
