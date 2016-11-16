from hair import Hair


class Circle(object):
    NumHairs = 30

    def __init__(self, x, y, radius, index):
        self.index = index
        self.x = x
        self.y = y
        self.radius = radius
        self.diameter = self.radius * 2
        self.radiusSquared = self.radius**2
        angleIncrement = TAU / Circle.NumHairs
        self.hairs = [Hair(cos(angleIncrement * i) * self.radius,
                           sin(angleIncrement * i) * self.radius,
                           5, angleIncrement * i + PI, self)
                      for i in range(Circle.NumHairs)]
        self.speeds = [random(2), random(2), random(2)]
        self.accels = [random(0.5) - random(0.5),
                       random(0.5) - random(0.5),
                       random(0.5) - random(0.5)]
        self.hasIntersect = False
        self.intersectX = 0
        self.intersectY = 0

    def render(self, circles):
        ellipse(self.x, self.y, self.diameter, self.diameter)
        self.move(circles)

    def move(self, circles):
        angle = sin(self.speeds[0]) - cos(self.speeds[1])
        self.speeds[0] += self.accels[0]
        self.speeds[1] += self.accels[1]
        self.speeds[2] += self.accels[2]
        if angle < 0:
            angle += TAU
        elif angle >= TAU:
            angle -= TAU
        self.x += sin(angle)
        self.y -= cos(angle)
        self.checkBounds()
        self.checkIntersect(circles)

    def checkBounds(self):
        if self.x > width:
            self.x = 0
        if self.x < 0:
            self.x = width
        if self.y > height:
            self.y = 0
        if self.y < 0:
            self.y = height

    def checkIntersect(self, circles):
        flag = False
        flag2 = False
        for circle in circles:
            if circle.index is not self.index:
                flag = self.intersect(circle)
                if not flag2:
                    flag2 = flag
        if flag2:
            self.hairFocus()
        elif self.hasIntersect:
            self.revertFocus()
        self.hasIntersect = flag2

    def hairFocus(self):
        for hair in self.hairs:
            hair.focus(self.intersectX, self.intersectY)

    def revertFocus(self):
        for hair in self.hairs:
            hair.revertFocus()

    def intersect(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        diameterSquared = dx**2 + dy**2
        diameter = sqrt(diameterSquared)
        if (diameter > self.radius + other.radius
                or diameter < abs(self.radius - other.radius)):
            return False
        angle = ((self.radiusSquared - other.radiusSquared + diameterSquared)
                 / (2 * diameter))
        hyp = sqrt(self.radiusSquared - angle**2)
        intersectX = self.x + angle * (other.x - self.x) / diameter
        intersectY = self.y + angle * (other.y - self.y) / diameter
        paX = intersectX + hyp * (other.y - self.y) / diameter
        paY = intersectY - hyp * (other.x - self.x) / diameter
        self.repel(atan2(dy, dx))
        # ellipse(paX, paY, 15, 15)
        self.intersectX = intersectX
        self.intersectY = intersectY
        return True

    def repel(self, angle):
        self.x += cos(angle) / 4
        self.y += sin(angle) / 4

    def renderHair(self):
        for hair in self.hairs:
            hair.updatePos()
            hair.render()
