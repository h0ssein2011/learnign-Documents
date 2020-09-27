my_tuple = ()
brothers  =('Hassan','Mohamad')
sisters =('Akram','Maryam','Mahnaz')

siblings = brothers + sisters

print(len(siblings))
siblings = list(siblings)
family = ['Ali','Bahar'] + siblings

print(family)

parents ,siblings = family[:2] ,family[2:]
print(parents)
print(siblings)

fruits =('apple','banana' , 'peach' )
vegs = ('shalgham','carot')
animal_prods = ('meat','milk')

food_stuff_tp = fruits + vegs + animal_prods
food_stuff_tp = list(food_stuff_tp)

print(food_stuff_tp)
print(food_stuff_tp[4:])
new_ls = food_stuff_tp[:3] +food_stuff_tp[-3:]
print(new_ls)

del food_stuff_tp
'apple' in new_ls

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Is Estonia a nordic country?: ','Estonia' in nordic_countries  )
print('Is Iceland a nordic country?: ','Iceland' in nordic_countries  )












