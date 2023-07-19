from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink = Menu()
maker = CoffeeMaker()
money = MoneyMachine()
stop = False
while not stop:
    choice = input("What would you like? (espresso/latte/cappuccino/) : ").lower()
    options = drink.get_items()
    if choice == 'off':
        print("Thank you for using Coffee Machine")
        stop = True
    elif choice == 'report':
        maker.report()
        money.report()
    else:
        item = drink.find_drink(choice)
        if maker.is_resource_sufficient(item):
            if money.make_payment(item.cost):
                maker.make_coffee(item)
