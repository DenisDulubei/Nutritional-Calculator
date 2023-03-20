from turtle import Turtle

class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=40,stretch_len=0.5)
        self.lines=[]
        

    def draw_the_line(self):
            self.goto(0,0)
