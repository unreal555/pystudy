class Point:
    def __init__(self, x_=0, y_=0):
        self.x = x_
        self.y = y_

    def set(self, x, y):
        self.x = x
        self.y = y


def swap_point(point0, point1):
    return point1, point0
