# Rich Whiffen - 10/06/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 27 - kwargs and args - tkinter graphics

# convert miles to KM

from tkinter import *


def button_clicked():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometers converter")
window.config(padx=20, pady=20)

#input form
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

#title
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equalt to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_units = Label(text="Km")
km_units.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=button_clicked)
calc_button.grid(column=1, row=2)

window.mainloop()
