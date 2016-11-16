class Circle(object):
    def __init__(self, index, x, y, radius, xspeed, yspeed):
        self.index = index
        self.x = x
        self.y = y
        self.radius = radius
        self.rSqr = radius**2
        self.xspeed = xspeed
        self.yspeed = yspeed

    def update(self, circles):
        for circle in circles:
            if circle.index != self.index:
                self.intersect(circle)

    def drawSelf(self):
        stroke(102)
        noFill()
        ellipse(self.x, self.y, self.radius * 2, self.radius * 2)

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        # Wrap.
        if self.xspeed == 0 or self.yspeed == 0:
            return
        constrainedX = constrain(self.x, -self.radius, width + self.radius)
        constrainedY = constrain(self.y, -self.radius, height + self.radius)
        if constrainedX != self.x:
            if self.x < 0:
                self.x = width + self.radius
            else:
                self.x = -self.radius
        if constrainedY != self.y:
            if self.y < 0:
                self.y = height + self.radius
            else:
                self.y = -self.radius

    def intersect(self, other):
        distance = dist(self.x, self.y, other.x, other.y)
        if (distance > self.radius + other.radius
                or distance < abs(self.radius - other.radius)):
            return  # No solution.
        a = (self.rSqr - other.rSqr + distance**2) / (2 * distance)
        hyp = sqrt(self.rSqr - a**2)
        midpointX = Circle.calc2(self.x, '+', a, Circle.calc1(other.x, self.x, distance))
        midpointY = Circle.calc2(self.y, '+', a, Circle.calc1(other.y, self.y, distance))
        pointAX = Circle.calc2(midpointX, '+', hyp, Circle.calc1(other.y, self.y, distance))
        pointAY = Circle.calc2(midpointY, '-', hyp, Circle.calc1(other.x, self.x, distance))
        pointBX = Circle.calc2(midpointX, '-', hyp, Circle.calc1(other.y, self.y, distance))
        pointBY = Circle.calc2(midpointY, '+', hyp, Circle.calc1(other.x, self.x, distance))
        Circle.renderIntersect(midpointX, midpointY, pointAX, pointAY, pointBX, pointBY)

    @classmethod
    def renderIntersect(cls, midpointX, midpointY, pointAX, pointAY, pointBX, pointBY):
        stroke(0, 12)
        line(pointAX, pointAY, pointBX, pointBY)

    @classmethod
    def calc1(cls, first, second, distance):
        return (first - second) / distance

    @classmethod
    def calc2(cls, first, operation, second, function):
        if operation == '+':
            return first + second * function
        elif operation == '-':
            return first - second * function
