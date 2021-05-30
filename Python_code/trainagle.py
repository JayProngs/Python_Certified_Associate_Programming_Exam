from math import pow


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        dist = pow(pow(self.getx() - x, 2) + pow(self.gety() - y, 2), 0.5)
        return dist

    def distance_from_point(self, point):
        x = point.__x
        y = point.__y
        return self.distance_from_xy(x, y)


class Triangle():

    def __init__(self, vertice1, vertice2, vertice3):
        self.v1 = vertice1
        self.v2 = vertice2
        self.v3 = vertice3

    def perimeter(self):
        per = self.v1.distance_from_point(self.v2) \
              + self.v2.distance_from_point(self.v3) \
              + self.v3.distance_from_point(self.v1)
        return per


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
