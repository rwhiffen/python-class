# Rich Whiffen - 9/3/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 15 - The coffee machine - have to work with lists and dicts
#          to see if the machine cane make the drink and the user
#          paid enough.
#
#
#
#

from art import logo

DEBUG=False


MENU = {
    "espresso": {
        "ingredients": {
            "water": 350,
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
    "water": 900,
    "milk": 500,
    "coffee": 100,
}

money = 0

def make_the_drink(drink_name, ingredients):
    #stub - here's where we subtract teh amount of ingredients
    if DEBUG:
        print("make_the_drink")
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def take_money():
    #stub - here is where we ask and add up money
    if DEBUG:
        print("take_money")
    print("Insert Coins")
    total = int(input("How many quarters ")) * 0.25
    print(f"$ {total}")
    total += int(input("How many dimes ")) * 0.10
    print(f"$ {total}")
    total += int(input("How many nickles ")) * 0.05
    print(f"$ {total}")
    total += int(input("How many pennies ")) * 0.01
    print(f"$ {total}")
    return(total)

def sufficient_funds(payment, cost):
    #stub did they give us enough money for the drink cost
    # will return a True/False
    if DEBUG:
        print("sufficient_funds")
    if payment >= cost:
        return(True)
    else:
        return(False)

def we_have_the_ingredients(ingredients):
    #stub - walk the supplied list of ingredients
    # ensure list if less than amount of resources remaining.
    # return True/False.
    if DEBUG:
        print("we_have_the_ingredients")
    drink_is_ok = True
    for item in ingredients:
        #loop through all - if anyne one of them is too low
        #overall drink will be set to false
        if ingredients[item] > resources[item]:
            drink_is_ok = False
            print(f"There isn't enough of {item}")
    print(f"drink_is_ok {drink_is_ok}")
    return(drink_is_ok)


def main_menu():
    # start with the main menu
    global money # change the global variable
    still_open=True
    while still_open:
        print(logo)
        for key, value in MENU.items():
            print( key, "$", MENU[key]["cost"])
        drink_choice = input("​What would you like? (espresso/latte/cappuccino): ")
        if drink_choice == "off":
            still_open = False
        elif drink_choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        else:
            drink = MENU[drink_choice]
            if we_have_the_ingredients(drink["ingredients"]):
                if DEBUG:
                    print("we_have_the_ingredients passed")
                print(f"The drink costs {drink['cost']}")
                payment = take_money()
                if sufficient_funds(payment, drink["cost"]):
                    make_the_drink(drink_choice, drink["ingredients"])
                    money += payment
            else:
                print("Sorry we don't have the ingredients to make that")


main_menu()
