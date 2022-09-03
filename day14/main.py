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

DEBUG=False

def format_data(account):
  #make the string that gets printed - I had this in the main game_loop
  #but I like the final solutions version better, so copied it.

  name = account["name"]
  description = account["description"]
  country = account["country"]
  if DEBUG:
       print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"


def get_account():
    #start out by just returning an int to get the logic working
    # then I'll change it to the data structure.
    #temp_stub = randint(1, 100)

    #Honestly didn't get this - had to look at the solution.
    return random.choice(data)


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
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        user_guess=input("who has more followers:  A  or B ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        are_they_right=get_answer(user_guess, a_follower_count, b_follower_count)

        if are_they_right:
            score += 1
            print(f"you're right! your score is {score}")
        else:
            still_alive = False
            print(f"Nope! final score is {score}")

keep_playing=True
while keep_playing:
    game_loop()
    yes_no=input("Play again (y/n)?").lower()
    if yes_no == "n":
        keep_playing=False
        print("K-thx-bye!")
