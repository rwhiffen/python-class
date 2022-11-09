# Rich Whiffen - 11/9/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 33 - working with APIs
#
# simple request & response - Kanye quotes 

from tkinter import *
import requests #pip3 install requests
DEBUG = True
kayne_being_a_jackass = {} #make this a global empty

def get_quote():
    global kayne_being_a_jackass
    kanye_api = requests.get(url="https://api.kanye.rest")
    kanye_api.raise_for_status() #raise the actual excetpion
    if DEBUG:
        print(kanye_api)
    kayne_being_a_jackass = kanye_api.json()
    if DEBUG:
        print(f"kayne_being_a_jackass: {kayne_being_a_jackass}")
        print(kayne_being_a_jackass["quote"])
    canvas.itemconfig(quote_text, text=kayne_being_a_jackass["quote"])

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)
get_quote()


window.mainloop()
