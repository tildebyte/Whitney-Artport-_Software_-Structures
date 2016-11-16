class Circle(object):
    # Strength of gravitational pull.
    Gravity = 0.075
    # Collision velocity along x axis.
    xCollVel = 0
    # Collision velocity along y axis.
    yCollVel = 0
    # Maximum distance allowed for connections.
    MaxDistance = 150
    # x point of center of gravity.
    GravityX = 0
    # y point of center of gravity.
    GravityY = 0
    # Offset to warp gravitational field.
    GravityXOffset = 1.1
    # The starting radius of the creation of the circles.
    InitRadius = 130
    BgColor = color(0)
    FgColor = color(0)


    def __init__(self, index, x, y, xVel, yVel, TotalCircles):
        # Circle global ID.
        self.index = index
        # Circle x position.
        self.x = x
        # Circle y position.
        self.y = y
        # Circle radius.
        self.radius = 4
        # Current velocity along x-axis.
        self.xVel = xVel
        # Current velocity along y-axis.
        self.yVel = yVel
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
        # Late addition variable for alpha modification.
        self.alphaVar = random(35)

    def behave(self, circles, GravityX, GravityY):
        self.move()
        self.areWeClose(circles)
        self.areWeColliding(circles)
        self.areWeConnected(circles)
        self.applyGravity()
        self.render(circles, GravityX, GravityY)
        self.resetCollisions()

    def areWeClose(self, others):
        for other in others:
            if self.index != other.index:
                # if (abs(self.x - other.x) < 50
                #         and abs(self.y - other.y) < 50):
                #     self.mightCollide[other.index] = True
                # else:
                #     self.mightCollide[other.index] = False
                self.mightCollide[other.index] = (abs(self.x - other.x) < 50
                                                  and abs(self.y - other.y) < 50)

    def areWeColliding(self, others):
        for other in others:
            if (self.mightCollide[other.index]
                    and self.index != other.index):
                self.distances[other.index] = dist(self.x, self.y,
                                                   other.x, other.y)
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
                    and self.index != other.index):
                self.distances[other.index] = dist(self.x, self.y,
                                                   other.x, other.y)
                if self.distances[other.index] < Circle.MaxDistance:
                    self.thetas[other.index] = self.findAngle(other.x, other.y)
                    Circle.xCollVel += (cos(self.thetas[other.index])
                                        * (other.radius / 10.0))
                    Circle.yCollVel += (sin(self.thetas[other.index])
                                        * (other.radius / 10.0))
                    self.numConnections += 1
                else:
                    self.didCollide[other.index] = False
                    other.didCollide[self.index] = False
        if self.numConnections > 0:
            self.xVel += (Circle.xCollVel / self.numConnections) / 4.0
            self.yVel += (Circle.yCollVel / self.numConnections) / 4.0
        Circle.xCollVel = 0.0
        Circle.yCollVel = 0.0
        self.radius = self.numConnections + 1

    def applyGravity(self):
        # gravityTheta = self.findAngle(Circle.GravityX, Circle.GravityY)
        gravityTheta  = (-(self.findAngle(Circle.GravityX, Circle.GravityY) * PI))/180
        self.xVel += cos(gravityTheta) * Circle.Gravity * Circle.GravityXOffset
        self.yVel += sin(gravityTheta) * Circle.Gravity

    def move(self):
        self.x += self.xVel
        self.y += self.yVel

    def render(self, others, GravityX, GravityY):
        noFill()
        distance = dist(self.x, self.y, GravityX, GravityY)
        if distance > Circle.InitRadius:
            stroke(Circle.FgColor - distance, distance - self.alphaVar)
        else:
            stroke(distance, distance - self.alphaVar)
        point(self.x, self.y)
        noStroke()
        if self.numCollisions > 0:
            fill(Circle.FgColor, 4)
            ellipse(self.x, self.y, self.radius * 5.0, self.radius * 5.0 + 5)
            ellipse(self.x, self.y, self.radius * 3.0, self.radius * 3.0 + 5)
            if distance > Circle.InitRadius:
                fill(Circle.FgColor, 255)
            else:
                fill(Circle.BgColor, 255)
            ellipse(self.x, self.y, self.radius * 0.5, self.radius * 0.5)
        for other in others:
            if (self.didCollide[other.index]
                    and self.index != other.index):
                stroke(abs(self.thetas[other.index] - PI) * 0.0221, 5)
                line(self.x, self.y, other.x, other.y)
        noStroke()

    def resetCollisions(self):
        self.numCollisions = 0
        self.numConnections = 0

    def findAngle(self, otherX, otherY):
        # return atan2(self.y - otherY, self.x - otherX) + PI
        t = atan2(self.y - otherY, self.x - otherX)
        return 180 + (-(180 * t) / PI)
