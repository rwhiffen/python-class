# Rich Whiffen - 9/2/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 14 - number guessing game
#
# working with lists and scopes.
#
#

import random
from random import randint
from art import logo, vs
from game_data import data

DEBUG=True

def get_account():
    #start out by just returning an int to get the logic working
    # then I'll change it to the data structure.
    temp_stub = randint(1, 100)
    return(temp_stub)

def get_answer(user_guess, account_a, account_b):
    #had to steal this logic - my attempt was way worse
    # this was clever - return the == logic of guess == right-answer
    # if they're right it'll return true, if not it returns false, making
    # the if loop on win or loose super simple.
    if account_a > account_b:
        return user_guess == "a"
    else:
        return user_guess == "b"

def game_loop():
    print(logo)
    score=0 # starting counter
    still_alive=True
    account_b = get_account() # Prep the loop with a previous value.
    #this way the loop works the same way first time or later time...

    while still_alive:
        account_a = account_b #shift previous value to account_a
        account_b = get_account() # get a new random account_b to use.
        if DEBUG:
            print(f"A {account_a} B {account_b}")
        user_guess=input("who has more followers:  A {place_holder) or B {place_holder}").lower()
        are_they_right=get_answer(user_guess, account_a, account_b) #this will need to be the actual counts later not my randints

        if are_they_right:
            score += 1
            print(f"you're right! your score is {score}")
        else:
            still_alive = False
            print(f"Nope! final score is {score}")

game_loop()
