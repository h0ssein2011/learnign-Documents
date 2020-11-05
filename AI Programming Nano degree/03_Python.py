# from typing import Generator


# numbers = [
#     [34, 63, 88, 71, 29],
#     [90, 78, 51, 27, 45],
#     [63, 37, 85, 46, 22],
#     [51, 22, 34, 11, 18]
# ]


# def mean(num_list):
#     return sum(num_list) / len(num_list)


# def lm_mean(x): return sum(x)/len(x)


# averages = list(map(mean, numbers))
# averages_lambda = list(map(lm_mean, numbers))

# print(averages)
# print(averages_lambda)


# cities = ["New York City", "Los Angeles",
#           "Chicago", "Mountain View", "Denver", "Boston"]


# def is_short(name):
#     return len(name) < 10


# def is_short_lambda(x): return len(x) < 10


# short_cities = list(filter(is_short, cities))
# short_cities_lm = list(filter(is_short_lambda, cities))
# print(short_cities)
# print(short_cities_lm)


# lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

# def my_enumerate(x , start):
#     start = 0
#     for i in x:
#         start+=1
#         yield start , i

# for i, lesson in my_enumerate(lessons, 1):
#     print("Lesson {}: {}".format(i, lesson))


# def chunker(iterable , size = 4):

#     for i in range(0,len(iterable),size):
#         yield iterable[i:i+size]


# for chunk in chunker(range(25), 4):
#     print(list(chunk))


# class salesman(self):
#     def __init__(self, name,family,age,gender,email,address,wage):
#         self.name = name
#         self.family = family
#         self.age = age
#         self.gender = gender
#         self.email = email
#         self.address = address
#         self.wage =wage

#     def monthly_sales(self):
#         self.monthly_sales = sales

# class Shirt:
#     def __init__(self,color,size , style , price):
#         self.color = color
#         self.size = size
#         self.style = style
#         self.price = price

#     def change_price(self,new_price):
#         self.price = new_price

#     def discount(self , discount):
#         self.price = self.price * (1- discount)

# new_shirt = Shirt('red','S','long_sleve',15)
# Shirt.change_price(new_shirt,10)
# Shirt.discount(new_shirt,0.25)

# print(new_shirt.price)

# import argparse
# parser = argparse.ArgumentParser(description="this is a test ")
# parser.add_argument('--sum' ,default='max',nargs='+')
# parser.add_argument('--minus' ,default='max',nargs='-')

# print(parser.())

import argparse
import os
parser = argparse.ArgumentParser(description='show folders files')

parser.add_argument('Path', metavar='path', type=str, help='path to folder')


args = parser.parse_args()
input_path = args.Path

print('/n'.join(os.listdir(input_path)))

pets = ['dog', 'monkey', 'cat', 'tiger']


def ls_pop(ls):
    return ls.pop()


def ls_pop2(ls):
    ls.pop()


# print('pets before fucntion affected')
# print(pets)
print(ls_pop2(pets))
print('pets after fucntion affected')
print(pets)


bool = False


def bool_change(bool):
    if bool == True:
        bool = False
    else:
        bool = True


test = {'test': 1, 'test2': 2, 'test3': 7}
print(test.get("test3"))
print(2 in test.values())
print('test' in test)

