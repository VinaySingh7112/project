from turtle import Turtle
ALIGN="center"
FONT=("Courier",24,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        # with open("data.txt") as data:
        #     self.score=int(data.read())
        self.goto(0,270)
        self.penup()
        self.color("white")
        
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGN,font=FONT)
        with open("data.txt",mode="w") as data:
            data.write(f"{self.score}")

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGN,font=FONT)
        

   
    
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()