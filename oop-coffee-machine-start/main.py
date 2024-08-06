from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu=Menu()
choice = menu.get_items()
is_on=True
while is_on:
    option=menu.get_items()
    choice=input(f"What would you like? ({option}):")
    if choice=="off":
        is_on=False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_choice=menu.find_drink(choice)
        if money_machine.make_payment(drink_choice.cost) and coffee_maker.is_resource_sufficient(drink_choice):
            coffee_maker.make_coffee(drink_choice)

