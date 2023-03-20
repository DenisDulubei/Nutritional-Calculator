from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.rscore=0
        self.lscore=0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,190)
        self.write(self.lscore,False,align="center",font=("Courier",80,"bold"))
        self.goto(100,190)
        self.write(self.rscore,False,align="center",font=("Courier",80,"bold"))
    def point_left(self):
        self.lscore+=1
        self.update_scoreboard()
    def point_right(self):
        self.rscore+=1
        self.update_scoreboard()
    
        
        
    