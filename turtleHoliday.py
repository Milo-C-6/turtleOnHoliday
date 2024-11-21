import turtle
import random

artist = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
artist.speed(50)

def initShape(x,y,color="none",size=-1): #creative title
    artist.setheading(0)
    artist.teleport(x,y)
    artist.pensize(0)
    artist.pendown
    if color=="none":
        color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    if size==-1:
        size = round(random.uniform(1, 2), 2)
    artist.color(color)
    return [size,color]

def present(x=artist.position()[0],y=artist.position()[1],size=-1,color="none"):
    size=initShape(x,y,color,size)

    artist.begin_fill()
    for i in range(4):
        if i%2==0:
            artist.forward(25*size[0])
        else:
            artist.forward(30*size[0])
        artist.right(90)
    artist.end_fill()
    artist.penup
    artist.forward(10.5*size[0])
    artist.color("yellow")
    artist.pendown()
    artist.begin_fill()
    artist.right(90)
    for i in range(4):
        if i%2==0:
            artist.forward(30*size[0])
        else:
            artist.forward(4*size[0])
        artist.left(90)
    artist.end_fill()
    artist.teleport(x,y-5*size[0])
    artist.left(90)
    artist.begin_fill()
    for i in range(4):
        if i%2==0:
            artist.forward(25*size[0])
        else:
            artist.forward(4*size[0])
        artist.right(90)
    artist.end_fill()

def tree(x=artist.position()[0],y=artist.position()[1]):
    
    initShape(x,y,[111, 78, 55])
    
    artist.begin_fill()
    for i in range(4):
        if i%2==0:
            artist.forward(50)
        else:
            artist.forward(220)
        artist.left(90)
    artist.end_fill()

    artist.color("green")
    artist.pencolor("darkgreen")
    artist.pensize(3)
    artist.teleport(x-200,y+20)
    for i in range(0,9):
        artist.teleport(artist.position()[0],artist.position()[1]+35)
        artist.begin_fill()
        artist.forward(450-i*50)
        artist.left(135)
        artist.forward(50)
        artist.left(45)
        artist.forward(380-i*50)
        artist.left(45)
        artist.forward(50) 
        artist.right(artist.heading())
        artist.end_fill()
        artist.forward(25)

def christmasLight(size=-1,x=artist.position()[0],y=artist.position()[1],color="none"):
    properties=initShape(x,y,color,size)

    artist.color("gray")
    artist.begin_fill()
    for i in range(4):
        artist.forward(6*properties[0])
        artist.right(90)
    artist.end_fill()
    artist.teleport(x,y-6*properties[0])
    artist.right(90)
    artist.begin_fill()
    artist.forward(1*properties[0])
    artist.color(properties[1])
    artist.circle(3*properties[0])
    artist.end_fill()
    artist.begin_fill()
    artist.left(90)
    trianglePos = artist.position()
    artist.forward(6*properties[0])
    artist.goto(trianglePos[0]+3*properties[0],trianglePos[1]-5*properties[0])
    artist.goto(trianglePos)
    artist.end_fill()
    artist.teleport(x+6*properties[0],y)

def christmasLightRows(amt):
    for i in range(amt):
        christmasLight(-1,artist.position()[0],artist.position()[1])
        if i!=amt-1:
            artist.color("black")
            for i2 in range(2):
                artist.setheading(315)
                artist.circle(10,90)

def fireplace(x=artist.position()[0],y=artist.position()[1]):
    initShape(x,y,"salmon")
    artist.begin_fill()
    for i in range(4):
        if i%2==0:
            artist.forward(300)
        else:
            artist.forward(250)

        artist.left(90)
    artist.end_fill()
    artist.backward(45)
    artist.color("saddle brown")
    artist.begin_fill()
    for i in range(4):
        if i%2==0:
            artist.forward(390)
        else:
            artist.forward(30)
        artist.right(90)
    artist.end_fill()
    artist.penup()
    artist.left(90)
    artist.forward(250)
    artist.right(90)
    artist.pendown()
    artist.begin_fill()
    for i in range(4):
        if i%2==0:
            artist.forward(390)
        else:
            artist.forward(60)
        artist.left(90)
    artist.end_fill()
'''
tree(0,-200)
for i in range(9):
    artist.teleport(-170+i*25,-110+i*35)
    christmasLightRows(9-i)
'''

fireplace()
turtle.done()