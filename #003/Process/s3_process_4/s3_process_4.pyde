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
circleA = None
circleB = None


def setup():
    size(300, 300)
    frameRate(30)
    circleA = Circle(150, 150, 60)
    circleB = Circle(150, 150, 90)
    ellipseMode(CENTER)
    rectMode(CENTER)
    noStroke()


def draw():
    background(204)
    circleA.update()
    circleB.update()
    fill(153, 150)
    noStroke()
    ellipse(circleA.x, circleA.y, circleA.radius * 2, circleA.radius * 2)
    ellipse(circleB.x, circleB.y, circleB.radius * 2, circleB.radius * 2)
    intersect(circleA, circleB)


class Circle(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.r2 = radius**2
        self.xspeed = random(-2.0, 2.0)
        self.yspeed = random(-2.0, 2.0)
        self.xdir = 1
        self.ydir = -1

    def update(self):
        self.x += self.xspeed * self.xdir
        self.y += self.yspeed * self.ydir
        # Bounce.
        constrainedX = constrain(self.x, self.radius, width - self.radius)
        constrainedY = constrain(self.y, self.radius, height - self.radius)
        if constrainedX != self.x:
            self.xdir *= -1
        if constrainedY != self.y:
            self.ydir *= -1


def intersect(circleA, circleB):
    distance = dist(circleA.x, circleA.y, circleB.x, circleB.y)
    if (distance > circleA.radius + circleB.radius
            or distance < abs(circleA.radius - circleB.radius)):
        return  # No solution.
    a = (circleA.r2 - circleB.r2 + distance**2) / (2 * distance)
    hyp = sqrt(circleA.r2 - a**2)
    midpointX = calc2(circleA.x, '+', a, calc1(circleB.x, circleA.x, distance))
    midpointY = calc2(circleA.y, '+', a, calc1(circleB.y, circleA.y, distance))
    pointAX = calc2(midpointX, '+', hyp, calc1(circleB.y, circleA.y, distance))
    pointAY = calc2(midpointY, '-', hyp, calc1(circleB.x, circleA.x, distance))
    pointBX = calc2(midpointX, '-', hyp, calc1(circleB.y, circleA.y, distance))
    pointBY = calc2(midpointY, '+', hyp, calc1(circleB.x, circleA.x, distance))
    render(midpointX, midpointY, pointAX, pointAY, pointBX, pointBY)


def render(midpointX, midpointY, pointAX, pointAY, pointBX, pointBY):
    stroke(0)
    point(midpointX, midpointY)
    line(pointAX, pointAY, pointBX, pointBY)

def calc1(first, second, distance):
    return (first - second) / distance


def calc2(first, operation, second, function):
    if operation == '+':
        return first + second * function
    elif operation == '-':
        return first - second * function
