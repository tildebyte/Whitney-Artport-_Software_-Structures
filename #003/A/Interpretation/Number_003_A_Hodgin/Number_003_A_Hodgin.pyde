'''
A surface filled with one hundred medium to small sized circles.
Each circle has a different size and direction, but moves at the same
slow rate.

Display the instantaneous intersections of the circles

Implemented by Robert Hodgin <http://flight404.com>
6 April 2004
Processing v.68 <http://processing.org>

Port to Processing.py/Processing 2.0 by Ben Alkov 17 July 2014
'''
from __future__ import division

from circle import Circle


# ****************************************************************************
# INITIALIZE VARIABLES
# ****************************************************************************
Renderer = P3D
sketchX = 600  # x dimension of sketch.
sketchY = 600  # y dimension of sketch.
sketchXMid = sketchX / 2  # x midpoint of sketch.
sketchYMid = sketchY / 2  # y midpoint of sketch.
TotalCircles = 100  # Total number of circles.
GravityX = 0  # Location of gravity source.
GravityY = 0  #   '
Circle.BgColor = color(255)
Circle.FgColor = color(0)
circles = None


# ****************************************************************************
# SETUP FUNCTION
# ****************************************************************************
def setup():
    global circles
    size(sketchX, sketchY, Renderer)
    background(Circle.BgColor)
    smooth()
    colorMode(RGB, 255)
    ellipseMode(RADIUS)
    noStroke()
    frameRate(30)
    Circle.AngleOffset = random(TAU)
    initRadius = 150
    circles = [Circle(i, initRadius, TotalCircles)
               for i in range(TotalCircles)]


# ****************************************************************************
# MAIN LOOP FUNCTION
# ****************************************************************************
def draw():
    translate(sketchXMid, sketchYMid)
    rotateX(PI)
    background(Circle.BgColor)
    for circle in circles:
        circle.behave(circles, GravityX, GravityY)


def mousePressed():
    setup()
