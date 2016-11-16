from util import getFunc


class Grid(object):
    '''A grid of values, capable of drawing a vector indicating direction.'''
    MarginX = 20
    MarginY = 20
    GapX = 3
    GapY = 3
    MarginX2 = MarginX * 2
    MarginY2 = MarginY * 2
    def __init__(self, value, SketchWidth, SketchHeight):
        self.value = value
        self.fieldWidth = (SketchWidth - Grid.MarginX2) / Grid.GapX
        self.fieldHeight = (SketchHeight - Grid.MarginY2) / Grid.GapY
        self.field = [[self.value
                       for _ in range(self.fieldHeight)]
                      for _ in range(self.fieldWidth)]

    def update(self):
        for i in range(len(self.field)):
            for k in range(len(self.field[0])):
                x, y = self.getLocation(i, k)
                line(x, y,
                     x + 10 * getFunc('cos', self.field[i][k]),
                     y + 10 * getFunc('sin', self.field[i][k]))

    @staticmethod
    def getLocation(x, y):
        return x * Grid.GapX + Grid.MarginX, y * Grid.GapY + Grid.MarginY
