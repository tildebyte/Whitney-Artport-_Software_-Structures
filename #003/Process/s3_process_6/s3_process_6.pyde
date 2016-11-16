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
NumCircles = 100
circles = None


def setup():
    size(640, 480)
    circles = [Circle(random(width), random(height), random(2, 6) * 10)
               for _ in range(NumCircles)]
    ellipseMode(CENTER)
    background(255)


def draw():
    noFill()
    stroke(0)
    for circle in circles:
        circle.render()
    # Processing 2.x draws staic shapes VERY poorly when looping. Try
    #   commenting this out...
    noLoop()

class Circle(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def render(self):
        ellipse(self.x, self.y, self.radius, self.radius)
