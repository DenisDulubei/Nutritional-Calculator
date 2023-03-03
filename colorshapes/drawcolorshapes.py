from turtle import Turtle, Screen
import turtle
import random
timmy=Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
sides=3

while sides<10:
    
    for i in range(sides):
        angle=360/sides
        timmy.forward(100)
        timmy.right(angle)
    timmy.pensize(sides)
    timmy.color(random.choice(colors))
    sides+=1


screen=Screen()
screen.exitonclick()
