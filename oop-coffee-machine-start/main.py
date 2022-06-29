from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
cost = 0
while is_on:
    options = menu.get_items()
    choice = input(f'Which drink do you want to get : {options}')
    if choice == "off":
        is_on = False
        break
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        print(f"cost: {menu.find_drink(choice).cost}")
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    next = input("Do you want something other? ('y' or 'n')")
    if next == 'n':
        break





