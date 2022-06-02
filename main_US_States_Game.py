import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_data = pandas.read_csv("50_states.csv")
all_states = state_data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    user_input = screen.textinput(title=f"{len(guessed_states)} / 50 correct answers", prompt="What's the another "
                                                                                              "state name").title()
    answer_state = user_input.capitalize()
    if answer_state == "Exit":
        # List comprehension used instead of for loop and inside if condition to create new list
        missed_states = [state for state in all_states if state not in guessed_states]
        new_file = pandas.DataFrame(missed_states)
        new_file.to_csv("states_to_learn.csv")
        break

    if answer_state.capitalize() in all_states:
        guessed_states.append(answer_state)
        match = state_data[state_data.state == answer_state]
        trtl = turtle.Turtle()
        trtl.hideturtle()
        trtl.penup()
        trtl.goto(int(match.x), int(match.y))
        trtl.write(answer_state.capitalize())


screen.exitonclick()
