# import colorgram
# colors=colorgram.extract("inspiration.jpg", 6)

# rgbcolors=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     newclr=(r,g,b)
#     rgbcolors.append(newclr)

colorlist=[(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130)]
import random
import turtle as turtle_module
turtle_module.colormode(255)
tim=turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

numberofdots=100
for dot_count in range(1, numberofdots+1):

    tim.dot(20,random.choice(colorlist))
    tim.forward(50)
    if dot_count %10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen=turtle_module.Screen()
screen.exitonclick()