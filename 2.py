"""
    7.6
    author Kalugin Alexander
    email sashakalugin74@gmail.com
    version 3.11 16/12/23
    group 10701223
"""
import math
class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c

    def getDiscriminant(self):
        return pow(self.__b, 2) - (4 * self.__a * self.__c)
    def getRoot1(self):
        discriminant = self.getDiscriminant()
        if discriminant > 0:
            return -1 * self.__b + math.sqrt(discriminant) / (2 * self.__a)
        else:
            return 0
    def gerRoot2(self):
        discriminant = self.getDiscriminant()
        if discriminant > 0:
            return -1 * self.__b - math.sqrt(discriminant) / (2 * self.__a)
        else:
            return 0
    def getRoot3(self):
        discriminant = self.getDiscriminant()
        if discriminant == 0:
            return -1 * self.__b / (2 * self.__a)

a = eval(input("Введите значение а:"))
b = eval(input("Введите значение b:"))
c = eval(input("Введите значение с:"))
equation = QuadraticEquation(a, b, c)
discriminant = equation.getDiscriminant()
if discriminant > 0:
    print("Корни уравнения:", equation.getRoot1(), 'и', equation.gerRoot2())
elif discriminant == 0:
    print("Корень уравнения:", equation.getRoot3())
else:
    print("Уравнение не имеет вещественных корней")