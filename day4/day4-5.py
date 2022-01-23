rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
# Rich Whiffen - 1/22/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 4 - assignment 4.5 - Rock Paper Scisors
# mutli-dimensional arrays/lists

hands = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
comp_choice = random.randint(0,2)

print(f"YOU: {hands[choice]}")
print(f"ME: {hands[comp_choice]}")

if choice == 0 and comp_choice == 2:
    print("\n Awwwww, you win!")
elif choice == 1 and comp_choice == 0:
    print("\n Awwwww, you win!")
elif choice == 2 and comp_choice == 1:
    print("\n Awwwww, you win!")
elif choice == comp_choice:
    print("\n Dang, its a draw")
else:
    print("Victory is Mine!")
