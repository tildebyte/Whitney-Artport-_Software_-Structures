# Draw a (tiny) translucent square.
def tpoint(x, y, sandColor, opacity):
    noStroke()
    fill(sandColor, opacity * 255)
    rect(x, y, 1, 1)
