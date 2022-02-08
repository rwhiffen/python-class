# Rich Whiffen - 2/7/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 8 - assignment 8.3 - Test for primes by hand.
#
# Ideally this would be a while loop so you could abort as soon as you
# hit a mod==0, but it works.

#Write your code below this line 👇
debug=False

def prime_checker(number):
    midpoint = round(number / 2)
    prime=True
    if debug:
        print(midpoint)
    for test in range (2,midpoint):
        if (number % test == 0):
            prime=False
        if debug:
            print(f"test: {test}")
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
