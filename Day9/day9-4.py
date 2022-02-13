# Rich Whiffen - 2/12/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 8 - assignment 9.4 - blind auction

from replit import clear #this only works in the class simlulator I think
#HINT: You can call clear() to clear the output in the console.
from art import logo

debug=False

print(logo)

all_bids={}
def take_bid(new_name, new_bid):
  all_bids[new_name]=new_bid

more_names=True

while more_names:
  name=input("What is your name?")
  bid=int(input("What is your bid: $"))
  take_bid(name, bid)
  ask_more=input("Any more bidders (yes/no)?")
  if ask_more.lower() == "no":
    more_names=False
  clear()

if debug:
  print(all_bids)

max_bid=0
max_bidder=""
for key in all_bids:
  if debug:
    print(key)
    print(all_bids[key])

  if all_bids[key] > max_bid:
    max_bid=all_bids[key]
    max_bidder=key
print(f"The max bid was ${max_bid} by {max_bidder}")
