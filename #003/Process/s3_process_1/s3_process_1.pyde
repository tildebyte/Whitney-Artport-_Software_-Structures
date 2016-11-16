"""
Circle Intersection
by William Ngan <contact@metaphorical.net>

Modified by Casey Reas

Port to Processing.py/Processing 2.0 by Ben Alkov 11 July 2014
"""
circleA = None
circleB = None


def setup():
    size(800, 800)
    frameRate(30)
    circleA = Circle(150, 150, 50)
    circleB = Circle(150, 150, 60)
    ellipseMode(CENTER)
    rectMode(CENTER)
    noStroke()
    smooth()


def draw():
    background(226)
    fill(153, 150)
    ellipse(circleA.x, circleA.y, circleA.radius * 2, circleA.radius * 2)
    ellipse(circleB.x, circleB.y, circleB.radius * 2, circleB.radius * 2)
    circleB.x = mouseX
    circleB.y = mouseY
    intersect(circleA, circleB)


class Circle(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.r2 = radius**2


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
    renderIntersect(midpointX, midpointY, pointAX, pointAY, pointBX, pointBY)


def renderIntersect(midpointX, midpointY, pointAX, pointAY, pointBX, pointBY):
    fill(0)
    rect(midpointX, midpointY, 5, 5)
    ellipse(pointAX, pointAY, 10, 10)
    ellipse(pointBX, pointBY, 10, 10)


def calc1(first, second, distance):
    return (first - second) / distance


def calc2(first, operation, second, function):
    if operation == '+':
        return first + second * function
    elif operation == '-':
        return first - second * function