after matching
{'German_shepherd_dog_04890.jpg': ['german shepherd dog', 'german shepherd dog', 0], 'cat_02.jpg': ['cat', 'cat', 0], 'Beagle_01141.jpg': ['beagle', 'beagle', 1], 'Golden_retriever_05223.jpg': ['golden retriever', 'golden retriever', 1], 'gecko_80.jpg': ['ecko', 'ecko', 0], 'Dalmatian_04068.jpg': ['dalmatian', 'dalmatian', 1], 'Golden_retriever_05257.jpg': ['golden retriever', 'golden retriever', 0], 'Rabbit_002.jpg': ['rabbit', 'rabbit', 0], 'Great_pyrenees_05435.jpg': ['great pyrenees', 'great pyrenees', 1], 'Miniature_schnauzer_06884.jpg': ['miniature schnauzer', 'miniature schnauzer', 1], 'Poodle_07956.jpg': ['poodle', 'poodle', 0], 'Boston_terrier_02285.jpg': ['boston terrier', 'boston terrier', 0], 'Great_pyrenees_05367.jpg': ['great pyrenees', 'great pyrenees', 0], 'Saint_bernard_08010.jpg': ['saint bernard', 'saint bernard', 1], 'Boston_terrier_02303.jpg': ['boston terrier', 'boston terrier', 0], 'Beagle_01125.jpg': ['beagle', 'beagle', 1], 'Poodle_07927.jpg': ['poodle', 'poodle', 0], 'German_shorthaired_pointer_04986.jpg': ['german shorthaired pointer', 'german shorthaired pointer', 1], 'Basenji_00963.jpg': ['basenji', 'basenji', 1], 'fox_squirrel_01.jpg': [
    'fox squirrel', 'fox squirrel', 1], 'great_horned_owl_02.jpg': ['reat horned owl', 'reat horned owl', 0], 'Great_dane_05320.jpg': ['great dane', 'great dane', 1], 'Dalmatian_04037.jpg': ['dalmatian', 'dalmatian', 1], 'Golden_retriever_05182.jpg': ['golden retriever', 'golden retriever', 0], 'Collie_03797.jpg': ['collie', 'collie', 1], 'Golden_retriever_05195.jpg': ['golden retriever', 'golden retriever', 0], 'Boxer_02426.jpg': ['boxer', 'boxer', 1], 'gecko_02.jpg': ['ecko', 'ecko', 0], 'Boston_terrier_02259.jpg': ['boston terrier', 'boston terrier', 0], 'Saint_bernard_08036.jpg': ['saint bernard', 'saint bernard', 1], 'Cocker_spaniel_03750.jpg': ['cocker spaniel', 'cocker spaniel', 1], 'German_shepherd_dog_04931.jpg': ['german shepherd dog', 'german shepherd dog', 0], 'Basset_hound_01034.jpg': ['basset hound', 'basset hound', 0], 'polar_bear_04.jpg': ['olar bear', 'olar bear', 0], 'Beagle_01170.jpg': ['beagle', 'beagle', 0], 'Dalmatian_04017.jpg': ['dalmatian', 'dalmatian', 1], 'cat_07.jpg': ['cat', 'cat', 0], 'skunk_029.jpg': ['skunk', 'skunk', 1], 'cat_01.jpg': ['cat', 'cat', 0], 'Basenji_00974.jpg': ['basenji', 'basenji', 1]}
{'German_shepherd_dog_04890.jpg': ['german shepherd dog', 'german shepherd dog', 0, 1, 0], 'cat_02.jpg': ['cat', 'cat', 0, 0, 0], 'Beagle_01141.jpg': ['beagle', 'beagle', 1, 0, 1], 'Golden_retriever_05223.jpg': ['golden retriever', 'golden retriever', 1, 0, 1], 'gecko_80.jpg': ['ecko', 'ecko', 0, 0, 0], 'Dalmatian_04068.jpg': ['dalmatian', 'dalmatian', 1, 1, 0], 'Golden_retriever_05257.jpg': ['golden retriever', 'golden retriever', 0, 0, 1], 'Rabbit_002.jpg': ['rabbit', 'rabbit', 0, 0, 0], 'Great_pyrenees_05435.jpg': ['great pyrenees', 'great pyrenees', 1, 0, 1], 'Miniature_schnauzer_06884.jpg': ['miniature schnauzer', 'miniature schnauzer', 1, 0, 1], 'Poodle_07956.jpg': ['poodle', 'poodle', 0, 1, 0], 'Boston_terrier_02285.jpg': ['boston terrier', 'boston terrier', 0, 1, 0], 'Great_pyrenees_05367.jpg': ['great pyrenees', 'great pyrenees', 0, 0, 1], 'Saint_bernard_08010.jpg': ['saint bernard', 'saint bernard', 1, 1, 0], 'Boston_terrier_02303.jpg': ['boston terrier', 'boston terrier', 0, 1, 0], 'Beagle_01125.jpg': ['beagle', 'beagle', 1, 0, 1], 'Poodle_07927.jpg': ['poodle', 'poodle', 0, 1, 0], 'German_shorthaired_pointer_04986.jpg': ['german shorthaired pointer', 'german shorthaired pointer', 1, 0, 1], 'Basenji_00963.jpg': ['basenji', 'basenji', 1, 0, 1], 'fox_squirrel_01.jpg': [
    'fox squirrel', 'fox squirrel', 1, 0, 0], 'great_horned_owl_02.jpg': ['reat horned owl', 'reat horned owl', 0, 0, 0], 'Great_dane_05320.jpg': ['great dane', 'great dane', 1, 0, 1], 'Dalmatian_04037.jpg': ['dalmatian', 'dalmatian', 1, 1, 0], 'Golden_retriever_05182.jpg': ['golden retriever', 'golden retriever', 0, 0, 1], 'Collie_03797.jpg': ['collie', 'collie', 1, 0, 1], 'Golden_retriever_05195.jpg': ['golden retriever', 'golden retriever', 0, 0, 1], 'Boxer_02426.jpg': ['boxer', 'boxer', 1, 0, 1], 'gecko_02.jpg': ['ecko', 'ecko', 0, 0, 0], 'Boston_terrier_02259.jpg': ['boston terrier', 'boston terrier', 0, 1, 0], 'Saint_bernard_08036.jpg': ['saint bernard', 'saint bernard', 1, 1, 0], 'Cocker_spaniel_03750.jpg': ['cocker spaniel', 'cocker spaniel', 1, 1, 0], 'German_shepherd_dog_04931.jpg': ['german shepherd dog', 'german shepherd dog', 0, 1, 0], 'Basset_hound_01034.jpg': ['basset hound', 'basset hound', 0, 1, 0], 'polar_bear_04.jpg': ['olar bear', 'olar bear', 0, 0, 0], 'Beagle_01170.jpg': ['beagle', 'beagle', 0, 0, 1], 'Dalmatian_04017.jpg': ['dalmatian', 'dalmatian', 1, 1, 0], 'cat_07.jpg': ['cat', 'cat', 0, 0, 0], 'skunk_029.jpg': ['skunk', 'skunk', 1, 0, 0], 'cat_01.jpg': ['cat', 'cat', 0, 0, 0], 'Basenji_00974.jpg': ['basenji', 'basenji', 1, 0, 1]}
