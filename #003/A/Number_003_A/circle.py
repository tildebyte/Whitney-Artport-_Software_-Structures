class Circle(object):
    '''A circle object'''

    def __init__(self, index, x, y, radius, xspeed, yspeed):
        self.index = index
        self.x = x
        self.y = y
        self.radius = radius
        self.rSqr = self.radius**2
        self.xspeed = xspeed
        self.yspeed = yspeed

    def update(self, circles):
        for circle in circles:
            if circle.index != self.index:
                self.intersect(circle)

    def drawSelf(self):
        stroke(0)
        point(self.x, self.y)

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.xspeed > 0 and self.x > width + self.radius:
            self.x = -self.radius
        elif self.x < -self.radius:
            self.x = width + self.radius
        if self.yspeed > 0 and self.y > height + self.radius:
            self.y = -self.radius
        elif self.y < -self.radius:
            self.y = height + self.radius

    def intersect(self, other):
        distance = dist(self.x, self.y, other.x, other.y)
        if (distance > self.radius + other.radius
                or distance < abs(self.radius - other.radius)):
            return  # No solution.
        a = (self.rSqr - other.rSqr + distance**2) / (2 * distance)
        hyp = sqrt(self.rSqr - a**2)
        midpointX = Circle.calc2(self.x, '+', a,
                                 Circle.calc1(other.x, self.x, distance))
        midpointY = Circle.calc2(self.y, '+', a,
                                 Circle.calc1(other.y, self.y, distance))
        pointAX = Circle.calc2(midpointX, '+', hyp,
                               Circle.calc1(other.y, self.y, distance))
        pointAY = Circle.calc2(midpointY, '-', hyp,
                               Circle.calc1(other.x, self.x, distance))
        pointBX = Circle.calc2(midpointX, '-', hyp,
                               Circle.calc1(other.y, self.y, distance))
        pointBY = Circle.calc2(midpointY, '+', hyp,
                               Circle.calc1(other.x, self.x, distance))
        Circle.renderIntersect(pointAX, pointAY, pointBX, pointBY)

    @classmethod
    def renderIntersect(cls, pointAX, pointAY, pointBX, pointBY):
        stroke(255 - dist(pointAX, pointAY, pointBX, pointBY) * 4)
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
