# Rich Whiffen - 9/27/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 26 - spell out a word in nato alphabet
#
# changed my variable names to match her code so i can follow along
# with the video

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
#turns out iterrows is the equiv of .items() in pandas
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
