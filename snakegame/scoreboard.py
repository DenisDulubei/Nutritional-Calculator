from turtle import Turtle,Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"SCORE:{self.score}",False,align="center",font=("Courier" , 12, "normal"))
    
    def game_over(self):

        self.goto(0,0)
        self.write("GAME OVER !",False,align="center",font=("Courier" , 20, "normal"))
        
    # def play_again(self):
    #     self.screen.textinput(title="PLAY AGAIN", prompt="type y/n")
        

    def keep_the_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
    


        

