from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f'​What would you like? {menu.get_items()}')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_machine.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
           




