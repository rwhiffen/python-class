# Rich Whiffen - 11/3/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 31 - intermediate capstone project - flash cards
#
# part 1 make the UI
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {} #blank global dict
to_learn = {} # blank global dict
DEBUG=True

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_data_frame = pandas.read_csv("data/french_words.csv")
    words_to_learn = word_data_frame.to_dict(orient="records")
else:
    words_to_learn = word_data_frame.to_dict(orient="records")

if DEBUG:
    print(words_to_learn)

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) # stop the previous timer to start a new one

    current_card = random.choice(words_to_learn)
    if DEBUG:
        print(current_card["French"])

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    words_to_learn.remove(current_card)
    if DEBUG:
        print(len(to_learn))
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# setup window
window = Tk()
window.title("Flashy-flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#set up card canvas and front
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263, image=card_front_image)
card_title = canvas.create_text(400,158, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="WORD", font=("Ariel", 60, "bold"))


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


#prep buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1,column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1,column=0)

next_card() # this is a clever way to pre-stage the text...
            # this was the class idea, not mine :-(
window.mainloop()
