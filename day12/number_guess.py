# Rich Whiffen - 9/1/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 12 - number guessing game
#
# basically an exercise in scoping variables.
#
# going to steal the first 4 lines from source replit.

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_guess(user_guess, target_number, turns_left):
    if user_guess > target_number:
        print("Your guess is too high")
        return (turns_left-1)
    elif user_guess < target_number:
        print("Your guess is too low")
        return (turns_left-1)
    else:
        print("You got it!")
        return (turns_left-1)

def set_the_turns():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return(EASY_LEVEL_TURNS) # return global var value
    else:
        return(HARD_LEVEL_TURNS)

def game_loop():
    target_number = randint(1, 100)  # pick the target number
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    turns_left=set_the_turns()
    user_guess=0 #set the guess for first round, zero is not a possible ranint
    while user_guess != target_number:
        print(f"You have {turns_left} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        turns_left=check_guess(user_guess,target_number, turns_left)
        if turns_left < 1:
            print("you are out of guesses")
            print(f"The number was {target_number}")
            user_guess = target_number
        elif user_guess != target_number:
            print("Guess Again.")


game_loop()
