from util import checkBounds

# Pixel Rider object.
class PxRider(object):
    def __init__(self):
        self.theta = random(TAU)
        self.deltaV = 0.0
        self.charge = 0

    def move(self, x, y, radius):
        # Add velocity to theta.
        self.theta = (self.theta + self.deltaV + PI) % TAU - PI
        self.deltaV += random(-0.001, 0.001)

        # Apply friction brakes.
        if abs(self.deltaV) > 0.02:
            self.deltaV *= 0.9

        # Draw.
        px = x + radius * cos(self.theta)
        py = y + radius * sin(self.theta)
        screenColor = get(int(px), int(py))
        if brightness(screenColor) > 48:
            PxRider.glowpoint(px, py)
            self.charge = 164
        else:
            stroke(self.charge)
            point(px, py)
            self.charge *= 0.98

    @classmethod
    def glowpoint(cls, px, py):
        for i in range(-2, 3):
            for j in range(-2, 3):
                a = (0.8 - i**2 * 0.1) - j**2 * 0.1
                PxRider.tpoint(px + i, py + j, '#FFFFFF', a)

    @classmethod
    def tpoint(cls, x, y, myColor, opacity):
        # Place translucent point.
        screenColor = get(int(x), int(y))
        r = red(screenColor) + (red(myColor) - red(screenColor)) * opacity
        g = green(screenColor) + (green(myColor) - green(screenColor)) * opacity
        b = blue(screenColor) + (blue(myColor) - blue(screenColor)) * opacity
        stroke(color(r, g, b))
        point(x, y)
