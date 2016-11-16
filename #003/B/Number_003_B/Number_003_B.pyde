'''
Structure #003B

A surface filled with one hundred medium to small sized circles. Each
circle has a different size and direction, but moves at the same slow
rate.

Display the aggregate intersections of the circles

Implemented by Casey Reas
8 March 2004
Processing v.68

Port to Processing.py/Processing 2.0 by Ben Alkov 16 June 2014
'''
from circle import Circle


NumCircles = 100
circles = None


def setup():
    global circles
    size(800, 600)
    circles = [Circle(random(width), height / NumCircles * i,
                      (random(2, 6)) * 10, random(-0.25, 0.25),
                      random(-0.25, 0.25), i) for i in range(NumCircles)]
    strokeWeight(0.5)
    ellipseMode(CENTER)
    background(255)


def draw():
    stroke(0, 10)
    for circle in circles:
        circle.update(circles)
        circle.move()
