# Rich Whiffen - 11/4/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 32 - make an email birthday app.
#

import smtplib

my_email = "rwhiffen@gmail.com"
password = "#############"

with smtplib.SMTP("smtp.gmail.com") as connection:

    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(
        from_addr=my_email,
        to_address="rich@whiffen.org"
        msg="Subject: Test emails!\n\n testing stuff, yay!"
        )
