from __future__ import annotations
import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other: ComplexNumber):
        return self.real == other.real and self.imaginary == other.imaginary

    def destructure(self, c1: ComplexNumber, c2: ComplexNumber) -> (int, int, int, int):
        return (c1.real, c1.imaginary, c2.real, c2.imaginary)

    def __add__(self, other):
        if type(other) == ComplexNumber:
            (a, b, c, d) = self.destructure(self, other)

            return ComplexNumber(a + c, b + d)

        return ComplexNumber(self.real + other, self.imaginary)

    def __radd__(self, other):
        return ComplexNumber(other + self.real, self.imaginary)

    def __mul__(self, other):
        if type(other) == ComplexNumber:
            (a, b, c, d) = self.destructure(self, other)

            return ComplexNumber(a * c - b * d, b * c + a * d)

        return ComplexNumber(self.real * other, self.imaginary * other)

    def __rmul__(self, other):
        return ComplexNumber(other * self.real, other * self.imaginary)

    def __sub__(self, other):
        if type(other) == ComplexNumber:
            (a, b, c, d) = self.destructure(self, other)

            return ComplexNumber(a - c, b - d)

        return ComplexNumber(self.real - other, self.imaginary)

    def __rsub__(self, other):
        return ComplexNumber(other - self.real, -self.imaginary)

    def __truediv__(self, other):
        if type(other) == ComplexNumber:
            (a, b, c, d) = self.destructure(self, other)
            denom = (c ** 2 + d ** 2)
            
            return ComplexNumber((a * c + b * d) / denom, (b * c - a * d) / denom)

        return ComplexNumber(self.real / other, self.imaginary / other)

    def __rtruediv__(self, other):
        denom = self.real ** self.real + self.imaginary ** self.imaginary

        return ComplexNumber(other * self.real / denom, other * self.imaginary/denom).conjugate()

    def __abs__(self):
        a = self.real
        b = self.imaginary

        return math.sqrt(a ** 2 + b ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        e = math.e ** self.real

        return ComplexNumber(e * math.cos(self.imaginary), e * math.sin(self.imaginary))
