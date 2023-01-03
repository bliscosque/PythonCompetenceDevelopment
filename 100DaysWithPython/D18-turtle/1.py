from turtle import Turtle, Screen, colormode
import random
turtle=Turtle()
turtle.shape("turtle")
turtle.color("red")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#desenhando um quadrado
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

#desenhando dashed line
# for _ in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(19)
#     turtle.pendown()

#desenhando uma série de figuras geometricas
# def draw(n_sides):
#     turtle.color(random.choice(colours))
#     angle=360/n_sides
#     for _ in range(n_sides):
#         turtle.forward(100)
#         turtle.right(angle)
# for side in range(3,11):
#     draw(side)

#random walk
# directions=[0,90,180,270]
# turtle.pensize(15)
# turtle.speed("fastest")
# for _ in range(200):
#     turtle.color(random.choice(colours))
#     turtle.forward(30)
#     turtle.setheading(random.choice(directions))

#spirograph
colormode(255)
def random_color():
    color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return color
turtle.speed("fastest")
for _ in range(360//5):
    turtle.color(random_color())
    turtle.circle(100)
    turtle.setheading(turtle.heading()+5)

screen=Screen()
screen.exitonclick()