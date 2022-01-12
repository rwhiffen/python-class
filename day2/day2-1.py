# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# Rich Whiffen - 1/11/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 2 - assignment 2.1
# this seems clumsy - I suspect there's some easier ways
# to do this but I'm playing along with what
# we've been taught so far.
whole_number_string = str(two_digit_number)
first_num = int(whole_number_string[0])
second_num = int(whole_number_string[1])
digit_sum = first_num + second_num
#print (str(first_num) + " + " + str(second_num) + " = " + str(digit_sum))
print (str(digit_sum))
