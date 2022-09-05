import turtle
import pandas

screen = turtle.Screen()
screen.title("US States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

# extract the states
#new_item for item in list if test

guessed_states = []
while len(guessed_states) < 50:
    user_answer = screen.textinput(f"{len(guessed_states)} / 50 guessed right", prompt="Make another guess").title()
    if user_answer == "Exit":

        missing_states = [state for state in all_states if state not in guessed_states]

        new_states = pandas.DataFrame(missing_states)
        new_states.to_csv("states_to_learn_again.csv")
        break
    if user_answer in all_states:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(f"{user_answer}", align="center", font=("Courier", 12, "bold"))





