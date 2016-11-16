'''
A surface filled with one hundred medium to small sized circles.
Each circle has a different size and direction, but moves at the same slow
rate.

Display the instantaneous intersections of the circles

Implemented by William Ngan <http://metaphorical.net>
4 April 2004
Processing v.68 <http://processing.org>

Port to Processing.py/Processing 2.0 by Ben Alkov 29 August - 5 September 2014
'''
from circle import Circle


circles = []


def setup():
    global circles
    size(600, 600)
    frameRate(30)
    noFill()
    ellipseMode(CENTER)
    circles = [Circle(random(width), random(height), 15 + random(20), i)
               for i in range(50)]  # 50 circles


def draw():
    background(255)
    noStroke()
    fill(0)
    for circle in circles:
        circle.render(circles)
    noFill()
    stroke(255)
    for circle in circles:
        circle.renderHair()
