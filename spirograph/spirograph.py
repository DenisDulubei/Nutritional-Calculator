from turtle import Turtle,Screen
import turtle
import random
timmy=Turtle()
timmy.speed("fastest")
turtle.colormode(255)
def random_color():
    red=random.randint(0, 255)
    green=random.randint(0, 255)
    blue=random.randint(0, 255)
    colors=(red,green,blue)
    return colors
def draw_spirograph(sizeofgap):
    for i in range(int(360/sizeofgap)) :
        timmy.circle(100)
        timmy.setheading(timmy.heading()+sizeofgap)
        timmy.color(random_color())

draw_spirograph(5)
screen=Screen()
screen.exitonclick()