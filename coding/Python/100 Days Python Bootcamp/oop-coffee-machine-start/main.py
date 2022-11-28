from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 150,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
Machine_is_on = True

def sufficent_resource(choice,item):
    if  resources[item] < MENU[choice]['ingredients'][item]:
            print('Sorry there is not enough water.')
            return False
    return True
    

while Machine_is_on :
    choice = input('What would you like? (espresso/latte/cappuccino): ​')
    if choice == 'off':
        Machine_is_on = False
    elif choice == 'report':
        print(resources['water'],'ml')
        print(resources['milk'],'ml')
        print(resources['coffee'],'gr')
        print(profit,'$')
    else:
        for item in ['water','milk','coffee']:
        
            if sufficent_resource(choice,item):
                profit += MENU[choice]['cost']
                