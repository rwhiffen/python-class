# Rich Whiffen - 2/7/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 8 - assignment 8.4 - step one in the ceasar cipher
# similar to hangman will be taking it in stages
# it re-baselines with her code every time so it won't carry
# through more than that.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
debug=True
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
  cipher_text=""
  wrap=0 #init to prevent the debug error for wrap being un-init
  for letter in text:
    position=alphabet.index(letter)
    if shift + position < 26:
      cipher_text+=alphabet[position+shift]
    else:
      wrap=(shift+position)-26
      cipher_text+=alphabet[wrap]
    if debug:
      print(f"pos {position} wrap {wrap}")
  print(f"The encoded text is {cipher_text}")
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(text, shift)
