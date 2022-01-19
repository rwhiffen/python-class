# Rich Whiffen - 1/18/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 3 - assignment 3.5 - Love Calculator

first_digit = 0
second_digit = 0
lower_name1 = name1.lower()
lower_name2 = name2.lower()

#Count "t"
first_digit += lower_name1.count('t')
first_digit += lower_name2.count('t')

#Count "r"
first_digit += lower_name1.count('r')
first_digit += lower_name2.count('r')

#Count "u"
first_digit += lower_name1.count('u')
first_digit += lower_name2.count('u')

#Count "e"
first_digit += lower_name1.count('e')
first_digit += lower_name2.count('e')

#testing/debuggin
#print(f"lower_name1 - {lower_name1}")
#print(f"first_digit - {first_digit}")


#Count "L"
second_digit += lower_name1.count('l')
second_digit += lower_name2.count('l')

#Count "O"
second_digit += lower_name1.count('o')
second_digit += lower_name2.count('o')

#Count "V"
second_digit += lower_name1.count('v')
second_digit += lower_name2.count('v')

#Count "E"
second_digit += lower_name1.count('e')
second_digit += lower_name2.count('e')

#testing/debuging early on
#print(f"Your score is {first_digit}{second_digit}.")

#do a full concat so we can do if/else logic easier)
score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >=40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
     print(f"Your score is {score}.")
