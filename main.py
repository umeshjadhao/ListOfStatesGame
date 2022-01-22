import turtle
import pandas

# screen = turtle.Screen()
# screen.title("U.S States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape("blank_states_img.gif")
#
# guessed_state = []
#
# data = pandas.read_csv("50_states.csv")
#
# all_states = data["state"].to_list()

# while len(guessed_state) < 50:
#
#     answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
#                                     prompt="What's another state's name").title()
#     # print(answer_state)
#     if answer_state == "Exit":
#         missing_states = []
          # Using List compresension the same logic can be written as
          #guessed_state = [state for state in all_states if state not in guessed_state]
#         for state in all_states:
#             if state not in guessed_state:
#                 missing_states.append(state)
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break
#     # If the answer_state is one of the state in all the states
#     if answer_state in all_states:
#         guessed_state.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(int(state_data.x), int(state_data.y))  # Important to change the string to int
#         t.write(state_data.state.item())

# from turtle import Turtle
# import pandas
#
# screen = turtle.Screen()
# screen.title("U.S state guessing game")
# t = Turtle()
# image = "blank_states_img.gif"
# screen.addshape(image)
# t.shape(image)
#
# data = pandas.read_csv("50_states.csv")
#
# states_list = data["state"].to_list()
#
# guessed_state = []
# while len(guessed_state) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_state)}/50 State Correct", prompt="Guess another state").title()
#     if answer_state in states_list:
#         guessed_state.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(int(state_data.x), int(state_data.y))
#         t.write(state_data.state.item())
#     if answer_state == "Exit":
#         break
#
# screen.exitonclick()

from turtle import Turtle, Screen
import pandas
screen = Screen()
screen.addshape("blank_states_img.gif")
t = Turtle()
t.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
state = data.state.to_list()
guessed_state = []
while len(guessed_state) < 51:
    answer_text = screen.textinput(title="State name", prompt="Enter state name")
    if answer_text == "Exit":
        break
    guessed_state = [st for st in state if st == answer_text]
    if answer_text in state:
        data["state"]
        guessed_state.append(answer_text)
        state_data = data[data["state"] == answer_text]
        my_turtle = Turtle()
        my_turtle.hideturtle()
        my_turtle.penup()
        my_turtle.goto(int(state_data.x), int(state_data.y))
        my_turtle.write(answer_text)
        print(state_data.state.item())


screen.mainloop()