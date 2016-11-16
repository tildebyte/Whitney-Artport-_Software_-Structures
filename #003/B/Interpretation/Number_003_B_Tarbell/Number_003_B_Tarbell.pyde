'''
A surface filled with one hundred medium to small sized circles. Each
circle has a different size and direction, but moves at the same slow
rate.

Display the aggregate intersections of the circles.

Implemented by J. Tarbell <http://levitated.net>
8 April 2004
Processing v.68

Port to Processing.py/Processing 2.0 by Ben Alkov 10 July 2014
'''
from disc import Disc


# Object array.
discs = None
# Number of passes for SandPainters to render.
Passes = 11
NumDiscs = 100


def setup():
    global discs
    size(700, 700)
    ellipseMode(RADIUS)
    background(0)
    # Make 100 discs, arranged linearly.
    discs = [Disc(i) for i in range(NumDiscs)]


def draw():
    if Disc.ShowStructure:
        background(0)
        # Render circles and intersections.
        for disc in discs:
            disc.drawSelf()
    # Move discs.
    for disc in discs:
        disc.move()
        disc.render(discs, Passes)


def keyReleased():
    if key == ' ':
        background(0)
        Disc.ShowStructure = not Disc.ShowStructure
