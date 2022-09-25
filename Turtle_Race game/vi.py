from turtle import Turtle ,Screen
import random
import turtle

is_race_on=False

screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet " , prompt="Which turtle will win the Race ? Enter a Color")
print(user_bet)
colors=["red","yellow","green","blue","orange","brown"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]


for i in range(0,6):
    new_turtle=Turtle(shape="snak")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[i])
    all_turtles.append(new_turtle)

# if user_bet:
#     is_race_on=True

# while is_race_on:
#      for  turtle in all_turtles:
#         if turtle.xcor()>230:
#             is_race_on=False
#             winning_color=turtle.pencolor()
#             indexs=turtle.index(winning_color)
#             if winning_color==user_bet:
#                 print(f"You've Win !The {winning_color} turtle is the winner.  index{indexs}  ")
#             else:    
#                 print(f"You've lost!  The {winning_color} turtle is the winner")
            


#         rand_distance=random.randint(0,10)
#         turtle.forward(rand_distance)









screen.exitonclick()