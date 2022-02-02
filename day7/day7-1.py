# Rich Whiffen - 2/2/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 7 - assignment 7.1 - Hangman step 1
#Step 1
import random
debug=False
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word=""
chosen_word += random.choice(word_list)
if debug:
  print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()
if debug:
  print (guess)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
char=""

for char in chosen_word:
  if char == guess:
    print(f"{guess} right")
  else:
    print(f"{guess} wrong")
