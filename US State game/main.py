import turtle
import pandas 

screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]



while len(guessed_states)<50:
    
    answer_states=screen.textinput(title=f"{len(guessed_states)}/50 States correct",prompt="What is another state's name?").title()

    if answer_states=="Exit":
        missing_state=[state for state in all_states if state not in guessed_states ]
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learen.csv")        
        break
    

    if answer_states in all_states:
        guessed_states.append(answer_states)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_states]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_states)



