from tpoint import tpoint


# SandPainter object
class SandPainter(object):
    def __init__(self):
        self.p_variable = random(1.0)
        self.color = random(256)
        self.g_variable = random(0.01, 0.1)

    def render(self, x, y, otherX, otherY, passes):
        # draw painting sweeps
        tpoint(self.calc(x, otherX, self.p_variable),
               self.calc(y, otherY, self.p_variable),
               self.color, 0.11)
        maxg = 0.5
        self.g_variable += random(-0.050, 0.050)
        self.p_variable += random(-0.050, 0.050)
        self.g_variable = constrain(self.g_variable, -maxg, maxg)
        self.p_variable = constrain(self.p_variable, 0, 1.0)
        w = self.g_variable / 10.0
        for i in range(passes):
            tpoint(self.calc(x, otherX, self.p_variable + sin(i * w)),
                   self.calc(y, otherY, self.p_variable + sin(i * w)),
                   self.color, 0.1 - i / 110)
            tpoint(self.calc(x, otherX, self.p_variable - sin(i * w)),
                   self.calc(y, otherY, self.p_variable - sin(i * w)),
                   self.color, 0.1 - i / 110)

    @staticmethod
    def calc(coord, otherCoord, p):
        return otherCoord + (coord - otherCoord) * sin(p)
