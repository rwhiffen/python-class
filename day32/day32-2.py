# Rich Whiffen - 11/9/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 32 - Monday Motivation Project
#
# Didn't clean up the extra jibberish from the datetime classroom examples

#Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "rwhiffen@gmail.com"
MY_PASSWORD = "###########"
DEBUG = True
SEND_MAIL = False  # set if you want to try and send the email

print("START: playing with datetime/dt class")
now = dt.datetime.now()
print(now)
year = now.year
print(year)
month = now.month
print(month)
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)

print("DONE: playing with datetime/dt class")


now = dt.datetime.now()
weekday = now.weekday()
if DEBUG:
    print(f"weekday: {weekday}")
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    if DEBUG:
        print(f"found quote:{quote}")
    if SEND_MAIL:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Monday Motivation\n\n{quote}"
            )
    if DEBUG:
        print(MY_EMAIL)
        print(MY_EMAIL)
        print(f"Subject:Monday Motivation\n\n{quote}")
