class Circle(object):
    '''A circle object'''

    def __init__(self, centerX, centerY, radius, xspeed, yspeed, index):
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius
        self.rSqr = self.radius**2
        self.index = index
        self.xspeed = xspeed
        self.yspeed = yspeed

    def update(self, circles):
        for circle in circles:
            if circle.index != self.index:
                self.intersect(circle)

    def makepoint(self):
        stroke(0)
        point(self.centerX, self.centerY)

    def move(self):
        self.centerX += self.xspeed
        self.centerY += self.yspeed
        if self.xspeed > 0 and self.centerX > width + self.radius:
            self.centerX = -self.radius
        elif self.centerX < -self.radius:
            self.centerX = width + self.radius
        if self.yspeed > 0 and self.centerY > height + self.radius:
            self.centerY = -self.radius
        elif self.centerY < -self.radius:
            self.centerY = height + self.radius

    def intersect(self, other):
        dx = self.centerX - other.centerX
        dy = self.centerY - other.centerY
        dSqr = dx**2 + dy**2
        diameter = sqrt(dSqr)
        if (diameter > self.radius + other.radius
                or diameter < abs(self.radius - other.radius)):
            return  # no solution
        a = (self.rSqr - other.rSqr + dSqr) / (2 * diameter)
        h = sqrt(self.rSqr - a**2)
        x2 = self.centerX + a * (other.centerX - self.centerX) / diameter
        y2 = self.centerY + a * (other.centerY - self.centerY) / diameter
        paX = x2 + h * (other.centerY - self.centerY) / diameter
        paY = y2 - h * (other.centerX - self.centerX) / diameter
        pbX = x2 - h * (other.centerY - self.centerY) / diameter
        pbY = y2 + h * (other.centerX - self.centerX) / diameter
        stroke(dist(paX, paY, pbX, pbY) * 4, 12)
        line(paX, paY, pbX, pbY)
