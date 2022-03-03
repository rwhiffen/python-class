# Rich Whiffen - 3/1/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 10 - assignment 10.3 - Calculator
#
# workign functions and returning values - took a few days off here...

# this code is going to morph over time as it goes forward
# the baseline changes to the provided example


from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

num1 = int(input("what is the first number?:"))


for symbol in operations:
  print(symbol)

operation_symbol= input("pick an operation to perform:")
num2 = int(input("what is the second number?:"))

answer=""

calc_operation = operations[operation_symbol]
answer=calc_operation(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
