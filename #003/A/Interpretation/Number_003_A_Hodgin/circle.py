from __future__ import division


class Circle(object):
    # Strength of gravitational pull.
    Gravity = 0.075
    # Collision velocity along x axis.
    xCollVel = 0
    # Collision velocity along y axis.
    yCollVel = 0
    AngleOffset = 0
    BgColor = color(0)
    FgColor = color(0)
    MaxDistance = 150

    def __init__(self, index, initRadius, TotalCircles):
        # Circle global ID.
        self.index = index
        initTheta = (self.index * (TAU * 0.01)
                     + Circle.AngleOffset + random(radians(10)))
        # Circle x, y position.
        self.x = cos(initTheta) * initRadius
        self.y = sin(initTheta) * initRadius
        # Circle radius.
        self.radius = 2
        # Current velocity along x-axis.
        self.xVel = 0
        # Current velocity along y-axis.
        self.yVel = 0
        # Storage for collisions which might happen.
        self.mightCollide = [0] * TotalCircles
        # Storage for collisions which happened.
        self.didCollide = [0] * TotalCircles
        # Storage for the distances between circles.
        self.distances = [0] * TotalCircles
        # Storage for the angle (in radians) between two connected circles.
        self.thetas = [0] * TotalCircles
        # Number of collisions in one frame.
        self.numCollisions = 0
        # Total number of collisions.
        self.numConnections = 0

    def behave(self, circles, GravityX, GravityY):
        self.move()
        self.areWeClose(circles)
        self.areWeColliding(circles)
        self.areWeConnected(circles)
        self.applyGravity(GravityX, GravityY)
        self.render(circles)
        self.resetCollisions()

    def areWeClose(self, others):
        for other in others:
            if self.index != other.index:
                if (abs(self.x - other.x) < 50
                        and abs(self.y - other.y) < 50):
                    self.mightCollide[other.index] = True
                else:
                    self.mightCollide[other.index] = False

    def areWeColliding(self, others):
        for other in others:
            if (self.mightCollide[other.index]
                    and self.index != other.index):
                self.distances[other.index] = dist(other.x, other.y,
                                                   self.x, self.y)
                if (self.distances[other.index]
                        < (self.radius + other.radius) * 1.1):
                    self.didCollide[other.index] = True
                    other.didCollide[self.index] = True
                    self.thetas[other.index] = self.findAngle(other.x, other.y)
                    Circle.xCollVel += (cos(self.thetas[other.index])
                                        * ((other.radius + self.radius) / 2.0))
                    Circle.yCollVel += (sin(self.thetas[other.index])
                                        * ((other.radius + self.radius) / 2.0))
                    self.numCollisions += 1
        if self.numCollisions > 0:
            self.xVel = -Circle.xCollVel / self.numCollisions
            self.yVel = -Circle.yCollVel / self.numCollisions
        Circle.xCollVel = 0.0
        Circle.yCollVel = 0.0

    def areWeConnected(self, others):
        for other in others:
            if (self.didCollide[other.index]
                    and other.index != self.index):
                self.distances[other.index] = dist(other.x, other.y,
                                                   self.x, self.y)
                if self.distances[other.index] < Circle.MaxDistance:
                    self.thetas[other.index] = self.findAngle(other.x, other.y)
                    Circle.xCollVel += (cos(self.thetas[other.index])
                                        * (other.radius / 8.0))
                    Circle.yCollVel += (sin(self.thetas[other.index])
                                        * (other.radius / 8.0))
                    self.numConnections += 1
                else:
                    self.didCollide[other.index] = False
                    other.didCollide[self.index] = False
        if self.numConnections > 0:
            self.xVel += (Circle.xCollVel / self.numConnections) / 4.0
            self.yVel += (Circle.yCollVel / self.numConnections) / 4.0
        Circle.xCollVel = 0.0
        Circle.yCollVel = 0.0
        self.radius = self.numConnections * 0.85 + 2

    def applyGravity(self, GravityX, GravityY):
        gravityTheta = self.findAngle(GravityX, GravityY)
        self.xVel += cos(gravityTheta) * Circle.Gravity
        self.yVel += sin(gravityTheta) * Circle.Gravity

    def move(self):
        self.x += self.xVel
        self.y += self.yVel

    def render(self, others):
        noStroke()
        self.drawMe(0, 25, 1)
        self.drawMe(10, 50, 0.5)
        self.drawMe(10, 255, 0.3)
        if self.numCollisions > 0:
            noStroke()
            self.drawMe(0, 25, 1)
            self.drawMe(0, 55, 0.85)
            self.drawMe(0, 255, 0.7)
        for other in others:
            if (self.didCollide[other.index]
                    and self.index != other.index):
                with beginShape(LINE_LOOP):
                    xdist = self.x - other.x
                    ydist = self.y - other.y
                    stroke(Circle.FgColor, 150 - self.distances[other.index] * 2.0)
                    vertex(self.x, self.y)
                    vertex(self.x - xdist * 0.25 + random(-1.0, 1.0),
                           self.y - ydist * 0.25 + random(-1.0, 1.0))
                    vertex(self.x - xdist * 0.5 + random(-3.0, 3.0),
                           self.y - ydist * 0.5 + random(-3.0, 3.0))
                    vertex(self.x - xdist * 0.75 + random(-1.0, 1.0),
                           self.y - ydist * 0.75 + random(-1.0, 1.0))
                    vertex(other.x, other.y)
                line(self.x, self.y, other.x, other.y)
        noStroke()

    def resetCollisions(self):
        self.numCollisions = 0
        self.numConnections = 0

    def drawMe(self, shade, alpha, factor):
        r = self.radius * factor
        if shade == 0:
            fill(Circle.FgColor, alpha)
        else:
            fill(Circle.FgColor + self.radius * shade, alpha)
        ellipse(self.x, self.y, r, r)

    def findAngle(self, otherX, otherY):
        return atan2(self.y - otherY, self.x - otherX) + PI
