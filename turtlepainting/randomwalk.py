from turtle import Turtle, Screen
import turtle as t
import random
timmy=Turtle()
#thicknes=[1,5,10,15,20,25,30,35,40,45]
t.colormode(255)

timmy.pensize(5)
movement=[0,90,180,270]

def random_color():
    red=random.randint(0, 255)
    green=random.randint(0, 255)
    blue=random.randint(0, 255)
    colors=(red,green,blue)
    return colors
while True:
    timmy.forward(30)
    timmy.setheading(random.choice(movement))
    #timmy.pensize(random.choice(thicknes))
    timmy.color(random_color())





    






