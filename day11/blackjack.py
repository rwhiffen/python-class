# Rich Whiffen - 3/31/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 11 - blackjack game
#
# making this game: http://blackjack-final.appbrewery.repl.run
#
# lots of crap at work - haven't been doing as much of this as I would
# have liked :-(
#
# for the first version I'll use her hint for the list of cards
# but I think if we want to be able to deal multiple hands we'll needs
# a list that has all 52 elements and then subtract elements that have been
# dealt.

#     Picking back up in July - 7/6/2022 office move is over
#     have some free time back.
from os import system, name
from time import sleep
import random
from art import logo

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calc_score(cards):
    # take a list of cards and sum it
    if len(cards)==2 and sum(cards)==21:
        return 0 # someone has blackjack
    if sum(cards) > 21 and 11 in cards:
        #we have an ace - take it outside
        cards.remove(11)
        cards.append(1)
    if sum(cards) > 21 and 11 in cards:
        #we have a 2nd ace - take it out again (is this even possible?)
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_hands(user_score, computer_score):
    if computer_score == 0:
        return("    The computer wins with a blackjack!")
    elif user_score == 0:
        return("    You win with a blackjack!")
    elif user_score > 21:
            return("    You busted! You Lose ")
    elif computer_score > 21:
            return("    Dealer Busts! You Win ")
    elif user_score > computer_score:
        return("    You win ")
    elif user_score < computer_score:
        return("    The computer wins ")
    else:
        return("    Its a draw")


def deal_hand():
    # set blank hands for each player
    user_cards = []
    computer_cards = []
    is_player_done=False #logic control for the player hit/stand loop
    is_computer_done=False # logic control for the computer hit/stand loop

    for _ in range(2):
        user_cards.append(deal_card()) # the returned value isn't a list
        computer_cards.append(deal_card()) # the returned value isn't a list

    while not is_player_done:
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)

        print(f"   Your cards: {user_cards}, current count: {user_score}")
        print(f"   Computers shown card: {computer_cards[0]} ")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_player_done=True
            is_computer_done=True #if any of these three are true the game is over
        else:
            hit_me = input("Type y to hit, type n to stand: ").lower()
            if hit_me == "y":
                user_cards.append(deal_card())
            else:
                is_player_done=True

    # computer's return
    while not is_computer_done:
        print(f"   Computers cards: {computer_cards} ")
        if computer_score > 16:
            is_computer_done = True # it's at 17
        else:
            computer_cards.append(deal_card())
            computer_score = calc_score(computer_cards)

    print(f"   Your cards: {user_cards}, count: {user_score}")
    print(f"   Computers cards: {computer_cards},  count: {computer_score}")
    print(compare_hands(user_score, computer_score))

print(logo)
deal_hand() #go right into the first hand - then drop out to while loop
while input("Do you want to play another hand of blackjack? (type y or n):").lower() == "y":
    sleep(1)
    clear()
    deal_hand()
