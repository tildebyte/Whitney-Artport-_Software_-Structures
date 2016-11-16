"""
Structure 3 (work in progress)

A surface filled with one hundred medium to small sized circles.
Each circle has a different size and direction, but moves at the same
slow rate.
     Display:
A. The instantaneous intersections of the circles
B. The aggregate intersections of the circles

Implemented by Casey Reas <http:#groupc.net>
Uses circle intersection code from William Ngan <http:#metaphorical.net>
Processing v.68 <http:#processing.org>

Port to Processing.py/Processing 2.0 by Ben Alkov 11 July 2014.
Note that *neither* this sketch, nor it's original Java version, renders
identically to it's original when run under Processing 2.0+.
"""
circleA = None
circleB = None


def setup():
    size(300, 300)
    frameRate(30)
    circleA = Circle(150, 150, 90)
    circleB = Circle(150, 150, 120)
    ellipseMode(CENTER)
    rectMode(CENTER)
    noStroke()


def draw():
    circleA.update()
    circleB.update()
    intersect(circleA, circleB)


class Circle(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.r2 = radius**2
        self.xspeed = random(-2.0, 2.0)

    def update(self):
        self.x += self.xspeed + random(-0.1, 0.1)
        # Wrap.
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
    stroke(0, 0, 0, 26)
    point(midpointX, midpointY)
    line(pointAX, pointAY, pointBX, pointBY)


def calc1(first, second, distance):
    return (first - second) / distance


def calc2(first, operation, second, function):
    if operation == '+':
        return first + second * function
    elif operation == '-':
        return first - second * function
