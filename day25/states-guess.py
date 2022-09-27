# Rich Whiffen - 9/26/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 25 - working with csv, data frames and pandas
#
# guess all 50 states game
# the class provided a lot of the template code and data here.

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
if len(guessed_states) == 50:
    print("You got them all!")
else:
    score = 50 - len(guessed_states)
    print(f"You missed {score}")
    for missed in missing_states:
        print(missed)   
