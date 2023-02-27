class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print("x est egal à :", self.x, "et y est egal à :", self.y)

    def afficherX(self):
        print("x = ", self.x)

    def afficherY(self):
        print("y = ", self.y)

    def changerX(self):
        self.x = 20

    def changerY(self):
        self.y = 25


points = Point(10, 15)
points.afficherLesPoints()
points.changerX()
points.changerY()
points.afficherX()
points.afficherY()
