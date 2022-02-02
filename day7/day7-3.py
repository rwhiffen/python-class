#Step 3
# Rich Whiffen - 2/2/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 7 - assignment 7.3- Hangman step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while ("_" in display):

  guess = input("Guess a letter: ").lower()

#Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
      display[position] = letter

  print(display)
print("You win.")
