# Rich Whiffen - 3/8/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 10 - assignment 10.4 - Calculator
#
# workign functions and returning values - took a few days off here, again

# this code is going to morph over time as it goes forward
# the baseline changes to the provided example.
# this one loops for ever so it needs a way to break the loop.

#from replit import clear - this doesn't work outside of the class.
# I put my own clear function there that I googled.

from art import logo

def clear():
    print("\033[H\033[J", end="")

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
def calculator():
    print(logo)
    num1 = float(input("what is the first number?:"))
    should_continue=True
    for symbol in operations:
      print(symbol)
    while should_continue   :
        operation_symbol= input("pick an operation to perform:")
        num2 = float(input("what is the second number?:"))

        answer=""

        calc_operation = operations[operation_symbol]
        answer=calc_operation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
          num1 = answer
        else:
          should_continue = False
          clear()
          calculator() # first use of recursion....

calculator()
