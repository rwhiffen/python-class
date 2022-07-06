# Rich Whiffen - 3/31/2022
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

import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calc_score(cards):
    # take a list of cards and sum it
    if len(cards)==21 and sum(cards)==21:
        return 0
    if sum(cards) > 21 and 11 in cards:
        #we have an ace - take it outside
        cards.remove(11)
        cards.append(1)
    if sum(cards) > 21 and 11 in cards:
        #we have a 2nd ace - take it out again
        cards.remove(11)
        cards.append(1)
# set blank hands for each player
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card()) # the returned value isn't a list
    computer_cards.append(deal_card()) # the returned value isn't a list
