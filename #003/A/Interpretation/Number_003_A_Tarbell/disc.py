from pxrider import PxRider
from util import checkBounds

# Disc object.
class Disc(object):
    MAXRIDERS = 40

    def __init__(self, index, x, y, velocityX, velocityY, destRadius):
        # Identifier.
        self.index = index

        # Position.
        self.x = x
        self.y = y

        # Velocity.
        self.velocityX = velocityX
        self.velocityY = velocityY

        # Radius.
        self.destRadius = destRadius
        self.radius = 0

        numRiders = int(self.destRadius / 1.62)
        if (numRiders > Disc.MAXRIDERS):
            numRiders = Disc.MAXRIDERS

        # Create pixel riders.
        self.pxRiders = [PxRider() for _ in range(Disc.MAXRIDERS)]

    def drawSelf(self):
        stroke(0x32000000)
        noFill()
        ellipse(self.x, self.y, self.radius, self.radius)

    def render(self, discs):
        # Find intersecting points with all ascending discs.
        for disc in discs:
            if disc.index > self.index:
                # Find distance to other disc.
                distance = dist(disc.x, disc.y, self.x, self.y)

                # Intersection test.
                if distance < (disc.radius + self.radius):
                    # Complete containment test.
                    if distance > abs(disc.radius - self.radius):
                        # Find solutions.
                        a = ((self.radius**2 - disc.radius**2 + distance**2) /
                             (2 * distance))
                        p2x = self.x + a * (disc.x - self.x) / distance
                        p2y = self.y + a * (disc.y - self.y) / distance
                        hypotenuse = sqrt(self.radius**2 - a**2)
                        p3ax = p2x + hypotenuse * (disc.y - self.y) / distance
                        p3ay = p2y - hypotenuse * (disc.x - self.x) / distance
                        p3bx = p2x - hypotenuse * (disc.y - self.y) / distance
                        p3by = p2y + hypotenuse * (disc.x - self.x) / distance

                        # p3a and p3B may be identical - ignore self case (for
                        #   now).
                        stroke(255)
                        point(p3ax, p3ay)
                        point(p3bx, p3by)

    def move(self):
        # Add velocity to position.
        self.x += self.velocityX
        self.y += self.velocityY
        self.x, self.y = checkBounds(self.x, self.y, self.radius)
        # Increase to destination radius.
        if self.radius < self.destRadius:
            self.radius += 0.1

    def renderPxRiders(self):
        for pxRider in self.pxRiders:
            pxRider.move(self.x, self.y, self.radius)
