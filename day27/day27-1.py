# Rich Whiffen - 10/04/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 27 - TKinter guis

import tkinter

window = tkinter.Tk()
window.title("my gui window")

window.minsize(width=640, height=480)

# labels

my_label = tkinter.Label(text="I am a label", font=("Ariel", 24, "bold"))
my_label.pack(side="bottom")  # this is what pushes it to the gui

my_label["text"]= "New Text"  # these two lines do the same thing
my_label.config(text="New Text")

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

input = tkinter.Entry(width=10)
input.pack()

window.mainloop()
