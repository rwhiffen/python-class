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

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money=0

def make_the_drink():
    #stub - here's where we subtract teh amount of ingredients

def take_money():
    #stub - here is where we ask and add up money

def sufficent_funds():
    #stub did they give us enough money for the drink cost
    # will return a True/False

def main_menu():
    # start with the main menu
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
            if is_resource_sufficient(drink["ingredients"]):
                payment = take_money()
                if sufficient_funds(payment, drink["cost"]):
                    make_the_drink(choice, drink["ingredients"])


main_menu()
