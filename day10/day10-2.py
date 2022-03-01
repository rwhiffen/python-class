# Rich Whiffen - 2/26/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 10 - assignment 10.1 - Student grades
# workign functions and returning values - took a few days off here...

# cleverly she has us re-use the leap year code but
# change it to return T/F instead of texting the string

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  # zero reference the month to match the array
  month-=1
  if month == 1 and is_leap(year):
    return month_days[month] + 1
  else:
    return month_days[month]

#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
