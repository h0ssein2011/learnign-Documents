from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 150,
            "coffee": 18
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

def sufficent_resource(choice):
    for item in ['water','milk','coffee']:
        if  resources[item] < MENU[choice]['ingredients'][item]:
                print(f'Sorry there is not enough {item}.')
                return False
    return True

def get_coins():
    input('Please insert coins')
    total = int(input('How many quaters?')) * 0.25  
    total += int(input('How many dimes?')) * 0.1   
    total += int(input('How many nickle?')) * 0.05   
    total += int(input('How many Pennies?'))  * 0.01
    return total 

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
        if sufficent_resource(choice):
            inserted_coins = get_coins()
            print(inserted_coins)
            if MENU[choice]['cost'] <= inserted_coins:
                profit += MENU[choice]['cost']
                change = inserted_coins - MENU[choice]['cost']
                if change > 0 :
                    print(f'Here is the ${change} in change')
                for item in ['water','milk','coffee']:
                    resources[item] -= MENU[choice]['ingredients'][item]

            print(f'Here is your {choice}. Enjoy!') 


        else:
            print("Sorry that's not enough money. Money refunded")
        


                