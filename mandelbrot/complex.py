from math import sqrt


class Complex:
    def __init__(self, a, b):
        self.__real = a
        self.__imaginary = b

    def __add__(self, other):
        return Complex(self.__real + other.__real, self.__imaginary + other.__imaginary)

    def __mul__(self, other):
        return Complex(self.__real * other.__real - self.__imaginary * other.__imaginary,
                       self.__real * other.__imaginary + other.__real * self.__imaginary)

    def __neg__(self):
        return Complex(-self.__real, -self.__imaginary)

    def len2(self):
        return self.__real * self.__real + self.__imaginary * self.__imaginary

    def __len__(self):
        return sqrt(self.len2())
