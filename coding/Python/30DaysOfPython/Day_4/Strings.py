print('new \t 5\t25')

first_name = 'Hossein'
last_name = 'Mortazavi'
age = 35
print('my name is %s %s'%(first_name , last_name))
print('I am  %d years old'%(age))

a= 3 
b = 4

print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} ^ {b} = {a**b}')
print(f'{a} // {b} = {a//b}')

space =' '
print('Thirty' + space + 'days' +space + 'of' + space + 'Python')

company = 'Coding for All'
print(company)
print(len(company))
COMPANY = company.upper()
print(COMPANY)

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[0])
print(company.index('All'))
print(company.replace('Coding','Python'))
print(company.split())

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(companies.split(sep=','))

company = 'Coding For All'
print(company[0])
print(company[-1])
print(company[10])

abrevation = ''.join(i[0] for i in company.split())
print('abrevation is: ', abrevation)
txt ='Python For Everyone'
print('abrevation is: ', txt.split())

print(txt.find('C'))
print(txt.find('F'))
print(txt.rfind('l'))

txt = 'You cannot end a sentence with because because because is a conjunction'
print(txt.find('because'))
print(txt.rfind('because'))
slic='because because because'
print(txt[:txt.find(slic)]+txt[txt.find(slic)+len(slic):] )

company = 'Coding For All'
print('Coding' in company)
print('coding' in company)

company = '   Coding For All      ' 
print(company.strip())

txt1 = '30DaysOfPython'
txt2 = 'thirty_days_of_python'
print(txt1.isidentifier())
print(txt2.isidentifier())

libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('/ '.join([lib for lib in libs]))


print('I am enjoying this challenge.\n'+'I just wonder what is next.')
print('name \t  age \t country')
print('Hossein \t  35 \t Iran')

radius = 10
pi = 3.14
print(f'the area of a circle with radius {radius} is {radius ** 2 * pi } meter square')

num1 = 8 
num2 = 6 

print(f'{num1} + {num2} = {num1+num2}')
print(f'{num1} - {num2} = {num1-num2}')
print(f'{num1} * {num2} = {num1*num2}')
print(f'{num1} / {num2} = {num1/num2}')
print(f'{num1} // {num2} = {num1//num2}')
print(f'{num1} % {num2} = {num1%num2}')

