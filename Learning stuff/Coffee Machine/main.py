from menu import MENU, resources

stop = False
profit = 0

def moneyCalulation():

def isenough(ingredient) :
    for stuff in ingredient:
        if ingredient[stuff] >= resources[stuff]:
            print(f"Sorry there is not enough {stuff}")
            return False
    return True

while not stop :
    choice = input("What would you like? ( espresso/latte/cappuccino ) : ").lower()
    if choice == 'off' :
        print("Thank you for using Coffee Machine")
        stop = True
    elif choice == 'report':
        for item in resources:
            print(f"{item} : {resources[item]}")
        print(f"Money : {profit}")
    else:
        drink = MENU[choice]
        # print(drink)
        if isenough(drink["ingredients"]):
