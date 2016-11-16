'''
Structure #003A

A surface filled with one hundred medium to small sized circles. Each
circle has a different size and direction, but moves at the same slow
rate.

Display the instantaneous intersections of the circles.

Implemented by Casey Reas
8 March 2004
Processing v.68

Port to Processing.py/Processing 2.0 by Ben Alkov 8 May 2014
'''
from circle import Circle


NumCircles = 100
circles = None


def setup():
    global circles
    size(800, 600)
    frameRate(30)
    circles = [Circle(i, random(width), height / NumCircles * i,
                      (random(1, 6)) * 10, random(-1.0, 1.0),
                      random(-1.0, 1.0))
               for i in range(NumCircles)]
    ellipseMode(CENTER)
    background(255)


def draw():
    background(255)
    stroke(0)
    for circle in circles:
        circle.update(circles)
        circle.move()
        circle.drawSelf()
    noFill()
