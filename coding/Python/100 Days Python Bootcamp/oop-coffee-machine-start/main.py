from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def get_order(Options = ['espresso','latte','cappuccino']):
    order = input('what would you like?').lower()
    if order not in Options:
        print('Please enter a valid order')
    else :
        return order  

if __name__ == "__main__" :
    # get_order = get_order()
    print(get_order())