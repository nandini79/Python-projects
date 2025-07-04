from Coffee_Machine_menu import Menu
from Coffee_Machine_maker import CoffeeMaker
from Coffee_Machine_money import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

coffee_maker.report()
money_machine.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to have? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)