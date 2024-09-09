import math

class Vector:
    def __init__(self, x, y):
        self.__x = x  # privat attribut
        self.__y = y  # privat attribut

    # Getter metoder for x og y
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    @x.setter
    def x(self):
        return self.__x

    @y.setter
    def y(self):
        return self.__y

    # Dunder metode til at lægge to vektorer sammen
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Operand must be an instance of Vector")

    # Dunder metode til at trække en vektor fra en anden
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError("Operand must be an instance of Vector")

    # Dunder metode til at multiplicere en vektor med et tal
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        raise TypeError("Operand must be a number (int or float)")

    # Dunder metode til at dividere en vektor med et tal
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector(self.x / scalar, self.y / scalar)
        raise TypeError("Operand must be a non-zero number (int or float)")

    # Dunder metode til at returnere en strengrepræsentation af vektoren
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Metode til at beregne længden af vektoren
    def getLength(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Metode til at normalisere vektoren
    def normalize(self):
        length = self.getLength()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / length, self.y / length)

    # Metode til at beregne afstanden til en anden vektor
    def distance(self, other):
        if isinstance(other, Vector):
            diff = self - other
            return diff.getLength()
        raise TypeError("Operand must be an instance of Vector")
