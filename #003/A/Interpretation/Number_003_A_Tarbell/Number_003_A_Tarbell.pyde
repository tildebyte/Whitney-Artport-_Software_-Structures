'''
A surface filled with one hundred medium to small sized circles. Each
circle has a different size and direction, but moves at the same slow
rate.

Display the instantaneous intersections of the circles.

Implemented by J. Tarbell <http://levitated.net>
8 April 2004
Processing v.68

Port to Processing.py/Processing 2.0 by Ben Alkov 16 June 2014
'''
from disc import Disc


# Object array.
discs = []
num = 100


# Initialization.
def setup():
    size(500, 500)
    colorMode(RGB, 255)
    ellipseMode(RADIUS)
    background(0)
    frameRate(30)

    # Make some discs.
    # Arrange in anti - collapsing circle.
    for i in range(num):
        fx = 0.4 * width * cos(TAU * i / num)
        fy = 0.4 * width * sin(TAU * i / num)
        x = random(width / 2) + fx
        y = random(width / 2) + fy
        r = 5 + random(45)
        bt = 1
        if random(100) < 50:
            bt = -1
        discs.append(Disc(i, x, y, bt * fx / 1000.0, bt * fy / 1000.0, r))


# Main.
def draw():
    background(0)

    # Move discs.
    for disc in discs:
        disc.move()
        disc.drawSelf()
        disc.render(discs)
        disc.renderPxRiders()
