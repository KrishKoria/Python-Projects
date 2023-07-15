from menu import MENU, resources

stop = False
profit = 0


def money_calculation():
    print("Please insert Coins")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def is_enough(ingredient):
    for stuff in ingredient:
        if ingredient[stuff] >= resources[stuff]:
            print(f"Sorry there is not enough {stuff}")
            return False
    return True


def successful_transaction(received, price):
    if received >= price:
        change = round(received - price)
        print(f"Here is the change ${change}")
        global profit
        profit += price
        return True
    else:
        print("Sorry, that's not enough,Money refunded")
        return False


def make_coffee(name, order):
    for item in order:
        resources[item] -= order[item]
    print(f"Here is your {name}")


while not stop:
    choice = input("What would you like? ( espresso/latte/cappuccino ) : ").lower()
    if choice == 'off':
        print("Thank you for using Coffee Machine")
        stop = True
    elif choice == 'report':
        for item in resources:
            print(f"{item} : {resources[item]}")
        print(f"Money : {profit}")
    else:
        drink = MENU[choice]
        # print(drink)
        if is_enough(drink["ingredients"]):
            payment = money_calculation()
            if successful_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
