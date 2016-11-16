'''
A surface filled with one hundred medium to small sized circles.
Each circle has a different size and direction, but moves at the same
slow rate.

Display the aggregate intersections of the circles.

Implemented by Robert Hodgin <http://flight404.com>
7 April 2004
Processing v.68 <http://processing.org>

Port to Processing.py/Processing 2.0 by Ben Alkov 22 July 2014
'''
from circle import Circle


# ****************************************************************************
# INITIALIZE VARIABLES
# ****************************************************************************
Renderer = P3D
sketchX = 900  # x dimension of sketch.
sketchY = 500  # y dimension of sketch.
sketchXMid = sketchX / 2  # x midpoint of sketch.
sketchYMid = sketchY / 2  # y midpoint of sketch.
TotalCircles = 100  # Total number of circles.
Circle.BgColor = color(20)
Circle.FgColor = color(255)
circles = None  # Circle object array

# BOOLEAN FOR TESTING PURPOSES
clear = False
timer = 0
timerPause = 750
timerMax = 775


# ****************************************************************************
# SETUP FUNCTION
# ****************************************************************************
def setup():
    size(sketchX, sketchY, Renderer)
    background(Circle.BgColor)
    smooth()
    colorMode(RGB, 255)
    ellipseMode(RADIUS)
    noStroke()
    frameRate(30)
    createCircles()


# ****************************************************************************
# MAIN LOOP FUNCTION
# ****************************************************************************
def draw():
    translate(sketchXMid, sketchYMid)
    rotateX(radians(180))
    if clear:
        background(Circle.BgColor)
    dealWithTimer()
    if timer < timerPause:
        for circle in circles:
            circle.behave(circles, Circle.GravityX, Circle.GravityY)


def createCircles():
    global circles
    Circle.Gravity = random(0.005, 0.1)
    Circle.GravityX = random(-50, 50)
    Circle.GravityY = random(-50, 50)
    Circle.GravityXOffset = random(1.0, 1.24)
    Circle.MaxDistance = random(75, 150)
    Circle.InitRadius = random(100, 140)
    # Sets the initial point of rotation for the creation of the circles.
    angleOffset = random(TAU)
    circles = []
    for i in range(TotalCircles):
        xPos, yPos = initCirclePos(i, angleOffset, Circle.InitRadius)
        circles.append(Circle(i, xPos, yPos, 0, 0, TotalCircles))


def initCirclePos(index, angleOffset, initRadius):
    initAngle = index * 3.6 + angleOffset
    initTheta = (-((initAngle) * PI))/180
    # initTheta = index * (TAU * 0.01) + angleOffset
    initXVel = cos(initTheta) * initRadius
    initYVel = sin(initTheta) * initRadius
    return Circle.GravityX + initXVel, Circle.GravityY + initYVel


def dealWithTimer():
    global timer
    if timer > timerMax:
        timer = 0
        background(Circle.BgColor)
        createCircles()
    timer += 1
