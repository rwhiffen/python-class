#Step 2
# Rich Whiffen - 2/2/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 7 - assignment 7.2- Hangman step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
debug=True
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display=[]

for letter in chosen_word:
  display+="-"
if debug:
  print(display)

guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.

index_pos=0
for letter in chosen_word:
    if letter == guess:
        display[index_pos]=guess
    index_pos+=1
    if debug:
      print(index_pos)
      print(display)

#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

index_pos=0
for letter in chosen_word:
  print(display[index_pos], end = '')
  index_pos+=1
print("\n")
