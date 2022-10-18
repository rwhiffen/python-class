# Rich Whiffen - 10/17/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 30 - Exception Handling

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("file was closed")
    raise TypeError("This is an error that I made up, not a real error")

#BMI Example

height = float(input("Height in meters: "))
weight = int(input("Weight in kilos: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
