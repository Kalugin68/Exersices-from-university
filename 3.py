"""
    8.17
    author Kalugin Alexander
    email sashakalugin74@gmail.com
    version 3.11 16/12/23
    group 10701223
"""

import math

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x  # Приватное поле данных x
        self.__y = y  # Приватное поле данных y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def distance(self, other_point):
        return math.sqrt((self.__x - other_point.get_x())**2 + (self.__y - other_point.get_y())**2)

    def isNearBy(self, p1):
        return self.distance(p1) < 5

    def __str(self):
        return self.__x, self.__y

def main():
    point1_x = float(input("Enter the x coordinate for the first point: "))
    point1_y = float(input("Enter the y coordinate for the first point: "))

    point2_x = float(input("Enter the x coordinate for the second point: "))
    point2_y = float(input("Enter the y coordinate for the second point: "))

    p1 = Point(point1_x, point1_y)
    p2 = Point(point2_x, point2_y)

    print(f"The distance between the two points is",round(p1.distance(p2), 2))
    print(f"Are the points near each other?", p1.isNearBy(p2))

main()