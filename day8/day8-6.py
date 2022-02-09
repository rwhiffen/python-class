# Rich Whiffen - 2/8/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 8 - assignment 8.6 - step six in the ceasar cipher
# similar to hangman will be taking it in stages
# it re-baselines with her code every time so it won't carry
# through more than that.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(input_text, shift_amount, cipher_direction):

  output_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for letter in input_text:
    position = alphabet.index(letter)

    new_position = position + shift_amount
    output_text += alphabet[new_position]
  print(f"The {cipher_direction}ed text is {output_text}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(text, shift, direction)
