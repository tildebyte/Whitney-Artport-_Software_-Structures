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
    circles = [Circle(random(width), random(height), random(2, 6) * 10,
                      random(-2.0, 2.0), random(-2.0, 2.0))
               for _ in range(NumCircles)]
    ellipseMode(CENTER)
    background(255)


def draw():
    background(255)
    noFill()
    stroke(0)
    for circle in circles:
        circle.move()


class Circle(object):
    def __init__(self, x, y, radius, xspeed, yspeed):
        self.x = x
        self.y = y
        self.radius = radius
        self.xspeed = xspeed
        self.yspeed = yspeed

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        # Wrap.
        if self.xspeed == 0 or self.yspeed == 0:
            return
        constrainedX = constrain(self.x, -self.radius, width + self.radius)
        constrainedY = constrain(self.y, -self.radius, height + self.radius)
        if constrainedX != self.x:
            if self.x < 0:
                self.x = width + self.radius
            else:
                self.x = -self.radius
        if constrainedY != self.y:
            if self.y < 0:
                self.y = height + self.radius
            else:
                self.y = -self.radius
        ellipse(self.x, self.y, self.radius, self.radius)
