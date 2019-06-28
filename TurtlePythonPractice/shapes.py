from turtle import *

color("blue", "red")

def star():
    for i in range(5):
        forward(100)
        right(144)



def EquTriangle(): 
    forward(100) # draw base
    left(120)
    forward(100)
    left(120)
    forward(100)

def Square():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)

def pentagon():
    for i in range(5):
        forward(100)
        right(72)

def hexagon():
    for i in range(6):
        forward(100)
        right(60)

def octagon():
    for i in range(8):
        forward(100)
        right(45)

def circles():
    circle(100)
    color('blue')

def allshapes():
    star()
    EquTriangle()
    Square()
    pentagon()
    hexagon()
    octagon()
    circles()
    







 

    