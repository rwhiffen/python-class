# Rich Whiffen - 10/17/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 30 - Exception Handling - redo NATO alphabet code to catch non-letters


import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
