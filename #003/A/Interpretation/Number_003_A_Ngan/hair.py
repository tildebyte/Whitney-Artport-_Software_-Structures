class Hair(object):
    speedFactor = 5

    def __init__(self, regX, regY, radius, angle, parent):
        self.radius = radius
        self.initRadius = radius
        self.angle = angle
        self.initAngle = angle
        self.parent = parent
        self.regX = regX
        self.regY = regY
        self.nextX = self.parent.x + self.regX + cos(self.angle) * self.radius
        self.nextY = self.parent.y + self.regY + sin(self.angle) * self.radius
        self.x = self.nextX
        self.y = self.nextY

    def focus(self, intersectX, intersectY):
        dx = intersectX - (self.parent.x + self.regX)
        dy = intersectY - (self.parent.y + self.regY)
        self.angle = atan2(dy, dx)
        self.radius = dist(intersectX, intersectY,
                           self.parent.x + self.regX,
                           self.parent.y + self.regY)

    def revertFocus(self):
        self.angle = self.initAngle
        self.radius = self.initRadius

    def updatePos(self):
        self.nextX = self.parent.x + self.regX + cos(self.angle) * self.radius
        self.nextY = self.parent.y + self.regY + sin(self.angle) * self.radius
        dx = self.nextX - self.x
        dy = self.nextY - self.y
        if abs(dx) > 1:
            self.x += dx / Hair.speedFactor
            self.y += dy / Hair.speedFactor
        if abs(dx) > 200 or abs(dy) > 200:
            self.x = self.nextX
            self.y = self.nextY

    def render(self):
        # pass
        line(self.parent.x + self.regX, self.parent.y + self.regY,
             self.x, self.y)
