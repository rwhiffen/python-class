# Rich Whiffen - 9/7/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 16 - intermediate OOP
#
# working with the coffee Machine project again
#

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
#my_items = MenuItem()
my_money = MoneyMachine()
my_coffee_machine = CoffeeMaker()

is_on = True



while is_on:
    options = my_menu.get_items()
    drink_choice = input(f"What would your like {options}?")
    if drink_choice == "off":
        is_on = False
    elif drink_choice == "report":
        my_coffee_machine.report()
        my_money.report()
    else:
        drink = my_menu.find_drink(drink_choice)
        have_ingredients = my_coffee_machine.is_resource_sufficient(drink)
        if have_ingredients:
            if my_money.make_payment(drink.cost):
                my_coffee_machine.make_coffee(drink)

            
