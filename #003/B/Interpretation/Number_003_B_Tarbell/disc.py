from sandpainter import SandPainter
from tpoint import tpoint


# Disc object.
class Disc(object):
    # SandPainters.
    NumSands = 1
    # Display flag.
    ShowStructure = False

    def __init__(self, index):
        self.index = index
        self.x = random(width)
        self.y = random(height)
        self.velocityX = random(-1.0, 1.0)
        self.destRadius = 20 + random(20)
        self.radius = 1.0
        # Create sand painters.
        self.sandpainters = [SandPainter() for _ in range(Disc.NumSands)]

    def drawSelf(self):
        stroke(64)
        noFill()
        ellipse(self.x, self.y, self.radius, self.radius)

    def render(self, others, passes):
        # Find intersecting points with all ascending discs.
        for disc in others:
            if disc.index > self.index:
                # Find distance to other disc.
                distance = dist(disc.x, disc.y, self.x, self.y)
                # intersection test
                if distance < (disc.radius + self.radius):
                    # complete containment test
                    if distance > abs(disc.radius - self.radius):
                        # find circle intersection solutions
                        a = ((self.radius**2 - disc.radius**2 + distance**2) /
                             (2 * distance))
                        p2x = self.x + a * (disc.x - self.x) / distance
                        p2y = self.y + a * (disc.y - self.y) / distance
                        hypotenuse = sqrt(self.radius * self.radius - a * a)
                        p3ax = p2x + hypotenuse * (disc.y - self.y) / distance
                        p3ay = p2y - hypotenuse * (disc.x - self.x) / distance
                        p3bx = p2x - hypotenuse * (disc.y - self.y) / distance
                        p3by = p2y + hypotenuse * (disc.x - self.x) / distance
                        if Disc.ShowStructure:
                            stroke(255)
                            point(p3ax, p3ay)
                            point(p3bx, p3by)
                        else:
                            # `p3a` and `p3b` may be identical - ignore this
                            #       case (for now).
                            tpoint((p3ax - 1), p3ay, 255, 0.21)
                            tpoint((p3ax + 1), p3ay, 0, 0.21)
                            tpoint((p3bx - 1), p3by, 255, 0.21)
                            tpoint((p3bx + 1), p3by, 0, 0.21)
                        # Draw SandPainters.
                        for sandpainter in self.sandpainters:
                            sandpainter.render(p3ax, p3ay, p3bx, p3by, passes)

    def move(self):
        # Move radius towards destination radius.
        if self.radius < self.destRadius:
            self.radius += 0.02

        # Add velocity to position.
        self.x += self.velocityX
        self.boundsCheck()

    def boundsCheck(self):
        xIncrement = width + self.radius * 2
        yIncrement = height + self.radius * 2
        constrainedX = constrain(self.x, 0 - self.radius, width + self.radius)
        constrainedY = constrain(self.y, 0 - self.radius, height + self.radius)
        prevx = self.x
        prevy = self.y
        if constrainedX != prevx:
            if prevx < 0:
                self.x += xIncrement
            else:
                self.x -= xIncrement
            self.y = random(height)
        if constrainedY != prevy:
            if prevy < 0:
                self.y += yIncrement
            else:
                self.y -= yIncrement
            self.x = random(width)
