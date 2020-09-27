

dog ={}
dog['name'] = 'popy'
dog['color'] =' blue'
dog['breed']  = True
dog['legs'] = 3
dog['age'] = 8

print(dog)



students = {'first_name':'Reza', 'last_name':'Abasi', 'gender':'Male', 'age':35, 'marital status':'single',
'skills':['Linux','win'], 'country':'Iraq', 'city':'Dadyut' , 'address':'21- jaadeh'}
print(students)
print(len(students))
print(students.values())
print(students['skills'])
print(type(students['skills']))
students['skills'].append(['ICT','react'])
print(students['skills'])
print(students.keys())
print(students.values())

students_ls = students.items()
print(students_ls)

del students['skills']
print(students)
del students


























