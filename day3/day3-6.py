# Rich Whiffen - 1/19/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 3 - assignment 3.6 - Treasure Island
#
# simple flow chart if/else logig choose your adventure game.
#
# three single ticks for multi-line - handy feature remember this.
#

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
action = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" ')

#use .lower() to fix case - Note - in the instruction example they do
# action = input('asdf').lower() - so you can lower it at input time.

if (action.lower() == "right"):
    print('You fell into a hole. Game Over.') #dead end
else:
    action = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ')
    if (action.lower() == "swim"):
        print('You get attacked by an angry trout. Game Over.') #dead end
    else:
        action = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
        if (action.lower() == "red"):
            print("It's a room full of fire. Game Over.")
        elif (action.lower() == "blue"):
            print("You enter a room of beasts. Game Over.")
        elif (action.lower() == "yellow"):
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
