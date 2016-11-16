"""
Structure 3 (work in progress)

A surface filled with one hundred medium to small sized circles.
Each circle has a different size and direction, but moves at the same
slow rate.
Display:
A. The instantaneous intersections of the circles
B. The aggregate intersections of the circles

Implemented by Casey Reas <http://groupc.net>
Uses circle intersection code from William Ngan <http://metaphorical.net>
Processing v.68 <http://processing.org>

Port to Processing.py/Processing 2.0 by Ben Alkov 11 July 2014.
"""
from circle import Circle

NumCircles = 100
circles = None


def setup():
    size(640, 480)
    circles = [Circle(i, random(width), random(height), random(2, 6) * 10,
                      random(-1.25, 1.25), random(-1.25, 1.25))
               for i in range(NumCircles)]
    ellipseMode(CENTER)
    background(255)


def draw():
    background(255)
    for circle in circles:
        circle.update(circles)
        circle.move()
