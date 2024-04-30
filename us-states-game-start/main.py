import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(750, 550)
screen.title("U.S. States Game")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states_list = data["state"].to_list()

guessed_states = []

user_correct = 49
game_is_on = True
while game_is_on:

    answer_state = screen.textinput(title=str(user_correct) + "/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        game_is_on = False
        missing_states = [i for i in states_list if i not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

    if answer_state in states_list:

        user_correct += 1

        states_list.remove(answer_state)

        guessed_states.append(answer_state)

        state = data[data["state"] == answer_state]

        cor_x = int(state["x"])
        cor_y = int(state["y"])

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto((cor_x, cor_y))
        t.write(answer_state, font=("Arial", 8, "normal"))

    if user_correct == 50:
        game_over = turtle.Turtle()
        game_over.hideturtle()
        game_over.penup()
        game_over.goto((-300, -50))
        game_over.color("blue")
        game_over.write("God Bless America \n        And You", font=("Arial", 50, "normal"))
        game_is_on = False

screen.exitonclick()

